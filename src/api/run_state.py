"""In-memory run state for near-real-time UI updates."""
from __future__ import annotations

from datetime import datetime, timezone
from threading import Lock
from uuid import uuid4


_RUNS: dict[str, dict] = {}
_LOCK = Lock()
_MAX_RUNS = 500


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def create_run(trigger_type: str, input_text: str) -> str:
    run_id = str(uuid4())
    with _LOCK:
        _RUNS[run_id] = {
            "run_id": run_id,
            "status": "queued",
            "trigger_type": trigger_type,
            "input_text": input_text,
            "output": "",
            "error": "",
            "events": [],
            "cancel_requested": False,
            "created_at": _now_iso(),
            "updated_at": _now_iso(),
        }
        # Prevent unbounded memory growth. Never drop queued/running rows — otherwise the UI
        # loses /agent/runs/{id} while the worker thread is still alive (spinner/trace die early).
        if len(_RUNS) > _MAX_RUNS:
            terminal = frozenset({"completed", "error", "cancelled"})
            items = sorted(_RUNS.items(), key=lambda kv: str(kv[1].get("updated_at") or ""))
            for k, v in items:
                if len(_RUNS) <= _MAX_RUNS:
                    break
                st = str(v.get("status") or "").strip().lower()
                if st in terminal:
                    _RUNS.pop(k, None)
    return run_id


def mark_running(run_id: str):
    with _LOCK:
        run = _RUNS.get(run_id)
        if not run:
            return
        run["status"] = "running"
        run["updated_at"] = _now_iso()


def add_event(run_id: str, event_type: str, title: str, detail: str = ""):
    with _LOCK:
        run = _RUNS.get(run_id)
        if not run:
            return
        run["events"].append(
            {"ts": _now_iso(), "type": event_type, "title": title, "detail": detail}
        )
        run["updated_at"] = _now_iso()


def complete_run(run_id: str, output: str):
    with _LOCK:
        run = _RUNS.get(run_id)
        if not run:
            return
        run["status"] = "completed"
        run["output"] = output
        run["updated_at"] = _now_iso()


def fail_run(run_id: str, error: str):
    with _LOCK:
        run = _RUNS.get(run_id)
        if not run:
            return
        run["status"] = "error"
        run["error"] = error
        run["updated_at"] = _now_iso()


def get_run(run_id: str) -> dict | None:
    with _LOCK:
        run = _RUNS.get(run_id)
        if not run:
            return None
        # Shallow copy the row but snapshot events so JSON responses see a stable list length
        # even if callbacks append concurrently mid-serialize (rare).
        out = dict(run)
        ev = run.get("events")
        if isinstance(ev, list):
            out["events"] = list(ev)
        return out


def list_runs(*, limit: int = 50, status: str | None = None) -> list[dict]:
    with _LOCK:
        rows = list(_RUNS.values())
    st = str(status or "").strip().lower()
    if st and st != "all":
        rows = [r for r in rows if str(r.get("status") or "").strip().lower() == st]
    rows.sort(key=lambda r: str(r.get("updated_at") or ""), reverse=True)
    out = [dict(r) for r in rows[: max(1, int(limit))]]
    return out


def request_cancel(run_id: str) -> bool:
    """Ask the running agent to stop at the next cooperative checkpoint (between LLM/tool steps)."""
    with _LOCK:
        run = _RUNS.get(run_id)
        if not run or run.get("status") != "running":
            return False
        run["cancel_requested"] = True
        run["updated_at"] = _now_iso()
        return True


def is_cancel_requested(run_id: str) -> bool:
    with _LOCK:
        run = _RUNS.get(run_id)
        return bool(run and run.get("cancel_requested"))


def mark_cancelled(run_id: str, detail: str = "Stopped by user"):
    """Mark run as cancelled after cooperative stop (or if worker catches cancel)."""
    with _LOCK:
        run = _RUNS.get(run_id)
        if not run:
            return
        run["status"] = "cancelled"
        run["error"] = detail
        run["output"] = ""
        run["updated_at"] = _now_iso()
        run["events"].append(
            {"ts": _now_iso(), "type": "run_cancelled", "title": "Run stopped", "detail": detail}
        )

