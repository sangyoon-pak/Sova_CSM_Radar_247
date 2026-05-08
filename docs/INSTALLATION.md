# Installation guide (A–Z)

Single path from **empty clone** to **running Sova** with models and (optional) Gmail. This is the **canonical install document** for host environments (venv + `python run.py`). The project is not container-first; **`gog`** OAuth/keyring requires a normal OS user environment.

After the app is up, the **Configure** tab’s prompt/runtime layout is documented in [ARCHITECTURE.md](ARCHITECTURE.md) § **Configure tab: runtime diagram (UI)** (same structure as the in-app diagram).

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

### Host install matrix (current)

- **macOS:** fully supported host path (`venv` + `run.py` + local `gog` script).
- **Linux:** supported host path (`venv` + `run.py`), with manual `gog` install.
- **Windows:** supported via **WSL2** host path (`venv` + `run.py`); native Windows `gog` path is not the default documented flow yet.

---

## 1. Clone and enter the project

```bash
git clone https://github.com/sangyoon-pak/Sova_CSM_Radar_247.git
cd Sova_CSM_Radar_247
```

Use the HTTPS or SSH URL from your Git host (fork or upstream).

---

## 2. Python virtual environment

### 2.1 Confirm (or install) Python 3.10+

Sova requires **Python 3.10+** (3.12 recommended). Many systems ship with an older Python; check first:

```bash
python3 --version
```

If the printed version is below 3.10 — or no `python3` is found — install a supported interpreter using one of the options below.

**macOS (Homebrew, recommended):**

```bash
brew install python@3.12
# Homebrew prints the exact path; typically /opt/homebrew/opt/python@3.12/bin/python3.12
```

**Ubuntu / Debian (apt):**

```bash
sudo apt update
sudo apt install -y python3.12 python3.12-venv python3-pip
# Older distros: enable deadsnakes PPA first:
#   sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt update
```

**Windows (WSL2 strongly recommended):** install Ubuntu via WSL2, then follow the Debian/Ubuntu instructions above. For native Windows, use [python.org](https://www.python.org/downloads/) installers and ensure “Add Python to PATH” is checked.

**Multiple Pythons / version manager (pyenv):** if the system Python is locked to an older version and you cannot upgrade it system-wide, use **pyenv**:

```bash
# macOS: brew install pyenv
# Linux: see https://github.com/pyenv/pyenv#installation
pyenv install 3.12.7
pyenv local 3.12.7        # writes .python-version in the project folder
```

### 2.2 Create and activate the venv

Sova needs an **isolated Python environment with `requirements.txt` installed** — modern macOS and Linux block global `pip install` (PEP 668), and mixing Sova's deps with other projects causes conflicts. The doc uses Python's built-in `venv` because it ships with the interpreter, but **any equivalent works** (`uv`, `virtualenv`, `conda`/`mamba`, Docker, etc.) — just point step §4's `python run.py` at that environment's interpreter.

Create the venv with the specific Python you confirmed above (replace `python3.12` with the binary you just installed if different):

```bash
python3.12 -m venv .venv
source .venv/bin/activate          # Windows CMD: .venv\Scripts\activate.bat
                                   # Windows PowerShell: .venv\Scripts\Activate.ps1
python --version                   # should now print 3.10+ (3.12 recommended)
pip install --upgrade pip
pip install -r requirements.txt
```

> Activate the venv in **every shell** before running `python run.py`, `pip install`, or any of the CLIs installed by `requirements.txt` (`uvicorn`, `langsmith`, `huggingface-cli`, `transformers-cli`, etc.). Without activation those commands resolve to system binaries (or fail), not the venv copies.
>
> **Anaconda / Miniconda users:** If your prompt still shows `(base)` after activating `.venv`, you can end up with a hybrid interpreter (Anaconda stdlib mixed with `.venv` packages) and confusing tracebacks like `/opt/anaconda3/...` plus `.venv/site-packages`. Run `conda deactivate` until `(base)` disappears, then `source .venv/bin/activate` again. Confirm with `which python` → it should be `.../Sova_CSM_Radar_247/.venv/bin/python`.

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

### zsh tip: `unknown file attribute: b`

If **`zsh` prints that message** after pasting steps from docs or chat, it is rarely Python itself—it is usually the shell interpreting something oddly (truncated paste, smart quotes, or conda + hook ordering). Prefer **typing one command per line** (no `# …` tails on `conda deactivate` until things work). Use the interpreter explicitly so you bypass any conda alias:

```bash
conda deactivate
source .venv/bin/activate
pip install -r requirements.txt
./.venv/bin/python run.py
```

If `(base)` is still shown next to `(.venv)`, **`conda deactivate` again** (sometimes twice) until `which python` resolves to `.../.venv/bin/python`.

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
