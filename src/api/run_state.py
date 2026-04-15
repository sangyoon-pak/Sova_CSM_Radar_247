"""In-memory run state for near-real-time UI updates."""
from __future__ import annotations

from datetime import datetime, timezone
from threading import Lock
from uuid import uuid4


_RUNS: dict[str, dict] = {}
_LOCK = Lock()


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def create_run(trigger_type: str, input_text: str) -> str:
    run_id = str(uuid4())
    with _LOCK:
        _RUNS[run_id] = {
            "run_id": run_id,
            "status": "running",
            "trigger_type": trigger_type,
            "input_text": input_text,
            "output": "",
            "error": "",
            "events": [],
            "cancel_requested": False,
            "created_at": _now_iso(),
            "updated_at": _now_iso(),
        }
    return run_id


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
        return dict(run) if run else None


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

