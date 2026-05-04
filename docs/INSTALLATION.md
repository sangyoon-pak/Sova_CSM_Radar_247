# Installation guide (A–Z)

Single path from **empty clone** to **running Sova** with models and (optional) Gmail. Host install only (venv + `python run.py`); this project does not ship as a Docker image—**`gog`** needs local OAuth and a file keyring.

**Time:** ~15–30 minutes after you have API keys, longer if you set up Google Cloud OAuth for the first time.

---

## 0. What you need

- **Python 3.10+** (3.12 recommended)
- **Git**
- **Network** for `pip` and LLM APIs
- **LLM API access** — typically [OpenRouter](https://openrouter.ai/) (or OpenAI direct / Gemini via OpenRouter; see [LLM_MODELS.md](LLM_MODELS.md))
- **ripgrep** (`rg`) on `PATH` — used for knowledge-base search ([install](https://github.com/BurntSushi/ripgrep#installation))
- **Gmail** — Google Cloud project, **Gmail API** enabled, **OAuth client** JSON (`credentials.json`), and the **`gog`** CLI (see [GMAIL_SETUP.md](GMAIL_SETUP.md))

**OS notes:** The bundled `scripts/install-gog-local.sh` installs **macOS** `gog` binaries. On **Linux**, install a compatible `gog` build and set `PATH` / `GOG_HOME` accordingly. On **Windows**, use **WSL2** (recommended) or extend the install story for native Windows.

---

## 1. Clone and enter the project

```bash
git clone <your-repo-url>
cd email_draft_agent
```

Use the HTTPS or SSH URL from your Git host (fork or upstream).

---

## 2. Python virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows CMD: .venv\Scripts\activate.bat
                                   # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 3. Install ripgrep

Required for document search in the retrieval pipeline.

- **macOS (Homebrew):** `brew install ripgrep`
- **Ubuntu/Debian:** `sudo apt install ripgrep` (or download a `.deb` from the ripgrep releases page)
- **Windows:** `winget install BurntSushi.ripgrep.MSVC` or [download `rg.exe`](https://github.com/BurntSushi/ripgrep/releases) and add its folder to `PATH`

Verify: `rg --version`

---

## 4. Run the API server (before Configure)

The **Configure** tab is part of the web UI. Start the server first so you can open the app in a browser and save settings.

From the project root, venv activated:

```bash
python run.py
```

Open **http://127.0.0.1:8000** (or your `HOST`:`PORT`). The server can start before you add API keys; you need keys (via Configure or the environment) before chat and tools will call models.

---

## 5. Configuration (Configure UI, optional host environment)

Runtime values are resolved in this order:

1. **Configure** (saved in the SQLite database) — use the **Configure** tab in the browser with the server running (where that key is supported), including **Gmail (`gog`)** fields. Saved values **override** environment variables for those keys.
2. **Process environment** — export variables before `python run.py` when you do **not** rely on the database (e.g. headless servers), or to supply defaults that Configure does not override.
3. **Built-in defaults** — see `src/config.py`.

**`.env.example`** is a **checklist of variable names only** — the app does **not** load a `.env` file. Use Configure + Save, or export real env vars before `python run.py`.

**Minimum for chat + RAG:** open **Configure** and set provider preset, API keys, models, embedding settings, and (optionally) `RETRIEVAL_RANKING_POLICY` JSON for vendor-specific retrieval tuning without code changes (or export the same variable names before starting the process and restart after changing them).

Grey hints under fields show **recommended defaults**; the **Saved in Configure** section lists values you have stored in the database (masked).

To clear everything saved in Configure and start over: **Configure → Clear all database overrides**, or run **`scripts/reset_configure_overrides.py`**. Both also remove **local gog OAuth token files** under the effective **`GOG_HOME`** (see [GMAIL_SETUP.md](GMAIL_SETUP.md)); the **`gog` binary is not removed**.

Restart the server after changing exported environment variables. Details: [LLM_MODELS.md](LLM_MODELS.md), [LANGSMITH.md](LANGSMITH.md).

### LLM provider without OpenRouter

If you prefer **direct OpenAI** (no OpenRouter account), set **`LLM_PROVIDER_PRESET=openai`**, export **`OPENAI_API_KEY`**, and choose **OpenAI model ids** for `LLM_MODEL` / role overrides (for example `gpt-4o` instead of `openai/gpt-4o`). Embeddings can stay on OpenRouter or follow your chosen embedding provider in **Configure** — see variable notes in [LLM_MODELS.md](LLM_MODELS.md) and `.env.example`.

The **`gemini_openrouter`** preset is another OpenRouter-based path (Gemini model slugs via the same HTTP client); it is **not** “no OpenRouter.”

### Gmail + `gog` (optional, under Configure)

Inbox tools need **`gog`** and a one-time OAuth in the terminal — follow [GMAIL_SETUP.md](GMAIL_SETUP.md). Then save **`GOG_*`** in **Configure → Gmail** so they persist across restarts (or set them only via process environment for headless servers).

1. Create a **Google OAuth client** (Desktop type) and enable **Gmail API** — see [GMAIL_SETUP.md](GMAIL_SETUP.md) §1.
2. Save the JSON as **`credentials.json`** in the **project root** (next to `run.py`), **or** set **`GOG_CREDENTIALS_PATH`** in Configure or the environment.
3. Run **`scripts/install-gog-local.sh`** (macOS) or install `gog` another way on your OS.
4. Complete **one-time OAuth** in a terminal (`gog auth credentials`, `gog auth add …`).
5. In **Configure → Gmail**, fill in **`GOG_HOME`**, **`GOG_ACCOUNT`**, keyring fields, **Save configuration**, and confirm the checklist turns green (reopen Configure or reload if needed).

---

## 6. First visit in the UI

1. **Landing** — overview and links (this flow).
2. **Configure** — everything in **§5** (LLM, embeddings, optional Gmail + `gog`).
3. **Workbench** — set **agent profile** (vendor, role, product scope).
4. **Knowledge** — upload `.md` / `.txt` and **Reindex** if you use RAG.
5. **Run history** — inspect traces after runs.

---

## 7. Verify

- **Health:** `GET http://127.0.0.1:8000/health` → `{"status":"ok"}`
- **Learning memory (API-only operators):** `GET http://127.0.0.1:8000/memory/learning` returns constraints, exemplars, merged **`instructions`**, timestamps, and optional **`last_partition_json`** / **`last_partition_updated_at`** (last distill input partition) from the app database (**no LLM**). **`DELETE /memory/learning`** clears those settings (including **last partition**), legacy **`agent_learning_instructions`**, **and** deletes all **`agent_feedback`** rows. The delete JSON includes **`feedback_deleted`** (row count). Use **GET** to read the same merged `{learning_section}` source (`get_runtime_learning_instructions()`). The **Configure** load (`GET /settings/runtime`) includes this under **`distilled_learning`**. After `POST /memory/feedback` or `POST /memory/refresh`, poll **GET** if you are not using the browser. Pipeline (pool sampling, single reinforcement LLM): [ARCHITECTURE.md](ARCHITECTURE.md) § Self-evolution and feedback.
- **Gmail (if configured):**

```bash
.venv/bin/python -c "from src.agent.tools.gmail_tool import fetch_inbox_emails; print(fetch_inbox_emails(max_results=2)[:600])"
```

---

## Doc map

| Doc | Topic |
|-----|--------|
| [README.md](../README.md) | Features, quick commands |
| **This file** | End-to-end install |
| [GMAIL_SETUP.md](GMAIL_SETUP.md) | Gmail / `gog` only |
| [LLM_MODELS.md](LLM_MODELS.md) | Model roles and presets |
| [LANGSMITH.md](LANGSMITH.md) | Tracing |
| [SEARCH_AGENT.md](SEARCH_AGENT.md) | Retrieval architecture |
| [ARCHITECTURE.md](ARCHITECTURE.md) | End-to-end runtime, API, Configure map |

---

## Security

- Never commit **`.env`**, **`credentials.json`**, or **`scripts/.local/`** token data.
- Rotate keys if they are ever exposed.
