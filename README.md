# Proactive CSM Assistant

> *Repository folder may still be named `email_draft_agent`; the product direction is a **proactive CSM assistant**—inbox-aware, doc-grounded replies for customer success.*

Local console with **grep / RAG document search**, Gmail probe, and a dashboard for runs and knowledge. No OpenClaw, no VPS, no 24/7 heartbeat.

## Features

- **Grep-based search**: LLM analyzes query → extracts search terms → ripgrep through knowledge base
- **Gmail probe**: Fetches inbox via gog CLI using local gog keyring (GOG_HOME)
- **Cron control**: UI to add/edit/disable cron jobs
- **Dashboard**: Workbench (probe + task prompt + follow-up chat), run history, knowledge uploads

## Neutral Scope Config Examples

Use `RC_SCOPE_*` to make retrieval scope-aware without hard-coding product names:

```bash
# Disable scope routing entirely
RC_SCOPE_ENABLE=false

# Enable scope routing with your own labels
RC_SCOPE_ENABLE=true
RC_SCOPE_FIELD=product
RC_SCOPE_LABELS=product_a,product_b,platform,enterprise
RC_SCOPE_PENALTY=100
RC_SCOPE_EXCLUSIVE_THRESHOLD=0.75
```

## Roadmap

- **Search Agent** — Smarter retrieval: re-rank results, optional refined search when insufficient. See [docs/SEARCH_AGENT.md](docs/SEARCH_AGENT.md).
- **LangSmith tracing** — Observability for agent runs and tool calls. See [docs/LANGSMITH.md](docs/LANGSMITH.md).
- **Memory & history** — DB-backed interaction log with UI controls to clear or summarize older runs.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # Edit with your keys
brew install ripgrep   # For doc search
```

See `docs/GMAIL_SETUP.md` for Gmail OAuth.

**LLM routing:** optional per-role OpenRouter models (`LLM_MODEL_MAIN`, `LLM_MODEL_SEARCH_JSON`, etc.). See [docs/LLM_MODELS.md](docs/LLM_MODELS.md).

**Web search:** you can persist “RC URLs” in the dashboard and enable them; the agent can then pull citations from those domains via OpenRouter web search.

## Run

```bash
python run.py
```

Open http://127.0.0.1:8000
