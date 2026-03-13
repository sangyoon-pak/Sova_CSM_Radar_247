## Short-term TODOs

### Batch 1 – Architecture & behavior
- **B1-1 (tmr-6)**: Validate the current search agent architecture and tool wiring (which Python files are invoked as tools and how they interact).
- **B1-2 (tmr-3)**: Refine `src/agent/prompts.py` and overall behavior so the agent works cleanly for both cron jobs and direct user queries (no hard allowlist, no rejecting user questions).

### Batch 2 – Memory & history
- **B2-1 (tmr-1)**: Add agent memory backed by a small DB and expose delete-history controls in the UI.
- **B2-2 (tmr-2)**: Design and implement memory flushing/compaction to keep token count low while preserving important context.

### Batch 3 – UX for tools & docs
- **B3-1**: On the UI, show tool calls (e.g. `fetch_inbox_emails`, `search_appier_docs`) in near real-time while a run is in progress.
- **B3-2**: Ensure that even for non-cron user queries, the agent can look up and use the same documentation flow as cron-driven probes.

### Batch 4 – Document ingestion & notifications
- **B4-1 (tmr-4)**: Enhance the dashboard UI so users can upload documents directly into the knowledge base.
- **B4-2 (tmr-5)**: Implement a document upload parser/ingestion pipeline so uploaded files are normalized and searchable by the search agent.
- **B4-3**: Build a notification pipeline (decide channels and triggers) so the system can notify when drafts are ready or when errors occur.