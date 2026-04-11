# Gmail setup (SOVA Agent)

The SOVA Agent uses **`gog`** (gogcli) locally under `email_draft_agent/` to read Gmail. OAuth must be completed **on the machine** where the app runs so tokens live next to `GOG_HOME`.

For **LLM / embeddings / provider presets**, use the web UI **Configure** tab or copy from `.env.example`. Saved Configure values are stored in the app database and **override** `.env` until cleared.

---

## 1. One-time OAuth (local)

From the `email_draft_agent/` repo root:

```bash
cd scripts

# 1) Install gog to ./scripts/.local (one-time)
./install-gog-local.sh

# 2) Use the .local dir (has gog binary)
export GOG_HOME="$(pwd)/.local" HOME="$(pwd)/.local"
export PATH="$(pwd)/.local/bin:$PATH"
# Use the same passphrase here and in .env (below); pick a strong random string.
export GOG_KEYRING_BACKEND=file GOG_KEYRING_PASSWORD=YOUR_KEYRING_PASSPHRASE

# 3) Register OAuth client (if not done)
# Download OAuth client JSON from Google Cloud Console and place it at:
#   email_draft_agent/credentials.json
# Or set GOG_CREDENTIALS_PATH (absolute path) / Configure → OAuth client JSON path.
./.local/bin/gog auth credentials ../credentials.json

# 4) Complete OAuth in browser (replace with your Gmail)
./.local/bin/gog auth add YOUR_EMAIL --services gmail --readonly --manual
```

1. Open the URL in your browser  
2. Sign in and authorize  
3. Copy the **full redirect URL** from the address bar (after redirect)  
4. Paste it into the terminal when prompted  

---

## 2. Environment variables

### 2a. Gmail / `gog` (minimal `.env`)

Put these in `email_draft_agent/.env` (or set the same fields in **Configure → Gmail**):

```bash
GOG_HOME=./scripts/.local
GOG_ACCOUNT=YOUR_EMAIL
GOG_KEYRING_BACKEND=file
GOG_KEYRING_PASSWORD=YOUR_KEYRING_PASSPHRASE
# Optional: absolute path to Google OAuth client JSON if not using ./credentials.json
# GOG_CREDENTIALS_PATH=/absolute/path/to/credentials.json
# Optional: isolate gog config under GOG_HOME (matches one-time OAuth exports)
# XDG_CONFIG_HOME=./scripts/.local/.config
```

Use a **strong, private** `GOG_KEYRING_PASSWORD` if others can access the `scripts/.local` tree. Do **not** commit `credentials.json` (see `.gitignore`).

### 2b. Configure tab ↔ `.env` (full reference)

These environment variables correspond to **Configure** in the UI. The **Environment sync** section on Configure compares your on-disk `.env` with values the server loaded at startup (restart after editing `.env` manually).

| Environment variable | Configure section | Notes |
|---------------------|-------------------|--------|
| `LLM_PROVIDER_PRESET` | Provider & API | `openrouter` (default) · `openai` · `gemini_openrouter` |
| `OPENROUTER_BASE_URL` | Provider & API | Default `https://openrouter.ai/api/v1`; for `openai` preset, effective base is `https://api.openai.com/v1` unless overridden in Configure |
| `OPENROUTER_API_KEY` | Provider & API | Chat + embeddings; can also be pasted in Configure (stored in DB) |
| `OPENAI_API_KEY` | — (env only) | Used when preset is `openai` if `OPENROUTER_API_KEY` is not used; not a separate Configure field |
| `LLM_MODEL` | LLM models | Default model |
| `LLM_MODEL_MAIN` | LLM models | Main agent |
| `LLM_MODEL_SEARCH_JSON` | LLM models | Search / JSON steps |
| `LLM_MODEL_SEARCH_RERANK` | LLM models | Rerank |
| `LLM_MODEL_MEMORY` | LLM models | Memory / learning |
| `RAG_EMBEDDING_PROVIDER` | Embeddings | e.g. `openrouter` |
| `RAG_EMBEDDING_MODEL` | Embeddings | e.g. `openai/text-embedding-3-large` |
| `GOG_HOME` | Gmail | |
| `GOG_ACCOUNT` | Gmail | |
| `GOG_KEYRING_BACKEND` | Gmail | |
| `GOG_KEYRING_PASSWORD` | Gmail | Can be set in Configure (DB) instead of `.env` |
| `XDG_CONFIG_HOME` | Gmail | |
| `GOG_CREDENTIALS_PATH` | Gmail | OAuth client JSON path |

A filled-out template (including LangSmith, server, KB path) is in **`.env.example`**. Model roles and tuning are summarized in **`docs/LLM_MODELS.md`**.

---

## 3. Test

```bash
cd email_draft_agent
.venv/bin/python -c "
from src.agent.tools.gmail_tool import fetch_inbox_emails
print(fetch_inbox_emails(max_results=2)[:500])
"
```

---

## Note

If you previously completed OAuth only on a **VPS** (Docker), tokens live there—not on your laptop. Run the OAuth flow **locally** once so tokens are stored under `email_draft_agent/scripts/.local` (or your chosen `GOG_HOME`).
