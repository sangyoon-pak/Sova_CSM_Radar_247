# Sova - CSM Radar Agent 24/7

Sova is an inbox-aware CSM copilot that turns customer email threads into evidence-backed follow-up actions using retrieval over product knowledge.

> Clone or rename the project folder as **`Sova_CSM_Radar_247`** (or your preferred name). Product naming should remain **Sova - CSM Radar Agent 24/7** across docs and UI.

## Walkthrough videos

Source files live in [docs/assets/](docs/assets/). On GitHub’s website, **Markdown links** to `.mp4` files in the repo open the file viewer and often feel like a download; **`<video src="...">`** only gets a real player if `src` points at a **direct file URL** (typically `raw.githubusercontent.com` or a URL GitHub generates when you attach a clip in the README editor).

Players below use **`raw.githubusercontent.com`** with ref **`docs%2Freadme-walkthrough-outcomes-2026-05-06`** (the **`docs/readme-walkthrough-outcomes-2026-05-06`** integration branch—the slash is encoded so GitHub parses the branch name correctly). Paths that said **`main`** 404 until those assets are merged into default branch. **After this work lands on `main`,** do a find-replace: `docs%2Freadme-walkthrough-outcomes-2026-05-06` → `main` in every URL below (and in the “Open in repo UI” links).

### Landing page and Configure





### Workbench

<video src="https://raw.githubusercontent.com/sangyoon-pak/Sova_CSM_Radar_247/docs%2Freadme-walkthrough-outcomes-2026-05-06/docs/assets/workbench.mp4" controls muted playsinline width="100%"></video>

