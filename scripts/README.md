# Scripts (runtime, install, local hygiene)

This folder stays small. **Do not remove** items the app or install docs depend on.

| File | Purpose |
|------|--------|
| `gmail-get-decoded.py` | Invoked by `src/agent/tools/gmail_tool.py` for Gmail fetch (subprocess). Required at runtime when using Gmail. |
| `install-gog-local.sh` | Bundled `gog` CLI installer (macOS). See [docs/INSTALLATION.md](../docs/INSTALLATION.md). |
| `reset_configure_overrides.py` | Clears Configure DB overrides and local gog OAuth under effective `GOG_HOME`. See [docs/INSTALLATION.md](../docs/INSTALLATION.md) and [docs/GMAIL_SETUP.md](../docs/GMAIL_SETUP.md). |
| `reset_local_data.py` | **Destructive:** removes local app SQLite, KB FTS DB, RAG dir, and uploaded KB files under `data/`, then runs `init_db()`. Use **before publishing or cloning for public distribution** so no trial DB/uploads ship (`python scripts/reset_local_data.py --yes`). **Stop the server first.** |

**`scripts/.local/`** — Default layout for `GOG_HOME` (binaries + OAuth). Listed in `.gitignore`; never commit tokens or `credentials.json` here.
