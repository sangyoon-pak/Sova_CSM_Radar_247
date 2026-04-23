# Sova Docs Index

This index is the canonical map for implementing and operating **Sova - CSM Radar Agent 24/7**.

## Start Here

- New users: [INSTALLATION.md](INSTALLATION.md)
- Product overview: [../README.md](../README.md)
- Retrieval foundation: [SEARCH_AGENT.md](SEARCH_AGENT.md)

## Build And Architecture

- **Runtime flow, API routes, Workbench vs probe, and Configure map:** [ARCHITECTURE.md](ARCHITECTURE.md)
- **Prompts (code vs `app_settings` DB, seeding, upgrades):** [PROMPTS.md](PROMPTS.md)
- Agent guardrails and behavior boundaries: [AGENT_GUARDRAILS.md](AGENT_GUARDRAILS.md)
- Action card data/UX contract: [ACTION_CARD_SPEC.md](ACTION_CARD_SPEC.md)
- Search and retrieval internals: [SEARCH_AGENT.md](SEARCH_AGENT.md)

## Operations

- Installation and first run: [INSTALLATION.md](INSTALLATION.md)
- Gmail and `gog` setup: [GMAIL_SETUP.md](GMAIL_SETUP.md)
- Model/provider configuration: [LLM_MODELS.md](LLM_MODELS.md)
- Tracing/observability: [LANGSMITH.md](LANGSMITH.md)
- Troubleshooting and failure-mode playbook: [OPERATIONS_RUNBOOK.md](OPERATIONS_RUNBOOK.md)

## Release And Distribution

- Pre-release and public distribution checklist: [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md)
- **Local data wipe / scripts inventory:** [../scripts/README.md](../scripts/README.md) (`reset_local_data.py`, `reset_configure_overrides.py`, and other helpers)

## Automated tests

This repository does **not** ship a `tests/` pytest suite; quality relies on manual runs, **Run history**, and operator checklists. When changing agent or retrieval behavior, exercise Workbench probe + chat and review traces.

## Ownership Expectations

- Keep docs aligned with code under `src/`.
- Update this index when adding or renaming docs.
- If you change **agent prompt text** in `src/agent/prompts.py`, read [PROMPTS.md](PROMPTS.md): runtime uses the database unless defaults are re-seeded or fields are cleared in Configure.
- If behavior changes affect CSM relevance, retrieval, or action cards, update:
  - `AGENT_GUARDRAILS.md`
  - `ACTION_CARD_SPEC.md`
  - `SEARCH_AGENT.md`

