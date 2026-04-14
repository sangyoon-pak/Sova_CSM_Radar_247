# LLM models (OpenRouter / OpenAI-compatible)

Chat calls use **`src/agent/chat_llm.py`** (`get_chat_llm`). Model ids are **not** hard-coded in call sites; they come from settings (`src/config.py`) and optional **Configure** DB overrides (see `src/runtime_config.py`).

**Provider preset:** `LLM_PROVIDER_PRESET` — `openrouter` (default), `openai` (direct OpenAI + `OPENAI_API_KEY`), or `gemini_openrouter` (Gemini model ids via OpenRouter). Same HTTP client; base URL and keys follow the preset (see `.env.example` as a reference list and **Configure** in the UI).

## Environment variables

| Variable | Role | Fallback |
|----------|------|----------|
| `LLM_MODEL` | Default chat model for every role | Required baseline (set in Configure or env; see `.env.example`) |
| `LLM_MODEL_MAIN` | Main email agent (`create_agent` + tools) | `LLM_MODEL` |
| `LLM_MODEL_SEARCH_JSON` | Search: subquery split, term extraction, sufficiency, refine | `LLM_MODEL` |
| `LLM_MODEL_SEARCH_RERANK` | Search: snippet rerank (1–5 scores) | `LLM_MODEL` |
| `LLM_MODEL_MEMORY` | Memory compaction (summarize old interactions) | `LLM_MODEL` |

Embedding / RAG vectors are separate: `RAG_EMBEDDING_PROVIDER` and `RAG_EMBEDDING_MODEL` (Configure, env, or defaults — see `src/agent/tools/doc_search.py`).

## Web search (RC URLs)

Web search is enabled **only** when the user has saved and enabled RC URLs in the dashboard.

- RC URLs are managed via the UI and stored in the local DB.
- The agent can call `search_rc_web()` to fetch relevant web docs from enabled RC URL domains, using OpenRouter’s Responses API + `web` plugin (with citations).

## Typical tuning

- Use a **stronger** model for `LLM_MODEL_MAIN` (multi-step tool use, drafting).
- Use a **cheaper** model for `LLM_MODEL_SEARCH_JSON` if it reliably returns strict JSON.
- Use a **mid-tier** model for `LLM_MODEL_SEARCH_RERANK` if the cheap model mis-scores snippets.

## Code map

| Purpose | Module |
|---------|--------|
| Main agent | `src/agent/email_agent.py` |
| Subquery split, sufficiency, refine | `src/agent/tools/search_agent.py` |
| Term extraction | `src/agent/search_terms_extractor.py` |
| Rerank | `src/agent/tools/search_agent.py` |
| Memory compaction | `src/agent/memory.py` |

## LangSmith

When tracing is enabled, runs still group by **run name** / **tags** (for example `search_agent.split_focus_subqueries`). The **model id** in each trace reflects the resolved configuration above.
