# Sova (email_draft_agent)

> *Repository folder name may remain `email_draft_agent`; the product is **Sova** — a CSM Radar Agent: inbox-aware, doc-grounded assistance.*

Local web console with **grep / RAG document search**, Gmail (via **`gog`**), cron jobs, and dashboards for runs and knowledge.

## Install (A–Z)

**Start here:** **[docs/INSTALLATION.md](docs/INSTALLATION.md)** — clone, venv, Configure + env, ripgrep, optional Gmail, run server, first UI steps.

Quick copy-paste after clone:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
# Optional: see .env.example for variable names; use Configure → Save or export env vars before python run.py
# Install ripgrep for doc search — e.g. brew install ripgrep
python run.py               # http://127.0.0.1:8000
```

- **Gmail / `gog`:** [docs/GMAIL_SETUP.md](docs/GMAIL_SETUP.md)
- **Models & presets:** [docs/LLM_MODELS.md](docs/LLM_MODELS.md)
- **LangSmith:** [docs/LANGSMITH.md](docs/LANGSMITH.md)
- **Retrieval / search agent:** [docs/SEARCH_AGENT.md](docs/SEARCH_AGENT.md)

## Features

- **Grep-based search**: LLM → search terms → ripgrep over the knowledge base
- **Gmail**: inbox via local **`gog`** CLI and OAuth (`GOG_HOME`, keyring)
- **Cron**: UI for scheduled jobs
- **Dashboards**: Workbench, Action dashboard, Run history, Knowledge uploads

## RC scope (optional)

Use `RC_SCOPE_*` for scope-aware retrieval without hard-coding product names — see `.env.example` (reference) and [docs/SEARCH_AGENT.md](docs/SEARCH_AGENT.md).

## Run

```bash
python run.py
```

Open **http://127.0.0.1:8000** — use the **Landing** tab for setup guidance and **Configure** for runtime settings.
