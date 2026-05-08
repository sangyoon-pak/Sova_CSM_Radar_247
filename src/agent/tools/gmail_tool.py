"""Gmail fetch tool.

Uses gog CLI with keyring stored under GOG_HOME when set.
"""
import os
import re
import subprocess
from pathlib import Path

from src.runtime_config import (
    effective_gog_account,
    effective_gog_keyring_backend,
    effective_gog_keyring_password,
    effective_probe_inbox_gmail_search,
    effective_xdg_config_home,
    gog_credentials_path_resolved,
    gog_home_resolved,
)

# Minimal thread signal: Korean in decoded `subject\t` lines (same source as JSON `email_subject`).
_HANGUL_RE = re.compile(r"[\uac00-\ud7a3]")
# Few false positives; real Korean client subjects almost always exceed this.
_KO_SUBJECT_HANGUL_MIN = 3


def _subject_tails_concat(block: str) -> str:
    parts: list[str] = []
    for line in (block or "").splitlines():
        low = line.lower()
        if low.startswith("subject\t"):
            tail = line.split("\t", 1)[-1].strip()
            if tail:
                parts.append(tail)
    return " ".join(parts)


def _hangul_count(text: str) -> int:
    return len(_HANGUL_RE.findall(text or ""))


def _probe_language_footer_parts(block: str) -> tuple[str, str]:
    """
    Tag each decoded thread/email block for probes.

    - **ko**: only when `subject\\t` lines contain enough Hangul — strong signal the client-visible
      thread title is Korean (models still often default to English without this nudge).
    - **inferred**: otherwise the model picks language from the substantive customer body per the note.
    """
    subjects = _subject_tails_concat(block)
    if _hangul_count(subjects) >= _KO_SUBJECT_HANGUL_MIN:
        note = (
            "MANDATORY: Korean (Hangul) appears in this block's decoded subject line(s). Write **every** JSON string field "
            "for this thread's action in **Korean (한국어)** — title, brief, thread_title, curated_answer, every "
            "subquery/answer, technical_rationale, escalation_guidance, next_steps, thread_summary, skipped_note. "
            "Paraphrase English KB or internal replies into Korean for those fields; keep standard product names in Latin if needed."
        )
        return "ko", note
    note = (
        "You decide the language for this thread's dashboard JSON string fields from the **customer's "
        "primary question or request**. Prefer the **main body** of the earliest substantive **external client** "
        "message (and its subject), not a later internal line in another language (e.g. 'Thanks, looping in…'). "
        "Apply that language consistently to title, brief, curated_answer, subquery_answers, technical_rationale, "
        "escalation_guidance, next_steps, and thread_summary. If the substantive ask mixes languages, follow the "
        "language of the core ask. KB snippets may be English — still write dashboard prose in the client's language."
    )
    return "inferred", note


def _append_csm_language_footer(block: str) -> str:
    """Append csm_output_language (ko | inferred) and note to one decoded email/thread blob."""
    b = (block or "").strip()
    if not b:
        return b
    lang, note = _probe_language_footer_parts(b)
    note_one = note.replace("\n", " ")
    return b + f"\n\ncsm_output_language\t{lang}\ncsm_output_language_note\t{note_one}\n"


_PROBE_PREFLIGHT_TRAILER_HEADER = "PROBE_PREFLIGHT"
_PROBE_PREFLIGHT_SKIP_KEY = "RETRIEVAL_SKIP_THREAD_IDS"


def _build_probe_preflight_trailer(inbox_blob: str) -> str:
    """Return a `PROBE_PREFLIGHT: ...` trailer for the inbox tool output, or empty string.

    For threads whose latest Gmail message id matches the previously persisted
    `gmail_latest_message_id` on a still-visible dashboard card, list them under
    `RETRIEVAL_SKIP_THREAD_IDS` so the model can skip `search_product_docs` /
    `search_rc_web` / `fetch_gmail_thread` for those threads. Merge-time fingerprint
    skip in `merge_csm_actions_metadata` remains the safety net.
    """
    text = (inbox_blob or "").strip()
    if not text:
        return ""
    try:
        from src.agent.probe_actions import parse_inbox_tool_output_thread_message_ids
        from src.db import database
    except Exception:
        return ""

    msg_id_by_tid = parse_inbox_tool_output_thread_message_ids(text)
    if not msg_id_by_tid:
        return ""
    try:
        prev_by_thread = database.latest_dashboard_actions_by_gmail_thread()
    except Exception:
        return ""

    skip_pairs: list[tuple[str, str]] = []
    for gid, msg_id in msg_id_by_tid.items():
        prev = prev_by_thread.get(f"gid:{gid}")
        if not isinstance(prev, dict):
            continue
        prev_msg_id = str(prev.get("gmail_latest_message_id") or "").strip()
        if not prev_msg_id or prev_msg_id != msg_id:
            continue
        skip_pairs.append((gid, msg_id))

    if not skip_pairs:
        return ""
    ids = ",".join(g for g, _ in skip_pairs)
    return (
        f"\n\n{_PROBE_PREFLIGHT_TRAILER_HEADER}\n"
        f"{_PROBE_PREFLIGHT_SKIP_KEY}={ids}\n"
        "REASON\tlatest gmail message id matches the dashboard card on the previous probe; "
        "no new mail since last run\n"
    )


