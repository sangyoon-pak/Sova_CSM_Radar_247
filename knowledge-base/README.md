# Knowledge Base for OpenClaw RAG

Appier **solution** documents for ChromaDB retrieval. Used by the OpenClaw agent to answer technical client queries.

**Scope:** Product docs, reference cards, FAQs, technical specs. Sales materials and competitor docs are excluded.

## Source

Documents are formatted from NotebookLM exports via:

```bash
cd ../notebooklm_export
python format_for_rag.py
```

This produces markdown files with YAML frontmatter:

- `source`, `file_id`, `doc_type`, `product`, `content_type`, `language`
- `guide_summary`, `guide_keywords` (from NotebookLM AI summaries)

## Doc Types

| doc_type | Description |
|----------|-------------|
| product_overview | AIRIS, AIQUA, BotBonnie, AI Agent |
| competitive_analysis | Braze, Tealium, CleverTap, etc. |
| sales_material | Sales decks, playbooks, Growth Plan |
| reference_card | RC parts (aiqua_rc, airis_rc, bb_rc) |
| faq | ESS FAQ Bot, AI Agent FAQs |
| case_study | POP MART, Virgin Red, etc. |
| technical_docs | Image Specs, Developer guides |

## Ingestion

```bash
# From openclaw_project root
pip install chromadb langchain-text-splitters sentence-transformers pyyaml

# Ensure ChromaDB is running (scripts/deploy-chromadb.sh)
python scripts/ingest-knowledge-base.py
```

See `docs/RAG_ENGINE_CHOICE.md` for ChromaDB vs ClawRAG recommendation.
