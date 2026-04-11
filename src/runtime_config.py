"""
Effective runtime configuration: values saved via Configure UI (app_settings)
override environment-backed `Settings` from `src/config.py`.
"""
from __future__ import annotations

from pathlib import Path

from src.config import settings
from src.db import database
from src.env_file import dotenv_path, dotenv_snapshot_for_ui, mask_env_display


def _db_str(key: str) -> str | None:
    if not database.app_setting_is_set(key):
        return None
    v = database.get_app_setting(key, "")
    if v is None:
        return None
    return str(v)


def effective_llm_model() -> str:
    v = _db_str("llm_model")
    if v is not None and v.strip():
        return v.strip()
    return settings.llm_model.strip()


def effective_llm_model_main() -> str:
    v = _db_str("llm_model_main")
    if v is not None and v.strip():
        return v.strip()
    return settings.llm_model_for_main


def effective_llm_model_search_json() -> str:
    v = _db_str("llm_model_search_json")
    if v is not None and v.strip():
        return v.strip()
    return settings.llm_model_for_search_json


def effective_llm_model_search_rerank() -> str:
    v = _db_str("llm_model_search_rerank")
    if v is not None and v.strip():
        return v.strip()
    return settings.llm_model_for_search_rerank


def effective_llm_model_memory() -> str:
    v = _db_str("llm_model_memory")
    if v is not None and v.strip():
        return v.strip()
    return settings.llm_model_for_memory


def effective_rag_embedding_provider() -> str:
    v = _db_str("rag_embedding_provider")
    if v is not None and v.strip():
        return v.strip()
    return (settings.rag_embedding_provider or "openrouter").strip()


def effective_rag_embedding_model() -> str:
    v = _db_str("rag_embedding_model")
    if v is not None and v.strip():
        return v.strip()
    return (settings.rag_embedding_model or "").strip()


_VALID_PRESETS = frozenset({"openrouter", "openai", "gemini_openrouter"})
_DEFAULT_OPENAI_BASE = "https://api.openai.com/v1"


def effective_llm_provider_preset() -> str:
    v = _db_str("llm_provider_preset")
    if v is not None and v.strip():
        s = v.strip().lower()
        if s in _VALID_PRESETS:
            return s
    raw = (getattr(settings, "llm_provider_preset", None) or "openrouter").strip().lower()
    return raw if raw in _VALID_PRESETS else "openrouter"


def effective_chat_api_key() -> str | None:
    """API key for ChatOpenAI-compatible calls (OpenRouter, OpenAI direct, or Gemini-via-OR)."""
    if database.app_setting_is_set("openrouter_api_key"):
        v = (database.get_app_setting("openrouter_api_key") or "").strip()
        if v:
            return v
    preset = effective_llm_provider_preset()
    if preset == "openai":
        oa = getattr(settings, "openai_api_key", None)
        if oa and str(oa).strip():
            return str(oa).strip()
        or_k = settings.openrouter_api_key
        if or_k and str(or_k).strip():
            return str(or_k).strip()
        return None
    return settings.openrouter_api_key


def effective_chat_base_url() -> str:
    v = _db_str("openrouter_base_url")
    if v is not None and v.strip():
        return v.strip()
    preset = effective_llm_provider_preset()
    if preset == "openai":
        return _DEFAULT_OPENAI_BASE
    return settings.openrouter_base_url.strip()


def effective_openrouter_api_key() -> str | None:
    return effective_chat_api_key()


def effective_openrouter_base_url() -> str:
    return effective_chat_base_url()


def effective_gog_home() -> str:
    v = _db_str("gog_home")
    if v is not None:
        return v.strip()
    return (settings.gog_home or "").strip()


def gog_home_resolved() -> Path | None:
    raw = effective_gog_home()
    if not raw:
        return None
    p = Path(raw)
    if not p.is_absolute():
        root = Path(__file__).resolve().parent.parent
        p = (root / p).resolve()
    return p if p.exists() else None


def effective_gog_account() -> str:
    v = _db_str("gog_account")
    if v is not None:
        return v.strip()
    return (settings.gog_account or "").strip()


def effective_gog_keyring_backend() -> str:
    v = _db_str("gog_keyring_backend")
    if v is not None and v.strip():
        return v.strip()
    return (settings.gog_keyring_backend or "file").strip()


def effective_gog_keyring_password() -> str:
    v = _db_str("gog_keyring_password")
    if v is not None:
        return v.strip()
    return (settings.gog_keyring_password or "").strip()


def effective_xdg_config_home() -> str:
    v = _db_str("xdg_config_home")
    if v is not None:
        return v.strip()
    return (settings.xdg_config_home or "").strip()


def effective_gog_credentials_path() -> str:
    v = _db_str("gog_credentials_path")
    if v is not None:
        return v.strip()
    return (settings.gog_credentials_path or "").strip()


def gog_credentials_path_resolved() -> Path | None:
    p_raw = effective_gog_credentials_path().strip()
    if not p_raw:
        return None
    p = Path(p_raw)
    if not p.is_absolute():
        root = Path(__file__).resolve().parent.parent
        p = (root / p).resolve()
    return p if p.exists() else None


def _mask_env_row(key: str, val: str) -> str:
    if not val:
        return ""
    return mask_env_display(key, val)


