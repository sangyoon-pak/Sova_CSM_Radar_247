# Project TODO

Last updated: 2026-04-15

Single checklist: **completed** work from the rebuild + **remaining** tasks (merged from the former `docs/IMPLEMENTATION_TODO_STATUS.md` and this file). For implementation detail, see paths in the completed section.

---


----
Agent is not reacting to the right queries. clearly some of the email I mentioned should have been created as cards.. should investigate why ? 

agent thread on workbench : 
nbox probe — no dashboard items (nothing required CSM follow-up).

The email from Confluence is a weekly content recommendation and does not require any action.
User
4/15/2026, 1:42:20 AM
what are the emails part of the probe you collected ?
Sova Agent
4/15/2026, 1:42:33 AM
Here are the emails that were part of the probe:

1. **From:** Confluence  
   **Subject:** sangyoon.park, your team is working on these pages -- join the conversation  
   **Date:** Wed, 15 Apr 2026  
   **Summary:** Weekly content recommendations from Confluence, no action required.

2. **From:** 김민찬_함샤우트글로벌  
   **Subject:** 애피어 Daily News Monitoring_260415  
   **Date:** Wed, 15 Apr 2026  
   **Summary:** Daily news monitoring report for Appier, no immediate action required.

3. **From:** Michael Chang (JIRA)  
   **Subject:** [JIRA] (QGWL-25315) [APmall] Support for Direct "Opt-Out" Button in App Push (KISA Compliance)  
   **Date:** Tue, 14 Apr 2026  
   **Summary:** Discussion on compliance with KISA regulations for app push notifications, requires further legal or compliance team input.

4. **From:** Sangyoon Park  
   **Subject:** Re: [아모레몰] 마케팅활용동의 회원 속성 업데이트 문의  
   **Date:** Tue, 14 Apr 2026  
   **Summary:** Follow-up on marketing consent attribute updates in AIQUA, discussing technical details and seeking clarification.

5. **From:** 'Woopra' via Customer Success Team  
   **Subject:** [AIRIS QUOTA EXCEEDED]: 漢神百貨 (10,421,283/10,000,000) [104.21%]  
   **Date:** Tue, 14 Apr 2026  
   **Summary:** Notification of quota exceeded for a client, requires attention to manage usage.

6. **From:** 'Woopra' via Customer Success Team  
   **Subject:** [AIRIS QUOTA EXCEEDED]: Evolution Wellness IP (5,188,439/5,000,000) [103.77%]  
   **Date:** Tue, 14 Apr 2026  
   **Summary:** Notification of quota exceeded for another client, requires attention to manage usage.

7. **From:** 'Gamma' via CSM_KR  
   **Subject:** Your Gamma Google Slides are ready  
   **Date:** Tue, 14 Apr 2026  
   **Summary:** Notification that Google Slides are ready, no immediate action required.

8. **From:** 김상오/컨센트릭스  
   **Subject:** Re: [AIQUA] Push 개인화 발송 방식 관련 가이드 미팅 요청  
   **Date:** Tue, 14 Apr 2026  
   **Summary:** Inquiry about issues with AIQUA journey triggers and offline event uploads, requires technical investigation.

9. **From:** SY Park  
   **Subject:** [아모레퍼시픽] API를 통한 푸시 캠페인 CID 생성 문의  
   **Date:** Tue, 14 Apr 2026  
   **Summary:** Inquiry about creating campaign IDs for push notifications via AIQUA API, requires clarification on API usage.

10. **From:** Appier Talent Intelligence  
    **Subject:** Team Building: You're listed for "Q2_CSM_Sales_Tech_Team_Building_202604"  
    **Date:** Mon, 13 Apr 2026  
    **Summary:** Notification about a team building event, no immediate action required unless unable to attend.

These emails cover various topics, including compliance, technical inquiries, quota notifications, and internal updates.
User
4/15/2026, 1:43:18 AM
why weren't these part of action cards ? 

8. **From:** 김상오/컨센트릭스  
   **Subject:** Re: [AIQUA] Push 개인화 발송 방식 관련 가이드 미팅 요청  
   **Date:** Tue, 14 Apr 2026  
   **Summary:** Inquiry about issues with AIQUA journey triggers and offline event uploads, requires technical investigation.

