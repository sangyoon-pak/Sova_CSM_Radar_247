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


def _format_feedback_sample_for_distillation(idx: int, s: dict) -> str:
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
    return (
        f"[{idx}] verdict={verdict}{scope}\n"
        f"    note={note}\n"
        f"    correction={corr}"
    )


LEARNING_DISTILL_SYSTEM = """You distill operator feedback for a CSM inbox assistant (Gmail probe → JSON action cards, Workbench chat, optional Action dashboard card feedback).

Write 3–8 bullet rules that will be injected into the agent system prompt. Each bullet MUST:
- Map to at least one feedback item (you may merge related items).
- Name **concrete** situations the operator cares about (e.g. "internal AIRIS quota alerts from Woopra", "automated vendor success-team mail", "meeting-only invites with no product question") when the notes imply them. Do **not** replace specifics with vague phrases like "unnecessary cards" or "low-value items" without saying **what pattern** to skip or change.
- Stay in scope: inbox triage, probe JSON, `include_on_dashboard`, action categories (`client_technical` / `client_non_technical` / `internal`), internal vs client threads, retrieval/tool use. This is **not** generic product management or UX coaching.

FORBIDDEN unless the operator literally wrote that idea in a note/correction:
- Generic platitudes and process-speak (examples to avoid: "prioritize user needs", "streamline information", "implement feedback loops", "usability tests", "maintain consistency", "facilitate quick access", "ensure clarity in communication").
- Bullets that could apply to any SaaS dashboard with no tie to **email triage / CSM actions**.

If feedback is thin or contradictory, output fewer bullets and prefer one cautious rule over invented detail. No preamble — bullets only, each line starting with "- "."""


def clear_distilled_learning_instructions() -> dict:
    """Remove distilled rules from app_settings (feedback rows are unchanged)."""
    database.set_app_setting("agent_learning_instructions", "")
    snap = database.get_agent_learning_instructions_snapshot()
    return {"cleared": True, "instructions": snap["instructions"], "updated_at": snap["updated_at"]}


def refresh_learning_instructions(max_feedback: int = 80) -> dict:
    """
    Build compact runtime instructions from explicit user feedback.
    Stores the result in app_settings key: agent_learning_instructions.
    """
    samples = database.get_learning_feedback_samples(limit=max_feedback)
    if not samples:
        database.set_app_setting("agent_learning_instructions", "")
        return {"updated": True, "rules": 0}

    blocks: list[str] = []
    for i, s in enumerate(samples, start=1):
        blocks.append(_format_feedback_sample_for_distillation(i, s))
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

