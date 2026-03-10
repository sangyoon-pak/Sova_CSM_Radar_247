"""Gmail fetch tool. Uses gog CLI with credentials from openclaw_project when GOG_HOME is set."""
import os
import subprocess
from pathlib import Path

from src.config import settings


def _gog_env() -> dict[str, str]:
    # Use openclaw_project's gog credentials when GOG_HOME is set
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
    env = {**_gog_env(), **os.environ}
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
