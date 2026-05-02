"""SQLite database for interactions and cron jobs."""
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock
from typing import Optional, Sequence

from src.config import settings

_WRITE_LOCK = Lock()


def _utc_now_iso() -> str:
    """UTC instant for persisted timestamps; offset-aware so UIs parse as UTC."""
    return datetime.now(timezone.utc).isoformat()


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
    from src.agent.prompt_seed import seed_prompt_library_if_needed

    seed_prompt_library_if_needed()


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
        now = _utc_now_iso()
        conn.execute(
            """INSERT INTO agent_interactions (created_at, trigger_type, input_text, output_text, status, error_message, metadata)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                now,
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


def is_dashboard_probe_trigger(trigger_type: str | None) -> bool:
    """True for cron probes, thread Scan inbox, manual API probes (dashboard inbox review runs)."""
    return _is_probe_dashboard_trigger(trigger_type)


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


def get_interactions_by_ids(ids: Sequence[int]) -> dict[int, dict]:
    """Batch-load interactions for learning distillation (Run history context)."""
    uniq: list[int] = []
    seen: set[int] = set()
    for raw in ids:
        try:
            i = int(raw)
        except (TypeError, ValueError):
            continue
        if i <= 0 or i in seen:
            continue
        seen.add(i)
        uniq.append(i)
    if not uniq:
        return {}
    conn = _conn()
    conn.row_factory = sqlite3.Row
    qmarks = ",".join("?" * len(uniq))
    rows = conn.execute(
        f"""SELECT id, created_at, trigger_type, input_text, output_text, status, error_message, metadata
            FROM agent_interactions WHERE id IN ({qmarks})""",
        uniq,
    ).fetchall()
    conn.close()
    return {int(r["id"]): dict(r) for r in rows}


def _parse_interaction_metadata(raw: str | None) -> dict:
    if not raw:
        return {}
    try:
        out = json.loads(raw)
        return out if isinstance(out, dict) else {}
    except json.JSONDecodeError:
        return {}


def parse_interaction_metadata(raw: str | None | dict) -> dict:
    """Parse `agent_interactions.metadata` JSON (or pass through dict)."""
    if isinstance(raw, dict):
        return dict(raw)
    return _parse_interaction_metadata(raw if isinstance(raw, str) else None)


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


def _dashboard_actions_same_item(removed: dict, other: dict) -> bool:
    """
    True when two csm_actions entries refer to the same dashboard dedupe identity
    (Gmail thread id, or from+subject when thread id is absent). Used when removing
    a card so older probe runs do not keep a ghost row that blocks re-emission on the next probe.
    """
    if not isinstance(removed, dict) or not isinstance(other, dict):
        return False
    rg = str(removed.get("gmail_thread_id") or "").strip()
    og = str(other.get("gmail_thread_id") or "").strip()
    if rg and og:
        return rg == og
    if rg or og:
        return False
    efa = str(removed.get("email_from") or "").strip().lower()
    efb = str(other.get("email_from") or "").strip().lower()
    esa = str(removed.get("email_subject") or "").strip().lower()
    esb = str(other.get("email_subject") or "").strip().lower()
    return bool(efa and efb and esa and esb and efa == efb and esa == esb)


def _cascade_remove_dashboard_action_peers(
    conn: sqlite3.Connection,
    *,
    exclude_interaction_id: int,
    removed_action: dict,
) -> None:
    """Strip matching actions from other visible inbox-review interactions (same open connection)."""
    if not isinstance(removed_action, dict) or not removed_action:
        return
    where_probe = (
        "(trigger_type LIKE 'cron:%' OR trigger_type = 'thread_probe' "
        "OR trigger_type LIKE 'manual_probe%')"
    )
    rows = conn.execute(
        f"""SELECT id, metadata FROM agent_interactions
            WHERE id != ? AND {where_probe}
            AND NOT (COALESCE(json_extract(metadata, '$.csm_dashboard_removed'), 0) = 1)""",
        (exclude_interaction_id,),
    ).fetchall()
    for r in rows:
        rid = int(r["id"])
        # sqlite3.Row does not implement .get(); access by key directly.
        md = _parse_interaction_metadata(r["metadata"])
        acts = md.get("csm_actions")
        if not isinstance(acts, list):
            continue
        kept: list = []
        for a in acts:
            if isinstance(a, dict) and _dashboard_actions_same_item(removed_action, a):
                continue
            kept.append(a)
        if len(kept) == len(acts):
            continue
        md["csm_actions"] = kept
        if len(kept) == 0:
            md["csm_dashboard_removed"] = True
        conn.execute(
            "UPDATE agent_interactions SET metadata = ? WHERE id = ?",
            (json.dumps(md), rid),
        )


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
        raw = actions[action_index]
        removed_action = dict(raw) if isinstance(raw, dict) else {}
        actions = list(actions)
        actions.pop(action_index)
        md["csm_actions"] = actions
        if len(actions) == 0:
            md["csm_dashboard_removed"] = True
        conn.execute(
            "UPDATE agent_interactions SET metadata = ? WHERE id = ?",
            (json.dumps(md), interaction_id),
        )
        _cascade_remove_dashboard_action_peers(
            conn,
            exclude_interaction_id=interaction_id,
            removed_action=removed_action,
        )
        conn.commit()
        conn.close()
        return True


def set_csm_dashboard_action_status(interaction_id: int, action_index: int, status: str) -> bool:
    """Set one action status in metadata.csm_actions."""
    st = (status or "").strip().lower()
    if st not in {"not_started", "in_progress", "completed"}:
        return False
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
        item = dict(actions[action_index] or {})
        item["status"] = st
        actions[action_index] = item
        md["csm_actions"] = actions
        conn.execute(
            "UPDATE agent_interactions SET metadata = ? WHERE id = ?",
            (json.dumps(md), interaction_id),
        )
        conn.commit()
        conn.close()
        return True


def set_csm_dashboard_action_category(interaction_id: int, action_index: int, category: str) -> bool:
    """Set one action `category` in metadata.csm_actions (canonical probe categories)."""
    allowed = {"client_technical", "client_non_technical", "internal"}
    cat = (category or "").strip().lower()
    if cat not in allowed:
        return False
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
        item = dict(actions[action_index] or {})
        item["category"] = cat
        actions[action_index] = item
        md["csm_actions"] = actions
        conn.execute(
            "UPDATE agent_interactions SET metadata = ? WHERE id = ?",
            (json.dumps(md), interaction_id),
        )
        conn.commit()
        conn.close()
        return True


def latest_dashboard_actions_by_gmail_thread(limit: int = 800) -> dict[str, dict]:
    """
    Latest visible dashboard action per gmail_thread_id.
    Used to carry user status and reopen completed cards when new thread updates arrive.
    """
    rows = list_probe_interactions(limit=limit, offset=0, source="all", status_filter="all")
    out: dict[str, dict] = {}
    for r in rows:
        md = parse_interaction_metadata(r.get("metadata"))
        acts = md.get("csm_actions")
        if not isinstance(acts, list):
            continue
        for a in acts:
            if not isinstance(a, dict):
                continue
            gid = str(a.get("gmail_thread_id") or "").strip()
            ef = str(a.get("email_from") or "").strip().lower()
            es = str(a.get("email_subject") or "").strip().lower()
            keys: list[str] = []
            if gid:
                keys.append(f"gid:{gid}")
            if ef and es:
                keys.append(f"fs:{ef}||{es}")
            if not keys:
                continue
            enriched = dict(a)
            try:
                enriched["_probe_merge_interaction_id"] = int(r.get("id") or 0)
            except (TypeError, ValueError):
                enriched["_probe_merge_interaction_id"] = 0
            for k in keys:
                if k in out:
                    continue
                out[k] = enriched
    return out


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
        now = _utc_now_iso()
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


def list_kb_document_local_paths() -> list[str]:
    """
    Paths stored on kb_documents rows (for reconciling FTS/FAISS with the registry).
    Order is undefined; callers should dedupe and resolve under the KB root.
    """
    conn = _conn()
    rows = conn.execute(
        "SELECT path FROM kb_documents WHERE path IS NOT NULL AND TRIM(path) != ''"
    ).fetchall()
    conn.close()
    return [str(r[0]) for r in rows if r and r[0]]


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
        now = _utc_now_iso()
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
        now = _utc_now_iso()
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


def delete_app_setting(key: str) -> None:
    """Remove a key so runtime falls back to environment / defaults."""
    with _WRITE_LOCK:
        conn = _conn()
        conn.execute("DELETE FROM app_settings WHERE key = ?", (key,))
        conn.commit()
        conn.close()


def app_setting_is_set(key: str) -> bool:
    conn = _conn()
    row = conn.execute("SELECT 1 FROM app_settings WHERE key = ?", (key,)).fetchone()
    conn.close()
    return row is not None


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

    # Best-effort: tombstone + full FTS/FAISS rebuild from current registry (runs outside DB lock).
    try:
        from threading import Thread

        from src.agent.tools import doc_search

        kb_root = getattr(settings, "kb_path_resolved", None)
        if kb_root and removed_path:

            def _purge_search_after_delete() -> None:
                p = Path(removed_path)
                doc_search.tombstone_files([p])
                doc_search.reindex_kb(Path(kb_root))

            Thread(target=_purge_search_after_delete, daemon=True).start()
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
        now = _utc_now_iso()
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
            ORDER BY id ASC
            LIMIT ? OFFSET ?
            """,
            (limit, offset),
        ).fetchall()
    else:
        rows = conn.execute(
            """
            SELECT id, created_at, updated_at, url, title, tags, scope, enabled
            FROM rc_urls
            ORDER BY id ASC
            LIMIT ? OFFSET ?
            """,
            (limit, offset),
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def upsert_rc_url_tree_nodes(*, main_rc_url: str, nodes: list[dict]) -> int:
    """
    Upsert discovered URL tree nodes for one main RC URL.
    Returns number of processed nodes.
    """
    main = (main_rc_url or "").strip()
    if not main:
        raise ValueError("main_rc_url is required")
    if not nodes:
        return 0
    with _WRITE_LOCK:
        conn = _conn()
        now = _utc_now_iso()
        count = 0
        for n in nodes:
            u = str((n or {}).get("url") or "").strip()
            if not u:
                continue
            depth = int((n or {}).get("depth") or 0)
            if depth < 0:
                depth = 0
            parent_url = str((n or {}).get("parent_url") or "").strip() or None
            title = str((n or {}).get("title") or "").strip() or None
            meta = (n or {}).get("metadata")
            conn.execute(
                """
                INSERT INTO rc_url_tree (main_rc_url, url, depth, parent_url, title, metadata, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(main_rc_url, url) DO UPDATE SET
                  depth=excluded.depth,
                  parent_url=excluded.parent_url,
                  title=COALESCE(excluded.title, rc_url_tree.title),
                  metadata=COALESCE(excluded.metadata, rc_url_tree.metadata),
                  updated_at=excluded.updated_at
                """,
                (
                    main,
                    u,
                    depth,
                    parent_url,
                    title,
                    json.dumps(meta) if isinstance(meta, dict) else None,
                    now,
                ),
            )
            count += 1
        conn.commit()
        conn.close()
        return count


def list_rc_url_tree(main_rc_url: str, limit: int = 2000, offset: int = 0) -> list[dict]:
    main = (main_rc_url or "").strip()
    if not main:
        return []
    conn = _conn()
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT id, created_at, updated_at, main_rc_url, url, depth, parent_url, title, metadata
        FROM rc_url_tree
        WHERE main_rc_url = ?
        ORDER BY depth ASC, id ASC
        LIMIT ? OFFSET ?
        """,
        (main, limit, offset),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def list_rc_url_tree_by_host(host: str, enabled_main_only: bool = True, limit: int = 5000) -> list[dict]:
    h = (host or "").strip().lower()
    if not h:
        return []
    conn = _conn()
    conn.row_factory = sqlite3.Row
    if enabled_main_only:
        rows = conn.execute(
            """
            SELECT t.id, t.created_at, t.updated_at, t.main_rc_url, t.url, t.depth, t.parent_url, t.title, t.metadata
            FROM rc_url_tree t
            JOIN rc_urls r ON r.url = t.main_rc_url
            WHERE r.enabled = 1
              AND lower(replace(replace(t.main_rc_url, 'https://', ''), 'http://', '')) LIKE ? || '%'
            ORDER BY t.depth ASC, t.id ASC
            LIMIT ?
            """,
            (h, limit),
        ).fetchall()
    else:
        rows = conn.execute(
            """
            SELECT id, created_at, updated_at, main_rc_url, url, depth, parent_url, title, metadata
            FROM rc_url_tree
            WHERE lower(replace(replace(main_rc_url, 'https://', ''), 'http://', '')) LIKE ? || '%'
            ORDER BY depth ASC, id ASC
            LIMIT ?
            """,
            (h, limit),
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def clear_rc_url_tree(main_rc_url: str) -> int:
    main = (main_rc_url or "").strip()
    if not main:
        raise ValueError("main_rc_url is required")
    with _WRITE_LOCK:
        conn = _conn()
        cur = conn.execute("DELETE FROM rc_url_tree WHERE main_rc_url = ?", (main,))
        conn.commit()
        deleted = cur.rowcount or 0
        conn.close()
        return deleted


def rc_url_tree_summary(main_rc_url: str) -> dict:
    main = (main_rc_url or "").strip()
    if not main:
        return {"main_rc_url": "", "count": 0, "max_depth": 0, "updated_at": None}
    conn = _conn()
    conn.row_factory = sqlite3.Row
    row = conn.execute(
        """
        SELECT
          COUNT(*) AS cnt,
          COALESCE(MAX(depth), 0) AS max_depth,
          MAX(updated_at) AS updated_at
        FROM rc_url_tree
        WHERE main_rc_url = ?
        """,
        (main,),
    ).fetchone()
    conn.close()
    d = dict(row) if row else {}
    return {
        "main_rc_url": main,
        "count": int(d.get("cnt") or 0),
        "max_depth": int(d.get("max_depth") or 0),
        "updated_at": d.get("updated_at"),
    }


def set_rc_url_enabled(url: str, enabled: bool) -> None:
    u = (url or "").strip()
    if not u:
        raise ValueError("url is required")
    with _WRITE_LOCK:
        conn = _conn()
        now = _utc_now_iso()
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
        # Cascade delete discovered URL-tree nodes for this main URL.
        conn.execute("DELETE FROM rc_url_tree WHERE main_rc_url = ?", (u,))
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


def delete_all_agent_feedback() -> int:
    """Delete every row in agent_feedback (Run history + Action dashboard learning inputs)."""
    with _WRITE_LOCK:
        conn = _conn()
        cur = conn.execute("DELETE FROM agent_feedback")
        conn.commit()
        deleted = int(cur.rowcount or 0)
        conn.close()
        return deleted


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
        SELECT created_at, interaction_id, verdict, note, correction, metadata
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


def get_agent_learning_instructions_snapshot() -> dict:
    """Distilled feedback rules for Configure / GET /memory/learning (no LLM)."""
    conn = _conn()
    conn.row_factory = sqlite3.Row
    row = conn.execute(
        "SELECT value, updated_at FROM app_settings WHERE key = ?",
        ("agent_learning_instructions",),
    ).fetchone()
    conn.close()
    if not row:
        return {"instructions": "", "updated_at": None}
    return {
        "instructions": (row["value"] or "").strip(),
        "updated_at": row["updated_at"],
    }


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


def _normalize_thread_metadata_row(d: dict) -> dict:
    meta = d.get("metadata")
    if isinstance(meta, str) and meta.strip():
        try:
            d["metadata"] = json.loads(meta)
        except json.JSONDecodeError:
            d["metadata"] = {}
    elif meta is None:
        d["metadata"] = {}
    return d


def get_thread_by_id(thread_id: int) -> dict | None:
    conn = _conn()
    conn.row_factory = sqlite3.Row
    row = conn.execute(
        """
        SELECT id, created_at, updated_at, title, pinned, metadata
        FROM conversation_threads WHERE id = ?
        """,
        (int(thread_id),),
    ).fetchone()
    conn.close()
    if not row:
        return None
    return _normalize_thread_metadata_row(dict(row))


def find_action_review_thread(source_interaction_id: int, action_index: int) -> dict | None:
    """Return existing Workbench thread scoped to one probe action (dashboard card), if any."""
    sid = int(source_interaction_id)
    idx = int(action_index)
    conn = _conn()
    conn.row_factory = sqlite3.Row
    row = conn.execute(
        """
        SELECT id, created_at, updated_at, title, pinned, metadata
        FROM conversation_threads
        WHERE json_extract(metadata, '$.kind') = 'action_review'
          AND CAST(json_extract(metadata, '$.source_interaction_id') AS INTEGER) = ?
          AND CAST(json_extract(metadata, '$.action_index') AS INTEGER) = ?
        LIMIT 1
        """,
        (sid, idx),
    ).fetchone()
    conn.close()
    if row:
        return _normalize_thread_metadata_row(dict(row))
    # Fallback if json_extract unavailable or legacy rows
    conn = _conn()
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT id, created_at, updated_at, title, pinned, metadata
        FROM conversation_threads
        ORDER BY id DESC
        LIMIT 800
        """
    ).fetchall()
    conn.close()
    for r in rows:
        d = _normalize_thread_metadata_row(dict(r))
        m = d.get("metadata") or {}
        if not isinstance(m, dict):
            continue
        if (
            m.get("kind") == "action_review"
            and int(m.get("source_interaction_id") or -1) == sid
            and int(m.get("action_index") or -1) == idx
        ):
            return d
    return None


