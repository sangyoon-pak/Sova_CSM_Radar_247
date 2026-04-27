# Sova - CSM Radar Agent 24/7

Sova is an inbox-aware CSM copilot that turns customer email threads into evidence-backed follow-up actions using retrieval over product knowledge.

> Repository folder naming may still use `email_draft_agent`; product naming should remain **Sova - CSM Radar Agent 24/7** across docs and UI.

## What Sova Does

- Probes inbox threads (Gmail via local `gog` + OAuth)
- Classifies whether a thread requires CSM action
- Runs retrieval (RAG + lexical search) for evidence-backed responses
- Builds action-card candidates and tracks status progression
- Supports manual and scheduled processing via cron workflows

## Architecture Flow

The full **request routing**, **Workbench vs probe**, **API surface**, **Configure map**, and **mermaid** diagrams live in one place so they do not drift from the code:

- **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** (canonical runtime architecture)

Related deep dives:

- [docs/SEARCH_AGENT.md](docs/SEARCH_AGENT.md)
- [docs/AGENT_GUARDRAILS.md](docs/AGENT_GUARDRAILS.md)
- [docs/ACTION_CARD_SPEC.md](docs/ACTION_CARD_SPEC.md)

## Install And First Run

Use the full A-Z guide:

- **[docs/INSTALLATION.md](docs/INSTALLATION.md)** (canonical install path)

Quick local bootstrap:

```bash
python3 -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
# install ripgrep (rg) on PATH
python run.py
```

Open `http://127.0.0.1:8000`, then configure models and optional Gmail in **Configure**.

## Dependencies And External Setup

- `ripgrep` (`rg`) is required for lexical retrieval
- LLM provider/API credentials are required for chat + retrieval orchestration
- Gmail support requires local `gog`, Google OAuth credentials, and keyring values

Detailed docs:

- Gmail setup: [docs/GMAIL_SETUP.md](docs/GMAIL_SETUP.md)
- Model/provider setup: [docs/LLM_MODELS.md](docs/LLM_MODELS.md)
- Tracing and observability: [docs/LANGSMITH.md](docs/LANGSMITH.md)

## Behavior Contract (Guardrails)

Sova should create action cards only for customer-relevant CSM work, not for internal-only or non-actionable notifications.

- Relevance decisions should be explicit and auditable
- Retrieval should run for CSM-relevant threads before final card drafting
- If evidence is insufficient, the agent should state a gap instead of fabricating certainty
- User-adjustable guidance is preferred over hardcoded product rules

See [docs/AGENT_GUARDRAILS.md](docs/AGENT_GUARDRAILS.md) for the full contract.

## Retrieval Foundation

Retrieval is the core of Sova quality and sustainability:

- Uses multi-stage recall: vector RAG + `ripgrep` + FTS
- Applies scope-aware ranking and LLM rerank
- Supports sufficiency checks and query refinement loops

This design reduces hallucinations, improves answer traceability, and keeps behavior adaptable as docs evolve.

Reference: [docs/SEARCH_AGENT.md](docs/SEARCH_AGENT.md)

## Action Dashboard Expectations

Action cards should include enough metadata for practical execution:

- thread title and source linkage
- customer identity signal (name and/or domain)
- actionable summary and recommended next step
- status transitions (`not_started`, `in_progress`, `completed`)
- retrieval evidence metadata for follow-up Q&A

Reference: [docs/ACTION_CARD_SPEC.md](docs/ACTION_CARD_SPEC.md)

## Troubleshooting Quick Map

- False-positive/non-CSM cards -> check guardrail policy and exclusion rules
- Product thread with no retrieval evidence -> verify search path and indexing
- Previously probed thread skipped unexpectedly -> inspect dedup/state reset path
- Cron behavior mismatch -> verify interval semantics and job intent

Runbook: [docs/OPERATIONS_RUNBOOK.md](docs/OPERATIONS_RUNBOOK.md)

## Security And Release Hygiene

- Do not commit secrets (`credentials.json`, API keys, local token stores)
- Keep private/internal knowledge out of public distributions
- Validate docs, setup flow, and cross-platform host-install messaging before release

Checklist: [docs/RELEASE_CHECKLIST.md](docs/RELEASE_CHECKLIST.md)

## Full Documentation Map

Use [docs/README.md](docs/README.md) for the complete documentation index.
