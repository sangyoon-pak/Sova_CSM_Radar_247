"""
Effective runtime configuration: values saved via Configure UI (app_settings)
override process-environment-backed `Settings` from `src/config.py` (built-in defaults
when unset). Configure UI overrides (below) apply on top of ``Settings`` (from process
environment and built-in defaults) for keys saved in the database.
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path
from typing import Any

from src.config import settings
from src.db import database

# Stored ciphertext in DB when CONFIGURE_ENCRYPTION_KEY is set; decrypted for API + policy.
GUARDRAIL_ENCRYPTED_KEYS: frozenset[str] = frozenset(
    {
        "guardrail_include_intent_keywords",
        "guardrail_exclude_intent_keywords",
        "guardrail_team_guidance",
    }
)

_SENSITIVE_KEY = re.compile(r"(?i)(key|secret|password|token|credential)")


def mask_env_display(key: str, value: str) -> str:
    if not value:
        return ""
    if _SENSITIVE_KEY.search(key):
        return "••••••••" if len(value) > 6 else "••••"
    if len(value) > 120:
        return value[:117] + "…"
    return value

# Keys persisted by Configure (PATCH /settings/runtime). Bulk-cleared together.
RUNTIME_CONFIGURE_KEYS: tuple[str, ...] = (
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
    "guardrail_include_sender_domains",
    "guardrail_exclude_sender_domains",
    "guardrail_include_intent_keywords",
    "guardrail_exclude_intent_keywords",
    "guardrail_team_guidance",
    "guardrail_strictness",
    "prompt_email_agent_system_template",
    "prompt_probe_user_message",
    "prompt_probe_mode_append",
    "prompt_action_review_append",
)


def _gog_home_for_oauth_cleanup() -> Path | None:
    """Directory where gog stores keyring + cached OAuth client copy (see docs/GMAIL_SETUP.md)."""
    h = gog_home_resolved()
    if h is not None and h.is_dir():
        return h
    bundled = _repo_root() / "scripts" / ".local"
    if bundled.is_dir():
        return bundled
    return None


def _path_must_be_under(base: Path, p: Path) -> bool:
    try:
        p.resolve().relative_to(base.resolve())
        return True
    except ValueError:
        return False


def clear_gog_local_oauth_files() -> dict[str, Any]:
    """
    Delete gog OAuth tokens and the gogcli copy of the client JSON under GOG_HOME.
    Does not remove scripts/.local/bin/gog. Safe to call before clearing DB overrides
    so effective GOG_HOME from saved Configure is still applied.
    """
    removed: list[str] = []
    errors: list[str] = []
    home = _gog_home_for_oauth_cleanup()
    if home is None:
        return {
            "home": None,
            "removed": removed,
            "errors": errors,
            "skipped": "GOG_HOME not set and scripts/.local not found",
        }

    base = home.resolve()
    gogcli = base / "Library" / "Application Support" / "gogcli"
    keyring_dir = gogcli / "keyring"
    cred_file = gogcli / "credentials.json"

    def _unlink(path: Path) -> None:
        if not path.is_file():
            return
        if not _path_must_be_under(base, path):
            errors.append(f"refused (path outside GOG_HOME): {path}")
            return
        try:
            path.unlink()
            removed.append(str(path))
        except OSError as e:
            errors.append(f"{path}: {e}")

    _unlink(cred_file)

    if keyring_dir.is_dir():
        for entry in keyring_dir.iterdir():
            if entry.is_file():
                _unlink(entry)
            elif entry.is_dir():
                # unlikely; skip nested dirs for safety
                pass

    return {
        "home": str(base),
        "removed": removed,
        "errors": errors,
        "skipped": None,
    }


def clear_runtime_configure_overrides() -> None:
    """Remove all Configure-saved values from app_settings (effective config falls back to env + defaults)."""
    for key in RUNTIME_CONFIGURE_KEYS:
        database.delete_app_setting(key)
    from src.agent.prompt_seed import LEGACY_PROMPT_KEYS, seed_prompt_library_if_needed

    for key in LEGACY_PROMPT_KEYS:
        database.delete_app_setting(key)
    seed_prompt_library_if_needed()


def _db_str(key: str) -> str | None:
    if not database.app_setting_is_set(key):
        return None
    v = database.get_app_setting(key, "")
    if v is None:
        return None
    return str(v)


def _db_str_decrypted(key: str) -> str | None:
    raw = _db_str(key)
    if raw is None:
        return None
    if key in GUARDRAIL_ENCRYPTED_KEYS:
        from src.configure_crypto import decrypt_configure_value

        return decrypt_configure_value(raw)
    return raw


def persist_app_setting(key: str, value: str) -> None:
    """Persist a Configure value; encrypts guardrail text fields when encryption is enabled."""
    v = value
    if key in GUARDRAIL_ENCRYPTED_KEYS:
        from src.configure_crypto import encrypt_configure_value

        v = encrypt_configure_value(value)
    database.set_app_setting(key, v)


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
    # Only treat DB as an override when non-empty. A saved empty string would otherwise
    # override process env and break gog token decryption (aes.KeyUnwrap integrity check).
    v = _db_str("gog_keyring_password")
    if v is not None and v.strip():
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


def effective_guardrail_include_sender_domains() -> str:
    v = _db_str("guardrail_include_sender_domains")
    if v is not None:
        return v.strip()
    return (getattr(settings, "guardrail_include_sender_domains", None) or "").strip()


def effective_guardrail_exclude_sender_domains() -> str:
    v = _db_str("guardrail_exclude_sender_domains")
    if v is not None:
        return v.strip()
    return (getattr(settings, "guardrail_exclude_sender_domains", None) or "").strip()


def effective_guardrail_include_intent_keywords() -> str:
    v = _db_str_decrypted("guardrail_include_intent_keywords")
    if v is not None:
        return v.strip()
    return (getattr(settings, "guardrail_include_intent_keywords", None) or "").strip()


def effective_guardrail_exclude_intent_keywords() -> str:
    v = _db_str_decrypted("guardrail_exclude_intent_keywords")
    if v is not None:
        return v.strip()
    return (getattr(settings, "guardrail_exclude_intent_keywords", None) or "").strip()


def effective_guardrail_team_guidance() -> str:
    v = _db_str_decrypted("guardrail_team_guidance")
    if v is not None:
        return v.strip()
    return (getattr(settings, "guardrail_team_guidance", None) or "").strip()


def effective_guardrail_strictness() -> str:
    v = _db_str("guardrail_strictness")
    raw = ""
    if v is not None:
        raw = v.strip().lower()
    else:
        raw = (getattr(settings, "guardrail_strictness", None) or "balanced").strip().lower()
    if raw not in {"strict", "balanced", "permissive"}:
        return "balanced"
    return raw


def effective_prompt_email_agent_system_template() -> str:
    """Full system prompt template with {vendor_name}, {role_title}, {product_context}, {learning_section}."""
    v = _db_str("prompt_email_agent_system_template")
    if v is not None and v.strip():
        return v
    from src.agent.prompts import EMAIL_AGENT_SYSTEM_TEMPLATE

    return EMAIL_AGENT_SYSTEM_TEMPLATE


def effective_prompt_probe_user_message() -> str:
    v = _db_str("prompt_probe_user_message")
    if v is not None and v.strip():
        return v.strip()
    from src.agent.prompts import PROBE_TRIGGER_MESSAGE

    return PROBE_TRIGGER_MESSAGE


def effective_prompt_probe_mode_append() -> str:
    v = _db_str("prompt_probe_mode_append")
    if v is not None and v.strip():
        return v.strip()
    from src.agent.prompts import PROBE_MODE_SYSTEM_APPEND

    return PROBE_MODE_SYSTEM_APPEND.strip()


def effective_prompt_action_review_append() -> str:
    v = _db_str("prompt_action_review_append")
    if v is not None and v.strip():
        return v.strip()
    from src.agent.prompts import ACTION_REVIEW_SYSTEM_APPEND

    return ACTION_REVIEW_SYSTEM_APPEND.strip()


def _mask_env_row(key: str, val: str) -> str:
    if not val:
        return ""
    return mask_env_display(key, val)


def recommended_ui_hints() -> dict[str, str]:
    """
    Static recommended defaults for Configure grey hints (same role as a former .env.example).
    Does not reflect runtime effective values or OS environment.
    """
    s = settings
    base = (s.llm_model or "openai/gpt-4o").strip()
    role_small = "openai/gpt-4o-mini"
    return {
        "llm_model": base,
        "llm_model_main": base,
        "llm_model_search_json": role_small,
        "llm_model_search_rerank": role_small,
        "llm_model_memory": role_small,
        "rag_embedding_provider": (s.rag_embedding_provider or "openrouter").strip(),
        "rag_embedding_model": (s.rag_embedding_model or "openai/text-embedding-3-large").strip(),
        "openrouter_base_url": (s.openrouter_base_url or "https://openrouter.ai/api/v1").strip(),
        "guardrail_strictness": "balanced",
    }


def configure_saved_masked() -> dict[str, str]:
    """Only keys the user saved via Configure, values masked for display."""
    out: dict[str, str] = {}
    for k in RUNTIME_CONFIGURE_KEYS:
        if not database.app_setting_is_set(k):
            continue
        v = database.get_app_setting(k, "") or ""
        s = str(v)
        if k in GUARDRAIL_ENCRYPTED_KEYS and s.startswith("enc:v1:"):
            out[k] = "••• (encrypted at rest — forms above show decrypted text)"
        elif k.startswith("prompt_") and len(s) > 0:
            out[k] = f"••• ({len(s)} chars — see Prompt overrides above)"
        else:
            out[k] = _mask_env_row(k, s)
    return out


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def gog_setup_diagnostics() -> dict[str, Any]:
    """
    Lightweight checks for the Configure UI (Gmail is configured via CLI + env; see docs/GMAIL_SETUP.md).
    All checks must pass for `complete` — this does not prove OAuth tokens work, only that prerequisites exist.
    """
    root = _repo_root()
    checks: list[dict[str, str | bool]] = []

    gog_bin_ok = False
    gh = gog_home_resolved()
    if gh is not None:
        cand = gh / "bin" / "gog"
        if cand.is_file():
            gog_bin_ok = True
    if not gog_bin_ok:
        bundled = root / "scripts" / ".local" / "bin" / "gog"
        if bundled.is_file():
            gog_bin_ok = True
    if not gog_bin_ok:
        w = shutil.which("gog")
        if w:
            gog_bin_ok = True
    checks.append(
        {
            "id": "gog_binary",
            "ok": gog_bin_ok,
            "label": "gog CLI available",
            "hint": "Run scripts/install-gog-local.sh or ensure bin/gog exists under GOG_HOME, or gog is on PATH.",
        }
    )

    cred_ok = False
    ex = gog_credentials_path_resolved()
    if ex is not None and ex.is_file():
        cred_ok = True
    elif (root / "credentials.json").is_file():
        cred_ok = True
    checks.append(
        {
            "id": "oauth_client",
            "ok": cred_ok,
            "label": "OAuth client JSON present",
            "hint": "Put credentials.json at the project root or set GOG_CREDENTIALS_PATH to your Google OAuth client file.",
        }
    )

    acct_ok = bool(effective_gog_account().strip())
    checks.append(
        {
            "id": "gmail_account",
            "ok": acct_ok,
            "label": "Gmail account (GOG_ACCOUNT)",
            "hint": "Export GOG_ACCOUNT (or use a saved app_settings override) before starting the server.",
        }
    )

    kr_ok = bool(effective_gog_keyring_password().strip())
    checks.append(
        {
            "id": "keyring_password",
            "ok": kr_ok,
            "label": "Keyring password (GOG_KEYRING_PASSWORD)",
            "hint": "Must match the passphrase you used with gog auth in the terminal (export or saved override).",
        }
    )

    complete = all(bool(c.get("ok")) for c in checks)
    return {"complete": complete, "checks": checks}


def runtime_settings_snapshot() -> dict:
    """Payload for GET /settings/runtime (values + metadata for the Configure UI)."""
    keys_db = RUNTIME_CONFIGURE_KEYS
    stored = {k: database.app_setting_is_set(k) for k in keys_db}
    or_key_db = database.app_setting_is_set("openrouter_api_key") and bool(
        (database.get_app_setting("openrouter_api_key") or "").strip()
    )
    gog_pw_db = database.app_setting_is_set("gog_keyring_password") and bool(
        (database.get_app_setting("gog_keyring_password") or "").strip()
    )
    oai_k = getattr(settings, "openai_api_key", None) or ""
    from src.agent.prompts import build_prompt_effective_by_mode
    from src.configure_crypto import encryption_enabled

    # Preview must never take down the whole snapshot: a bad template (missing `{placeholder}`)
    # would otherwise 500 GET /settings/runtime and leave Configure fields empty.
    try:
        prompt_effective_by_mode = build_prompt_effective_by_mode()
    except Exception as e:
        prompt_effective_by_mode = {
            "assemble_order": (
                "Preview failed — usually a `{placeholder}` mismatch in the main system template. "
                "Keep {vendor_name}, {product_context}, {role_title}, {learning_section}."
            ),
            "modes": [],
            "preview_error": f"{type(e).__name__}: {e}",
        }

    return {
        "configure_encryption_enabled": encryption_enabled(),
        "prompt_effective_by_mode": prompt_effective_by_mode,
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
            "guardrail_include_sender_domains": effective_guardrail_include_sender_domains(),
            "guardrail_exclude_sender_domains": effective_guardrail_exclude_sender_domains(),
            "guardrail_include_intent_keywords": effective_guardrail_include_intent_keywords(),
            "guardrail_exclude_intent_keywords": effective_guardrail_exclude_intent_keywords(),
            "guardrail_team_guidance": effective_guardrail_team_guidance(),
            "guardrail_strictness": effective_guardrail_strictness(),
            "prompt_email_agent_system_template": effective_prompt_email_agent_system_template(),
            "prompt_probe_user_message": effective_prompt_probe_user_message(),
            "prompt_probe_mode_append": effective_prompt_probe_mode_append(),
            "prompt_action_review_append": effective_prompt_action_review_append(),
        },
        "stored_in_database": {k: stored[k] for k in keys_db},
        "openrouter_api_key_set_in_database": or_key_db,
        "openrouter_api_key_set_in_env": bool((settings.openrouter_api_key or "").strip()),
        "openai_api_key_set_in_env": bool(oai_k.strip()),
        "gog_keyring_password_set_in_database": gog_pw_db,
        "gog_setup": gog_setup_diagnostics(),
        "recommended_hints": recommended_ui_hints(),
        "configure_saved_masked": configure_saved_masked(),
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
                "hint": "Direct OpenAI API; set OPENAI_API_KEY or paste a key in Configure. RC web search uses OpenAI Responses + web_search (not OpenRouter).",
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
