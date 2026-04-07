# Scripts Inventory

This folder is intentionally small and each file has a current use:

- `gmail-get-decoded.py` — Gmail read helper used by runtime inbox fetch tool.
- `install-gog-local.sh` — local gog CLI installer for Gmail OAuth setup.
- `test-gmail-local.sh` — quick local Gmail verification helper.
- `test_search_agent_e2e.py` — end-to-end retrieval smoke test.
- `test_retrieval_local.py` — local retrieval debugging with query/file inputs.
- `test_full_agent_reply.py` — full agent debug run with optional retrieval logging.
- `test_langsmith_trace.py` — minimal LangSmith tracing verification.

If a script is no longer referenced in docs, runtime paths, or active debugging workflows,
it should be removed in the next cleanup pass.

