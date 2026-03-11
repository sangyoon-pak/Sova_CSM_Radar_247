# LangSmith Tracing

Traces agent runs, tool calls, and LLM invocations for debugging. Free tier: 5,000 traces/month.

## Setup

1. Sign up at [smith.langchain.com](https://smith.langchain.com)
2. Create an API key (Settings → API Keys)
3. Add to `.env`:

```
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=lsv2_pt_...
LANGSMITH_PROJECT=email_draft_agent
```

## Verify Tracing

Run a test invocation and check LangSmith:

```bash
.venv/bin/python scripts/test_langsmith_trace.py
```

Then open [smith.langchain.com](https://smith.langchain.com) → **Projects** → `email_draft_agent` (or `default`).

## No Traces Appearing?

1. **Check both projects** — Traces may appear under `default` or `email_draft_agent`
2. **Trigger an agent run** — Traces only appear when you run the agent (dashboard "Run" or `/agent/run` API)
3. **Wait a few seconds** — Traces can take 5–30 seconds to show up
4. **Verify env in worker** — If using uvicorn with reload, ensure `.env` is loaded. `load_dotenv()` is called in `run.py` and `src/main.py`
5. **API key** — Ensure the key is valid and has no typos (starts with `lsv2_pt_`)
