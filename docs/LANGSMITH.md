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
LANGSMITH_PROJECT=Sova_CSM_Radar_247
```

For ad-hoc Python, export `LANGSMITH_*` in your shell (process env is not read from Configure DB unless the app loads it).

**Project name matters:** Whatever you save under **Configure → LangSmith project** is written to the app database and **overrides** `LANGSMITH_PROJECT` from the process environment for agent runs. Traces are tagged to that name. If this doc shows one example name but your Configure value differs (e.g. `sova` or `my_team`), you must open **that** project in LangSmith to see new traces. Confirm the effective name via **`GET /settings/runtime`** (JSON includes **`langsmith_project`** and **`langsmith_tracing`**) or the Configure form after save.

## Verify Tracing

Start the app (`python run.py`), enable LangSmith in **Configure**, then trigger any agent run (Workbench, **Scan inbox**, or **Run history** / API). Open [smith.langchain.com](https://smith.langchain.com) → **Projects** → **the same project name as Configure** (example: `Sova_CSM_Radar_247`; yours may differ) after a few seconds.

Each LLM span uses the resolved model id (see [LLM_MODELS.md](LLM_MODELS.md)); filter traces by model or by run name (e.g. `search_agent.split_focus_subqueries`, `search_agent.policy_rerank`, `retrieval.kb_web_gate`).

## No Traces Appearing?

1. **Open the correct LangSmith project** — Must match **`langsmith_project`** from Configure / **`GET /settings/runtime`**. This is the most common “suddenly empty” confusion after renaming the project in Configure or using a different workspace.
2. **Tracing toggle** — **Configure → LangSmith tracing** = **true**. If a DB row exists with `false`, it overrides a `true` in `.env` until you change it.
3. **API key present** — Configure shows “key stored in database” / env; `_ensure_langsmith_env` sends nothing to LangSmith if tracing is on but the key is missing.
4. **Trigger an agent run** — Traces appear only when the agent runs (Workbench, **Scan inbox**, probe, or `/agent/run`). Inbox-peek short paths still invoke tools but parent traces use `email_agent.run_agent` when routing runs the full agent.
5. **Wait a few seconds** — Ingestion can take ~5–30s; refresh the project view.
6. **Org / filters in LangSmith** — Check workspace, date filter, and that you are not in a different LangSmith account than the API key.
7. **API key validity** — Keys start with `lsv2_pt_`; rotate if revoked.

### Quick local check (developers)

From repo root with the same `data/agent.db` as the running server:

```bash
.venv/bin/python -c "from src.runtime_config import effective_langsmith_project, effective_langsmith_tracing; print(effective_langsmith_project(), effective_langsmith_tracing())"
```

You should see the project name to select in the LangSmith UI and `True` if tracing is enabled.
