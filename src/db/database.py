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


def _is_probe_dashboard_trigger(trigger_type: str | None) -> bool:
    t = (trigger_type or "").strip()
    if t.startswith("cron:"):
        return True
    if t == "thread_probe":
        return True
    if t.startswith("manual_probe"):
        return True
    return False


def get_interaction_by_id(interaction_id: int) -> dict | None:
    conn = _conn()
    conn.row_factory = sqlite3.Row
    row = conn.execute(
        """SELECT id, created_at, trigger_type, input_text, output_text, status, error_message, metadata
           FROM agent_interactions WHERE id = ?""",
        (interaction_id,),
    ).fetchone()
    conn.close()
    return dict(row) if row else None


def _parse_interaction_metadata(raw: str | None) -> dict:
    if not raw:
        return {}
    try:
        out = json.loads(raw)
        return out if isinstance(out, dict) else {}
    except json.JSONDecodeError:
        return {}


def dismiss_probe_from_dashboard(interaction_id: int) -> bool:
    """
    Hide a probe run from the Action dashboard (metadata flag). Row stays in DB for Run history.
    """
    with _WRITE_LOCK:
        conn = _conn()
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT id, trigger_type, metadata FROM agent_interactions WHERE id = ?",
            (interaction_id,),
        ).fetchone()
        if not row:
            conn.close()
            return False
        d = dict(row)
        if not _is_probe_dashboard_trigger(d.get("trigger_type")):
            conn.close()
            return False
        md = _parse_interaction_metadata(d.get("metadata"))
        md["csm_dashboard_removed"] = True
        conn.execute(
            "UPDATE agent_interactions SET metadata = ? WHERE id = ?",
            (json.dumps(md), interaction_id),
        )
        conn.commit()
        conn.close()
        return True


def remove_csm_dashboard_action(interaction_id: int, action_index: int) -> bool:
    """Remove one item from metadata.csm_actions; hide run from dashboard if none left."""
    with _WRITE_LOCK:
        conn = _conn()
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT id, trigger_type, metadata FROM agent_interactions WHERE id = ?",
            (interaction_id,),
        ).fetchone()
        if not row:
            conn.close()
            return False
        d = dict(row)
        if not _is_probe_dashboard_trigger(d.get("trigger_type")):
            conn.close()
            return False
        md = _parse_interaction_metadata(d.get("metadata"))
        actions = md.get("csm_actions")
        if not isinstance(actions, list) or action_index < 0 or action_index >= len(actions):
            conn.close()
            return False
        actions = list(actions)
        actions.pop(action_index)
        md["csm_actions"] = actions
        if len(actions) == 0:
            md["csm_dashboard_removed"] = True
        conn.execute(
            "UPDATE agent_interactions SET metadata = ? WHERE id = ?",
            (json.dumps(md), interaction_id),
        )
        conn.commit()
        conn.close()
        return True


def list_probe_interactions(
    *,
    limit: int = 30,
    offset: int = 0,
    source: str = "all",
    status_filter: str | None = None,
) -> list[dict]:
    """
    Inbox review runs: cron:*, thread_probe, manual_probe.
    source: all | cron | thread_probe | manual_probe
    status_filter: None or 'all' = any status; 'completed' | 'error' to filter.
    """
    src = (source or "all").strip().lower()
    if src not in ("all", "cron", "thread_probe", "manual_probe"):
        src = "all"
    st = (status_filter or "").strip().lower()
    if st in ("", "all"):
        st = None
    elif st not in ("completed", "error"):
        st = None

    if src == "cron":
        where = "trigger_type LIKE 'cron:%'"
        params: list = []
    elif src == "thread_probe":
        where = "trigger_type = 'thread_probe'"
        params = []
    elif src == "manual_probe":
        where = "(trigger_type = 'manual_probe' OR trigger_type LIKE 'manual_probe_%')"
        params = []
    else:
        where = (
            "(trigger_type LIKE 'cron:%' OR trigger_type = 'thread_probe' "
            "OR trigger_type LIKE 'manual_probe%')"
        )
        params = []

    if st:
        where = f"({where}) AND status = ?"
        params.append(st)

    # CSM dismissed probe runs stay in DB but are hidden from the Action dashboard.
    where = (
        f"({where}) AND NOT (COALESCE(json_extract(metadata, '$.csm_dashboard_removed'), 0) = 1)"
    )

    sql = f"""SELECT id, created_at, trigger_type, input_text, output_text, status, error_message, metadata
              FROM agent_interactions
              WHERE {where}
              ORDER BY created_at DESC
              LIMIT ? OFFSET ?"""
    params.extend([limit, offset])

    conn = _conn()
    conn.row_factory = sqlite3.Row
    rows = conn.execute(sql, tuple(params)).fetchall()
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
        conn.commit()
        conn.close()
        return dict(row) if row else {}
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


