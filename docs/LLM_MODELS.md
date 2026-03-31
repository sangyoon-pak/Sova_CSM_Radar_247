# LLM models (OpenRouter)

Chat calls use **`src/agent/chat_llm.py`** (`get_chat_llm`). Model ids are **not** hard-coded in call sites; they come from settings (`src/config.py`), which read `.env`.

## Environment variables

| Variable | Role | Fallback |
|----------|------|----------|
| `LLM_MODEL` | Default chat model for every role | Required baseline (see `.env.example`) |
| `LLM_MODEL_MAIN` | Main email agent (`create_agent` + tools) | `LLM_MODEL` |
| `LLM_MODEL_SEARCH_JSON` | Search: subquery split, term extraction, sufficiency, refine | `LLM_MODEL` |
| `LLM_MODEL_SEARCH_RERANK` | Search: snippet rerank (1–5 scores) | `LLM_MODEL` |
| `LLM_MODEL_MEMORY` | Memory compaction (summarize old interactions) | `LLM_MODEL` |

Embedding / RAG vectors are separate: `RAG_EMBEDDING_PROVIDER` and `RAG_EMBEDDING_MODEL` in `.env` (see `src/agent/tools/doc_search.py`).

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

When tracing is enabled, runs still group by **run name** / **tags** (for example `search_agent.split_focus_subqueries`). The **model id** in each trace reflects the resolved env vars above.
