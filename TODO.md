## Short-term TODOs

### Batch 1 – Architecture & behavior
- [x] **B1-1 (tmr-6)**: Validate the current search agent architecture and tool wiring (which Python files are invoked as tools and how they interact).
- [x] **B1-2 (tmr-3)**: Refine `src/agent/prompts.py` and overall behavior so the agent works cleanly for both cron jobs and direct user queries (no hard allowlist, no rejecting user questions).

### Batch 2 – Memory & history
- [x] **B2-1 (tmr-1)**: Add agent memory backed by a small DB and expose delete-history controls in the UI.
- [x] **B2-2 (tmr-2)**: Design and implement memory flushing/compaction to keep token count low while preserving important context.

### Batch 3 – UX for tools & docs
- [x] **B3-1**: On the UI, show tool calls / run events in near real-time while a run is in progress (via async run + `/agent/runs/:run_id` polling).
- [x] **B3-2**: Ensure that for non-cron user queries, the same doc-search flow (`search_product_docs` → search agent) is used when the agent determines product relevance.
- [x] **B3-3**: Tool outputs/details and chain/model steps are displayed under collapsible sections in the “Run trace” panel.
- [x] **B3-4**: Shows recent cron run summaries on the UI (via `/cron/summary`).

### Batch 4 – Document ingestion & notifications
- [x] **B4-1 (tmr-4)**: Enhance the dashboard UI so users can upload documents directly into the knowledge base.
- [x] **B4-2 (tmr-5)**: Implement a document upload parser/ingestion pipeline so uploaded files are normalized and searchable by the search agent (md/txt -> markdown into `knowledge-base/`).



------------------new----------------------
### UI
- [x] **Enterprise / CSM wording (v1)**: Dashboard rebranded to **Proactive CSM Assistant**; nav **Workbench**; product blurb under header; FastAPI title/README aligned. Folder rename remains separate (see Agent Utility).
- [x] **Combine chat + run (v1 — single workbench)**: One **CSM workbench** section: profile → actions → task prompt → latest response + **Run trace** → divider → **Follow-up conversation** (same agent backend). Reduces split-brain between “Run Agent” and “Chat Test.”
- **Proposal — next iterations (pick one path)**:
  1. **Unified thread (recommended long-term)**: Treat every user message as one row in `conversation_threads`; “Probe” / “Run with prompt” append to the thread and stream the same transcript. Sidebar: thread list + search.
  2. **Composer modes**: One textarea with a segmented control `[ Task | Chat ]`—Task runs probe-style tools by default, Chat stays lightweight; both log to the same run history with `mode` in metadata.
  3. **Split view (wide screens)**: Left: transcript; right: trace + citations; mobile stacks workbench → trace → chat.

Continue polishing density, empty states, and onboarding copy as the proactive CSM roadmap lands.



### Agent Utility 
- Build a notification pipeline (decide channels and triggers) so the system can notify when drafts are ready or when errors occur.
- need to handle the language dynamically. when asked in korean, doc retrieve can retrieve the data regardless of the language but output should be in the language it was asked in (both email probe and user <> interaction, the final output should be in the language the query is asked in)
- Shifting from email drafting agent to proactive assistant CSM agent. I badly want this agent to do this.
1) periodically probe inbox and analyse the queries
2) Agent should be able to sense if there are emails that come from the clients asking about what to do with appier product. If agent senses that it is appier product related client questions, it should be able to search through the docs and list up all the relevant information and actions item for CSM to review. Agent should be proactively also trying to answer the questions if they can as part of the process. 
3) Agent should be able to nofify the CSM. I think the best way is to notify CSM through the web browser push. I have web push notification muted still, I can tell if there is something on my email inbox on the top of the browser tab with the number within parenthesis (). 
4) we should change the name of the directory from 'email_draft_agent' to proactive_csm_agent
- cron job is to be set by users asking agent to set a cron job. e.g) I want you to probe email every 3 hours and get back to me with the drafted version of action items with the relevant documents that could answers the client email inquries. 



## wrap-up 
- appier related documents should not be exposed on the repo
- any important variables (API tokens etc) should not be exposed on the repo.
- update the md files that shows how to install this software package including external dependencies that requires users to install and configure such as API tokens, gogcli, and open router part. Include general guide line if openrouter is not an option for some users.  
- update the md files as for how the retrieval works and why this way can be business critical and sustainable. 
- update the md files as for how the agent self evolves. 
- the UI should include what this software is all about and what it is aiming to do to help CSM concisely can take reference from md files. 
- should include how to install all the dependencies and set variables (e.g API keys) on the MD file.  
- pack up the code to run in the container. 

- update the md files as for how the agent self evolves.  


