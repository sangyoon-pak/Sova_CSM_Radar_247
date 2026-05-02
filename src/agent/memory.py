"""Agent memory compaction and feedback distillation.

- **`compact_memory`**: summarizes older `agent_interactions` into `agent_memory` rows
  and deletes those interactions. This path does **not** populate `{learning_section}`.
- **`refresh_learning_instructions`**: condenses recent `agent_feedback` via an LLM into
  **`app_settings.agent_learning_instructions`**, which the main agent reads at runtime
  (`get_runtime_learning_instructions` / `render_email_agent_system`).
"""
from __future__ import annotations

import json
from datetime import datetime
from typing import Any, Sequence

from langchain_core.messages import HumanMessage, SystemMessage

from src.agent.chat_llm import get_chat_llm
from src.runtime_config import effective_llm_model_memory
from src.db import database


MEMORY_COMPACTION_PROMPT = """You are compressing a CSM assistant's past interactions into a concise, durable memory.

You will receive a list of interactions (each with created_at, trigger_type, input_text, output_text).
Your goal is to extract only the reusable knowledge that will still be useful in future runs, such as:
- Stable facts about the user's preferences, tone, or style.
- Important decisions, conclusions, or troubleshooting steps that might be needed again.
- Recurrent client questions and the high-level answers.

Do NOT repeat full emails, long drafts, or full action-board dumps. Do NOT include private or unnecessary detail.
Write 3-10 bullet points capturing only the enduring, reusable information.

Return the bullets as plain text, each bullet starting with '- '."""


def _get_llm():
    return get_chat_llm(model=effective_llm_model_memory(), temperature=0)


def _format_interactions_for_compaction(interactions: Sequence[dict]) -> str:
    lines: list[str] = []
    for i in interactions:
        created = i.get("created_at")
        created_s = str(created)
        trigger = i.get("trigger_type", "")
        inp = (i.get("input_text") or "")[:400]
        out = (i.get("output_text") or i.get("error_message") or "")[:600]
        lines.append(
            f"- created_at: {created_s}\n"
            f"  trigger_type: {trigger}\n"
            f"  input: {inp}\n"
            f"  output: {out}"
        )
    return "\n\n".join(lines)


def compact_memory(before: datetime | None = None, max_interactions: int = 200) -> dict:
    """
    Summarize older interactions into a single memory note and delete them.

    - `before`: cutoff datetime; if None, uses now().
    - `max_interactions`: maximum number of interactions to summarize in one run.
    """
    cutoff = before or datetime.utcnow()
    interactions = database.get_interactions_before(cutoff, limit=max_interactions)
    if not interactions:
        return {"summarized": 0, "deleted": 0}

    llm = _get_llm()
    formatted = _format_interactions_for_compaction(interactions)
    prompt = f"{MEMORY_COMPACTION_PROMPT}\n\nINTERACTIONS:\n{formatted}"
    response = llm.invoke([HumanMessage(content=prompt)])
    summary = str(response.content).strip()

    ids = [i["id"] for i in interactions if "id" in i]
    database.insert_memory(summary=summary, interaction_ids=ids)
    deleted = database.delete_interactions_by_ids(ids)
    return {"summarized": len(ids), "deleted": deleted}


def _parse_feedback_metadata(raw: Any) -> dict[str, Any]:
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, str) and raw.strip():
        try:
            out = json.loads(raw)
            return out if isinstance(out, dict) else {}
        except json.JSONDecodeError:
            return {}
    return {}


_RUN_HISTORY_INPUT_EXCERPT = 900
_RUN_HISTORY_OUTPUT_EXCERPT = 1600


def _format_run_history_excerpt(inter: dict | None) -> str:
    """Probe input/output so verdict-only Run history (e.g. useful) can be distilled into concrete rules."""
    if not inter:
        return "    run_context: (interaction not found — cannot ground a rule on this row.)"
    trig = str(inter.get("trigger_type") or "")
    inp = (inter.get("input_text") or "").strip().replace("\r\n", "\n")
    outp = (inter.get("output_text") or inter.get("error_message") or "").strip().replace("\r\n", "\n")
    inp = inp[:_RUN_HISTORY_INPUT_EXCERPT]
    outp = outp[:_RUN_HISTORY_OUTPUT_EXCERPT]
    return (
        "    run_context:\n"
        f"      trigger_type: {trig}\n"
        "      input_excerpt:\n"
        f"{inp}\n"
        "      output_excerpt:\n"
        f"{outp}"
    )


