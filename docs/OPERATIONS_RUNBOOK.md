# Operations Runbook

Use this runbook to debug common Sova issues and maintain reliable behavior.

## Quick Health Checks

- API health: `GET /health` should return `{"status":"ok"}`.
- Runtime config: verify Configure values are saved as intended.
- Search prerequisites: confirm `rg --version` works in runtime environment.
- Gmail prerequisites (if used): `gog` binary available and OAuth token usable.

## Symptom To Cause Map

### 1) Non-CSM emails still create action cards

Likely causes:

- Relevance prompt/logic too permissive
- Missing exclusion policy for internal notifications
- User guidance not configured

Actions:

- Review guardrail outcomes and rationale logs.
- Tighten relevance policy per [AGENT_GUARDRAILS.md](AGENT_GUARDRAILS.md).
- Add sender-domain or intent exclusions in UI-configurable policy.

### 2) Previously probed email does not re-create card after backend data delete

Likely causes:

- Residual dedup state remains in a second table/cache.
- Probe path is not using the same reset assumptions.

Actions:

- Verify all related records were removed, not only primary card rows.
- Re-run probe and compare decision logs for dedup reason.
- Treat as bug if state is clean but thread remains skipped.

### 3) Product-related thread does not run retrieval from uploaded docs

Likely causes:

- Search invocation path was skipped for the thread.
- Uploaded document index not refreshed/reindexed.
- Scope routing/ranking suppresses relevant docs.

Actions:

- Confirm `search_product_docs`/`search_with_agent` path executed.
- Reindex after upload and re-test.
- Inspect retrieval debug output for source mix and ranking.

### 4) RAG not triggered for expected inquiry

Likely causes:

- Incorrect search terms from extraction/split
- Query classified as insufficiently actionable
- Embedding/index issues

Actions:

- Reproduce with a small Workbench question or **Scan inbox**, then inspect **Run history** / LangSmith traces for `search_product_docs` and subquery steps.
- Check subqueries and refined term variants in logs or trace payloads.
- Validate embedding/provider configuration in Configure or environment.

### 5) Timezone mismatch in workbench thread times

Likely causes:

- UI rendering uses local browser time while backend uses configured timezone.
- Missing normalization before display.

Actions:

- Verify configured timezone value.
- Compare backend timestamp payload vs rendered UI value.
- Normalize timezone conversion rules in frontend/backend boundary.

### 6) Cron jobs confusing or not meeting intent

Likely causes:

- UI wording does not map cleanly to interval semantics.
- No clear separation between agent-created and manually created jobs.

Actions:

- Expose human-readable schedule summary.
- Validate next-run preview before save.
- Keep both manual and NL-assisted creation paths with clear labels.

## Recommended debug flow

- Start app: `python run.py`
- Use **Workbench** or **Scan inbox** for realistic retrieval + tool traces.
- Use **Run history** (expand a run) and optional **LangSmith** (see [LANGSMITH.md](LANGSMITH.md)) for LLM/tool spans.

## Observability Checklist

- Enable tracing (LangSmith) for difficult behavior regressions.
- Keep run-level logs for relevance gate, retrieval path, and card decision.
- Capture before/after examples when changing guardrails.