def runtime_settings_snapshot() -> dict:
    """Payload for GET /settings/runtime (values + metadata for the Configure UI)."""
    keys_db = [
        "llm_provider_preset",
        "llm_model",
        "llm_model_main",
        "llm_model_search_json",
        "llm_model_search_rerank",
        "llm_model_memory",
        "rag_embedding_provider",
        "rag_embedding_model",
        "openrouter_api_key",
        "openrouter_base_url",
        "gog_home",
        "gog_account",
        "gog_keyring_backend",
        "gog_keyring_password",
        "xdg_config_home",
        "gog_credentials_path",
    ]
    stored = {k: database.app_setting_is_set(k) for k in keys_db}
    or_key_db = database.app_setting_is_set("openrouter_api_key") and bool(
        (database.get_app_setting("openrouter_api_key") or "").strip()
    )
    gog_pw_db = database.app_setting_is_set("gog_keyring_password") and bool(
        (database.get_app_setting("gog_keyring_password") or "").strip()
    )
    oai_k = getattr(settings, "openai_api_key", None) or ""
    dotenv_p = dotenv_path()
    env_from_pydantic = {
        "llm_provider_preset": getattr(settings, "llm_provider_preset", "openrouter") or "openrouter",
        "llm_model": settings.llm_model,
        "llm_model_main": settings.llm_model_main or "",
        "llm_model_search_json": settings.llm_model_search_json or "",
        "llm_model_search_rerank": settings.llm_model_search_rerank or "",
        "llm_model_memory": settings.llm_model_memory or "",
        "rag_embedding_provider": settings.rag_embedding_provider,
        "rag_embedding_model": settings.rag_embedding_model,
        "openrouter_base_url": settings.openrouter_base_url,
        "openrouter_api_key": settings.openrouter_api_key or "",
        "openai_api_key": oai_k,
        "gog_home": settings.gog_home or "",
        "gog_account": settings.gog_account or "",
        "gog_keyring_backend": settings.gog_keyring_backend or "",
        "gog_keyring_password": settings.gog_keyring_password or "",
        "xdg_config_home": settings.xdg_config_home or "",
        "gog_credentials_path": settings.gog_credentials_path or "",
    }
    env_masked = {k: _mask_env_row(k, str(v)) for k, v in env_from_pydantic.items()}
    return {
        "effective": {
            "llm_provider_preset": effective_llm_provider_preset(),
            "llm_model": effective_llm_model(),
            "llm_model_main": effective_llm_model_main(),
            "llm_model_search_json": effective_llm_model_search_json(),
            "llm_model_search_rerank": effective_llm_model_search_rerank(),
            "llm_model_memory": effective_llm_model_memory(),
            "rag_embedding_provider": effective_rag_embedding_provider(),
            "rag_embedding_model": effective_rag_embedding_model(),
            "openrouter_base_url": effective_chat_base_url(),
            "gog_home": effective_gog_home(),
            "gog_account": effective_gog_account(),
            "gog_keyring_backend": effective_gog_keyring_backend(),
            "xdg_config_home": effective_xdg_config_home(),
            "gog_credentials_path": effective_gog_credentials_path(),
        },
        "stored_in_database": {k: stored[k] for k in keys_db},
        "openrouter_api_key_set_in_database": or_key_db,
        "openrouter_api_key_set_in_env": bool((settings.openrouter_api_key or "").strip()),
        "openai_api_key_set_in_env": bool(oai_k.strip()),
        "gog_keyring_password_set_in_database": gog_pw_db,
        "env_loaded": env_masked,
        "dotenv_path": str(dotenv_p.resolve()),
        "dotenv_exists": dotenv_p.exists(),
        "dotenv_file": dotenv_snapshot_for_ui(),
        "env_raw": env_masked,
        "recommended_models": [
            "openai/gpt-4o",
            "openai/gpt-4o-mini",
            "anthropic/claude-3.5-sonnet",
            "google/gemini-pro-1.5",
        ],
        "recommended_embedding_models": [
            "openai/text-embedding-3-large",
            "openai/text-embedding-3-small",
        ],
        "provider_presets": {
            "openrouter": {
                "label": "OpenRouter",
                "hint": "Multi-vendor models via one API; use vendor/model ids.",
                "default_base_url": "https://openrouter.ai/api/v1",
                "recommended_models": [
                    "openai/gpt-4o",
                    "openai/gpt-4o-mini",
                    "anthropic/claude-3.5-sonnet",
                    "google/gemini-2.0-flash-001",
                ],
                "recommended_embedding_models": ["openai/text-embedding-3-large", "openai/text-embedding-3-small"],
            },
            "openai": {
                "label": "OpenAI",
                "hint": "Direct OpenAI API; set OPENAI_API_KEY in .env or paste key in UI.",
                "default_base_url": _DEFAULT_OPENAI_BASE,
                "recommended_models": ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "o1-mini"],
                "recommended_embedding_models": ["text-embedding-3-large", "text-embedding-3-small"],
            },
            "gemini_openrouter": {
                "label": "Gemini (via OpenRouter)",
                "hint": "Google Gemini models routed through OpenRouter (same client as OpenRouter preset).",
                "default_base_url": "https://openrouter.ai/api/v1",
                "recommended_models": [
                    "google/gemini-2.0-flash-001",
                    "google/gemini-pro-1.5",
                ],
                "recommended_embedding_models": ["openai/text-embedding-3-large", "openai/text-embedding-3-small"],
            },
        },
    }
