# Release Checklist

Use this checklist before sharing Sova beyond private/internal development.

## Product Execution First

### Agent Quality And Guardrails

- [ ] CSM relevance guardrails prevent internal-only `email`s (for example quota alerts) from creating action cards.
- [ ] User-guided guardrail controls are available in UI (avoid hardcoded-only filtering) for agent's behaviour. 
- [ ] Previously probed threads can be re-processed correctly after relevant backend state reset.
- [ ] Product-related inquiry paths reliably trigger retrieval before drafting action cards.


### Retrieval And Knowledge Behavior

- [ ] `docs/SEARCH_AGENT.md` is treated as the retrieval foundation and reflects current behavior.
- [ ] Uploaded less-refined documents (for example PDF/doc-derived text) are validated in retrieval flow.
- [ ] Retrieval metadata is retained so follow-up Q&A can reference prior evidence.
- [ ] Known retrieval regressions (for example specific inquiry misses) are tested before release.

### Product Readiness

- [ ] Action cards include thread title and customer domain/name metadata.
- [ ] Card statuses support `not_started`, `in_progress`, `completed`.
- [ ] Action cards support status change and sorting/filtering in dashboard UI.
- [ ] Text feedback input is available for action-card-level self-evolution (not only like/dislike).
- [ ] OpenRouter credit balance is visible in UI across tabs when OpenRouter is configured.
- [ ] Workbench thread timestamps respect configured timezone.
- [ ] action card should have client's email. Should consider what is the best way as agent can be confused on the thread with many email addresses and sender and recepient keeps changing between 
- [ ] texts spilling on the UI. for example, action card, uploaded documents, words go out of space rather than come below.. 

### Cron And Scheduling Readiness

- [ ] Cron supports both manual UI setup and natural-language agent-assisted setup.
- [ ] Cron tab UX clearly explains interval behavior and next-run expectations.
- [ ] Scheduled probe flow can produce drafted action items with relevant document evidence.

## Release Hardening And Distribution

### Documentation Readiness

- [ ] Top-level README reflects current architecture and setup.
- [ ] Install path is validated against [INSTALLATION.md](INSTALLATION.md).
- [ ] Gmail setup is validated against [GMAIL_SETUP.md](GMAIL_SETUP.md).
- [ ] Installation docs include OpenRouter setup and fallback guidance for non-OpenRouter users.
- [ ] Search/retrieval behavior is consistent with [SEARCH_AGENT.md](SEARCH_AGENT.md).
- [ ] Guardrails and action-card contract docs are current.
- [ ] Architecture diagram is present and aligned with current subagent/retrieval flow.
- [ ] Self-evolution/feedback behavior is documented in md files.

### Security And Secrets

- [ ] `credentials.json` is not committed.
- [ ] API keys/tokens are not present in tracked files.
- [ ] Local OAuth/token material under `scripts/.local/` is excluded.
- [ ] Any leaked key is rotated before release.

### Knowledge And Data Hygiene

- [ ] Internal/private knowledge-base content is excluded from public distribution.
- [ ] Appier or other restricted client docs are removed or redacted.
- [ ] Runtime data directories do not include private user/customer data in release artifacts.
- [ ] On a machine that held trial runs, optionally run **`python scripts/reset_local_data.py --yes`** (stop the server first) to wipe local SQLite, KB FTS, RAG artifacts, and uploaded KB files under `data/` before publishing or sharing a clean tree. See [scripts/README.md](../scripts/README.md).

### Repository Hygiene

- [ ] Remove obsolete experiments and irrelevant artifacts.
- [ ] `scripts/` matches [scripts/README.md](../scripts/README.md) (runtime, install, and optional local data reset).
- [ ] Confirm `.gitignore` blocks sensitive/generated content.

## Cross-Platform Expectations

- [ ] Host-install instructions are clear for macOS/Linux/Windows paths.
- [ ] Distribution messaging clarifies host-first operation (`venv + python run.py`).
- [ ] `gog` and OAuth constraints are explicitly documented for non-container environments.

## Naming And Public UX

- [ ] Product naming is consistent as **Sova - CSM Radar Agent 24/7** across docs.
- [ ] Public install guidance can be reached from GitHub README.
- [ ] Landing/Configure links are ready to point to public docs once published.
- [ ] Landing page links to published GitHub/docs guidance after release.
- [ ] Configure tab includes link path to published `gog` setup guidance after release.
