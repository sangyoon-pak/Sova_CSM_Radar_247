"""Parse structured CSM action items from probe agent output (JSON block).

Intent for the action dashboard is **not** inferred with hard-coded keyword lists.

1. **Configure (UI / runtime_config)** — operator rules: include/exclude sender domains and intent
   keywords, plus strictness. These always apply first.
2. **Probe LLM JSON** — `include_on_dashboard` and `category` are the model’s decisions; the
   parser trusts them (subject to Configure). Tune the agent via prompts and UI memory, not
   new Python regexes here.
"""
from __future__ import annotations

import json
import re
from typing import Any

_GMAIL_TID_RE = re.compile(r"^[a-zA-Z0-9_-]{6,128}$")


def _GMAIL_THREAD_ID_OK(s: str) -> bool:
    return bool(s and _GMAIL_TID_RE.match(s.strip()))


def _include_dashboard_explicitly_no(a: dict[str, Any]) -> bool:
    """JSON coercion only — not a business rule. Models sometimes emit string booleans."""
    v = a.get("include_on_dashboard")
    if v is False:
        return True
    if isinstance(v, str) and v.strip().lower() in ("false", "0", "no"):
        return True
    return False


def _include_dashboard_explicitly_yes(a: dict[str, Any]) -> bool:
    """JSON coercion only: read the LLM’s `include_on_dashboard` whether it is bool or string."""
    v = a.get("include_on_dashboard")
    if v is True:
        return True
    if isinstance(v, str) and v.strip().lower() in ("true", "1", "yes"):
        return True
    return False


_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})")

def _csv_set(v: Any) -> set[str]:
    raw = str(v or "")
    return {x.strip().lower() for x in raw.split(",") if x.strip()}


def _guardrail_policy_for_merge(md: dict | None) -> dict[str, str]:
    """
    Resolve Configure guardrails for probe parsing. Interaction metadata often omits these
    keys (e.g. thread probe), so we fall back to DB/env via runtime_config — otherwise
    exclude keywords and strictness never apply.
    """
    from src.runtime_config import (
        effective_guardrail_exclude_intent_keywords,
        effective_guardrail_exclude_sender_domains,
        effective_guardrail_include_intent_keywords,
        effective_guardrail_include_sender_domains,
        effective_guardrail_strictness,
    )

    m = md or {}

    def pick(key: str, fallback) -> str:
        """If key is absent, use runtime/DB. If key is present (even empty string), use it."""
        if key not in m:
            return fallback()
        v = m.get(key)
        if v is None:
            return fallback()
        return str(v).strip()

    return {
        "include_sender_domains": pick("guardrail_include_sender_domains", effective_guardrail_include_sender_domains),
        "exclude_sender_domains": pick("guardrail_exclude_sender_domains", effective_guardrail_exclude_sender_domains),
        "include_intent_keywords": pick("guardrail_include_intent_keywords", effective_guardrail_include_intent_keywords),
        "exclude_intent_keywords": pick("guardrail_exclude_intent_keywords", effective_guardrail_exclude_intent_keywords),
        "strictness": pick("guardrail_strictness", effective_guardrail_strictness),
    }


def _guardrail_domain(email_from: str) -> str:
    m = _EMAIL_RE.search(email_from or "")
    return (m.group(1).strip().lower() if m else "")


