# Project TODO

Last updated: 2026-04-15

Single checklist: **completed** work from the rebuild + **remaining** tasks (merged from the former `docs/IMPLEMENTATION_TODO_STATUS.md` and this file). For implementation detail, see paths in the completed section.



### Configure / observability


- [x] **LangSmith**: API + trace settings in Configure so users can opt in to tracing/monitoring (`docs/LANGSMITH.md` alignment)
- [x] **Workbench** message/thread timestamps use the same **timezone** as Configure (not only browser local)

### Landing & layout

- [x] **Landing**: “Next steps” **collapsed by default**, expand on click; fold **email provider** note into that block; remove empty spacing
- [x] **Knowledge — uploaded documents** list: **collapsed by default**, expand on click; tighten spacing (no large empty gaps)

### Action dashboard / cards

- [ ] **Action cards**: **collapsed by default**, expand on click; **bulk select + bulk delete** dismiss
- [ ] **Action board**: **text feedback** to the agent (not only like/dislike / Run history)
- [ ] **Optional**: sort/filter by **priority** or **customer domain** (metadata exists; UI controls not built yet)
- [ ] each card should have the retrieved doc data in metadata. It might not have to show all the details but when user asks an extensive question, agent should be able to answer. 
- [ ] action cards are made but it does not retrieve from document to curate the card yet..
### Workbench / threads

- [ ] **Bulk select + bulk delete** for threads

### Cron

- [ ] Cron tab **UX** (clearer interval-oriented flows, presets, copy)
- [ ] Optional: user asks agent to **create/adjust** cron jobs in natural language (beyond manual CRON expression)

---

## Remaining — agent behavior & docs

### Foundations (from original backlog)

- [ ] Keep **search/retrieval** aligned with `docs/SEARCH_AGENT.md` as the foundation; extend features on top
- [ ] **Docs refresh**: architecture diagram (Users → Agent → subagents → RAG → answer); sync all `docs/*.md` with current code
- [ ] **Install guide**: external deps (API tokens, gog, OpenRouter), and alternatives if OpenRouter is not an option
- [ ] **Docs**: why retrieval is designed this way (business-critical / sustainable)
- [ ] **Docs**: self-evolution / learning from feedback

### Agent utility / RAG

- [ ] Card should be created based on the launguage the email is mostly used in. 
- [ ] Investigate runs where inbox is fetched but **RAG is not used** 
- [ ] **Less-refined uploads** (PDF, noisy docs): expected behavior, limits, and UX messaging

### Action cards (edge cases)

- [ ] **Internal-only** mail (e.g. quota notices) still surfacing as cards: tune guardrails / optional **query-analysis** sub-step
- [ ] **Re-probe after DB reset** still missing threads/cards: verify dedupe keys and probe merge behavior when “fresh start” is intended

---

## Remaining — pre-distribution / distribution

### Pre-distribution

- [ ] No Appier-internal-only documents in the public repo
- [ ] Remove irrelevant scratch/test artifacts from the tree where appropriate
- [ ] **Knowledge base** content not pushed to public GitHub (`.gitignore` / policy); verify
- [ ] No secrets/tokens committed

### Distribution

- [ ] Repo/product naming: **Sova — CSM Radar Agent 24/7** (local + GitHub) when ready
- [ ] **Host install** story: mac/linux/windows via venv + `run.py` (not container-first); `gog`/OAuth need a normal OS env (`docs/GMAIL_SETUP.md`)
- [ ] **Public docs UX**: canonical `docs/INSTALLATION.md`; README links; optional future docs site; landing links when published

### Post-distribution

- [ ] Landing links to **GitHub** guides once the repo is public
- [ ] Configure **gog** section links to the published GitHub doc page
- [ ] simple user-guide video that shows what it does. you can 
---

## Pointer

The former standalone file `docs/IMPLEMENTATION_TODO_STATUS.md` is merged here. See that path for a one-line redirect.