Open in repo UI: [workbench.mp4](https://github.com/sangyoon-pak/Sova_CSM_Radar_247/blob/docs%2Freadme-walkthrough-outcomes-2026-05-06/docs/assets/workbench.mp4)

### Action dashboard cards

<video src="https://raw.githubusercontent.com/sangyoon-pak/Sova_CSM_Radar_247/docs%2Freadme-walkthrough-outcomes-2026-05-06/docs/assets/action%20card.mp4" controls muted playsinline width="100%"></video>

Open in repo UI: [action card.mp4](https://github.com/sangyoon-pak/Sova_CSM_Radar_247/blob/docs%2Freadme-walkthrough-outcomes-2026-05-06/docs/assets/action%20card.mp4)

### Knowledge base

<video src="https://raw.githubusercontent.com/sangyoon-pak/Sova_CSM_Radar_247/docs%2Freadme-walkthrough-outcomes-2026-05-06/docs/assets/Knowledge%20walkthrough.mp4" controls muted playsinline width="100%"></video>

Open in repo UI: [Knowledge walkthrough.mp4](https://github.com/sangyoon-pak/Sova_CSM_Radar_247/blob/docs%2Freadme-walkthrough-outcomes-2026-05-06/docs/assets/Knowledge%20walkthrough.mp4)

### Agent learning

<video src="https://raw.githubusercontent.com/sangyoon-pak/Sova_CSM_Radar_247/docs%2Freadme-walkthrough-outcomes-2026-05-06/docs/assets/Agent%20learning.mp4" controls muted playsinline width="100%"></video>

Open in repo UI: [Agent learning.mp4](https://github.com/sangyoon-pak/Sova_CSM_Radar_247/blob/docs%2Freadme-walkthrough-outcomes-2026-05-06/docs/assets/Agent%20learning.mp4)

### Cron (scheduled probes)

<video src="https://raw.githubusercontent.com/sangyoon-pak/Sova_CSM_Radar_247/docs%2Freadme-walkthrough-outcomes-2026-05-06/docs/assets/cron.mp4" controls muted playsinline width="100%"></video>

Open in repo UI: [cron.mp4](https://github.com/sangyoon-pak/Sova_CSM_Radar_247/blob/docs%2Freadme-walkthrough-outcomes-2026-05-06/docs/assets/cron.mp4)

**Alternative GitHub-native option:** In the GitHub web UI, edit this README and **drag each `.mp4`** into the editor. GitHub uploads it and inserts a host URL (often `user-images.githubusercontent.com` …). That URL can be used as the only `src` in `<video>` — it tends to behave the same everywhere on GitHub but has a **size limit** (commonly 10MB on free accounts); large walkthroughs usually stay in-repo with `raw.githubusercontent.com` as above.

## What Sova Does (at a glance)

- Probes inbox threads (Gmail via local `gog` + OAuth)
- Classifies whether a thread requires CSM action
- Runs retrieval (RAG + lexical search) for evidence-backed responses
- Builds action-card candidates and tracks status progression
- Supports manual and scheduled processing via cron workflows

## Outcomes—and the product features behind them

Each row is **what you want in the workflow** paired with **how Sova implements it** (still one agent process behind the scenes; diagrams and routing live in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)).

| Expected outcome | What delivers it |
|------------------|------------------|
| Spend time on threads that truly need a CSM | **Inbox probe** runs (Scan inbox / scheduled jobs): Gmail is read via **`gog` + OAuth**; the LangChain **`email_agent`** scores threads and emits structured probe JSON; **merge + guardrails** (`probe_actions`) decide what becomes dashboard cards under Configure policy ([AGENT_GUARDRAILS.md](docs/AGENT_GUARDRAILS.md)). |
| Answers grounded in your content, not generic web rambling | **`search_product_docs`** drives the KB pipeline (RAG + lexical/`ripgrep` + rerank); optional **`search_rc_web`** follows **Configure** `rc_web_retrieval_mode` (for example KB-first with a gate, or augment with hosted docs). Details: [SEARCH_AGENT.md](docs/SEARCH_AGENT.md). |
| A team-visible queue you can run | **Action dashboard** cards from merged probe metadata; **category overrides** via the dashboard API; status progression and **action-review** Workbench threads for deep dives on one candidate ([docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [docs/AGENT_GUARDRAILS.md](docs/AGENT_GUARDRAILS.md)). |
| No outbound email surprises | Gmail integration is **read-only** (`gmail_tool` → local fetch script); richer customer-facing drafts come from explicit **Workbench** requests, not from silent sends. |
| Triage matches your products, vendors, and tone | **Workbench** agent profile + **Configure** (prompt keys, models, retrieval ranking policy, Gmail paths) persisted in **`app_settings`** via the runtime-settings API—composed into each **`run_agent`** invocation. Prompt keys: [docs/PROMPTS.md](docs/PROMPTS.md). |
| Coverage when the team is offline | Built-in **cron / scheduler** + API routes kick the same probe path on a timetable so backlog does not silently grow. |
| Behavior improves after operator corrections | **`/memory/*`**: feedback ingestion, learning refresh/compaction, and **distilled rules** layered into later runs alongside profile and Configure prompts. |
| Explainability after the fact | **Run history** in the UI snapshots what ran; paired with optional observability setups (see [docs/LANGSMITH.md](docs/LANGSMITH.md)) where enabled. |

**Workbench vs probe (quick distinction):** normal **Workbench** chat is `run_agent(..., probe=False)` with conversation history and tools; a **full inbox probe** is `probe=True` (or classifier-triggered equivalents)—isolated input, probe-shaped JSON output, then merge into the dashboard pipeline. See **Workbench threads vs full inbox probe** in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).



## Architecture Flow

The full **request routing**, **Workbench vs probe**, **API surface**, **Configure map**, and **mermaid** diagrams live in one place so they do not drift from the code:

- **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** (canonical runtime architecture, including the **Configure tab runtime diagram** that matches the web UI)

Related deep dives:

- [docs/SEARCH_AGENT.md](docs/SEARCH_AGENT.md)
- [docs/AGENT_GUARDRAILS.md](docs/AGENT_GUARDRAILS.md)
- [docs/ACTION_CARD_SPEC.md](docs/ACTION_CARD_SPEC.md)

## Install And First Run

Use the full A-Z guide (canonical):

- **[docs/INSTALLATION.md](docs/INSTALLATION.md)** (canonical install path)
- **[docs/README.md](docs/README.md)** (full documentation index)

Quick local bootstrap:

```bash
python3 -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
# install ripgrep (rg) on PATH
python run.py
```

Open `http://127.0.0.1:8000`, then configure models and optional Gmail in **Configure**.

## Dependencies And External Setup

- `ripgrep` (`rg`) is required for lexical retrieval
- LLM provider/API credentials are required for chat + retrieval orchestration
- Gmail support requires local `gog`, Google OAuth credentials, and keyring values

Detailed docs:

- Gmail setup: [docs/GMAIL_SETUP.md](docs/GMAIL_SETUP.md)
- Model/provider setup: [docs/LLM_MODELS.md](docs/LLM_MODELS.md)
- Tracing and observability: [docs/LANGSMITH.md](docs/LANGSMITH.md)

## Behavior Contract (Guardrails)

Sova should create action cards only for customer-relevant CSM work, not for internal-only or non-actionable notifications.

- Relevance decisions should be explicit and auditable
- Retrieval should run for CSM-relevant threads before final card drafting
- If evidence is insufficient, the agent should state a gap instead of fabricating certainty
- User-adjustable guidance is preferred over hardcoded product rules

See [docs/AGENT_GUARDRAILS.md](docs/AGENT_GUARDRAILS.md) for the full contract.

## Retrieval Foundation

Retrieval is the core of Sova quality and sustainability:

- Uses multi-stage recall: vector RAG + `ripgrep` + FTS
- Applies scope-aware ranking and LLM rerank
- Supports sufficiency checks and query refinement loops

This design reduces hallucinations, improves answer traceability, and keeps behavior adaptable as docs evolve.

Reference: [docs/SEARCH_AGENT.md](docs/SEARCH_AGENT.md)

## Action Dashboard Expectations

Action cards should include enough metadata for practical execution:

- thread title and source linkage
- customer identity signal (name and/or domain)
- actionable summary and recommended next step
- **`category`:** `client_technical` | `client_non_technical` | `internal` (legacy probe values are normalized in `probe_actions`)
- status transitions (`not_started`, `in_progress`, `completed`); operators can fix miscategorisation from the UI
- retrieval evidence metadata for follow-up Q&A

**Configure** exposes assembled prompts by mode plus **Distilled learning rules** (single reinforcement pass over partitioned feedback → **`agent_learning_constraints`** + **`agent_learning_exemplars`**, injected as `{learning_section}`), distinct from DB compaction. Reference: [docs/ACTION_CARD_SPEC.md](docs/ACTION_CARD_SPEC.md), [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) § Self-evolution and feedback.

## Troubleshooting Quick Map

- False-positive/non-CSM cards -> check guardrail policy and exclusion rules
- Product thread with no retrieval evidence -> verify search path and indexing
- Previously probed thread skipped unexpectedly -> inspect dedup/state reset path
- Cron behavior mismatch -> verify interval semantics and job intent

Runbook: [docs/OPERATIONS_RUNBOOK.md](docs/OPERATIONS_RUNBOOK.md)

## Security And Release Hygiene

- Do not commit secrets (`credentials.json`, API keys, local token stores)
- Keep private/internal knowledge out of public distributions; **local KB uploads and SQLite** live under `data/` and **`knowledge-base/`** — both are listed in `.gitignore` and must not be force-added for a public tree
- Validate docs, setup flow, and cross-platform host-install messaging before release

Checklist: [docs/RELEASE_CHECKLIST.md](docs/RELEASE_CHECKLIST.md)

## Full Documentation Map

Use [docs/README.md](docs/README.md) for the complete documentation index.
