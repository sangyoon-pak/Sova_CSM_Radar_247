# AGENTS.md

## Cursor Cloud specific instructions

### Product overview

Sova is a local-first CSM (Customer Success Manager) copilot that monitors Gmail threads, classifies CSM-relevant items, and produces evidence-backed action cards using RAG retrieval over product knowledge. Single-process Python/FastAPI app with a vanilla HTML/CSS/JS SPA frontend.

### Running the application

1. Activate the venv: `source /workspace/.venv/bin/activate`
2. Start the server: `HOST=0.0.0.0 PORT=8000 python run.py` from `/workspace`
3. The UI is served at `http://localhost:8000` (root route serves `index.html`)
4. Health check: `GET /health` returns `{"status":"ok"}`

### Key dev notes

- **No automated test suite**: the repo does not ship a `tests/` directory. Quality is verified via manual Workbench runs and operator checklists (see `docs/README.md`).
- **No `.env` file loading**: the app reads from process environment variables and SQLite `app_settings` (Configure UI). `.env.example` is a reference only.
- **Missing pip deps**: `requirements.txt` does not list `pypdf` and `python-docx`, but they are required by `src/agent/tools/doc_upload.py`. Install them alongside `requirements.txt`.
- **ripgrep (`rg`)** must be on PATH for the retrieval pipeline.
- **LLM API keys** must be set as environment variables or configured via the Configure UI before chat/retrieval features work. See `.env.example` for variable names.
- **Gmail features** require the `gog` CLI + Google OAuth setup (optional; all non-Gmail features work without it).
- **SQLite DB** is auto-created at `./data/agent.db` on first startup.
- **Frontend** is a single-file SPA at `src/web/index.html` (~5600 lines); no build step required.
- Server binds to `HOST`/`PORT` (defaults: `127.0.0.1:8000`). Use `HOST=0.0.0.0` for external access.

### Lint / build / test

- No linter or formatter is configured in the repo.
- No build step is needed (pure Python + static HTML).
- No automated tests exist; test manually via the Workbench UI or API endpoints.
