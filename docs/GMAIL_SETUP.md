# Gmail Setup for Email Draft Agent

Uses the same gog CLI and credentials as openclaw_project. OAuth must be completed **locally** for the agent to fetch emails.

---

## 1. One-time OAuth (Local)

Run from `openclaw_project/scripts`:

```bash
cd ../openclaw_project/scripts

# Use the .local dir (has gog binary and credentials.json)
export GOG_HOME="$(pwd)/.local" HOME="$(pwd)/.local"
export PATH="$(pwd)/.local/bin:$PATH"
export GOG_KEYRING_BACKEND=file GOG_KEYRING_PASSWORD=openclaw-gmail

# Register OAuth client (if not done)
./.local/bin/gog auth credentials ../credentials.json

# Complete OAuth in browser (replace with your Gmail)
./.local/bin/gog auth add sangyoon.park@appier.com --services gmail --readonly --manual
```

1. Open the URL in your browser
2. Sign in and authorize
3. Copy the **full redirect URL** from the address bar (after redirect)
4. Paste it into the terminal when prompted

---

## 2. Configure email_draft_agent

In `email_draft_agent/.env`:

```bash
GOG_HOME=../openclaw_project/scripts/.local
GOG_ACCOUNT=sangyoon.park@appier.com
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

If you previously completed OAuth only on the VPS (Docker), the tokens are stored there—not on your Mac. You must run the OAuth flow locally once to store tokens in `openclaw_project/scripts/.local`.