def create_thread(*, title: str | None = None, pinned: bool = False, metadata: dict | None = None) -> dict:
    with _WRITE_LOCK:
        conn = _conn()
        conn.row_factory = sqlite3.Row
        now = _utc_now_iso()
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
        return _normalize_thread_metadata_row(dict(row)) if row else {}


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
        now = _utc_now_iso()
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


def _delete_one_thread_unlocked(conn: sqlite3.Connection, thread_id: int) -> dict | None:
    """
    Delete one thread using an open connection (caller holds _WRITE_LOCK and commits).
    Returns None if the thread did not exist; otherwise the same shape as delete_thread.
    """
    conn.row_factory = sqlite3.Row
    tid = int(thread_id)
    row = conn.execute(
        "SELECT id, title, created_at, updated_at FROM conversation_threads WHERE id = ?",
        (tid,),
    ).fetchone()
    if not row:
        return None
    c0 = conn.execute(
        """
        DELETE FROM agent_interactions
        WHERE json_extract(metadata, '$.thread_id') IS NOT NULL
          AND (
            CAST(json_extract(metadata, '$.thread_id') AS INTEGER) = ?
            OR CAST(json_extract(metadata, '$.thread_id') AS TEXT) = ?
          )
        """,
        (tid, str(tid)),
    )
    c1 = conn.execute("DELETE FROM conversation_messages WHERE thread_id = ?", (tid,))
    c2 = conn.execute("DELETE FROM conversation_threads WHERE id = ?", (tid,))
    return {
        "deleted": int(c2.rowcount or 0),
        "deleted_messages": int(c1.rowcount or 0),
        "deleted_interactions": int(c0.rowcount or 0),
        "thread": dict(row),
    }


