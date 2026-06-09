"""Cron job manager using APScheduler."""
import re
from datetime import datetime
from zoneinfo import ZoneInfo

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from src.config import settings
from src.api import run_state
from src.db import database
from src.runtime_config import (
    effective_customer_email_domains,
    effective_guardrail_exclude_intent_keywords,
    effective_guardrail_exclude_sender_domains,
    effective_guardrail_include_intent_keywords,
    effective_guardrail_include_sender_domains,
    effective_guardrail_strictness,
)


_scheduler: BackgroundScheduler | None = None

# APScheduler uses ISO weekdays (0=Mon … 6=Sun). Classic Unix cron uses 0=Sun, 1=Mon …
_WEEKDAY_DOW_TOKENS = frozenset({"1-5", "0-4", "mon-fri", "mon,tue,wed,thu,fri"})


def _is_numeric_dow_field(dow: str) -> bool:
    d = (dow or "").strip()
    return bool(d) and d not in {"*", "?"} and not re.search(r"[a-zA-Z]", d)


def _unix_dow_to_aps_number(unix_dow: int) -> int:
    """Map Unix cron DOW (0=Sun, 1=Mon, …, 6=Sat, 7=Sun) to APScheduler (0=Mon … 6=Sun)."""
    return (int(unix_dow) + 6) % 7


def _convert_unix_dow_atom(atom: str) -> str:
    atom = (atom or "").strip()
    if atom in ("*", "?"):
        return atom
    m = re.fullmatch(r"(\d+)(?:-(\d+))?(?:/(\d+))?", atom)
    if not m:
        return atom
    start_s, end_s, step_s = m.group(1), m.group(2), m.group(3)
    step = int(step_s) if step_s else None
    if end_s is None:
        aps = _unix_dow_to_aps_number(int(start_s))
        base = str(aps)
        return f"{base}/{step}" if step else base
    start_a = _unix_dow_to_aps_number(int(start_s))
    end_a = _unix_dow_to_aps_number(int(end_s))
    if step:
        return f"{start_a}-{end_a}/{step}"
    return f"{start_a}-{end_a}"


def _convert_unix_dow_field_to_apscheduler(dow: str) -> str:
    """Convert a Unix-style numeric day-of-week field to APScheduler-compatible tokens."""
    d = (dow or "*").strip()
    if d == "1-5":
        return "mon-fri"
    if not _is_numeric_dow_field(d):
        return d
    return ",".join(_convert_unix_dow_atom(part) for part in d.split(","))


def normalize_cron_expression_for_apscheduler(cron_expr: str) -> str:
    """
    Normalize 5-field cron for APScheduler.

    User-facing presets and NL generation follow Unix DOW (1=Mon … 5=Fri). APScheduler
  uses ISO DOW (0=Mon … 6=Sun), so `1-5` would mean Tue–Sat without conversion.
    """
    raw = (cron_expr or "").strip()
    parts = raw.split()
    if len(parts) != 5:
        return raw
    dow = _convert_unix_dow_field_to_apscheduler(parts[4])
    if dow == parts[4]:
        return raw
    return " ".join([*parts[:4], dow])


def _cron_trigger(cron_expr: str, tz: str) -> CronTrigger:
    zone = (tz or "Asia/Seoul").strip() or "Asia/Seoul"
    normalized = normalize_cron_expression_for_apscheduler(cron_expr)
    return CronTrigger.from_crontab(normalized, timezone=zone)


def describe_cron_expression(cron_expr: str) -> str:
    """Return a user-facing schedule summary for common patterns."""
    parts = normalize_cron_expression_for_apscheduler(cron_expr or "").strip().split()
    if len(parts) != 5:
        return "Custom cron schedule"
    minute, hour, day, month, dow = parts
    weekdays = dow in _WEEKDAY_DOW_TOKENS
    if minute == "0" and hour.startswith("*/") and day == "*" and month == "*" and dow in {"*", * _WEEKDAY_DOW_TOKENS}:
        n = hour[2:] or "?"
        if weekdays:
            return f"Every {n} hours on weekdays"
        return f"Every {n} hours (all days)"
    if minute.isdigit() and hour.isdigit() and day == "*" and month == "*" and dow in {"*", * _WEEKDAY_DOW_TOKENS}:
        hh = int(hour)
        mm = int(minute)
        if weekdays:
            return f"At {hh:02d}:{mm:02d} on weekdays"
        return f"Daily at {hh:02d}:{mm:02d}"
    if day == "*" and month == "*" and weekdays:
        return "Weekdays only (custom time)"
    return "Custom cron schedule"


