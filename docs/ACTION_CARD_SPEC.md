# Action Card Spec

This file defines the expected action card contract for the Action dashboard.

## Card Purpose

An action card represents a customer-facing CSM task that needs follow-up and can be traced back to email/thread evidence.

## Required Fields

- `card_id`: unique identifier
- `thread_id`: source email thread ID
- `thread_title`: original thread subject/title
- `customer_identifier`: customer name when known
- `customer_domain`: sender domain fallback when name is unknown
- `summary`: concise action summary
- `recommended_next_step`: concrete suggested action
- `status`: `not_started | in_progress | completed`
- `created_at`: UTC timestamp
- `updated_at`: UTC timestamp

## Recommended Metadata

- `source_messages`: list of email IDs included in analysis
- `retrieval_evidence`: citations/snippets used for draft reasoning
- `confidence_label`: `high | medium | low`
- `priority`: `low | medium | high | urgent`
- `category` (probe JSON, persisted on each action): `client_technical` | `client_non_technical` | `internal` — triage label from the model; legacy values (`product_technical`, `account`, `other`, `general`) are normalized server-side to the canonical three.
- `owner`: assigned user/team
- `feedback_notes`: free-text user feedback for self-evolution loops

Operators can change **`category`** and **`status`** per card on the Action dashboard; those edits update the **current** interaction row only. The next inbox probe may emit a fresh **`category`** from the model for newly merged actions (model wins on merge).

## Status Behavior

- `not_started`: newly created or triaged but untouched
- `in_progress`: active execution
- `completed`: follow-up done and closed

Cards should support filtering and sorting by status, recency, priority, and customer domain.

## Retrieval Metadata Contract

Even when the card UI is concise, metadata should retain evidence needed for follow-up Q&A:

- doc/file reference
- snippet or normalized evidence text
- retrieval source type (`rag`, `grep`, `fts`, `web` when enabled)

Without this metadata, downstream assistant responses lose traceability.

## Feedback Model

Move beyond binary like/dislike where possible:

- Keep binary feedback optional for quick triage.
- Prefer free-text feedback attached to the card.
- Feed normalized feedback signals into agent evolution pipelines.
- **Action dashboard UI** sends card textarea notes as `POST /memory/feedback` with **`verdict: incorrect`** and **`action_index`** so they contribute to **negative** learning (`agent_learning_constraints`), not to operator-endorsed exemplars (`useful` / `correct` only).
- **Learning refresh sampling:** Reinforcement reads a **pool** of recent feedback rows, then passes a **fixed small batch** (five) to the distill LLM. The pipeline **reserves slots for dashboard rows** so a card note is still distilled even when many newer **run history** feedback rows exist (see [ARCHITECTURE.md](ARCHITECTURE.md) § Self-evolution and feedback).

Guardrail and architecture context: [AGENT_GUARDRAILS.md](AGENT_GUARDRAILS.md), [ARCHITECTURE.md](ARCHITECTURE.md).
