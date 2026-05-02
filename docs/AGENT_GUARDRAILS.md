# Agent Guardrails

This document defines behavior boundaries for CSM relevance, action card creation, and retrieval usage.

## Why This Exists

Recurring quality issues require explicit guardrails:

- Non-CSM/internal emails can trigger false-positive action cards.
- Previously processed threads can behave inconsistently after data resets.
- Product-related threads can skip retrieval from uploaded documents.

These rules should be treated as product contract guidance for ongoing implementation.

## CSM Relevance Decision Contract

Before creating an action card, classify the thread into one of these outcomes:

- `requires_csm_action`
- `informational_only`
- `internal_non_csm`
- `insufficient_context`

### Required Conditions For `requires_csm_action`

At least one must be true:

- Customer asks for help, clarification, escalation, or timeline.
- There is a customer-impacting risk, blocker, or incident requiring CSM coordination.
- There is a clear follow-up task that should be tracked.

### Exclusion Conditions

Default to no card when any of these are true and no override applies:

- Internal-only alerts (for example quota warning with no customer ask).
- System notifications with no customer communication intent.
- Automated status messages with no actionable next step.

## User-Guided Guardrails (Preferred Over Hardcoding)

The system should allow users to adjust relevance policy without code edits.

Recommended UI-configurable controls:

- Include/exclude sender domains
- Include/exclude intent keywords
- Product/team-specific relevance guidance text
- Card creation strictness (`strict`, `balanced`, `permissive`)

This keeps behavior adaptable across CSM teams and tenants.

## Retrieval Guardrail Contract

For threads classified as potentially CSM-relevant:

- **Mandatory KB for `client_technical`:** For probe JSON actions with **`category: client_technical`**, the probe executor must run **Knowledge base retrieval** (tool: `search_product_docs`) before final structured output; merge diagnostics flag `client_technical_without_kb_retrieval` when that did not happen. **RC documentation web** (`search_rc_web`, enabled RC URLs) still follows **`rc_web_retrieval_mode`** / the KB→web gate — it is not optional “extra” in modes that require web follow-up.
- For **`client_non_technical`** and **`internal`**, there is no forced KB/web sequence in the probe merge; the model may still call tools when useful.
- Search must include uploaded documents and indexed KB sources for grounded answers when the model chooses retrieval.
- If retrieval has low confidence, surface this as a gap instead of guessing.
- Retrieval ranking behavior should be configured through runtime policy (`RETRIEVAL_RANKING_POLICY`) rather than hardcoded vendor-specific boosts.

Detailed retrieval mechanics: [SEARCH_AGENT.md](SEARCH_AGENT.md).

## Previously Processed Threads

Expected behavior after deleting relevant backend state:

- The next probe should treat the thread as eligible for re-processing.
- Dedup checks should rely on current persisted state only.
- If still skipped, this is an operational bug and should be diagnosed with the runbook.

Debug workflow: [OPERATIONS_RUNBOOK.md](OPERATIONS_RUNBOOK.md).

## Decision Logging Requirements

Each processed thread should log:

- Relevance outcome label
- Top rationale signals (intent, sender, content cues)
- Retrieval attempted (`yes/no`) and source summary
- Card creation decision (`created/skipped`) with reason

This is required for reproducibility and user trust.
