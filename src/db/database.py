"""SQLite database for interactions and cron jobs."""
import json
import sqlite3
from pathlib import Path

from src.config import settings


def _db_path() -> Path:
    p = Path(settings.database_path)
    if not p.is_absolute():
        root = Path(__file__).parent.parent.parent
        p = (root / p).resolve()
    return p


def init_db():
    path = _db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    schema = (Path(__file__).parent / "schema.sql").read_text()
    conn = sqlite3.connect(str(path))
    conn.executescript(schema)
    conn.commit()
    conn.close()


def _conn():
    path = _db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(str(path), detect_types=sqlite3.PARSE_DECLTYPES)


def log_interaction(trigger_type: str, input_text: str, output_text: str, status: str = "completed", error_message: str | None = None, metadata: dict | None = None):
    conn = _conn()
    conn.execute(
        """INSERT INTO agent_interactions (trigger_type, input_text, output_text, status, error_message, metadata)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (trigger_type, input_text, output_text, status, error_message, json.dumps(metadata) if metadata else None),
    )
    conn.commit()
    conn.close()


def get_interactions(limit: int = 50, offset: int = 0):
    conn = _conn()
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """SELECT id, created_at, trigger_type, input_text, output_text, status, error_message, metadata
           FROM agent_interactions ORDER BY created_at DESC LIMIT ? OFFSET ?""",
        (limit, offset),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def add_cron_job(name: str, cron_expression: str, timezone: str = "Asia/Seoul"):
    conn = _conn()
    conn.execute(
        """INSERT INTO cron_jobs (name, cron_expression, timezone, enabled)
           VALUES (?, ?, ?, 1)
           ON CONFLICT(name) DO UPDATE SET cron_expression=excluded.cron_expression,
               timezone=excluded.timezone, enabled=1""",
        (name, cron_expression, timezone),
    )
    conn.commit()
    conn.close()


def get_cron_jobs():
    conn = _conn()
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """SELECT id, name, cron_expression, timezone, enabled, last_run_at, next_run_at
           FROM cron_jobs ORDER BY name"""
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def set_cron_enabled(name: str, enabled: bool):
    conn = _conn()
    conn.execute("UPDATE cron_jobs SET enabled = ? WHERE name = ?", (1 if enabled else 0, name))
    conn.commit()
    conn.close()


def delete_cron_job(name: str):
    conn = _conn()
    conn.execute("DELETE FROM cron_jobs WHERE name = ?", (name,))
    conn.commit()
    conn.close()
