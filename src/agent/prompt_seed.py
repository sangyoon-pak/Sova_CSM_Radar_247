"""Seed agent prompt library into app_settings from src/agent/prompts.py defaults.

Runtime reads prompts from the database only; this module is the bridge from code
defaults to the DB on first start and after full Configure clear.

See docs/PROMPTS.md for when edits to prompts.py reach existing databases.
"""
from __future__ import annotations

from src.db import database


def default_prompt_value(key: str) -> str:
    """Built-in default string for a prompt key (matches prompts.py constants)."""
    from src.agent import prompts as P

    return {
        "prompt_email_agent_system_template": P.EMAIL_AGENT_SYSTEM_TEMPLATE,
        "prompt_probe_user_message": P.PROBE_TRIGGER_MESSAGE,
        "prompt_probe_mode_append": P.PROBE_MODE_SYSTEM_APPEND.strip(),
        "prompt_action_review_append": P.ACTION_REVIEW_SYSTEM_APPEND.strip(),
    }[key]


PROMPT_LIBRARY_KEYS: tuple[str, ...] = (
    "prompt_email_agent_system_template",
    "prompt_probe_user_message",
    "prompt_probe_mode_append",
    "prompt_action_review_append",
)

# Removed from Configure but may still exist in older DBs; cleared with "clear all".
LEGACY_PROMPT_KEYS: tuple[str, ...] = ("prompt_system_extra", "prompt_probe_trigger")


def ensure_prompt_library_materialized() -> None:
    """
    Ensure every prompt library row in app_settings contains non-empty text.

    If a key is missing or only whitespace, write the bundled default from
    `default_prompt_value` so Configure and runtime share one source: the database.
    Safe to call repeatedly (idempotent once rows are valid).
    """
    for key in PROMPT_LIBRARY_KEYS:
        if not database.app_setting_is_set(key):
            database.set_app_setting(key, default_prompt_value(key))
            continue
        raw = database.get_app_setting(key)
        if raw is None or not str(raw).strip():
            database.set_app_setting(key, default_prompt_value(key))


def seed_prompt_library_if_needed() -> None:
    """
    For each canonical prompt key: if missing, insert defaults from prompts.py.

    Migrates legacy keys once: merges prompt_system_extra into the system template,
    copies prompt_probe_trigger into prompt_probe_user_message, then deletes legacy rows.
    """
    from src.agent import prompts as P

    # 1) Main system template (with placeholders for render_email_agent_system)
    if not database.app_setting_is_set("prompt_email_agent_system_template"):
        tmpl = P.EMAIL_AGENT_SYSTEM_TEMPLATE
        if database.app_setting_is_set("prompt_system_extra"):
            ex = (database.get_app_setting("prompt_system_extra") or "").strip()
            if ex:
                tmpl = tmpl.rstrip() + "\n\n## Legacy extra instructions (former Configure field)\n" + ex
            database.delete_app_setting("prompt_system_extra")
        database.set_app_setting("prompt_email_agent_system_template", tmpl)

    # 2) Probe user message (human turn for inbox probe / cron)
    if not database.app_setting_is_set("prompt_probe_user_message"):
        if database.app_setting_is_set("prompt_probe_trigger"):
            raw = (database.get_app_setting("prompt_probe_trigger") or "").strip()
            database.set_app_setting(
                "prompt_probe_user_message",
                raw if raw else P.PROBE_TRIGGER_MESSAGE,
            )
            database.delete_app_setting("prompt_probe_trigger")
        else:
            database.set_app_setting("prompt_probe_user_message", P.PROBE_TRIGGER_MESSAGE)

    if not database.app_setting_is_set("prompt_probe_mode_append"):
        database.set_app_setting("prompt_probe_mode_append", P.PROBE_MODE_SYSTEM_APPEND.strip())

    if not database.app_setting_is_set("prompt_action_review_append"):
        database.set_app_setting("prompt_action_review_append", P.ACTION_REVIEW_SYSTEM_APPEND.strip())

    ensure_prompt_library_materialized()
