"""Parse structured CSM action items from probe agent output (JSON block)."""
from __future__ import annotations

import json
import re
from typing import Any

from src.runtime_config import (
    effective_guardrail_exclude_sender_domains,
    effective_guardrail_exclude_subject_keywords,
    effective_guardrail_include_sender_domains,
    effective_guardrail_strictness,
)

_GMAIL_TID_RE = re.compile(r"^[a-zA-Z0-9_-]{6,128}$")
_EMAIL_IN_ANGLE_RE = re.compile(r"<([^>]+@[^>]+)>")


def _GMAIL_THREAD_ID_OK(s: str) -> bool:
    return bool(s and _GMAIL_TID_RE.match(s.strip()))


_MEETING_ONLY_PAT = re.compile(
    r"(?i)\b("
    r"meeting|invite|invitation|intro(duction)?|kick[\s-]?off|sync|catch[\s-]?up|"
    r"calendar|availability|schedule|scheduled|reschedul|zoom|meet|teams|webex|"
    r"미팅|회의|소개\s*세션|소개\s*미팅|일정|캘린더|초대|줌|팀즈"
    r")\b"
)
_TECH_OR_ACTION_PAT = re.compile(
    r"(?i)\b("
    r"api|sdk|error|bug|issue|troubleshoot|integration|config|payload|webhook|"
    r"data|export|report|cid|user[_ -]?id|push|campaign|attribute|query|sql|"
    r"장애|오류|이슈|설정|연동|리포트|데이터|문의|해결|원인|확인\s*요청"
    r")\b"
)

def _looks_non_actionable_meeting_invite(a: dict[str, Any]) -> bool:
    """
    Guardrail: skip cards that are only scheduling/intro invites with no product issue.
    This runs server-side after model output to reduce noisy dashboard cards.
    """
    text = " ".join(
        [
            str(a.get("title") or ""),
            str(a.get("brief") or ""),
            str(a.get("client_query_digest") or ""),
            str(a.get("thread_summary") or ""),
        ]
    )
    if not text.strip():
        return False
    has_meeting = bool(_MEETING_ONLY_PAT.search(text))
    has_tech = bool(_TECH_OR_ACTION_PAT.search(text))
    return has_meeting and not has_tech


def _csv_tokens(v: str) -> list[str]:
    return [x.strip().lower() for x in str(v or "").split(",") if x.strip()]


def _email_domain(v: str) -> str:
    t = str(v or "").strip().lower()
    if not t:
        return ""
    m = _EMAIL_IN_ANGLE_RE.search(t)
    if m:
        t = m.group(1).strip().lower()
    if "@" not in t:
        return ""
    return t.split("@", 1)[1].strip()


def _category_is_product_technical(cat: str) -> bool:
    c = str(cat or "").strip().lower()
    return c in {"product_technical", "product", "technical"}


def _is_excluded_by_user_guardrails(a: dict[str, Any], *, strictness: str) -> bool:
    include_domains = set(_csv_tokens(effective_guardrail_include_sender_domains()))
    exclude_domains = set(_csv_tokens(effective_guardrail_exclude_sender_domains()))
    exclude_subject_kw = _csv_tokens(effective_guardrail_exclude_subject_keywords())

    sender = str(a.get("email_from") or a.get("from") or "").strip()
    subject = str(a.get("email_subject") or a.get("subject") or "").strip().lower()
    brief = str(a.get("brief") or "").strip().lower()
    digest = str(a.get("client_query_digest") or a.get("client_ask_summary") or "").strip().lower()
    domain = _email_domain(sender)

    if include_domains and (not domain or domain not in include_domains):
        return True
    if domain and domain in exclude_domains:
        return True
    if exclude_subject_kw and any(kw in subject or kw in brief or kw in digest for kw in exclude_subject_kw):
        return True

    if strictness == "strict":
        # Strict mode suppresses low-signal cards with no concrete next step/evidence.
        refs = a.get("references") or []
        steps = a.get("next_steps") or []
        has_refs = isinstance(refs, list) and len(refs) > 0
        has_steps = isinstance(steps, list) and len(steps) > 0
        text = " ".join([subject, brief, digest])
        has_action_signal = bool(_TECH_OR_ACTION_PAT.search(text))
        if not (has_refs or has_steps or has_action_signal):
            return True

    return False


