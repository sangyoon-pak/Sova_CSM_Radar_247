"""Read project `.env` for Configure UI (read-only; does not change process env)."""
from __future__ import annotations

import re
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_DOTENV_PATH = _PROJECT_ROOT / ".env"

# Keys we surface in the Configure sync table (subset of what the app may use).
TRACKED_ENV_KEYS: tuple[str, ...] = (
    "LLM_PROVIDER_PRESET",
    "OPENROUTER_API_KEY",
    "OPENAI_API_KEY",
    "OPENROUTER_BASE_URL",
    "LLM_MODEL",
    "LLM_MODEL_MAIN",
    "LLM_MODEL_SEARCH_JSON",
    "LLM_MODEL_SEARCH_RERANK",
    "LLM_MODEL_MEMORY",
    "RAG_EMBEDDING_PROVIDER",
    "RAG_EMBEDDING_MODEL",
    "GOG_HOME",
    "GOG_ACCOUNT",
    "GOG_KEYRING_BACKEND",
    "GOG_KEYRING_PASSWORD",
    "XDG_CONFIG_HOME",
    "GOG_CREDENTIALS_PATH",
    "LANGSMITH_API_KEY",
)


def dotenv_path() -> Path:
    return _DOTENV_PATH


def read_dotenv_file(path: Path | None = None) -> dict[str, str]:
    """Parse KEY=VALUE lines (best-effort; supports quoted values)."""
    p = path or _DOTENV_PATH
    if not p.exists():
        return {}
    try:
        raw = p.read_text(encoding="utf-8")
    except OSError:
        return {}
    out: dict[str, str] = {}
    for line in raw.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if "=" not in s:
            continue
        key, _, rest = s.partition("=")
        key = key.strip()
        val = rest.strip()
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
        if key:
            out[key] = val
    return out


_SENSITIVE_KEY = re.compile(
    r"(?i)(key|secret|password|token|credential)",
)


def mask_env_display(key: str, value: str) -> str:
    if not value:
        return ""
    if _SENSITIVE_KEY.search(key):
        return "••••••••" if len(value) > 6 else "••••"
    if len(value) > 120:
        return value[:117] + "…"
    return value


def dotenv_snapshot_for_ui() -> dict:
    """Masked key→value map for tracked keys present in the file."""
    full = read_dotenv_file()
    out: dict[str, str] = {}
    for k in TRACKED_ENV_KEYS:
        if k in full:
            out[k] = mask_env_display(k, full[k])
    # Include any other keys from file that look LLM-related (optional discover)
    for k, v in sorted(full.items()):
        if k in out:
            continue
        if k.startswith("LLM_") or k.startswith("RAG_") or k.startswith("OPEN") or k.startswith("GOG"):
            out[k] = mask_env_display(k, v)
    return out
