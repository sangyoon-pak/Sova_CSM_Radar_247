"""Agent memory compaction: summarize older interactions into shorter notes.

This does NOT yet change how the main agent is prompted; it provides
infrastructure to keep the interactions table from growing unbounded while
retaining a high-level summary.
"""
from __future__ import annotations

from datetime import datetime
from typing import Sequence

from langchain_core.messages import HumanMessage

from src.agent.chat_llm import get_chat_llm
from src.config import settings
from src.db import database


MEMORY_COMPACTION_PROMPT = """You are compressing an email agent's past interactions into a concise, durable memory.

You will receive a list of interactions (each with created_at, trigger_type, input_text, output_text).
Your goal is to extract only the reusable knowledge that will still be useful in future runs, such as:
- Stable facts about the user's preferences, tone, or style.
- Important decisions, conclusions, or troubleshooting steps that might be needed again.
- Recurrent client questions and the high-level answers.

Do NOT repeat full emails or drafts. Do NOT include private or unnecessary detail.
Write 3-10 bullet points capturing only the enduring, reusable information.

Return the bullets as plain text, each bullet starting with '- '."""


def _get_llm():
    return get_chat_llm(model=settings.llm_model_for_memory, temperature=0)


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

