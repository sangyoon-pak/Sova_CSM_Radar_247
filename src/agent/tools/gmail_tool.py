"""Gmail fetch tool.

Uses gog CLI with keyring stored under GOG_HOME when set.
"""
import os
import subprocess
from pathlib import Path

from src.config import settings


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
    return result.stdout or "No emails found."
