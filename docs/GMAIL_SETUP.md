# Gmail setup

Gmail uses the **`gog`** CLI and Google OAuth. LLM/API keys are separate — see **[INSTALLATION.md](INSTALLATION.md)**.

**Flow:** (1) Google OAuth client + install `gog` → (2) one-time **`gog` sign-in in a terminal** → (3) **finish in the browser**: **Configure → Gmail** + **Save configuration** so **`GOG_*`** persist in the app database (no shell exports on every **`python run.py`**). Saved Configure values **take precedence** over the same variables in the process environment (see `effective_*` in `src/runtime_config.py`). Tokens on disk live under **`GOG_HOME`**.

---

## 1. OAuth client

In [Google Cloud Console](https://console.cloud.google.com/): enable **Gmail API**, configure the OAuth consent screen, create an **OAuth client ID** (Desktop app), download the JSON, and save it as **`credentials.json`** in the **repo root** (gitignored). Add test users if the app is in Testing.

---

## 2. Install `gog`

```bash
cd Sova_CSM_Radar_247/scripts
./install-gog-local.sh
```

Binary: **`scripts/.local/bin/gog`**. Default **`GOG_HOME=./scripts/.local`**.

---

## 3. Sign in once (terminal)

Use a normal shell (not an IDE Run task). From **repo root**, replace `CHANGE_ME` and `YOUR_EMAIL`:

```bash
cd scripts && \
export GOG_HOME="$(pwd)/.local" HOME="$(pwd)/.local" PATH="$(pwd)/.local/bin:$PATH" GOG_KEYRING_BACKEND=file GOG_KEYRING_PASSWORD='CHANGE_ME' && \
./.local/bin/gog auth credentials ../credentials.json && \
./.local/bin/gog auth add 'YOUR_EMAIL' --services gmail --readonly --manual
```

`gog` prints a URL (it may not open a browser). Open it → sign in → paste the **full redirect URL** from the address bar when prompted.

---

## 4. Finish in the UI (Configure)

The app **does not** run Google OAuth in the browser here — it only stores **`GOG_*`** so the running server can call **`gog`** on later restarts.

1. Start the API server if it is not running: **`python run.py`** from the repo root (see [INSTALLATION.md](INSTALLATION.md)).
2. Open the web UI (default **http://127.0.0.1:8000**).
3. Open the **Configure** tab.
4. Expand **Gmail (gog)**.
5. Enter the **same** values you used in §3 (and the same paths you expect for `GOG_HOME`):
   - **GOG_HOME** — e.g. `./scripts/.local` (relative to repo root) or an absolute path to that directory.
   - **GOG_ACCOUNT** — the Gmail address you authorized (required).
   - **GOG_KEYRING_BACKEND** — usually **`file`**.
   - **GOG_KEYRING_PASSWORD** — the **same** passphrase you used with `gog auth` in §3 (paste once; then **Save**).
   - **XDG_CONFIG_HOME** / **GOG_CREDENTIALS_PATH** — only if your layout needs them (otherwise leave empty).
6. Scroll to the bottom of **Configure** and click **Save configuration** (this saves the Gmail fields together with the rest of Configure).
7. Reload the page or collapse/reopen **Gmail (gog)**. The checklist should turn **green** when **gog**, OAuth client JSON, account, and keyring passphrase are all satisfied. If something stays red, read the line hints (common: empty **GOG_ACCOUNT** or passphrase mismatch).

---

## 5. Test

With the server running and §4 saved (or the same variables set only in the environment):

```bash
cd Sova_CSM_Radar_247
.venv/bin/python -c "from src.agent.tools.gmail_tool import fetch_inbox_emails; print(fetch_inbox_emails(max_results=2)[:500])"
```

---

## Reset local auth

Use **Configure → Clear all database overrides** (or **`scripts/reset_configure_overrides.py`**) to clear saved settings **and** delete gog token files under **`GOG_HOME`**. Or stop the server and manually delete **`…/gogcli/keyring/*`** and **`…/gogcli/credentials.json`**, then repeat **§3–5**. Optional: revoke the app under Google Account → Third-party access.

---

## New machine

Repeat **§2–5** on each machine; OAuth tokens are local.
