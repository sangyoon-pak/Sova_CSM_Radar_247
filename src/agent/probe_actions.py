"""Parse structured CSM action items from probe agent output (JSON block)."""
from __future__ import annotations

import json
import re
from typing import Any


def _normalize_actions(raw: Any) -> list[dict[str, Any]]:
    if not isinstance(raw, list):
        return []
    out: list[dict[str, Any]] = []
    for i, a in enumerate(raw):
        if not isinstance(a, dict):
            continue
        if a.get("include_on_dashboard") is False:
            continue
        steps = a.get("next_steps") or []
        if not isinstance(steps, list):
            steps = []
        refs = a.get("references") or []
        if not isinstance(refs, list):
            refs = []
        curated = (
            a.get("curated_answer")
            or a.get("suggested_answer")
            or a.get("answer_for_csm")
            or a.get("talking_points")
            or ""
        )
        tech = (
            a.get("technical_rationale")
            or a.get("technical_explanation")
            or a.get("rationale")
            or ""
        )
        escalate = (
            a.get("escalation_guidance")
            or a.get("escalation")
            or a.get("escalation_plan")
            or ""
        )
        out.append(
            {
                "title": str(a.get("title") or f"Action {i + 1}")[:240],
                "brief": str(a.get("brief") or "")[:2000],
                "curated_answer": str(curated)[:3000],
                "technical_rationale": str(tech)[:3500],
                "escalation_guidance": str(escalate)[:2500],
                "thread_summary": str(a.get("thread_summary") or "")[:4000],
                "category": str(a.get("category") or "general")[:120],
                "next_steps": [str(x)[:800] for x in steps[:15]],
                "references": [str(x)[:800] for x in refs[:12]],
            }
        )
    return out


def parse_probe_dashboard_json(text: str) -> dict[str, Any]:
    """
    Extract dashboard JSON from model output.
    Looks for ```json ... ``` blocks (last valid wins) or a trailing JSON object with "actions".
    Returns keys: actions (list), skipped_note (str|None), parse_error (str|None)
    """
    if not text or not str(text).strip():
        return {"actions": [], "skipped_note": None, "parse_error": "empty_output"}

    t = str(text)
    # Fenced blocks, try from last to first
    for m in reversed(list(re.finditer(r"```(?:json)?\s*([\s\S]*?)```", t, re.IGNORECASE))):
        chunk = m.group(1).strip()
        try:
            data = json.loads(chunk)
            if isinstance(data, dict) and isinstance(data.get("actions"), list):
                return {
                    "actions": _normalize_actions(data.get("actions")),
                    "skipped_note": (str(data.get("skipped_note")).strip()[:2000] if data.get("skipped_note") else None),
                    "parse_error": None,
                }
        except json.JSONDecodeError:
            continue

    # Brace scan: find last plausible start
    for anchor in ('{"actions"', '{"actions" :', '{\n  "actions"'):
        pos = t.rfind(anchor)
        if pos == -1:
            continue
        depth = 0
        end = pos
        for j in range(pos, len(t)):
            if t[j] == "{":
                depth += 1
            elif t[j] == "}":
                depth -= 1
                if depth == 0:
                    end = j + 1
                    break
        if end > pos:
            try:
                data = json.loads(t[pos:end])
                if isinstance(data, dict) and isinstance(data.get("actions"), list):
                    return {
                        "actions": _normalize_actions(data.get("actions")),
                        "skipped_note": (str(data.get("skipped_note")).strip()[:2000] if data.get("skipped_note") else None),
                        "parse_error": None,
                    }
            except json.JSONDecodeError:
                continue

    return {"actions": [], "skipped_note": None, "parse_error": "no_valid_json_actions_block"}


def merge_csm_actions_metadata(output_text: str, base_metadata: dict | None) -> dict:
    """Attach csm_actions + skipped_note + parse_error to interaction metadata."""
    md = dict(base_metadata or {})
    parsed = parse_probe_dashboard_json(output_text)
    md["csm_actions"] = parsed["actions"]
    if parsed.get("skipped_note"):
        md["csm_skipped_note"] = parsed["skipped_note"]
    if parsed.get("parse_error"):
        md["csm_actions_parse_error"] = parsed["parse_error"]
    return md


def format_probe_thread_reply(output_text: str, merged_metadata: dict) -> str:
    """Short message for Workbench transcript when probe returns structured JSON."""
    acts = merged_metadata.get("csm_actions") or []
    if acts:
        lines = [
            f"Inbox probe — **{len(acts)}** item(s) for CSM review (see **Action dashboard** for full brief).",
            "",
        ]
        for a in acts[:15]:
            t = (a.get("title") or "Item").strip()
            lines.append(f"• {t}")
        return "\n".join(lines)
    if merged_metadata.get("csm_skipped_note"):
        return (
            "Inbox probe — no dashboard items (nothing required CSM follow-up).\n\n"
            f"{merged_metadata['csm_skipped_note']}"
        )
    if merged_metadata.get("csm_actions_parse_error"):
        snippet = (output_text or "")[:1500].strip()
        return (
            "Inbox probe finished, but structured actions could not be parsed.\n"
            "Use **Run history** for the raw model output.\n\n"
            f"---\n{snippet}"
            + ("…" if len(output_text or "") > 1500 else "")
        )
    return output_text or ""