def _annotate_blocks_with_csm_lang(blob: str) -> str:
    """
    Append `csm_output_language` after each inbox thread block (split on 60 '=').
    Uses **ko** when subject lines show enough Hangul; otherwise **inferred** + LLM-chosen language from body.
    """
    blob = (blob or "").strip()
    if not blob:
        return blob
    sep = "\n" + "=" * 60 + "\n"
    parts = blob.split(sep)
    out: list[str] = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        out.append(_append_csm_language_footer(p))
    return sep.join(out) if len(out) > 1 else (out[0] if out else blob)


def _maybe_bootstrap_oauth(env: dict[str, str], project_root: Path) -> str | None:
    """
    Best-effort bootstrap:
    - ensure XDG_CONFIG_HOME exists under GOG_HOME
    - if OAuth client credentials haven't been registered yet, register them if we can find a credentials.json
    Returns an error string on hard failure, else None.
    """
    xdg = Path(env.get("XDG_CONFIG_HOME") or "")
    if xdg:
        try:
            xdg.mkdir(parents=True, exist_ok=True)
        except Exception:
            # Non-fatal; gog may still work with defaults.
            pass

    home = Path(env.get("HOME") or "")

    # If credentials already registered, nothing to do.
    # Best-effort checks for both XDG + macOS default location under HOME.
    gog_cfg_dir = xdg / "gog" if xdg else None
    mac_cfg = home / "Library" / "Application Support" / "gogcli" / "credentials.json" if home else None
    if (gog_cfg_dir and (gog_cfg_dir / "credentials.json").exists()) or (mac_cfg and mac_cfg.exists()):
        return None

    # Find a credentials.json to register (prefer explicit setting).
    candidates: list[Path] = []
    explicit = gog_credentials_path_resolved()
    if explicit:
        candidates.append(explicit)
    # In-repo location (this project only; set GOG_CREDENTIALS_PATH for another path).
    candidates.append(project_root / "credentials.json")
    cred = next((p for p in candidates if p.exists()), None)
    if not cred:
        return (
            "Missing OAuth client credentials.\n"
            f"Tried: {', '.join(str(p) for p in candidates)}\n"
            "Place Google OAuth client JSON at the repo root (e.g. Sova_CSM_Radar_247/credentials.json) or set GOG_CREDENTIALS_PATH, "
            "then run OAuth once (docs/GMAIL_SETUP.md)."
        )

    # Place credentials where gogcli expects them (macOS default path) as a safety net.
    if mac_cfg and not mac_cfg.exists():
        try:
            mac_cfg.parent.mkdir(parents=True, exist_ok=True)
            mac_cfg.write_bytes(cred.read_bytes())
        except Exception:
            pass

    # Register credentials with gog (best-effort). This does NOT complete OAuth token flow.
    gog_bin = env.get("GOG_BIN") or "gog"
    try:
        subprocess.run(
            [gog_bin, "auth", "credentials", str(cred)],
            capture_output=True,
            text=True,
            timeout=30,
            env={**env, **os.environ},
        )
    except Exception:
        # Non-fatal; next command will surface exact error.
        return None
    return None


def _gog_env() -> dict[str, str]:
    # If GOG_HOME is set, treat it as a self-contained gog home dir.
    gog_home = gog_home_resolved()
    if gog_home:
        home = str(gog_home.resolve())
        gog_bin_path = f"{home}/bin/gog"
        path = f"{home}/bin:{os.environ.get('PATH', '')}"
    else:
        home = os.environ.get("HOME", os.path.expanduser("~"))
        gog_bin_path = "gog"
        path = f"{home}/.local/bin:{os.environ.get('PATH', '')}"
    kr_pw = effective_gog_keyring_password()
    xdg = effective_xdg_config_home()
    if not xdg:
        xdg = f"{home}/.config"
    acct = effective_gog_account()
    env = {
        "HOME": home,
        "PATH": path,
        "GOG_HOME": home,
        "GOG_BIN": gog_bin_path,
        "GMAIL_SCRIPT_LOCAL": "1",
        "GOG_KEYRING_BACKEND": effective_gog_keyring_backend() or "file",
        "GOG_KEYRING_PASSWORD": kr_pw,
        "GOG_ACCOUNT": acct,
        "XDG_CONFIG_HOME": xdg,
    }
    return env


