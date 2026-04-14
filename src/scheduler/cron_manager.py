"""Cron job manager using APScheduler."""
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from src.config import settings
from src.db import database
from src.runtime_config import effective_scheduler_timezone


_scheduler: BackgroundScheduler | None = None


def _run_probe_job(name: str = "default"):
    from src.agent.probe_actions import merge_csm_actions_metadata
    from src.agent.prompts import PROBE_TRIGGER_MESSAGE
    from src.agent.email_agent import run_agent
    try:
        output = run_agent(PROBE_TRIGGER_MESSAGE, probe=True)
        existing = database.latest_dashboard_actions_by_gmail_thread()
        meta = merge_csm_actions_metadata(output, {}, existing_by_thread=existing)
        database.log_interaction(
            f"cron:{name}", PROBE_TRIGGER_MESSAGE, output, "completed", metadata=meta
        )
    except Exception as e:
        database.log_interaction(f"cron:{name}", PROBE_TRIGGER_MESSAGE, "", "error", str(e))


def get_scheduler() -> BackgroundScheduler:
    global _scheduler
    if _scheduler is None:
        tz = effective_scheduler_timezone()
        _scheduler = BackgroundScheduler(timezone=tz)
        _scheduler.start()
        for j in database.get_cron_jobs():
            if j.get("enabled", 1):
                _add_job_to_scheduler(j["name"], j["cron_expression"], j.get("timezone", "Asia/Seoul"))
    return _scheduler


def get_scheduler_timezone() -> str:
    return effective_scheduler_timezone()


def _add_job_to_scheduler(name: str, cron_expr: str, tz: str):
    sched = get_scheduler()
    job_id = f"probe_{name}"
    try:
        sched.remove_job(job_id)
    except Exception:
        pass
    parts = cron_expr.strip().split()
    if len(parts) != 5:
        parts = ["0", "*", "*", "*", "*"]
    trigger = CronTrigger(minute=parts[0], hour=parts[1], day=parts[2], month=parts[3], day_of_week=parts[4], timezone=tz)
    sched.add_job(_run_probe_job, trigger=trigger, id=job_id, name=name, args=[name])


def add_job(name: str, cron_expression: str, timezone: str = "Asia/Seoul"):
    database.add_cron_job(name, cron_expression, timezone)
    _add_job_to_scheduler(name, cron_expression, timezone)


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
