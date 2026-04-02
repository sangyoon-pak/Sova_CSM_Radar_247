"""SQLite database for interactions and cron jobs."""
import json
import sqlite3
from datetime import datetime
from pathlib import Path
from threading import Lock
from typing import Optional

from src.config import settings

_WRITE_LOCK = Lock()

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
    conn = sqlite3.connect(str(path), timeout=30)
    # Set WAL mode once at init time (doing this on every connection can
    # require an exclusive lock and cause "database is locked" under concurrency).
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.executescript(schema)
    conn.commit()
    conn.close()


def _conn():
    path = _db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(
        str(path),
        # Keep timestamps as plain strings; Python's default timestamp converter
        # expects "YYYY-MM-DD HH:MM:SS" but we also store ISO strings.
        detect_types=0,
        timeout=30,
        check_same_thread=False,
        isolation_level=None,  # autocommit; avoids lingering open transactions
    )
    # Avoid PRAGMA journal_mode here (can require exclusive lock).
    conn.execute("PRAGMA busy_timeout=30000;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    return conn


def log_interaction(trigger_type: str, input_text: str, output_text: str, status: str = "completed", error_message: str | None = None, metadata: dict | None = None):
    with _WRITE_LOCK:
        conn = _conn()
        conn.execute(
            """INSERT INTO agent_interactions (trigger_type, input_text, output_text, status, error_message, metadata)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (
                trigger_type,
                input_text,
                output_text,
                status,
                error_message,
                json.dumps(metadata) if metadata else None,
            ),
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


def get_interactions_before(before: datetime, limit: int = 200):
    """Fetch interactions created before the given datetime, newest first."""
    conn = _conn()
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """SELECT id, created_at, trigger_type, input_text, output_text, status, error_message, metadata
           FROM agent_interactions
           WHERE created_at < ?
           ORDER BY created_at DESC
           LIMIT ?""",
        (before, limit),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def delete_interactions(before: Optional[datetime] = None) -> int:
    """
    Delete interaction history.
    - If `before` is provided, delete rows with created_at < before.
    - If `before` is None, delete all rows.
    Returns the number of deleted rows.
    """
    with _WRITE_LOCK:
        conn = _conn()
        if before is None:
            cur = conn.execute("DELETE FROM agent_interactions")
        else:
            cur = conn.execute("DELETE FROM agent_interactions WHERE created_at < ?", (before,))
        conn.commit()
        deleted = cur.rowcount or 0
        conn.close()
        return deleted


def delete_interactions_by_ids(ids: list[int]) -> int:
    """Delete specific interactions by id."""
    if not ids:
        return 0
    with _WRITE_LOCK:
        conn = _conn()
        placeholders = ",".join("?" for _ in ids)
        cur = conn.execute(f"DELETE FROM agent_interactions WHERE id IN ({placeholders})", ids)
        conn.commit()
        deleted = cur.rowcount or 0
        conn.close()
        return deleted


def insert_memory(summary: str, interaction_ids: list[int] | None = None):
    """Insert a summarized memory note referencing the original interaction IDs."""
    with _WRITE_LOCK:
        conn = _conn()
        conn.execute(
            """INSERT INTO agent_memory (summary, source_interaction_ids)
               VALUES (?, ?)""",
            (summary, json.dumps(interaction_ids or [])),
        )
        conn.commit()
        conn.close()


def add_cron_job(name: str, cron_expression: str, timezone: str = "Asia/Seoul"):
    with _WRITE_LOCK:
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


def get_cron_run_summary(limit: int = 20):
    """
    Return recent cron execution summaries by trigger_type (e.g., cron:daily_probe).
    """
    conn = _conn()
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT trigger_type, status, created_at, output_text, error_message
        FROM agent_interactions
        WHERE trigger_type LIKE 'cron%'
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (limit,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def set_cron_enabled(name: str, enabled: bool):
    with _WRITE_LOCK:
        conn = _conn()
        conn.execute("UPDATE cron_jobs SET enabled = ? WHERE name = ?", (1 if enabled else 0, name))
        conn.commit()
        conn.close()


def delete_cron_job(name: str):
    with _WRITE_LOCK:
        conn = _conn()
        conn.execute("DELETE FROM cron_jobs WHERE name = ?", (name,))
        conn.commit()
        conn.close()


def upsert_kb_document(
    *,
    source_type: str,
    path: str | None = None,
    url: str | None = None,
    content_sha256: str | None = None,
    title: str | None = None,
    tags: list[str] | None = None,
    language: str | None = None,
    scope: str | None = None,
    last_updated: str | None = None,
    metadata: dict | None = None,
) -> dict:
    """
    Insert/update a KB document registry record.
    Uses (path) or (url) as the identity key.
    """
    if not path and not url:
        raise ValueError("Provide at least one of path or url")
    with _WRITE_LOCK:
        conn = _conn()
        conn.row_factory = sqlite3.Row
        now = datetime.utcnow().isoformat()
        tags_json = json.dumps(tags or []) if tags is not None else None
        meta_json = json.dumps(metadata) if metadata else None

    # Upsert by path or url.
    if path:
        conn.execute(
            """
            INSERT INTO kb_documents (source_type, path, url, content_sha256, title, tags, language, scope, last_updated, metadata, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(path) DO UPDATE SET
              source_type=excluded.source_type,
              url=COALESCE(excluded.url, kb_documents.url),
              content_sha256=COALESCE(excluded.content_sha256, kb_documents.content_sha256),
              title=COALESCE(excluded.title, kb_documents.title),
              tags=COALESCE(excluded.tags, kb_documents.tags),
              language=COALESCE(excluded.language, kb_documents.language),
              scope=COALESCE(excluded.scope, kb_documents.scope),
              last_updated=COALESCE(excluded.last_updated, kb_documents.last_updated),
              metadata=COALESCE(excluded.metadata, kb_documents.metadata),
              updated_at=excluded.updated_at
            """,
            (
                source_type,
                path,
                url,
                content_sha256,
                title,
                tags_json,
                language,
                scope,
                last_updated,
                meta_json,
                now,
            ),
        )
        row = conn.execute("SELECT * FROM kb_documents WHERE path = ?", (path,)).fetchone()
    else:
        conn.execute(
            """
            INSERT INTO kb_documents (source_type, path, url, content_sha256, title, tags, language, scope, last_updated, metadata, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(url) DO UPDATE SET
              source_type=excluded.source_type,
              path=COALESCE(excluded.path, kb_documents.path),
              content_sha256=COALESCE(excluded.content_sha256, kb_documents.content_sha256),
              title=COALESCE(excluded.title, kb_documents.title),
              tags=COALESCE(excluded.tags, kb_documents.tags),
              language=COALESCE(excluded.language, kb_documents.language),
              scope=COALESCE(excluded.scope, kb_documents.scope),
              last_updated=COALESCE(excluded.last_updated, kb_documents.last_updated),
              metadata=COALESCE(excluded.metadata, kb_documents.metadata),
              updated_at=excluded.updated_at
            """,
            (
                source_type,
                None,
                url,
                content_sha256,
                title,
                tags_json,
                language,
                scope,
                last_updated,
                meta_json,
                now,
            ),
        )
        row = conn.execute("SELECT * FROM kb_documents WHERE url = ?", (url,)).fetchone()
        conn.commit()
        conn.close()
        return dict(row) if row else {}


def list_kb_documents(limit: int = 200, offset: int = 0) -> list[dict]:
    conn = _conn()
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT id, created_at, updated_at, source_type, path, url, title, tags, language, scope, last_updated, metadata
        FROM kb_documents
        ORDER BY updated_at DESC, id DESC
        LIMIT ? OFFSET ?
        """,
        (limit, offset),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def delete_kb_document(doc_id: int) -> dict:
    """
    Delete a persisted KB document.
    - Removes the registry row from `kb_documents`.
    - If the registry row has a local `path`, deletes that file (best-effort) too.
    """
    with _WRITE_LOCK:
        conn = _conn()
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT id, path, url, source_type FROM kb_documents WHERE id = ?",
            (doc_id,),
        ).fetchone()
        if not row:
            conn.close()
            return {"deleted": 0}

        removed_path = None
        kb_root = getattr(settings, "kb_path_resolved", None)
        path = row["path"]
        if path and kb_root:
            try:
                abs_p = Path(path).resolve()
                # Safety: only delete files under our knowledge base folder.
                if abs_p == kb_root or kb_root in abs_p.parents:
                    abs_p.unlink(missing_ok=True)
                    removed_path = str(abs_p)
            except Exception:
                removed_path = None

        conn.execute("DELETE FROM kb_documents WHERE id = ?", (doc_id,))
        conn.commit()
        conn.close()
        return {
            "deleted": 1,
            "removed_path": removed_path,
            "source_type": row["source_type"],
        }


def upsert_rc_url(
    *,
    url: str,
    title: str | None = None,
    tags: list[str] | None = None,
    scope: str | None = None,
    enabled: bool = True,
) -> dict:
    u = (url or "").strip()
    if not u:
        raise ValueError("url is required")
    with _WRITE_LOCK:
        conn = _conn()
        conn.row_factory = sqlite3.Row
        now = datetime.utcnow().isoformat()
        conn.execute(
        """
        INSERT INTO rc_urls (url, title, tags, scope, enabled, updated_at)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(url) DO UPDATE SET
          title=COALESCE(excluded.title, rc_urls.title),
          tags=COALESCE(excluded.tags, rc_urls.tags),
          scope=COALESCE(excluded.scope, rc_urls.scope),
          enabled=excluded.enabled,
          updated_at=excluded.updated_at
        """,
        (
            u,
            title,
            json.dumps(tags or []) if tags is not None else None,
            scope,
            1 if enabled else 0,
            now,
        ),
        )
        row = conn.execute("SELECT * FROM rc_urls WHERE url = ?", (u,)).fetchone()
        conn.commit()
        conn.close()
        return dict(row) if row else {}


def list_rc_urls(limit: int = 200, offset: int = 0, enabled_only: bool = False) -> list[dict]:
    conn = _conn()
    conn.row_factory = sqlite3.Row
    if enabled_only:
        rows = conn.execute(
            """
            SELECT id, created_at, updated_at, url, title, tags, scope, enabled
            FROM rc_urls
            WHERE enabled = 1
            ORDER BY updated_at DESC, id DESC
            LIMIT ? OFFSET ?
            """,
            (limit, offset),
        ).fetchall()
    else:
        rows = conn.execute(
            """
            SELECT id, created_at, updated_at, url, title, tags, scope, enabled
            FROM rc_urls
            ORDER BY updated_at DESC, id DESC
            LIMIT ? OFFSET ?
            """,
            (limit, offset),
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def set_rc_url_enabled(url: str, enabled: bool) -> None:
    u = (url or "").strip()
    if not u:
        raise ValueError("url is required")
    with _WRITE_LOCK:
        conn = _conn()
        now = datetime.utcnow().isoformat()
        conn.execute(
            "UPDATE rc_urls SET enabled = ?, updated_at = ? WHERE url = ?",
            (1 if enabled else 0, now, u),
        )
        conn.commit()
        conn.close()


def delete_rc_url(url: str) -> int:
    u = (url or "").strip()
    if not u:
        raise ValueError("url is required")
    with _WRITE_LOCK:
        conn = _conn()
        cur = conn.execute("DELETE FROM rc_urls WHERE url = ?", (u,))
        conn.commit()
        deleted = cur.rowcount or 0
        conn.close()
        return deleted
