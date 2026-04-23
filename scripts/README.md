# Scripts (runtime + install only)

This folder stays small. **Do not remove** items the app or install docs depend on.

| File | Purpose |
|------|--------|
| `gmail-get-decoded.py` | Invoked by `src/agent/tools/gmail_tool.py` for Gmail fetch (subprocess). Required at runtime when using Gmail. |
| `install-gog-local.sh` | Bundled `gog` CLI installer (macOS). See [docs/INSTALLATION.md](../docs/INSTALLATION.md). |
| `reset_configure_overrides.py` | Clears Configure DB overrides and local gog OAuth under effective `GOG_HOME`. See [docs/INSTALLATION.md](../docs/INSTALLATION.md) and [docs/GMAIL_SETUP.md](../docs/GMAIL_SETUP.md). |

**`scripts/.local/`** — Default layout for `GOG_HOME` (binaries + OAuth). Listed in `.gitignore`; never commit tokens or `credentials.json` here.