def _format_feedback_sample_for_distillation(idx: int, s: dict, run_ctx_by_id: dict[int, dict]) -> str:
    verdict = str(s.get("verdict") or "")
    note = (s.get("note") or "").strip()[:420]
    corr = (s.get("correction") or "").strip()[:420]
    meta = _parse_feedback_metadata(s.get("metadata"))
    scope_bits: list[str] = []
    if meta.get("source") == "action_dashboard":
        scope_bits.append("action_dashboard")
        if meta.get("action_index") is not None:
            scope_bits.append(f"action_index={meta.get('action_index')}")
    elif meta.get("source") == "run_history":
        scope_bits.append("run_history")
    scope = f" ({', '.join(scope_bits)})" if scope_bits else ""
    block = (
        f"[{idx}] verdict={verdict}{scope}\n"
        f"    note={note}\n"
        f"    correction={corr}"
    )
    if meta.get("source") == "run_history":
        raw_iid = s.get("interaction_id")
        try:
            iid = int(raw_iid) if raw_iid is not None else None
        except (TypeError, ValueError):
            iid = None
        if iid is not None:
            block += "\n" + _format_run_history_excerpt(run_ctx_by_id.get(iid))
    return block


LEARNING_DISTILL_SYSTEM = """You distill the **FEEDBACK** block in the user message into short rules for a CSM inbox assistant (Gmail probe → JSON action cards, Workbench chat, optional Action dashboard card feedback).

Output **only** lines starting with "- ". No preamble, no numbering.

**Grounding (non-negotiable):**
- Every bullet must be justified **only** by text in that FEEDBACK block: `note`, `correction`, and (for `run_history`) the `run_context` excerpts. Do **not** invent vendors, products, tools, alert names, or email categories that **do not appear** in FEEDBACK.
- **Never** treat illustrative wording anywhere in *this* system prompt as if it were operator feedback. If FEEDBACK does not mention a scenario, do **not** output a bullet about it.

**How to read items:**
- **action_dashboard**: follow the operator note/correction; optional `action_index` in metadata scopes one card.
- **run_history** with `run_context`: excerpts are truncated probe input/output. **useful** / **correct** = endorse keeping that style of probe output for that kind of input. **incorrect** / **noisy** = change or stop that pattern. Tie bullets to **words or structure** in those excerpts (subjects, senders, JSON shapes), not generic praise.

**Count and tone:**
- Emit **1–8** bullets based on how many **distinct** signals appear in FEEDBACK. One unrelated "useful" row → **at most 1–2** bullets grounded in that row's excerpts, not a generic triage checklist.
- Prefer concrete wording copied or tightly paraphrased from FEEDBACK over invented abstractions.

Stay in scope: inbox triage, probe JSON, `include_on_dashboard`, action categories (`client_technical` / `client_non_technical` / `internal`), internal vs client threads, retrieval/tool use — but only when FEEDBACK actually touches that scope.

FORBIDDEN in bullets unless FEEDBACK explicitly supports it:
- Generic platitudes ("prioritize user needs", "streamline", "implement feedback loops", "maintain consistency", …).
- Vague rules with no anchor in FEEDBACK ("skip low-value items", "only actionable insights") without quoting what FEEDBACK showed.

If FEEDBACK is thin or contradictory, output **fewer** bullets; one cautious line tied to FEEDBACK beats invented detail."""


def clear_distilled_learning_instructions() -> dict:
    """Clear distilled rules and all stored feedback (Run history + Action dashboard).

    Removes `agent_learning_instructions` and deletes every row in `agent_feedback`
    so the next distillation starts from an empty sample set.
    """
    feedback_deleted = database.delete_all_agent_feedback()
    database.set_app_setting("agent_learning_instructions", "")
    snap = database.get_agent_learning_instructions_snapshot()
    return {
        "cleared": True,
        "feedback_deleted": feedback_deleted,
        "instructions": snap["instructions"],
        "updated_at": snap["updated_at"],
    }


def refresh_learning_instructions(max_feedback: int = 80) -> dict:
    """
    Build compact runtime instructions from explicit user feedback.
    Stores the result in app_settings key: agent_learning_instructions.
    """
    samples = database.get_learning_feedback_samples(limit=max_feedback)
    if not samples:
        database.set_app_setting("agent_learning_instructions", "")
        return {"updated": True, "rules": 0}

    run_ids: list[int] = []
    for s in samples:
        if _parse_feedback_metadata(s.get("metadata")).get("source") != "run_history":
            continue
        raw_iid = s.get("interaction_id")
        try:
            if raw_iid is not None:
                run_ids.append(int(raw_iid))
        except (TypeError, ValueError):
            continue
    run_ctx_by_id = database.get_interactions_by_ids(run_ids)

    blocks: list[str] = []
    for i, s in enumerate(samples, start=1):
        blocks.append(_format_feedback_sample_for_distillation(i, s, run_ctx_by_id))
    user_content = "FEEDBACK (newest-first):\n\n" + "\n\n".join(blocks)
    llm = _get_llm()
    response = llm.invoke(
        [
            SystemMessage(content=LEARNING_DISTILL_SYSTEM),
            HumanMessage(content=user_content),
        ]
    )
    rules = str(response.content or "").strip()
    database.set_app_setting("agent_learning_instructions", rules)
    bullet_count = len([ln for ln in rules.splitlines() if ln.strip().startswith("-")])
    return {"updated": True, "rules": bullet_count}

