"""Gmail fetch tool.

Uses gog CLI with keyring stored under GOG_HOME when set.
"""
import os
import re
import subprocess
from pathlib import Path

from src.config import settings

_HANGUL_RE = re.compile(r"[\uac00-\ud7a3]")
_LATIN_RE = re.compile(r"[A-Za-z]")
# Stop scoring at typical reply/forward delimiters (English chain below drowns out Korean lead).
_QUOTE_OR_FORWARD_SPLIT = re.compile(
    r"(?is)"
    r"(?:\n-{3,}\s*Original Message\s*-{3,}\s*\n|"
    r"\n-{3,}\s*Forwarded message\s*-{3,}\s*\n|"
    r"\n={20,}\s*\n|"
    r"\n_{10,}\s*\n|"
    r"\n\*{5,}\s*\n|"
    r"\n보낸 사람\s*:|"
    r"\n보낸 날짜\s*:|"
    r"\n발신자\s*:|"
    r"\n-----Original Message-----\s*\n|"
    r"\nOn .{1,200} wrote:\s*\n|"
    r"\nFrom:\s*.+\nSent:\s*.+\n|"
    r"\nGet Outlook for\s|"
    r"\nSent from my iPhone)"
)
_META_PREFIXES = (
    "id\t",
    "thread_id\t",
    "label_ids\t",
    "from\t",
    "to\t",
    "subject\t",
    "date\t",
    "attachment\t",
    "csm_output_language\t",
)


def _body_text_for_lang_detection(block: str) -> str:
    """Strip Gmail header lines so English headers do not drown out Korean body."""
    lines_out: list[str] = []
    for line in block.splitlines():
        low = line.lower()
        if any(low.startswith(p) for p in _META_PREFIXES):
            continue
        lines_out.append(line)
    return "\n".join(lines_out)


def _lead_body_for_lang(block: str) -> str:
    """
    Only the customer's top message (before quoted thread / forward blocks).
    Full bodies often have huge English chains that wrongly force `en`.
    """
    body = _body_text_for_lang_detection(block)
    m = _QUOTE_OR_FORWARD_SPLIT.search(body)
    if m:
        body = body[: m.start()]
    return body[:5000].strip()


def _detect_csm_output_language(block: str) -> str:
    """
    Infer language the CSM dashboard strings should use for this thread.
    Returns 'ko', 'en', or 'mixed'.
    """
    lead = _lead_body_for_lang(block)
    h = len(_HANGUL_RE.findall(lead))
    ell = len(_LATIN_RE.findall(lead))
    # Bias Korean: short Korean asks are common; product terms add Latin without meaning "English email".
    if h >= 10:
        return "ko"
    if h >= 6 and (ell < 200 or h >= ell * 0.07):
        return "ko"
    if h >= 4 and ell < 90:
        return "ko"
    if h <= 2 and ell >= 50:
        return "en"
    if h >= 5 and ell >= 120:
        return "mixed"
    if h >= 6:
        return "ko"
    if ell > max(80, h * 12):
        return "en"
    return "mixed"


def _csm_lang_note(lang: str) -> str:
    if lang == "ko":
        return "MANDATORY: write every JSON string field in Korean (한국어). Do not use English for title/brief/answers."
    if lang == "en":
        return "MANDATORY: write every JSON string field in English."
    return "Match the customer's language mix; prefer Korean for Korean sentences and English for English quotes."


def _annotate_blocks_with_csm_lang(blob: str) -> str:
    """
    Append `csm_output_language\tko|en|mixed` after each inbox thread block (split on 60 '=').
    The probe model must follow this for dashboard JSON strings.
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
        lang = _detect_csm_output_language(p)
        note = _csm_lang_note(lang).replace("\n", " ")
        out.append(p + f"\n\ncsm_output_language\t{lang}\ncsm_output_language_note\t{note}\n")
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
    explicit = settings.gog_credentials_path_resolved
    if explicit:
        candidates.append(explicit)
    # Common in-repo locations.
    candidates.append(project_root / "credentials.json")
    candidates.append(project_root.parent / "openclaw_project" / "credentials.json")
    cred = next((p for p in candidates if p.exists()), None)
    if not cred:
        return (
            "Missing OAuth client credentials.\n"
            f"Tried: {', '.join(str(p) for p in candidates)}\n"
            "Place Google OAuth client JSON at email_draft_agent/credentials.json or set GOG_CREDENTIALS_PATH, "
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
    gog_home = settings.gog_home_resolved
    if gog_home:
        home = str(gog_home.resolve())
        gog_bin_path = f"{home}/bin/gog"
        path = f"{home}/bin:{os.environ.get('PATH', '')}"
    else:
        home = os.environ.get("HOME", os.path.expanduser("~"))
        gog_bin_path = "gog"
        path = f"{home}/.local/bin:{os.environ.get('PATH', '')}"
    env = {
        "HOME": home,
        "PATH": path,
        "GOG_HOME": home,
        "GOG_BIN": gog_bin_path,
        "GMAIL_SCRIPT_LOCAL": "1",
        "GOG_KEYRING_BACKEND": settings.gog_keyring_backend or "file",
        "GOG_KEYRING_PASSWORD": settings.gog_keyring_password or "openclaw-gmail",
        "GOG_ACCOUNT": settings.gog_account or "sangyoon.park@appier.com",
        "XDG_CONFIG_HOME": settings.xdg_config_home or f"{home}/.config",
    }
    return env


def fetch_inbox_emails(search: str = "in:inbox category:primary newer_than:2d", max_results: int = 10) -> str:
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
            ["python3", str(script_path), "--search", search, "--max", str(max_results)],
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
        _lang = _detect_csm_output_language(raw)
        _note = _csm_lang_note(_lang).replace("\n", " ")
        raw = raw + f"\n\ncsm_output_language\t{_lang}\ncsm_output_language_note\t{_note}\n"
    return raw or "No messages in thread."