def update_kb_document_metadata(doc_id: int, patch: dict) -> dict:
    """
    Merge a JSON patch into kb_documents.metadata for a given document id.
    """
    with _WRITE_LOCK:
        conn = _conn()
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT id, metadata FROM kb_documents WHERE id = ?",
            (int(doc_id),),
        ).fetchone()
        if not row:
            conn.close()
            return {}
        current = {}
        try:
            if row["metadata"]:
                current = json.loads(row["metadata"])
        except Exception:
            current = {}
        merged = dict(current or {})
        merged.update(patch or {})
        now = datetime.utcnow().isoformat()
        conn.execute(
            "UPDATE kb_documents SET metadata = ?, updated_at = ? WHERE id = ?",
            (json.dumps(merged), now, int(doc_id)),
        )
        out = conn.execute("SELECT * FROM kb_documents WHERE id = ?", (int(doc_id),)).fetchone()
        conn.commit()
        conn.close()
        return dict(out) if out else {}


def get_app_setting(key: str, default: str | None = None) -> str | None:
    conn = _conn()
    row = conn.execute("SELECT value FROM app_settings WHERE key = ?", (key,)).fetchone()
    conn.close()
    if not row:
        return default
    return row[0]


def set_app_setting(key: str, value: str) -> None:
    with _WRITE_LOCK:
        conn = _conn()
        now = datetime.utcnow().isoformat()
        conn.execute(
            """
            INSERT INTO app_settings (key, value, updated_at)
            VALUES (?, ?, ?)
            ON CONFLICT(key) DO UPDATE SET
              value=excluded.value,
              updated_at=excluded.updated_at
            """,
            (key, value, now),
        )
        conn.commit()
        conn.close()


def get_agent_profile_settings() -> dict:
    return {
        "vendor_name": get_app_setting("vendor_name", settings.agent_vendor_name) or settings.agent_vendor_name,
        "product_context": get_app_setting("product_context", settings.agent_product_context) or settings.agent_product_context,
        "role_title": get_app_setting("role_title", settings.agent_role_title) or settings.agent_role_title,
    }


def set_agent_profile_settings(*, vendor_name: str, product_context: str, role_title: str) -> dict:
    set_app_setting("vendor_name", (vendor_name or "").strip())
    set_app_setting("product_context", (product_context or "").strip())
    set_app_setting("role_title", (role_title or "").strip())
    return get_agent_profile_settings()


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

    # Best-effort: update derived stores after deletion (runs outside DB lock).
    try:
        from threading import Thread
        from src.agent.tools import doc_search
        kb_root = getattr(settings, "kb_path_resolved", None)
        if kb_root and removed_path:
            Thread(target=lambda: doc_search.tombstone_files([Path(removed_path)]), daemon=True).start()
    except Exception:
        pass
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


