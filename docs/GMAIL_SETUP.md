# Gmail Setup for Email Draft Agent

Installs and uses `gog` (gogcli) locally inside `email_draft_agent/`. OAuth must be completed **locally** for the agent to fetch emails.

---

## 1. One-time OAuth (Local)

From the `email_draft_agent/` repo root, run:

```bash
cd scripts

# 1) Install gog to ./scripts/.local (one-time)
./install-gog-local.sh

# 2) Use the .local dir (has gog binary)
export GOG_HOME="$(pwd)/.local" HOME="$(pwd)/.local"
export PATH="$(pwd)/.local/bin:$PATH"
export GOG_KEYRING_BACKEND=file GOG_KEYRING_PASSWORD=openclaw-gmail

# 3) Register OAuth client (if not done)
# Put credentials.json at email_draft_agent/credentials.json (or change the path below).
./.local/bin/gog auth credentials ../credentials.json

# 4) Complete OAuth in browser (replace with your Gmail)
./.local/bin/gog auth add YOUR_EMAIL --services gmail --readonly --manual

```

1. Open the URL in your browser
2. Sign in and authorize
3. Copy the **full redirect URL** from the address bar (after redirect)
4. Paste it into the terminal when prompted

---

## 2. Configure email_draft_agent

In `email_draft_agent/.env`:

```bash
GOG_HOME=./scripts/.local
GOG_ACCOUNT=YOUR_EMAIL
GOG_KEYRING_BACKEND=file
GOG_KEYRING_PASSWORD=openclaw-gmail
```

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

If you previously completed OAuth only on the VPS (Docker), the tokens are stored there—not on your Mac. You must run the OAuth flow locally once to store tokens in `email_draft_agent/scripts/.local`.