def _infer_relevance_outcome(a: dict[str, Any], policy: dict[str, str]) -> tuple[str, str]:
    """
    Decide whether a parsed action row belongs on the dashboard.

    Order: Configure excludes → Configure includes (boost) → LLM `include_on_dashboard` →
    LLM `category` → strictness default for ambiguous rows. No server-side “intent regex” lists.
    """
    from src.guardrail_semantic import parse_intent_phrases_blob, thread_text_matches_any_phrase

    text = " ".join(
        [
            str(a.get("title") or ""),
            str(a.get("brief") or ""),
            str(a.get("client_query_digest") or ""),
            str(a.get("thread_summary") or ""),
            str(a.get("email_subject") or ""),
        ]
    ).strip()
    if not text:
        return "insufficient_context", "empty_text"

    strictness = str(policy.get("strictness") or "balanced").strip().lower()
    include_domains = _csv_set(policy.get("include_sender_domains"))
    exclude_domains = _csv_set(policy.get("exclude_sender_domains"))
    include_phrases = parse_intent_phrases_blob(str(policy.get("include_intent_keywords") or ""))
    exclude_phrases = parse_intent_phrases_blob(str(policy.get("exclude_intent_keywords") or ""))
    from_domain = _guardrail_domain(str(a.get("email_from") or ""))

    if from_domain and from_domain in exclude_domains:
        return "internal_non_csm", f"excluded_domain:{from_domain}"
    if exclude_phrases and thread_text_matches_any_phrase(exclude_phrases, a):
        return "internal_non_csm", "excluded_intent_phrase"

    # Operator “always surface” rules (Configure UI) — natural-language phrases + embeddings/fallback.
    if include_phrases and thread_text_matches_any_phrase(include_phrases, a):
        return "requires_csm_action", "user_include_intent_phrase"
    if from_domain and include_domains and from_domain in include_domains:
        return "requires_csm_action", "user_include_sender_domain"

    # LLM-authored intent (probe JSON contract).
    if _include_dashboard_explicitly_yes(a):
        return "requires_csm_action", "model_include_dashboard"

    cat = str(a.get("category") or "").strip().lower()
    if cat in {"product_technical", "account"}:
        return "requires_csm_action", f"model_category:{cat}"

    # Ambiguous: model did not set dashboard visibility or product/account category.
    if strictness == "permissive":
        return "requires_csm_action", "permissive_ambiguous_intent"
    if strictness == "strict":
        return "informational_only", "strict_ambiguous_intent"
    return "informational_only", "model_intent_not_dashboard"


def _normalize_actions(
    raw: Any, policy: dict[str, str] | None = None
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """
    Returns (kept_actions, dropped_events) for diagnostics.
    dropped_events entries: index, title_snippet, stage, relevance_outcome?, relevance_reason?
    """
    if not isinstance(raw, list):
        return [], []
    out: list[dict[str, Any]] = []
    dropped: list[dict[str, Any]] = []
    p = policy or {}
    for i, a in enumerate(raw):
        if not isinstance(a, dict):
            continue
        title_hint = str(a.get("title") or "")[:120]
        if _include_dashboard_explicitly_no(a):
            dropped.append(
                {"index": i, "title": title_hint, "stage": "include_on_dashboard_false"}
            )
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
        relevance_outcome, relevance_reason = _infer_relevance_outcome(a, p)
        if relevance_outcome == "insufficient_context":
            dropped.append(
                {
                    "index": i,
                    "title": title_hint,
                    "stage": "insufficient_text",
                    "relevance_outcome": relevance_outcome,
                    "relevance_reason": relevance_reason,
                }
            )
            continue
        if relevance_outcome in {"internal_non_csm", "informational_only"} and p.get("strictness", "balanced") != "permissive":
            dropped.append(
                {
                    "index": i,
                    "title": title_hint,
                    "stage": "relevance_gate",
                    "relevance_outcome": relevance_outcome,
                    "relevance_reason": relevance_reason,
                }
            )
            continue
        thread_title = str(a.get("thread_title") or e_subj or a.get("title") or "").strip()[:400]
        customer_identifier = str(a.get("customer_identifier") or "").strip()[:200]
        customer_domain = _guardrail_domain(e_from)[:200]
        priority = str(a.get("priority") or "medium").strip().lower()
        if priority not in {"low", "medium", "high", "urgent"}:
            priority = "medium"
        confidence = str(a.get("confidence_label") or "medium").strip().lower()
        if confidence not in {"high", "medium", "low"}:
            confidence = "medium"
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
                "category": str(a.get("category") or "general")[:120],
                "thread_title": thread_title,
                "customer_identifier": customer_identifier,
                "customer_domain": customer_domain,
                "priority": priority,
                "confidence_label": confidence,
                "owner": str(a.get("owner") or "")[:160],
                "feedback_notes": str(a.get("feedback_notes") or "")[:2000],
                "source_messages": a.get("source_messages") if isinstance(a.get("source_messages"), list) else [],
                "retrieval_evidence": a.get("retrieval_evidence") if isinstance(a.get("retrieval_evidence"), list) else [],
                "relevance_outcome": relevance_outcome,
                "relevance_reason": relevance_reason,
                "next_steps": [str(x)[:800] for x in steps[:15]],
                "references": [str(x)[:800] for x in refs[:12]],
            }
        )
    return out, dropped