def delete_thread(thread_id: int) -> dict:
    """
    Delete a conversation thread, its messages, and agent_interactions rows
    whose metadata.thread_id points at this thread (Workbench memory + related run log).
    Cron / dashboard probe interactions without that metadata are unchanged.
    """
    with _WRITE_LOCK:
        conn = _conn()
        try:
            out = _delete_one_thread_unlocked(conn, thread_id)
            conn.commit()
            if out is None:
                return {"deleted": 0, "deleted_messages": 0, "deleted_interactions": 0}
            return out
        finally:
            conn.close()


def delete_threads(thread_ids: list) -> dict:
    """
    Delete many threads in one transaction. Unknown ids are skipped (per-id deleted: 0).
    At most 200 ids per call.
    """
    seen: set[int] = set()
    clean: list[int] = []
    for x in thread_ids or []:
        try:
            tid = int(x)
        except (TypeError, ValueError):
            continue
        if tid <= 0 or tid in seen:
            continue
        seen.add(tid)
        clean.append(tid)
    if len(clean) > 200:
        raise ValueError("At most 200 thread ids per bulk delete.")
    results: list[dict] = []
    deleted_threads = 0
    total_messages = 0
    total_interactions = 0
    with _WRITE_LOCK:
        conn = _conn()
        try:
            for tid in clean:
                out = _delete_one_thread_unlocked(conn, tid)
                if out is None:
                    results.append(
                        {
                            "thread_id": tid,
                            "deleted": 0,
                            "deleted_messages": 0,
                            "deleted_interactions": 0,
                        }
                    )
                else:
                    deleted_threads += 1
                    total_messages += int(out.get("deleted_messages") or 0)
                    total_interactions += int(out.get("deleted_interactions") or 0)
                    results.append(
                        {
                            "thread_id": tid,
                            "deleted": int(out.get("deleted") or 0),
                            "deleted_messages": int(out.get("deleted_messages") or 0),
                            "deleted_interactions": int(out.get("deleted_interactions") or 0),
                            "title": (out.get("thread") or {}).get("title"),
                        }
                    )
            conn.commit()
        finally:
            conn.close()
    return {
        "deleted_threads": deleted_threads,
        "deleted_messages": total_messages,
        "deleted_interactions": total_interactions,
        "results": results,
    }
