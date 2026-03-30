# Knowledge Base — Public / NotebookLM

Client-safe copy of Appier solution docs for NotebookLM. Clients can add these as sources to ask AI questions without contacting support.

## Fresh RC Crawls (AIQUA, AIRIS, BotBonnie)

Crawled from live docs sites; replaces outdated RC parts:

| Product | Folder | Parts | Source |
|---------|--------|-------|--------|
| AIQUA | `aiqua_rc/` | aiqua_part_1 … aiqua_part_6 | docs.aiqua.appier.com |
| AIRIS | `airis_rc/` | airis_part_1 … airis_part_3 | docs.airis.appier.com |
| BotBonnie | `botbonnie_rc/` | botbonnie_part_1 … botbonnie_part_3 | docs.botbonnie.appier.com |

Regenerate with: `python urls_to_md.py` (from `notebooklm_export/`).

## Legacy / Other Sources

Copied from `openclaw_project/knowledge-base/` with the following edits for public use:

| File | Change |
|------|--------|
| **016** (SLA) | Removed regional CS lead names and emails; replaced with "contact your designated Appier Customer Success Manager" |
| **026** (AIQUA FAQ) | Removed internal Confluence link, Sales dept ref, MAU tiers, roadmap dates, PM team ref; Question_PMM_EN→Question Answer; generic contact refs |
| **027, 028** (AIRIS FAQ) | Removed PM/PMM/Sales refs, Amorepacific, ESS placeholders, informal tone, internal Drive links, "not publicly available"; Question_PMM_EN→Question Answer |
| **029** (BotBonnie FAQ) | Removed internal Slack channel, PM refs, BotBonnie product team refs, Zwiz.ai, RT Mart, internal Google docs, "scheduled in 2025"; Question_PMM_EN→Question Answer |
| **030** (cross-product) | Removed PMM ref, "don't have publicly available"; Question_PMM_EN→Question Answer |
| **051, 052** (AI Agent) | Removed Q4/Q1 2026 roadmap dates, Danny Lin/Data Cloud PM contact; generic "future release" and "contact your Appier representative" |
| **005, 009** | Removed raw HubSpot CMS metadata (hs_id, hs_created_at, etc.) |
| **068** (AIRIS RC) | Replaced "Section In Progress / currently doing testing" with neutral "section is being updated" |

## Usage

1. Upload the `.md` files in this folder as sources to your NotebookLM notebook.
2. Clients can then ask questions about Appier products (AIRIS, AIQUA, BotBonnie, etc.) directly in NotebookLM.

## Updating

When `openclaw_project/knowledge-base/` is updated, re-copy and re-apply the same edits to 016 and 026 in this folder.
