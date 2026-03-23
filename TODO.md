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
- **B4-3**: Build a notification pipeline (decide channels and triggers) so the system can notify when drafts are ready or when errors occur.



## long-term
- Can users also upload documents as text files or provide the URL link on the UI on top ? 