def preview_next_runs(cron_expr: str, tz: str, count: int = 3) -> list[str]:
    """Return next N run times formatted in the given timezone."""
    out: list[str] = []
    try:
        zone = ZoneInfo((tz or "Asia/Seoul").strip() or "Asia/Seoul")
    except Exception:
        zone = ZoneInfo("Asia/Seoul")
    try:
        trigger = _cron_trigger(cron_expr, str(zone))
    except Exception:
        return out
    now = datetime.now(zone)
    ref = now
    prev = None
    for _ in range(max(0, int(count))):
        nxt = trigger.get_next_fire_time(prev, ref)
        if not nxt:
            break
        out.append(nxt.astimezone(zone).strftime("%Y-%m-%d %H:%M"))
        prev = nxt
        ref = nxt
    return out


def _run_probe_job(name: str = "default"):
    from src.agent.probe_actions import merge_csm_actions_metadata
    from src.agent.prompts import get_probe_trigger_message
    from src.agent.email_agent import run_agent
    run_id = run_state.create_run(trigger_type=f"cron:{name}", input_text=get_probe_trigger_message()[:500])
    run_state.mark_running(run_id)
    run_state.add_event(run_id, "chain_start", f"Cron job started: {name}")
    try:
        output = run_agent(get_probe_trigger_message(), probe=True)
        run_state.complete_run(run_id, output)
        existing = database.latest_dashboard_actions_by_gmail_thread()
        meta = merge_csm_actions_metadata(
            output,
            {
                "run_id": run_id,
                "guardrail_include_sender_domains": effective_guardrail_include_sender_domains(),
                "guardrail_exclude_sender_domains": effective_guardrail_exclude_sender_domains(),
                "guardrail_include_intent_keywords": effective_guardrail_include_intent_keywords(),
                "guardrail_exclude_intent_keywords": effective_guardrail_exclude_intent_keywords(),
                "guardrail_strictness": effective_guardrail_strictness(),
                "customer_email_domains": effective_customer_email_domains(),
            },
            existing_by_thread=existing,
        )
        database.log_interaction(
            f"cron:{name}", get_probe_trigger_message(), output, "completed", metadata=meta
        )
    except Exception as e:
        run_state.fail_run(run_id, str(e))
        database.log_interaction(f"cron:{name}", get_probe_trigger_message(), "", "error", str(e))


def migrate_cron_expressions_in_db() -> None:
    """Rewrite legacy Unix-style weekday fields (e.g. 1-5) to APScheduler form (mon-fri)."""
    for j in database.get_cron_jobs():
        raw = str(j.get("cron_expression") or "").strip()
        norm = normalize_cron_expression_for_apscheduler(raw)
        if norm and norm != raw:
            database.add_cron_job(
                j["name"],
                norm,
                str(j.get("timezone") or "Asia/Seoul"),
            )


def get_scheduler() -> BackgroundScheduler:
    global _scheduler
    if _scheduler is None:
        tz = getattr(settings, "scheduler_timezone", "Asia/Seoul")
        _scheduler = BackgroundScheduler(timezone=tz)
        _scheduler.start()
        migrate_cron_expressions_in_db()
        for j in database.get_cron_jobs():
            if j.get("enabled", 1):
                _add_job_to_scheduler(j["name"], j["cron_expression"], j.get("timezone", "Asia/Seoul"))
    return _scheduler


def get_scheduler_timezone() -> str:
    return getattr(settings, "scheduler_timezone", "Asia/Seoul")


def _add_job_to_scheduler(name: str, cron_expr: str, tz: str):
    sched = get_scheduler()
    job_id = f"probe_{name}"
    try:
        sched.remove_job(job_id)
    except Exception:
        pass
    trigger = _cron_trigger(cron_expr, tz)
    sched.add_job(_run_probe_job, trigger=trigger, id=job_id, name=name, args=[name])


def add_job(name: str, cron_expression: str, timezone: str = "Asia/Seoul"):
    normalized = normalize_cron_expression_for_apscheduler(cron_expression)
    database.add_cron_job(name, normalized, timezone)
    _add_job_to_scheduler(name, normalized, timezone)


def remove_job(name: str):
    database.delete_cron_job(name)
    try:
        get_scheduler().remove_job(f"probe_{name}")
    except Exception:
        pass


def toggle_job(name: str, enabled: bool):
    database.set_cron_enabled(name, enabled)
    jobs = database.get_cron_jobs()
    job = next((j for j in jobs if j["name"] == name), None)
    if job:
        if enabled:
            _add_job_to_scheduler(name, job["cron_expression"], job.get("timezone", "Asia/Seoul"))
        else:
            try:
                get_scheduler().remove_job(f"probe_{name}")
            except Exception:
                pass
