# LLM models (OpenRouter / OpenAI-compatible)

Chat calls use **`src/agent/chat_llm.py`** (`get_chat_llm`). Model ids are **not** hard-coded in call sites; they come from settings (`src/config.py`) and optional **Configure** DB overrides (see `src/runtime_config.py`).

**Provider preset:** `LLM_PROVIDER_PRESET` — `openrouter` (default), `openai` (direct OpenAI + `OPENAI_API_KEY`), or `gemini_openrouter` (Gemini model ids via OpenRouter). Same HTTP client; base URL and keys follow the preset (see `.env.example` as a reference list and **Configure** in the UI).

**API keys (Configure vs environment):** With **`openai`**, runtime key sources are **`openai_api_key`** (saved in Configure) and **`OPENAI_API_KEY`** (environment). With **`openrouter`** / **`gemini_openrouter`**, key sources are **`openrouter_api_key`** (saved in Configure) and **`OPENROUTER_API_KEY`** (environment). The OpenAI preset always uses **`https://api.openai.com/v1`** for chat; there is no separate configurable OpenAI chat base URL in the app.

**Configure grey hints:** Recommended defaults for base URL and model ids follow the **provider preset dropdown** (even before Save) via `recommended_hints_by_preset` from **`GET /settings/runtime`**, so you are not shown OpenAI defaults while the dropdown is set to OpenRouter.

## Environment variables

| Variable | Role | Fallback |
|----------|------|----------|
| `LLM_MODEL` | Default chat model for every role | Required baseline (set in Configure or env; see `.env.example`) |
| `LLM_MODEL_MAIN` | Main email agent (`create_agent` + tools) | `LLM_MODEL` |
| `LLM_MODEL_SEARCH_JSON` | Search: subquery split, term extraction, sufficiency, refine **and** small JSON “intent routers” in the main agent (see below) | `LLM_MODEL` |
| `LLM_MODEL_KB_WEB_GATE` | **RC path only:** JSON gate before hosted web in `search_rc_web` (`proceed_web` / `reason`). **Separate** from `LLM_MODEL_SEARCH_JSON` — does **not** affect intent routers or retrieval sufficiency JSON. | `LLM_MODEL` (via `effective_llm_model()` when unset — see `effective_llm_model_kb_web_gate()`) |
| `LLM_MODEL_SEARCH_RERANK` | Search: snippet rerank (1–5 scores) | `LLM_MODEL` |
| `LLM_MODEL_MEMORY` | Memory compaction (summarize old interactions) | `LLM_MODEL` |
| `RC_WEB_RETRIEVAL_MODE` | `kb_first` (default) or `always_augment` — controls whether `search_rc_web` always runs hosted web after KB; **not** an LLM model (stored like other runtime keys / Knowledge UI). | `kb_first` |

Embedding / RAG vectors are separate: `RAG_EMBEDDING_PROVIDER` and `RAG_EMBEDDING_MODEL` (Configure, env, or defaults — see `src/agent/tools/doc_search.py`).

## Web search (RC URLs)

Web search is enabled **only** when the user has saved and enabled RC URLs in the dashboard.

- RC URLs are managed via the UI and stored in the local DB.
- The agent can call `search_rc_web()` to combine **local KB** (`search_with_agent_structured`) with optional **hosted web** (`run_web_search` in `hosted_web_search.py`) per enabled domain. Provider behavior follows **Configure** preset (OpenRouter web plugin vs OpenAI Responses + `web_search` tool — same entrypoint).
- **KB→web gate:** In **`kb_first`** mode, a dedicated JSON step (`kb_web_gate.evaluate_kb_web_gate`, LangSmith name `search_rc_web.kb_web_gate`) decides whether to call hosted web after non-empty KB. Use **`LLM_MODEL_KB_WEB_GATE`** / Configure to tune it independently of **`LLM_MODEL_SEARCH_JSON`**. **`always_augment`** (Knowledge → RC URLs) skips the gate and always runs web after KB (higher token cost).

## JSON intent routers (`LLM_MODEL_SEARCH_JSON`)

The **same** resolved model as search JSON steps (`effective_llm_model_search_json()` in `src/agent/email_agent.py`) powers **lightweight routing** calls that must return parseable JSON:

- **`inbox_peek` vs full agent** — `_route_user_request`: a quick peek at the inbox listing without spinning up the full tool loop when the user only asked “what’s in my inbox”.
- **`run_full_inbox_probe` vs normal chat** — when `PROBE_THREAD_INTENT_CLASSIFIER` is in **`llm`** mode, a single classifier decides whether a Workbench message should trigger a **full inbox probe** (Gmail triage + dashboard merge) or stay in chat mode.

If you point `LLM_MODEL_SEARCH_JSON` at a model that is **cheap but sloppy on JSON**, retrieval **and** these routing decisions can degrade. Prefer models that follow JSON-only instructions reliably.

## KB→web gate (`LLM_MODEL_KB_WEB_GATE`)

- **Purpose:** One small JSON contract per RC retrieval: `{ "proceed_web": bool, "reason": str }` after the final diversified KB matches.
- **Not** the same role as `LLM_MODEL_SEARCH_JSON` — keep search/JSON routers on a model that handles **many** JSON shapes; optionally point the gate at a **cheap** model that only needs this single schema, or leave unset to inherit **`LLM_MODEL`**.
- **Code:** `src/agent/tools/kb_web_gate.py` (`effective_llm_model_kb_web_gate()` in `src/runtime_config.py`).

## Typical tuning

- Use a **stronger** model for `LLM_MODEL_MAIN` (multi-step tool use, drafting).
- Use a **cheaper** model for `LLM_MODEL_SEARCH_JSON` if it reliably returns strict JSON **including** the intent-router prompts above.
- Use a **mid-tier** model for `LLM_MODEL_SEARCH_RERANK` if the cheap model mis-scores snippets.

## Code map

| Purpose | Module |
|---------|--------|
| Main agent | `src/agent/email_agent.py` |
| Subquery split, sufficiency, refine | `src/agent/tools/search_agent.py` |
| KB→web gate (RC) | `src/agent/tools/kb_web_gate.py` |
| Term extraction | `src/agent/search_terms_extractor.py` |
| Rerank | `src/agent/tools/search_agent.py` |
| Memory compaction | `src/agent/memory.py` |

## LangSmith

When tracing is enabled, runs still group by **run name** / **tags** (for example `search_agent.split_focus_subqueries`, `retrieval.kb_web_gate` on the gate LLM invoke, and `@traceable` name `search_rc_web.kb_web_gate`). The **model id** in each trace reflects the resolved configuration above.
