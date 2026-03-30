# Email Draft Agent

Local Appier email assistant with **grep-based document search**. No OpenClaw, no VPS, no 24/7 heartbeat.

## Features

- **Grep-based search**: LLM analyzes query → extracts search terms → ripgrep through knowledge base
- **Gmail probe**: Fetches inbox via gog CLI using local gog keyring (GOG_HOME)
- **Cron control**: UI to add/edit/disable cron jobs
- **Dashboard**: View agent interactions, run probes/custom prompts, and test chat

## Roadmap

- **Search Agent** — Smarter retrieval: re-rank results, optional refined search when insufficient. See [docs/SEARCH_AGENT_ROADMAP.md](docs/SEARCH_AGENT_ROADMAP.md).
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

## Run

```bash
python run.py
```

Open http://127.0.0.1:8000
