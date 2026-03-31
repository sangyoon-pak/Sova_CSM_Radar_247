## Short-term TODOs

### Batch 1 – Architecture & behavior
- [x] **B1-1 (tmr-6)**: Validate the current search agent architecture and tool wiring (which Python files are invoked as tools and how they interact).
- [x] **B1-2 (tmr-3)**: Refine `src/agent/prompts.py` and overall behavior so the agent works cleanly for both cron jobs and direct user queries (no hard allowlist, no rejecting user questions).

### Batch 2 – Memory & history
- [x] **B2-1 (tmr-1)**: Add agent memory backed by a small DB and expose delete-history controls in the UI.
- [x] **B2-2 (tmr-2)**: Design and implement memory flushing/compaction to keep token count low while preserving important context.

### Batch 3 – UX for tools & docs
- [x] **B3-1**: On the UI, show tool calls / run events in near real-time while a run is in progress (via async run + `/agent/runs/:run_id` polling).
- [x] **B3-2**: Ensure that for non-cron user queries, the same doc-search flow (`search_appier_docs` → search agent) is used when the agent determines Appier/product relevance.
- [x] **B3-3**: Tool outputs/details and chain/model steps are displayed under collapsible sections in the “Run trace” panel.
- [x] **B3-4**: Shows recent cron run summaries on the UI (via `/cron/summary`).

### Batch 4 – Document ingestion & notifications
- [x] **B4-1 (tmr-4)**: Enhance the dashboard UI so users can upload documents directly into the knowledge base.
- [x] **B4-2 (tmr-5)**: Implement a document upload parser/ingestion pipeline so uploaded files are normalized and searchable by the search agent (md/txt -> markdown into `knowledge-base/`).

------------------new----------------------
- Build a notification pipeline (decide channels and triggers) so the system can notify when drafts are ready or when errors occur.
- need to handle the language dynamically. when asked in korean, doc retrieve can retrieve the data regardless of the language but output should be in the language it was asked in. 
- remove all the appier specific dependency from the core codebase to other adjacent files (e.g @prompt.py, memory.py, etc)
- [ ] Remove remaining Appier-specific dependencies outside the retrieval core (e.g. email agent wrapper name, prompts, tool docstrings). Goal: share the search tool/stack across industries with only config/RC metadata changes.
- [ ] Add neutral configuration examples (e.g. `RC_SCOPE_*`) to docs/ and verify both `RC_SCOPE_ENABLE=true/false` behave as expected.
- [ ] Add regression tests that assert “no hard-coded product/appier strings” inside retrieval core modules (`doc_search.py`, `search_agent.py`).
- [ ] Audit and delete any scripts that are no longer used after the refactor (ensure `scripts/` only contains relevant entrypoints).
- Agent memory for self-evolution. If the answer is not correct, it should take note and memorise it. But how can we make it self-evolve ? 
- Shifting from email drafting agent to proactive assistant CSM agent. e.g Agent probes email inbox and find look up client queries and analyse the intent of the queries. Agent decides if it is Appier product-related. If yes, it searches documents to find the most relevant infomation and notify CSM with answers to each of the client query so that CSM can draft and send the email dramatically fast. 
- Can users also upload documents as text files or provide the URL link on the UI on top ? 
- what is the best way for agent to nofify CSM ? 
- all still the retrieval is week. AR and BB should not be retrieved. When improving it, we should always avoid hard-coding into the core code base. 
Output : ere are the responses to your queries regarding the AIQUA API and campaign setup:

1. **Endpoint Confirmation**: The endpoint `POST https://api.quantumgraph.com/qga/clients-data/` is indeed the correct endpoint for uploading events to AIQUA, and it aligns with the "Event Upload API" you mentioned [source](060_aiqua_part_6.md).

2. **Event Not Showing in Dropdown**: If the `tier_price_dropped` event is not appearing in the campaign trigger dropdown, it could be due to a delay in the event registration or a configuration issue. Ensure that the event is correctly set up and registered in AIQUA. If the issue persists, it might require further investigation by your Appier Customer Success Manager (CSM) or support team.

3. **Device Value for App Push Campaigns**: When setting up app push campaigns, the `device` value should match the target platform. Use "android" or "ios" for respective platforms. Using "web" is generally for web-based triggers and might not trigger app-specific campaigns [source](026_ESS FAQ Bot_AIQUA_v2 (20250317) - Sheet1.pdf).

4. **User Action Trigger for Tier Events**: For campaigns based on user actions like the `tier_price_dropped` event, each user must trigger the event individually. The event should be sent for each user you want to target, rather than sending it once for a group [source](061_airis_part_1.md).

5. **Tier Configuration**: Setting up tiers such as "VIP" can be done through segmentation in AIQUA. You can create segments based on various attributes, including membership status or other custom criteria. This allows for flexible targeting and personalization [source](062_airis_part_2.md).

6. **Batch Event Upload**: The AIQUA API currently supports individual event uploads per request. The rate limit is 2 requests per second, 20 requests per minute, and 250 requests per day. For large volumes, you would need to manage the requests within these limits or contact Appier support for potential batch processing solutions [source](060_aiqua_part_6.md).

If you need further assistance, I recommend reaching out to your Appier CSM or support team for detailed guidance tailored to your setup.
