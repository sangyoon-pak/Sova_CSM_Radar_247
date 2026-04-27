"""LLM gate: after KB retrieval, decide whether hosted RC web search should still run."""

from __future__ import annotations

import json

from langchain_core.messages import HumanMessage
from langsmith import traceable

from src.agent.chat_llm import get_chat_llm
from src.runtime_config import effective_llm_model_kb_web_gate

KB_WEB_GATE_PROMPT = """You decide whether the retrieved local knowledge-base snippets are sufficient to answer the user's query without consulting external web documentation, or whether a web search pass should still run.

User query:
{query}

Retrieved chunk previews (path/title + snippet excerpt, truncated):
{previews}

Return STRICT JSON only (no markdown, no prose outside JSON):
{{"proceed_web": true or false, "reason": "<short string>"}}

Rules:
- Set "proceed_web": true if snippets are irrelevant, off-topic, too thin, contradictory, outdated hints, or clearly insufficient to answer the query safely.
- Set "proceed_web": false if snippets plausibly contain enough grounded material for a confident, doc-backed answer.
"""


def _format_match_previews(matches: list[dict], *, max_items: int = 12, snippet_len: int = 280) -> str:
    lines: list[str] = []
    for m in matches[:max_items]:
        path = str(m.get("path") or m.get("file") or "").strip()
        meta = m.get("meta") or {}
        title = (meta.get("title") or "").strip()
        head = title or path or "chunk"
        sn = (m.get("snippet") or m.get("line") or "")[:snippet_len]
        lines.append(f"- {head}: {sn}")
    return "\n".join(lines) if lines else "(no chunks)"


def _parse_gate_json(raw: str) -> tuple[bool, str] | None:
    text = (raw or "").strip()
    if "```" in text:
        parts = text.split("```")
        if len(parts) >= 2:
            text = parts[1]
            if text.startswith("json"):
                text = text[4:]
    text = text.strip()
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None
    if not isinstance(data, dict):
        return None
    return bool(data.get("proceed_web")), str(data.get("reason", "")).strip()


@traceable(name="search_rc_web.kb_web_gate", run_type="chain")
def evaluate_kb_web_gate(query: str, final_matches: list[dict]) -> tuple[bool, str]:
    """
    Returns (proceed_web, reason).

    On JSON parse failure, returns (True, "gate_json_parse_failed") so hosted web still runs
    (safe default: avoid silent skip of web when the gate model misformats).
    """
    previews = _format_match_previews(final_matches)
    prompt = KB_WEB_GATE_PROMPT.format(query=(query or "").strip(), previews=previews)
    llm = get_chat_llm(model=effective_llm_model_kb_web_gate(), temperature=0.0)
    response = llm.invoke(
        [HumanMessage(content=prompt)],
        config={
            "run_name": "retrieval.kb_web_gate",
            "tags": ["search_rc_web", "kb_web_gate"],
            "metadata": {"match_count": len(final_matches)},
        },
    )
    raw = (response.content or "").strip()
    parsed = _parse_gate_json(raw)
    if parsed is None:
        return True, "gate_json_parse_failed"
    return parsed[0], parsed[1] or "ok"