def _normalize_actions(raw: Any) -> list[dict[str, Any]]:
    if not isinstance(raw, list):
        return []
    out: list[dict[str, Any]] = []
    strictness = effective_guardrail_strictness()
    for i, a in enumerate(raw):
        if not isinstance(a, dict):
            continue
        if a.get("include_on_dashboard") is False:
            continue
        if strictness != "permissive" and _looks_non_actionable_meeting_invite(a):
            continue
        if _is_excluded_by_user_guardrails(a, strictness=strictness):
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
        client_digest = str(
            a.get("client_query_digest")
            or a.get("client_ask_summary")
            or a.get("client_query_summary")
            or ""
        )[:4000]
        sub_raw = a.get("subquery_answers") or a.get("subqueries") or []
        sub_pairs: list[dict[str, str]] = []
        if isinstance(sub_raw, list):
            for item in sub_raw[:20]:
                if not isinstance(item, dict):
                    continue
                sq = str(
                    item.get("subquery")
                    or item.get("question")
                    or item.get("q")
                    or item.get("topic")
                    or ""
                ).strip()[:800]
                ans = str(
                    item.get("answer")
                    or item.get("response")
                    or item.get("a")
                    or ""
                ).strip()[:4500]
                if sq or ans:
                    sub_pairs.append({"subquery": sq, "answer": ans})
        gid = str(a.get("gmail_thread_id") or a.get("email_thread_id") or "").strip()
        if gid and not _GMAIL_THREAD_ID_OK(gid):
            gid = ""
        e_from = str(a.get("email_from") or a.get("from") or "").strip()[:400]
        e_subj = str(a.get("email_subject") or a.get("subject") or "").strip()[:400]
        st = str(a.get("status") or "").strip().lower()
        if st not in {"not_started", "in_progress", "completed"}:
            st = "not_started"
        category = str(a.get("category") or "general")[:120]
        # Reliability gate: product/technical cards must have retrieval evidence.
        if strictness != "permissive" and _category_is_product_technical(category) and not refs:
            continue
        out.append(
            {
                "title": str(a.get("title") or f"Action {i + 1}")[:240],
                "brief": str(a.get("brief") or "")[:2000],
                "curated_answer": str(curated)[:3000],
                "technical_rationale": str(tech)[:3500],
                "escalation_guidance": str(escalate)[:2500],
                "client_query_digest": client_digest,
                "subquery_answers": sub_pairs,
                "thread_summary": str(a.get("thread_summary") or "")[:4000],
                "gmail_thread_id": gid[:128] if gid else "",
                "email_from": e_from,
                "email_subject": e_subj,
                "status": st,
                "category": category,
                "next_steps": [str(x)[:800] for x in steps[:15]],
                "references": [str(x)[:800] for x in refs[:12]],
            }
        )
    return out


def _action_fingerprint(a: dict[str, Any]) -> str:
    """Stable digest for update detection on the same Gmail thread."""
    parts = [
        str(a.get("title") or "").strip(),
        str(a.get("brief") or "").strip(),
        str(a.get("client_query_digest") or "").strip(),
        str(a.get("thread_summary") or "").strip(),
        str(a.get("curated_answer") or "").strip(),
    ]
    return "||".join(parts)


def _dedupe_key(a: dict[str, Any]) -> str:
    gid = str(a.get("gmail_thread_id") or "").strip()
    if gid:
        return f"gid:{gid}"
    ef = str(a.get("email_from") or "").strip().lower()
    es = str(a.get("email_subject") or "").strip().lower()
    if ef and es:
        return f"fs:{ef}||{es}"
    return ""


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


