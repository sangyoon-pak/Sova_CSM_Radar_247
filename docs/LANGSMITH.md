# LangSmith Tracing

Traces agent runs, tool calls, and LLM invocations for debugging. Free tier: 5,000 traces/month.

## Setup

1. Sign up at [smith.langchain.com](https://smith.langchain.com)
2. Create an API key (Settings → API Keys)
3. Set LangSmith credentials either:
   - in **Configure** (recommended for app runtime), or
   - in the server process environment before startup.

```
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=lsv2_pt_...
LANGSMITH_PROJECT=email_draft_agent
```

For ad-hoc Python, export `LANGSMITH_*` in your shell (process env is not read from Configure DB unless the app loads it).

## Verify Tracing

Start the app (`python run.py`), enable LangSmith in **Configure**, then trigger any agent run (Workbench, **Scan inbox**, or **Run history** / API). Open [smith.langchain.com](https://smith.langchain.com) → **Projects** → `email_draft_agent` (or `default`) after a few seconds.

Each LLM span uses the resolved model id (see [LLM_MODELS.md](LLM_MODELS.md)); filter traces by model or by run name (e.g. `search_agent.split_focus_subqueries`, `search_agent.policy_rerank`, `retrieval.kb_web_gate`).

## No Traces Appearing?

1. **Check both projects** — Traces may appear under `default` or `email_draft_agent`
2. **Trigger an agent run** — Traces only appear when you run the agent (dashboard "Run" or `/agent/run` API)
3. **Wait a few seconds** — Traces can take 5–30 seconds to show up
4. **Check Configure vs env source** — In Configure, confirm LangSmith key status, then run the agent once to emit traces
5. **API key** — Ensure the key is valid and has no typos (starts with `lsv2_pt_`)