def insert_feedback(
    *,
    interaction_id: int | None,
    verdict: str,
    note: str | None = None,
    correction: str | None = None,
    metadata: dict | None = None,
) -> dict:
    verdict_norm = (verdict or "").strip().lower()
    if verdict_norm not in {"correct", "incorrect", "useful", "noisy"}:
        raise ValueError("verdict must be one of: correct, incorrect, useful, noisy")
    with _WRITE_LOCK:
        conn = _conn()
        conn.row_factory = sqlite3.Row
        conn.execute(
            """
            INSERT INTO agent_feedback (interaction_id, verdict, note, correction, metadata)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                interaction_id,
                verdict_norm,
                (note or "").strip() or None,
                (correction or "").strip() or None,
                json.dumps(metadata) if metadata else None,
            ),
        )
        row = conn.execute("SELECT * FROM agent_feedback ORDER BY id DESC LIMIT 1").fetchone()
        conn.commit()
        conn.close()
        return dict(row) if row else {}


def list_feedback(limit: int = 100, offset: int = 0) -> list[dict]:
    conn = _conn()
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT id, created_at, interaction_id, verdict, note, correction, metadata
        FROM agent_feedback
        ORDER BY id DESC
        LIMIT ? OFFSET ?
        """,
        (limit, offset),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_learning_feedback_samples(limit: int = 80) -> list[dict]:
    conn = _conn()
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT created_at, verdict, note, correction
        FROM agent_feedback
        WHERE (correction IS NOT NULL AND TRIM(correction) != '')
           OR (note IS NOT NULL AND TRIM(note) != '')
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_runtime_learning_instructions() -> str:
    return (get_app_setting("agent_learning_instructions", "") or "").strip()


def db_stats() -> dict:
    path = _db_path()
    conn = _conn()
    def _count(tbl: str) -> int:
        row = conn.execute(f"SELECT COUNT(*) FROM {tbl}").fetchone()
        return int(row[0]) if row else 0
    stats = {
        "database_path": str(path),
        "database_size_bytes": path.stat().st_size if path.exists() else 0,
        "agent_interactions": _count("agent_interactions"),
        "agent_memory": _count("agent_memory"),
        "agent_feedback": _count("agent_feedback"),
        "kb_documents": _count("kb_documents"),
        "rc_urls": _count("rc_urls"),
    }
    conn.close()
    return stats


def optimize_data_store(
    *,
    interactions_keep_days: int = 30,
    memory_keep_days: int = 60,
    feedback_keep_days: int = 120,
    purge_memory_table: bool = False,
    delete_report_outputs: bool = False,
    vacuum: bool = True,
) -> dict:
    with _WRITE_LOCK:
        conn = _conn()
        cur = conn.cursor()
        deleted = {
            "agent_interactions": 0,
            "agent_memory": 0,
            "agent_feedback": 0,
            "report_outputs": 0,
        }
        if interactions_keep_days >= 0:
            c = cur.execute(
                "DELETE FROM agent_interactions WHERE created_at < datetime('now', ?)",
                (f"-{int(interactions_keep_days)} days",),
            )
            deleted["agent_interactions"] = c.rowcount or 0
        if purge_memory_table:
            c = cur.execute("DELETE FROM agent_memory")
            deleted["agent_memory"] = c.rowcount or 0
        elif memory_keep_days >= 0:
            c = cur.execute(
                "DELETE FROM agent_memory WHERE created_at < datetime('now', ?)",
                (f"-{int(memory_keep_days)} days",),
            )
            deleted["agent_memory"] = c.rowcount or 0
        if feedback_keep_days >= 0:
            c = cur.execute(
                "DELETE FROM agent_feedback WHERE created_at < datetime('now', ?)",
                (f"-{int(feedback_keep_days)} days",),
            )
            deleted["agent_feedback"] = c.rowcount or 0
        conn.commit()
        conn.execute("PRAGMA wal_checkpoint(TRUNCATE);")
        if vacuum:
            conn.execute("VACUUM;")
        conn.close()

    deleted_files = 0
    if delete_report_outputs:
        reports_dir = Path(__file__).parent.parent.parent / "data" / "reports"
        if reports_dir.exists():
            for p in reports_dir.glob("*"):
                if p.is_file() and p.suffix.lower() in {".txt", ".json"} and "fixtures" not in str(p):
                    try:
                        p.unlink(missing_ok=True)
                        deleted_files += 1
                    except Exception:
                        pass
    deleted["report_outputs"] = deleted_files
    return {"deleted": deleted, "stats": db_stats()}


def create_thread(*, title: str | None = None, pinned: bool = False, metadata: dict | None = None) -> dict:
    with _WRITE_LOCK:
        conn = _conn()
        conn.row_factory = sqlite3.Row
        now = datetime.utcnow().isoformat()
        conn.execute(
            """
            INSERT INTO conversation_threads (title, pinned, metadata, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                (title or "").strip() or None,
                1 if pinned else 0,
                json.dumps(metadata) if metadata else None,
                now,
                now,
            ),
        )
        row = conn.execute("SELECT * FROM conversation_threads ORDER BY id DESC LIMIT 1").fetchone()
        conn.commit()
        conn.close()
        return dict(row) if row else {}


def list_threads(limit: int = 50, offset: int = 0, query: str | None = None) -> list[dict]:
    conn = _conn()
    conn.row_factory = sqlite3.Row
    q = (query or "").strip()
    if q:
        rows = conn.execute(
            """
            SELECT id, created_at, updated_at, title, pinned, metadata
            FROM conversation_threads
            WHERE COALESCE(title, '') LIKE ?
            ORDER BY pinned DESC, updated_at DESC, id DESC
            LIMIT ? OFFSET ?
            """,
            (f"%{q}%", limit, offset),
        ).fetchall()
    else:
        rows = conn.execute(
            """
            SELECT id, created_at, updated_at, title, pinned, metadata
            FROM conversation_threads
            ORDER BY pinned DESC, updated_at DESC, id DESC
            LIMIT ? OFFSET ?
            """,
            (limit, offset),
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def add_message(*, thread_id: int, role: str, content: str, metadata: dict | None = None) -> dict:
    role_norm = (role or "").strip().lower()
    if role_norm not in {"user", "assistant", "system"}:
        raise ValueError("role must be one of: user, assistant, system")
    with _WRITE_LOCK:
        conn = _conn()
        conn.row_factory = sqlite3.Row
        now = datetime.utcnow().isoformat()
        conn.execute(
            """
            INSERT INTO conversation_messages (thread_id, role, content, metadata, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                int(thread_id),
                role_norm,
                content,
                json.dumps(metadata) if metadata else None,
                now,
            ),
        )
        conn.execute(
            "UPDATE conversation_threads SET updated_at = ? WHERE id = ?",
            (now, int(thread_id)),
        )
        row = conn.execute("SELECT * FROM conversation_messages ORDER BY id DESC LIMIT 1").fetchone()
        conn.commit()
        conn.close()
        return dict(row) if row else {}


def list_messages(thread_id: int, limit: int = 200, offset: int = 0) -> list[dict]:
    conn = _conn()
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT id, created_at, thread_id, role, content, metadata
        FROM conversation_messages
        WHERE thread_id = ?
        ORDER BY id ASC
        LIMIT ? OFFSET ?
        """,
        (int(thread_id), limit, offset),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def delete_thread(thread_id: int) -> dict:
    """
    Delete a conversation thread and its messages.
    (No foreign key constraints are enforced, so we delete messages first.)
    """
    with _WRITE_LOCK:
        conn = _conn()
        conn.row_factory = sqlite3.Row
        tid = int(thread_id)
        row = conn.execute(
            "SELECT id, title, created_at, updated_at FROM conversation_threads WHERE id = ?",
            (tid,),
        ).fetchone()
        if not row:
            conn.close()
            return {"deleted": 0}
        c1 = conn.execute("DELETE FROM conversation_messages WHERE thread_id = ?", (tid,))
        c2 = conn.execute("DELETE FROM conversation_threads WHERE id = ?", (tid,))
        conn.commit()
        conn.close()
        return {"deleted": int(c2.rowcount or 0), "deleted_messages": int(c1.rowcount or 0), "thread": dict(row)}