9. **From:** SY Park  
   **Subject:** [아모레퍼시픽] API를 통한 푸시 캠페인 CID 생성 문의  
   **Date:** Tue, 14 Apr 2026  
   **Summary:** Inquiry about creating campaign IDs for push notifications via AIQUA API, requires clarification on API usage.

4. **From:** Sangyoon Park  
   **Subject:** Re: [아모레몰] 마케팅활용동의 회원 속성 업데이트 문의  
   **Date:** Tue, 14 Apr 2026  
   **Summary:** Follow-up on marketing consent attribute updates in AIQUA, discussing technical details and seeking clarification.
Sova Agent
4/15/2026, 1:43:23 AM
The emails you mentioned were not part of action cards because the inbox probe was primarily focused on identifying emails that required immediate CSM follow-up or action. Here are the reasons why these specific emails might not have been highlighted as action cards:

8. **김상오/컨센트릭스:** This email involves technical issues related to AIQUA journey triggers and offline event uploads. While it requires technical investigation, it may not have been flagged as urgent or requiring immediate CSM intervention without further context or prioritization from the team.

9. **SY Park:** The inquiry about creating campaign IDs for push notifications via AIQUA API involves clarification on API usage. This type of inquiry often requires technical support or documentation review, which may not have been deemed urgent in the context of the inbox probe.

4. **Sangyoon Park:** This email involves a follow-up on marketing consent attribute updates in AIQUA. While it discusses technical details and seeks clarification, it may not have been prioritized as an immediate action item without additional context indicating urgency or impact.

In general, the inbox probe aims to identify emails that are clearly marked as requiring urgent action or follow-up based on the content and context provided. If these emails are indeed important, they can be manually escalated or reviewed by the CSM for further action.


---

## Remaining — product & UX

- [ ] Relevance outcome classification and exclusion guardrails in probe/card path (`src/agent/probe_actions.py`)
- [ ] Action card contract fields: `thread_title`, `customer_identifier`, `customer_domain`, `priority`, `confidence_label`, retrieval metadata lists, `csm_decision_summary`
- [ ] KB-first then RC web: `search_rc_web` calls KB retrieval before enabled RC URLs (`src/agent/tools/rc_web_search.py`)
- [x] Configure UI: guardrail domains, NL include/exclude intents, team guidance, strictness; optional Fernet at-rest encryption (`CONFIGURE_ENCRYPTION_KEY`) (`src/web/index.html`, `src/runtime_config.py`, `src/configure_crypto.py`)
- [x] Configure **Prompt overrides**: extra system text (all modes), probe trigger message, probe-mode append, action-review append (`src/agent/prompts.py` getters + Configure). Full base template still code-defined to preserve `{vendor_name}` / learning injection; extend via **Extra system instructions** first. 
- [ ] Probe metadata includes effective guardrail policy (`src/api/routes.py`, `src/scheduler/cron_manager.py`)
- [ ] Regression tests: `tests/test_probe_actions_guardrails.py`
- [ ] Dashboard: filter by action status / source / run status; sort by recency or status; status updates per card (`src/web/index.html`)
 

### Configure / observability


- [ ] **LangSmith**: API + trace settings in Configure so users can opt in to tracing/monitoring (`docs/LANGSMITH.md` alignment)
- [ ] **Workbench** message/thread timestamps use the same **timezone** as Configure (not only browser local)
- [x] Include/exclude intents: natural-language phrases + embedding/fallback matching (`src/guardrail_semantic.py`); encrypted at rest when `CONFIGURE_ENCRYPTION_KEY` is set; forms show decrypted text; remove rules by deleting lines
### Landing & layout

- [ ] **Landing**: “Next steps” **collapsed by default**, expand on click; fold **email provider** note into that block; remove empty spacing
- [ ] **Knowledge — uploaded documents** list: **collapsed by default**, expand on click; tighten spacing (no large empty gaps)

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

---

## Pointer

The former standalone file `docs/IMPLEMENTATION_TODO_STATUS.md` is merged here. See that path for a one-line redirect.