def format_action_review_chat_prefix(
    snapshot: dict[str, Any],
    *,
    source_interaction_id: int,
    action_index: int,
    probe_source_thread_id: int | None = None,
) -> str:
    """
    Prepended to normal user messages in Workbench when the thread is an action-review chat,
    so the model stays scoped to one dashboard action (no full-inbox triage unless asked).
    """

    def _clip(s: Any, n: int = 2000) -> str:
        t = str(s or "").strip()
        return t if len(t) <= n else t[: n - 1] + "…"

    gid = str(snapshot.get("gmail_thread_id") or "").strip()
    lines = [
        "[Action review — discuss ONLY this dashboard item. Do not re-triage the whole inbox unless the user explicitly asks.]",
        f"Probe interaction id: {int(source_interaction_id)} · action index: {int(action_index)}",
    ]
    if gid and _GMAIL_THREAD_ID_OK(gid):
        lines.append(f"Gmail thread id (use fetch_gmail_thread with this id for full thread text): {gid}")
    if probe_source_thread_id is not None:
        lines.append(
            f"Workbench thread where inbox probe was run (for reference only): {int(probe_source_thread_id)}"
        )
    lines.extend(
        [
            "",
            f"Title: {_clip(snapshot.get('title'), 500)}",
            f"Brief: {_clip(snapshot.get('brief'), 2000)}",
            f"Curated answer: {_clip(snapshot.get('curated_answer'), 2500)}",
            f"Technical rationale: {_clip(snapshot.get('technical_rationale'), 2500)}",
            f"Escalation guidance: {_clip(snapshot.get('escalation_guidance'), 1500)}",
            f"Client query (analyzed): {_clip(snapshot.get('client_query_digest'), 2500)}",
            f"Thread summary: {_clip(snapshot.get('thread_summary'), 2000)}",
        ]
    )
    subs = snapshot.get("subquery_answers")
    if isinstance(subs, list) and subs:
        lines.append("")
        lines.append("Sub-question answers:")
        for j, item in enumerate(subs[:15], start=1):
            if not isinstance(item, dict):
                continue
            sq = _clip(item.get("subquery"), 600)
            ans = _clip(item.get("answer"), 3000)
            lines.append(f"{j}. Q: {sq}")
            lines.append(f"   A: {ans}")
    steps = snapshot.get("next_steps")
    if isinstance(steps, list) and steps:
        lines.append("")
        lines.append("Next steps:")
        for s in steps[:15]:
            lines.append(f"- {_clip(s, 800)}")
    refs = snapshot.get("references")
    if isinstance(refs, list) and refs:
        lines.append("")
        lines.append("References:")
        for r in refs[:15]:
            lines.append(f"- {_clip(r, 900)}")
    return "\n".join(lines)


def merge_csm_actions_metadata(
    output_text: str,
    base_metadata: dict | None,
    *,
    existing_by_thread: dict[str, dict[str, Any]] | None = None,
) -> dict:
    """Attach csm_actions + skipped_note + parse_error to interaction metadata."""
    md = dict(base_metadata or {})
    parsed = parse_probe_dashboard_json(output_text)
    actions = list(parsed["actions"] or [])
    by_thread = existing_by_thread or {}
    merged: list[dict[str, Any]] = []
    skipped_unchanged = 0
    for a in actions:
        if not isinstance(a, dict):
            continue
        key = _dedupe_key(a)
        if key and key in by_thread:
            prev = by_thread.get(key) or {}
            prev_status = str(prev.get("status") or "").strip().lower()
            if prev_status not in {"not_started", "in_progress", "completed"}:
                prev_status = "not_started"
            same_fp = _action_fingerprint(a) == _action_fingerprint(prev)
            if same_fp:
                # No meaningful update for an existing thread card: skip this action.
                skipped_unchanged += 1
                continue
            else:
                # New update on same thread should reopen completed cards.
                a["status"] = "in_progress" if prev_status == "completed" else prev_status
        else:
            a["status"] = "not_started"
        merged.append(a)
    md["csm_actions"] = merged
    if not merged and skipped_unchanged > 0 and not parsed.get("skipped_note"):
        md["csm_skipped_note"] = (
            f"No meaningful updates across previously tracked threads ({skipped_unchanged} unchanged)."
        )
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