def fetch_inbox_emails(search: str | None = None, max_results: int = 10) -> str:
    q = (search or "").strip() or effective_probe_inbox_gmail_search()
    # Project root: src/agent/tools/ -> 3 levels up
    project_root = Path(__file__).parent.parent.parent.parent
    script_path = project_root / "scripts" / "gmail-get-decoded.py"
    if not script_path.exists():
        return "Error: gmail-get-decoded.py not found."
    # Ensure our gog env overrides any inherited shell vars.
    env = {**os.environ, **_gog_env()}
    bootstrap_err = _maybe_bootstrap_oauth(env, project_root)
    if bootstrap_err:
        return f"Error fetching Gmail: {bootstrap_err}\n\nRun OAuth locally: see docs/GMAIL_SETUP.md"
    try:
        result = subprocess.run(
            ["python3", str(script_path), "--search", q, "--max", str(max_results)],
            capture_output=True, text=True, timeout=90, env=env,
        )
    except subprocess.TimeoutExpired:
        return "Error: Gmail fetch timed out."
    except FileNotFoundError:
        return "Error: python3 or gmail-get-decoded.py not found."
    if result.returncode != 0:
        err = result.stderr or result.stdout or "Unknown error"
        if "No auth" in err or "No tokens" in err:
            err += "\n\nRun OAuth locally: see docs/GMAIL_SETUP.md"
        return f"Error fetching Gmail: {err}"
    raw = (result.stdout or "").strip()
    if raw:
        raw = _annotate_blocks_with_csm_lang(raw)
        # Probe-only: append a preflight trailer listing thread ids whose latest gmail message id
        # equals the one we already persisted on the dashboard card. The probe system prompt
        # (`probe_hint`) tells the model not to run KB/web/thread retrieval for those ids.
        try:
            from src.agent.email_agent import is_probe_mode_active
        except Exception:
            is_probe_mode_active = lambda: False  # noqa: E731
        if is_probe_mode_active():
            trailer = _build_probe_preflight_trailer(raw)
            if trailer:
                raw = raw + trailer
    # Stash the inbox blob so the KB planner can expand subqueries from the actual
    # customer emails rather than the probe instruction prompt.
    try:
        from src.agent.email_agent import record_gmail_tool_output
        record_gmail_tool_output(raw)
    except Exception:
        pass
    return raw or "No emails found."


_GMAIL_THREAD_ID_RE = re.compile(r"^[a-zA-Z0-9_-]{6,128}$")


def fetch_gmail_thread(thread_id: str) -> str:
    """
    Fetch and decode every message in one Gmail thread (gog: gmail thread get).
    Use the thread id from inbox fetch lines `thread_id\t...`.
    """
    tid = (thread_id or "").strip()
    if not tid or not _GMAIL_THREAD_ID_RE.match(tid):
        return (
            "Error: Invalid Gmail thread id. Use the value after `thread_id` from fetch_inbox_emails "
            "(alphanumeric, 6–128 chars)."
        )
    project_root = Path(__file__).parent.parent.parent.parent
    script_path = project_root / "scripts" / "gmail-get-decoded.py"
    if not script_path.exists():
        return "Error: gmail-get-decoded.py not found."
    env = {**os.environ, **_gog_env()}
    bootstrap_err = _maybe_bootstrap_oauth(env, project_root)
    if bootstrap_err:
        return f"Error fetching Gmail: {bootstrap_err}\n\nRun OAuth locally: see docs/GMAIL_SETUP.md"
    try:
        result = subprocess.run(
            ["python3", str(script_path), tid, "thread"],
            capture_output=True,
            text=True,
            timeout=120,
            env=env,
        )
    except subprocess.TimeoutExpired:
        return "Error: Gmail thread fetch timed out."
    except FileNotFoundError:
        return "Error: python3 or gmail-get-decoded.py not found."
    if result.returncode != 0:
        err = result.stderr or result.stdout or "Unknown error"
        if "No auth" in err or "No tokens" in err:
            err += "\n\nRun OAuth locally: see docs/GMAIL_SETUP.md"
        return f"Error fetching Gmail thread: {err}"
    raw = (result.stdout or "").strip()
    if raw and not re.search(r"(?m)^csm_output_language\t", raw):
        raw = _append_csm_language_footer(raw)
    # Same purpose as in `fetch_inbox_emails`: feed the planner real thread content.
    try:
        from src.agent.email_agent import record_gmail_tool_output
        record_gmail_tool_output(raw)
    except Exception:
        pass
    return raw or "No messages in thread."
