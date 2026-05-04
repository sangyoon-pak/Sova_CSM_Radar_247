# Prompts: code vs database (for developers and coding agents)

## What actually runs

At **runtime**, the agent does **not** read `src/agent/prompts.py` directly for the four configurable prompts. It reads **`app_settings`** keys via `src/runtime_config.py` (`effective_prompt_email_agent_system_template`, `effective_prompt_probe_user_message`, `effective_prompt_probe_mode_append`, `effective_prompt_action_review_append`). If a key is missing or empty, the code falls back to the matching constant in `src/agent/prompts.py`.

So **`prompts.py` is the canonical default text in the repo**, but **an existing database may still hold older copies** that were seeded or edited earlier.

## Database keys (Configure / `app_settings`)

| Key | Constant in `prompts.py` | Role |
|-----|---------------------------|------|
| `prompt_email_agent_system_template` | `EMAIL_AGENT_SYSTEM_TEMPLATE` | Main system template (placeholders, learning block, etc.) |
| `prompt_probe_user_message` | `PROBE_TRIGGER_MESSAGE` | Human turn text for inbox probe / cron |
| `prompt_probe_mode_append` | `PROBE_MODE_SYSTEM_APPEND` | Extra system block appended when `probe=True` |
| `prompt_action_review_append` | `ACTION_REVIEW_SYSTEM_APPEND` | Extra system block for “Discuss this action” threads |
| `agent_learning_constraints` | — | **CONSTRAINTS** section from **`refresh_learning_instructions`**: negative feedback (`incorrect` / `noisy`), action-card corrections, and endorsed card preferences; hyphen bullets |
| `agent_learning_exemplars` | — | **EXEMPLARS** section from the same refresh: endorsed **run_history** only (same single LLM pass as constraints) |
| `agent_learning_last_partition_json` | — | Last **`negative` / `endorsed`** partition JSON fed to the reinforcement LLM (debug / transparency); cleared with learning reset |
| `agent_learning_instructions` | — | **Legacy** single blob; cleared on refresh so split keys take precedence; `get_runtime_learning_instructions()` falls back to this only if split keys are empty |

The main template must keep the **`{learning_section}`** placeholder. At runtime it is filled from **`get_runtime_learning_instructions()`**, which merges **`agent_learning_constraints`** and **`agent_learning_exemplars`** (and falls back to legacy **`agent_learning_instructions`** if needed), not from the Workbench profile form. Configure shows the combined view under **Distilled learning rules**; `GET /memory/learning` and `GET /settings/runtime` → `distilled_learning` expose merged **`instructions`**, **`constraints`**, **`exemplars`**, and (on **`GET /memory/learning`**) **`last_partition_json`** — **no** LLM call.

Implementation: `src/agent/prompt_seed.py` (`PROMPT_LIBRARY_KEYS`, `default_prompt_value()`, `seed_prompt_library_if_needed()`).

## When `prompts.py` is written into the DB

1. **First app start / empty DB**: `seed_prompt_library_if_needed()` runs (from DB init and related paths). For each key above, **if the key is not set**, it copies the current value from `prompts.py` into `app_settings`.

2. **Materialization (`ensure_prompt_library_materialized`)**: After seed and on **every** `GET /settings/runtime` (Configure load), the app ensures each prompt key exists and is **non-empty**. If a row is missing or only whitespace, it is **back-filled** with `default_prompt_value(key)` from `prompts.py` and saved. This keeps the database as the single visible source in the UI.

3. **“Clear all Configure overrides”** (`POST /settings/runtime/clear-overrides`): prompt keys are removed, then `seed_prompt_library_if_needed()` runs again, so **missing** keys are filled from `prompts.py` (same as first install).

4. **Per-field reset in Configure**: `PATCH /settings/runtime` with an **empty string** for a prompt field **re-persists the bundled default** via `default_prompt_value(key)` so the row in `app_settings` always holds the full text (not an empty cell with a silent code fallback).

## What does *not* happen automatically

If a developer **only edits `prompts.py`** and commits:

- Installations that **already have** those rows in `app_settings` **keep the old text** until an operator updates Configure or resets as above.
- There is **no** automatic “overwrite DB whenever `prompts.py` changes” (by design: operators may customize prompts).

## What to do after changing `prompts.py`

Choose one:

- **Ship defaults to all environments that should match the repo**: document an upgrade step — e.g. clear the relevant prompt field in Configure (save empty) so the API re-injects `default_prompt_value()`, or use **Clear all Configure overrides** if appropriate for that deployment.
- **Operator-only change**: edit the text in the Configure UI; no need to change `prompts.py` unless you want new installs to match.

## Related code (quick map)

- Defaults and prose: `src/agent/prompts.py`
- Seed + `default_prompt_value()`: `src/agent/prompt_seed.py`
- Effective resolution: `src/runtime_config.py` (`effective_prompt_*`)
- API persistence and empty-field reset: `src/api/routes.py` (`PATCH /settings/runtime`, `PROMPT_LIBRARY_KEYS`)