def _decision_log_summary(actions: list[dict[str, Any]]) -> dict[str, Any]:
    by_outcome: dict[str, int] = {}
    by_reason: dict[str, int] = {}
    for a in actions:
        out = str(a.get("relevance_outcome") or "").strip() or "unknown"
        why = str(a.get("relevance_reason") or "").strip() or "unknown"
        by_outcome[out] = by_outcome.get(out, 0) + 1
        by_reason[why] = by_reason.get(why, 0) + 1
    return {"total_actions": len(actions), "outcomes": by_outcome, "reasons": by_reason}


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


def parse_probe_dashboard_json(text: str, *, policy: dict[str, str] | None = None) -> dict[str, Any]:
    """
    Extract dashboard JSON from model output.
    Looks for ```json ... ``` blocks (last valid wins) or a trailing JSON object with "actions".
    Returns keys: actions (list), skipped_note (str|None), parse_error (str|None),
    normalization_dropped (list), raw_action_count (int).
    """
    if not text or not str(text).strip():
        return {
            "actions": [],
            "skipped_note": None,
            "parse_error": "empty_output",
            "normalization_dropped": [],
            "raw_action_count": 0,
        }

    t = str(text)
    # Fenced blocks, try from last to first
    for m in reversed(list(re.finditer(r"```(?:json)?\s*([\s\S]*?)```", t, re.IGNORECASE))):
        chunk = m.group(1).strip()
        try:
            data = json.loads(chunk)
            if isinstance(data, dict) and isinstance(data.get("actions"), list):
                raw_list = data.get("actions") or []
                kept, norm_dropped = _normalize_actions(raw_list, policy=policy)
                return {
                    "actions": kept,
                    "skipped_note": (str(data.get("skipped_note")).strip()[:2000] if data.get("skipped_note") else None),
                    "parse_error": None,
                    "normalization_dropped": norm_dropped,
                    "raw_action_count": len(raw_list),
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
                    raw_list = data.get("actions") or []
                    kept, norm_dropped = _normalize_actions(raw_list, policy=policy)
                    return {
                        "actions": kept,
                        "skipped_note": (str(data.get("skipped_note")).strip()[:2000] if data.get("skipped_note") else None),
                        "parse_error": None,
                        "normalization_dropped": norm_dropped,
                        "raw_action_count": len(raw_list),
                    }
            except json.JSONDecodeError:
                continue

    return {
        "actions": [],
        "skipped_note": None,
        "parse_error": "no_valid_json_actions_block",
        "normalization_dropped": [],
        "raw_action_count": 0,
    }


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
    policy = _guardrail_policy_for_merge(md)
    md["csm_guardrail_policy_resolved"] = policy
    parsed = parse_probe_dashboard_json(output_text, policy=policy)
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
    md["csm_decision_summary"] = _decision_log_summary(merged)
    if not merged and skipped_unchanged > 0 and not parsed.get("skipped_note"):
        md["csm_skipped_note"] = (
            f"No meaningful updates across previously tracked threads ({skipped_unchanged} unchanged)."
        )
    if parsed.get("skipped_note"):
        md["csm_skipped_note"] = parsed["skipped_note"]
    if parsed.get("parse_error"):
        md["csm_actions_parse_error"] = parsed["parse_error"]
    md["csm_probe_diagnostics"] = {
        "raw_action_count": int(parsed.get("raw_action_count") or 0),
        "kept_after_normalization": len(actions),
        "kept_after_merge": len(merged),
        "normalization_dropped": list(parsed.get("normalization_dropped") or []),
        "dedupe_skipped_unchanged": skipped_unchanged,
    }
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
