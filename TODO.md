## Short-term TODOs

- **tmr-1**: Add agent memory backed by a small DB and expose delete-history controls in the UI.
- **tmr-2**: Design and implement memory flushing/compaction to keep token count low while preserving important context.
- **tmr-3**: Revise `src/agent/prompts.py` so the agent works for both cron jobs and direct user queries without rejecting user questions.
- **tmr-4**: Enhance the dashboard UI so users can upload documents directly into the knowledge base.
- **tmr-5**: Implement a document upload parser/ingestion pipeline so uploaded files are normalized and searchable by the search agent.
- **tmr-6**: Validate the current search agent architecture and tool wiring (which Python files are invoked as tools and how they interact).
- on the UI, UI should show the tool calls ideally in real-time processing
- also even if it is not a cron job, when users query, it should be able to look up the docs same as cron jobs
