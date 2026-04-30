# AGENTS.md

## Cursor Cloud specific instructions

### Overview

Sova is a single-process Python FastAPI application (CSM Radar Agent). It runs on port 8000 with an embedded SQLite database and serves a browser UI from `src/web/`.

### Running the application

```bash
source .venv/bin/activate
python run.py
```

Server starts at `http://127.0.0.1:8000`. Health check: `GET /health` → `{"status":"ok"}`.

Per `.cursor/rules/dev-server-restart.mdc`, Uvicorn runs with `reload=False`. After any code change, kill the existing process on port 8000 and restart:
```bash
lsof -ti:8000 | xargs kill -9 2>/dev/null
.venv/bin/python run.py
```

### Linting

No project-level linter config exists. Use `ruff` (installed in the venv):
```bash
ruff check src/
```
Pre-existing issues (unused imports, ambiguous variable name) are in the codebase — do not fix unless asked.

### Testing

No automated test suite exists in this repo. Verification is done via:
- Health endpoint: `curl http://127.0.0.1:8000/health`
- Import check: `python -c "from src.main import app"`
- API endpoint testing (see README §7 Verify)

### Key dependencies not in requirements.txt

The following packages are required at runtime but missing from `requirements.txt`:
- `pypdf` — PDF upload parsing in `src/agent/tools/doc_upload.py`
- `python-docx` — DOCX upload parsing in `src/agent/tools/doc_upload.py`

These must be installed alongside `requirements.txt`.

### System dependencies

- `ripgrep` (`rg`) must be on PATH — used for KB lexical search (pre-installed on Cloud VMs)
- Python 3.10+ (3.12 recommended)

### Configuration

The app does NOT load `.env` files. Configuration is either:
1. Set via the Configure UI tab (persisted in SQLite at `./data/agent.db`)
2. Exported as environment variables before starting the process

LLM API keys (OPENROUTER_API_KEY or OPENAI_API_KEY) are needed for chat/retrieval but the app starts and serves the UI without them.

### External services (optional)

- Gmail (`gog` CLI + Google OAuth) — only for inbox features
- LangSmith — only for tracing/observability
- LLM API provider — required for agent functionality but not for app startup/UI
