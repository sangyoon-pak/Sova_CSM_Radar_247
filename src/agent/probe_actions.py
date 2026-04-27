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
_THREAD_ID_LINE_RE = re.compile(r"(?im)^thread_id\t([^\n\r]+)$")
_FROM_LINE_RE = re.compile(r"(?im)^from\t(.+)$")
_SUBJECT_LINE_RE = re.compile(r"(?im)^subject\t(.+)$")


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
_EMAIL_ADDR_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
_HTTP_URL_RE = re.compile(r"https?://[^\s)>\]\"']+", re.IGNORECASE)
def _customer_identifier_from_fromline(v: str) -> str:
    s = str(v or "").strip()
    if not s:
        return ""
    m = re.match(r"^\s*\"?([^\"<]+?)\"?\s*<[^>]+>\s*$", s)
    if m:
        return m.group(1).strip()[:200]
    if "<" in s:
        return s.split("<", 1)[0].strip().strip('"')[:200]
    return s[:200]


def _extract_emails(s: str) -> list[str]:
    return [m.group(0).strip().lower() for m in _EMAIL_ADDR_RE.finditer(str(s or ""))]


def _pick_external_customer_email(*headers: str) -> str:
    internal_domains = {"appier.com"}
    candidates: list[str] = []
    for h in headers:
        candidates.extend(_extract_emails(h))
    seen: set[str] = set()
    ordered: list[str] = []
    for e in candidates:
        if e in seen:
            continue
        seen.add(e)
        ordered.append(e)
    for e in ordered:
        dom = e.split("@", 1)[1] if "@" in e else ""
        if dom and dom not in internal_domains:
            return e
    return ordered[0] if ordered else ""


def _name_for_email_in_header(header: str, email: str) -> str:
    h = str(header or "")
    em = str(email or "").strip().lower()
    if not h or not em:
        return ""
    # Common case: Name <email@domain>
    pat = re.compile(rf"\"?([^\"<>,;]+?)\"?\s*<\s*{re.escape(em)}\s*>", re.IGNORECASE)
    m = pat.search(h)
    if m:
        return m.group(1).strip()[:200]
    if em in h.lower():
        left = h[: h.lower().find(em)].strip().strip("<>,; ")
        left = left.rstrip("<").strip().strip('"')
        return left[:200]
    return ""


def _extract_probe_thread_identity_from_events(md: dict | None) -> dict[str, dict[str, str]]:
    """
    Build a map by gmail thread id from probe run tool output:
      {thread_id: {"email_from": ..., "email_subject": ..., "customer_identifier": ...}}
    Uses trace event detail from fetch_inbox_emails tool_end.
    """
    out: dict[str, dict[str, str]] = {}
    events = (md or {}).get("events")
    if not isinstance(events, list):
        return out
    for e in events:
        if not isinstance(e, dict):
            continue
        if str(e.get("type") or "").strip() != "tool_end":
            continue
        title = str(e.get("title") or "").strip().lower()
        if "tool output" not in title:
            continue
        detail = str(e.get("detail") or "")
        if not detail or "thread_id\t" not in detail:
            if "thread_id\\t" not in detail:
                continue
        # UI trace detail often stores escaped text (\\n, \\t); normalize so line regexes work.
        detail = (
            detail.replace("\\r\\n", "\n")
            .replace("\\n", "\n")
            .replace("\\t", "\t")
            .replace("\\r", "\n")
        )
        # Split loosely by message header blocks beginning with id\t or thread_id\t.
        blocks = re.split(r"(?im)(?=^(?:id|thread_id)\t)", detail)
        for b in blocks:
            if "thread_id\t" not in b:
                continue
            tm = _THREAD_ID_LINE_RE.search(b)
            if not tm:
                continue
            gid = tm.group(1).strip()
            if not _GMAIL_THREAD_ID_OK(gid):
                continue
            fm = _FROM_LINE_RE.search(b)
            sm = _SUBJECT_LINE_RE.search(b)
            e_from = fm.group(1).strip()[:400] if fm else ""
            e_subj = sm.group(1).strip()[:400] if sm else ""
            to_m = re.search(r"(?im)^to\t(.+)$", b)
            to_line = to_m.group(1).strip()[:400] if to_m else ""
            cust_email = _pick_external_customer_email(e_from, to_line)
            cid = ""
            if cust_email:
                cid = _name_for_email_in_header(e_from, cust_email) or _name_for_email_in_header(
                    to_line, cust_email
                )
            if not cid:
                cid = _customer_identifier_from_fromline(e_from)
            if not cid and cust_email:
                cid = cust_email.split("@", 1)[0][:200]
            rec = out.get(gid, {})
            if e_from and not rec.get("email_from"):
                rec["email_from"] = e_from
            if e_subj and not rec.get("email_subject"):
                rec["email_subject"] = e_subj
            if cid and not rec.get("customer_identifier"):
                rec["customer_identifier"] = cid
            if cust_email and not rec.get("customer_email"):
                rec["customer_email"] = cust_email
            out[gid] = rec
    return out


def _retrieval_tools_used(md: dict | None) -> set[str]:
    out: set[str] = set()
    m = md or {}
    tu = m.get("tools_used")
    if isinstance(tu, list):
        for x in tu:
            s = str(x or "").strip()
            if s:
                out.add(s)
    ev = m.get("events")
    if isinstance(ev, list):
        for e in ev:
            if not isinstance(e, dict):
                continue
            if str(e.get("type") or "").strip() != "tool_start":
                continue
            t = str(e.get("title") or "").strip().lower()
            if ":" in t:
                name = t.split(":", 1)[1].strip()
                if name:
                    out.add(name)
    return out


def _extract_identity_from_thread_text(raw: str) -> dict[str, str]:
    txt = str(raw or "")
    if not txt:
        return {}
    txt = (
        txt.replace("\\r\\n", "\n")
        .replace("\\n", "\n")
        .replace("\\t", "\t")
        .replace("\\r", "\n")
    )
    fm = _FROM_LINE_RE.search(txt)
    sm = _SUBJECT_LINE_RE.search(txt)
    to_m = re.search(r"(?im)^to\t(.+)$", txt)
    e_from = fm.group(1).strip()[:400] if fm else ""
    e_subj = sm.group(1).strip()[:400] if sm else ""
    to_line = to_m.group(1).strip()[:400] if to_m else ""
    c_email = _pick_external_customer_email(e_from, to_line)
    c_id = ""
    if c_email:
        c_id = _name_for_email_in_header(e_from, c_email) or _name_for_email_in_header(to_line, c_email)
    if not c_id:
        c_id = _customer_identifier_from_fromline(e_from)
    if not c_id and c_email:
        c_id = c_email.split("@", 1)[0][:200]
    out: dict[str, str] = {}
    if e_from:
        out["email_from"] = e_from
    if e_subj:
        out["email_subject"] = e_subj
    if c_id:
        out["customer_identifier"] = c_id
    if c_email:
        out["customer_email"] = c_email
    return out

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


def _extract_urls(text: str) -> list[str]:
    if not text:
        return []
    out: list[str] = []
    seen: set[str] = set()
    for m in _HTTP_URL_RE.finditer(text):
        u = m.group(0).rstrip(".,;")
        if u and u not in seen:
            seen.add(u)
            out.append(u)
    return out


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
        if not e_from:
            ts = str(a.get("thread_summary") or "")
            fm = _FROM_LINE_RE.search(ts)
            if fm:
                e_from = fm.group(1).strip()[:400]
        if not e_subj:
            ts = str(a.get("thread_summary") or "")
            sm = _SUBJECT_LINE_RE.search(ts)
            if sm:
                e_subj = sm.group(1).strip()[:400]
        src_msgs = a.get("source_messages")
        if isinstance(src_msgs, list) and src_msgs:
            lead = src_msgs[0] if isinstance(src_msgs[0], dict) else {}
            if isinstance(lead, dict):
                if not e_from:
                    e_from = str(
                        lead.get("from")
                        or lead.get("email_from")
                        or lead.get("sender")
                        or ""
                    ).strip()[:400]
                if not e_subj:
                    e_subj = str(
                        lead.get("subject")
                        or lead.get("email_subject")
                        or lead.get("thread_subject")
                        or ""
                    ).strip()[:400]
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
        model_title = str(a.get("title") or "").strip()
        # Prefer real email subject (from model or tool backfill) over LLM-crafted titles so
        # dashboard cards match the Gmail thread subject line.
        thread_title = str(e_subj or a.get("thread_title") or model_title or "").strip()[:400]
        display_title = str(e_subj or thread_title or model_title or f"Action {i + 1}").strip()[:240]
        customer_identifier = str(a.get("customer_identifier") or "").strip()[:200]
        customer_email = str(a.get("customer_email") or "").strip()[:320]
        if not customer_email:
            customer_email = _pick_external_customer_email(e_from)
        if not customer_identifier and e_from:
            customer_identifier = _customer_identifier_from_fromline(e_from)[:200]
        if not customer_identifier and customer_email:
            customer_identifier = customer_email.split("@", 1)[0][:200]
        customer_domain = _guardrail_domain(e_from)[:200]
        if not customer_domain and customer_email and "@" in customer_email:
            customer_domain = customer_email.split("@", 1)[1][:200]
        priority = str(a.get("priority") or "medium").strip().lower()
        if priority not in {"low", "medium", "high", "urgent"}:
            priority = "medium"
        confidence = str(a.get("confidence_label") or "medium").strip().lower()
        if confidence not in {"high", "medium", "low"}:
            confidence = "medium"
        ev_raw = a.get("retrieval_evidence") or []
        ev_norm: list[dict[str, str]] = []
        if isinstance(ev_raw, list):
            for it in ev_raw[:24]:
                if isinstance(it, dict):
                    sn = str(it.get("snippet") or it.get("text") or it.get("quote") or "")[:1200]
                    src = str(
                        it.get("path")
                        or it.get("title")
                        or it.get("url")
                        or it.get("file")
                        or ""
                    )[:400]
                    if sn or src:
                        ev_norm.append({"snippet": sn, "path": src})
                elif isinstance(it, str) and it.strip():
                    ev_norm.append({"snippet": it.strip()[:1200], "path": ""})
        refs_norm: list[str] = []
        refs_seen: set[str] = set()
        for r in refs[:20]:
            val = ""
            if isinstance(r, str):
                val = r.strip()
            elif isinstance(r, dict):
                title = str(r.get("title") or r.get("path") or r.get("label") or "").strip()
                url = str(r.get("url") or "").strip()
                val = " — ".join(x for x in (title, url) if x)
            if not val:
                continue
            if val in refs_seen:
                continue
            refs_seen.add(val)
            refs_norm.append(val[:800])
        # Auto-carry concrete sources from evidence into references (URLs and file paths).
        for ev in ev_norm:
            src = str(ev.get("path") or "").strip()
            if not src:
                continue
            for candidate in [src, *_extract_urls(src)]:
                c = candidate.strip()
                if not c or c in refs_seen:
                    continue
                refs_seen.add(c)
                refs_norm.append(c[:800])
                if len(refs_norm) >= 12:
                    break
            if len(refs_norm) >= 12:
                break
        out.append(
            {
                "title": display_title,
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
                "customer_email": customer_email,
                "customer_domain": customer_domain,
                "priority": priority,
                "confidence_label": confidence,
                "owner": str(a.get("owner") or "")[:160],
                "feedback_notes": str(a.get("feedback_notes") or "")[:2000],
                "source_messages": a.get("source_messages") if isinstance(a.get("source_messages"), list) else [],
                "retrieval_evidence": ev_norm,
                "relevance_outcome": relevance_outcome,
                "relevance_reason": relevance_reason,
                "next_steps": [str(x)[:800] for x in steps[:15]],
                "references": refs_norm[:12],
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


def _probe_action_still_on_dashboard(
    *,
    source_interaction_id: int,
    dedupe_key: str,
    fingerprint: str,
) -> bool:
    """
    True only if an action with the same dedupe key + fingerprint still exists on a probe
    interaction that is visible on the Action dashboard. Used so deleting a card (or clearing
    a run) allows the next probe to re-emit the same thread even when the model text matches.
    """
    if not source_interaction_id or not dedupe_key or not fingerprint:
        return False
    from src.db import database

    row = database.get_interaction_by_id(int(source_interaction_id))
    if not row:
        return False
    md = database.parse_interaction_metadata(row.get("metadata"))
    if md.get("csm_dashboard_removed"):
        return False
    acts = md.get("csm_actions")
    if not isinstance(acts, list):
        return False
    for a2 in acts:
        if not isinstance(a2, dict):
            continue
        if _dedupe_key(a2) != dedupe_key:
            continue
        if _action_fingerprint(a2) == fingerprint:
            return True
    return False


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


_RETRIEVAL_DIGEST_TOOLS = frozenset(
    {"search_product_docs", "search_rc_web", "fetch_gmail_thread", "fetch_inbox_emails"}
)


def _hydrate_clip(s: Any, n: int = 2000) -> str:
    t = str(s or "").strip()
    return t if len(t) <= n else t[: n - 1] + "…"


def _format_probe_events_retrieval_digest(events: Any, *, max_total_chars: int = 8000) -> str:
    """
    Pair tool_start / tool_end rows from UI/async probe metadata into short excerpts
    for inbox, Gmail thread fetch, and doc / web retrieval tools.
    """
    if not isinstance(events, list) or not events:
        return ""
    stack: list[tuple[str, str]] = []
    sections: list[str] = []
    for e in events:
        if not isinstance(e, dict):
            continue
        typ = str(e.get("type") or "")
        title = str(e.get("title") or "")
        detail = str(e.get("detail") or "")
        if typ == "tool_start" and title.startswith("Tool start:"):
            name = title.split("Tool start:", 1)[1].strip()
            if name in _RETRIEVAL_DIGEST_TOOLS:
                stack.append((name, detail[:2500]))
        elif typ == "tool_end" and title.strip() == "Tool output":
            out = detail[:4500]
            if not stack:
                continue
            name, inp = stack.pop()
            if name in _RETRIEVAL_DIGEST_TOOLS:
                sections.append(
                    f"**{name}**\n- Input (excerpt): {_hydrate_clip(inp, 1200)}\n"
                    f"- Output (excerpt): {_hydrate_clip(out, 3500)}"
                )
    if not sections:
        return ""
    body = "\n\n".join(sections)
    if len(body) > max_total_chars:
        body = body[: max_total_chars - 1] + "…"
    return body


def build_action_review_runtime_hydration(
    *,
    interaction_metadata: dict[str, Any],
    action_index: int,
    source_interaction_id: int,
    probe_source_thread_id: int | None = None,
    max_body_chars: int = 16000,
) -> str | None:
    """
    Per-reply system append for action-review Workbench threads: re-read latest `csm_actions[i]`
    from the probe interaction and optionally tool I/O from `metadata.events`, so follow-ups
    see refreshed snippets without relying only on the initial thread seed.
    """
    actions = interaction_metadata.get("csm_actions")
    if not isinstance(actions, list):
        return None
    if action_index < 0 or action_index >= len(actions):
        return None
    snap: dict[str, Any] = dict(actions[action_index])
    tool_digest = _format_probe_events_retrieval_digest(interaction_metadata.get("events"))

    lines: list[str] = [
        "## Fresh context (re-loaded from the saved probe run)",
        (
            f"Probe interaction id `{int(source_interaction_id)}` · action index `{int(action_index)}`. "
            "This block is rebuilt on **each** assistant reply from the latest `csm_actions` row on the server "
            "(e.g. after parser or dashboard updates)."
        ),
        "",
        (
            "**Use together with the thread seed above.** For **new**, **deeper**, or **verification** questions, "
            "**call tools again**: `fetch_gmail_thread` when you have a Gmail thread id and need full email text; "
            "`search_product_docs` / `search_rc_web` with queries that combine the user's latest message with the client ask. "
            "Do not rely only on the excerpts here when a fresh retrieval would materially change the answer."
        ),
        "",
    ]
    gid = str(snap.get("gmail_thread_id") or "").strip()
    if gid and _GMAIL_THREAD_ID_OK(gid):
        lines.append(f"Gmail thread id (for `fetch_gmail_thread`): `{gid}`")
    if probe_source_thread_id is not None:
        lines.append(f"Workbench thread where inbox probe was run (reference): `{int(probe_source_thread_id)}`")
    lines.append("")

    ev = snap.get("retrieval_evidence")
    if isinstance(ev, list) and ev:
        lines.append("### Retrieval evidence (latest saved action JSON)")
        for j, item in enumerate(ev[:24], start=1):
            if isinstance(item, dict):
                sn = _hydrate_clip(item.get("snippet") or item.get("text") or item.get("quote"), 1200)
                src = _hydrate_clip(
                    item.get("title") or item.get("path") or item.get("url") or item.get("file"),
                    400,
                )
                if sn or src:
                    lines.append(f"{j}. {src + ': ' if src else ''}{sn}".strip())
            else:
                lines.append(f"{j}. {_hydrate_clip(item, 1500)}")
        lines.append("")

    refs = snap.get("references")
    if isinstance(refs, list) and refs:
        lines.append("### References (latest)")
        for r in refs[:15]:
            if isinstance(r, str) and r.strip():
                lines.append(f"- {_hydrate_clip(r, 900)}")
            elif isinstance(r, dict):
                title = str(r.get("title") or r.get("path") or r.get("label") or "").strip()
                url = str(r.get("url") or "").strip()
                val = " — ".join(x for x in (title, url) if x)
                if val:
                    lines.append(f"- {_hydrate_clip(val, 900)}")
        lines.append("")

    ca = str(snap.get("curated_answer") or "").strip()
    if ca:
        lines.append("### Curated answer (latest)")
        lines.append(_hydrate_clip(ca, 4000))
        lines.append("")

    tool_digest = tool_digest.strip()
    if tool_digest:
        lines.append("### Original probe run — retrieval-related tool I/O (excerpt)")
        lines.append(_hydrate_clip(tool_digest, 8000))
        lines.append("")

    body = "\n".join(lines).strip()
    if not body:
        return None
    if len(body) > max_body_chars:
        body = body[: max_body_chars - 1] + "…"
    return body


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
    es_subj = str(snapshot.get("email_subject") or "").strip()
    ef_from = str(snapshot.get("email_from") or "").strip()
    cd_dom = str(snapshot.get("customer_domain") or "").strip()
    if es_subj or ef_from or cd_dom:
        lines.append("")
        if es_subj:
            lines.append(f"Email subject: {_clip(es_subj, 500)}")
        if ef_from:
            lines.append(f"From: {_clip(ef_from, 400)}")
        if cd_dom:
            lines.append(f"Customer domain: {_clip(cd_dom, 200)}")
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
    ev = snapshot.get("retrieval_evidence")
    if isinstance(ev, list) and ev:
        lines.append("")
        lines.append("Retrieval evidence (KB snippets attached to this action):")
        for j, item in enumerate(ev[:20], start=1):
            if isinstance(item, dict):
                sn = _clip(item.get("snippet") or item.get("text") or item.get("quote"), 1200)
                src = _clip(
                    item.get("title") or item.get("path") or item.get("url") or item.get("file"),
                    400,
                )
                if sn or src:
                    lines.append(f"{j}. {src + ': ' if src else ''}{sn}".strip())
            else:
                lines.append(f"{j}. {_clip(item, 1500)}")
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
    by_tid_from_tool = _extract_probe_thread_identity_from_events(md)
    used_tools = _retrieval_tools_used(md)
    has_retrieval = bool(used_tools.intersection({"search_product_docs", "search_rc_web"}))
    product_without_retrieval = 0
    fetched_tid_identity: dict[str, dict[str, str]] = {}
    by_thread = existing_by_thread or {}
    merged: list[dict[str, Any]] = []
    skipped_unchanged = 0
    for a in actions:
        if not isinstance(a, dict):
            continue
        gid0 = str(a.get("gmail_thread_id") or "").strip()
        if gid0 and gid0 in by_tid_from_tool:
            src = by_tid_from_tool.get(gid0) or {}
            if not str(a.get("email_from") or "").strip():
                ef = str(src.get("email_from") or "").strip()
                if ef:
                    a["email_from"] = ef[:400]
            if not str(a.get("email_subject") or "").strip():
                es = str(src.get("email_subject") or "").strip()
                if es:
                    a["email_subject"] = es[:400]
            if not str(a.get("customer_identifier") or "").strip():
                cid = str(src.get("customer_identifier") or "").strip()
                if cid:
                    a["customer_identifier"] = cid[:200]
            if not str(a.get("customer_email") or "").strip():
                ce = str(src.get("customer_email") or "").strip()
                if ce:
                    a["customer_email"] = ce[:320]
        need_identity = (
            gid0
            and (
                not str(a.get("email_from") or "").strip()
                or not str(a.get("email_subject") or "").strip()
                or not str(a.get("customer_email") or "").strip()
            )
        )
        if need_identity:
            if gid0 not in fetched_tid_identity:
                try:
                    from src.agent.tools.gmail_tool import fetch_gmail_thread

                    fetched_tid_identity[gid0] = _extract_identity_from_thread_text(fetch_gmail_thread(gid0))
                except Exception:
                    fetched_tid_identity[gid0] = {}
            src2 = fetched_tid_identity.get(gid0) or {}
            if not str(a.get("email_from") or "").strip() and src2.get("email_from"):
                a["email_from"] = str(src2.get("email_from"))[:400]
            if not str(a.get("email_subject") or "").strip() and src2.get("email_subject"):
                a["email_subject"] = str(src2.get("email_subject"))[:400]
            if not str(a.get("customer_email") or "").strip() and src2.get("customer_email"):
                a["customer_email"] = str(src2.get("customer_email"))[:320]
            if not str(a.get("customer_identifier") or "").strip() and src2.get("customer_identifier"):
                a["customer_identifier"] = str(src2.get("customer_identifier"))[:200]
        if not str(a.get("customer_email") or "").strip():
            ce = _pick_external_customer_email(str(a.get("email_from") or ""))
            if ce:
                a["customer_email"] = ce[:320]
        if not str(a.get("customer_identifier") or "").strip():
            cid2 = _customer_identifier_from_fromline(str(a.get("email_from") or ""))
            if not cid2:
                ce2 = str(a.get("customer_email") or "")
                if ce2 and "@" in ce2:
                    cid2 = ce2.split("@", 1)[0]
            if cid2:
                a["customer_identifier"] = cid2[:200]
        # If retrieval tools were never called this run, references/evidence must be empty.
        if not has_retrieval:
            a["references"] = []
            a["retrieval_evidence"] = []
        if str(a.get("category") or "").strip().lower() == "product_technical" and not has_retrieval:
            product_without_retrieval += 1
        key = _dedupe_key(a)
        if key and key in by_thread:
            prev = by_thread.get(key) or {}
            if isinstance(prev, dict):
                if not str(a.get("email_from") or "").strip():
                    pef = str(prev.get("email_from") or "").strip()
                    if pef:
                        a["email_from"] = pef[:400]
                if not str(a.get("email_subject") or "").strip():
                    pes = str(prev.get("email_subject") or "").strip()
                    if pes:
                        a["email_subject"] = pes[:400]
                if not str(a.get("customer_identifier") or "").strip():
                    pcid = str(prev.get("customer_identifier") or "").strip()
                    if pcid:
                        a["customer_identifier"] = pcid[:200]
                if not str(a.get("customer_email") or "").strip():
                    pce = str(prev.get("customer_email") or "").strip()
                    if pce:
                        a["customer_email"] = pce[:320]
                if not str(a.get("thread_title") or "").strip():
                    ptt = str(prev.get("thread_title") or "").strip()
                    if ptt:
                        a["thread_title"] = ptt[:400]
                ef_carry = str(a.get("email_from") or "").strip()
                if ef_carry:
                    a["customer_domain"] = _guardrail_domain(ef_carry)[:200]
            prev_status = str(prev.get("status") or "").strip().lower()
            if prev_status not in {"not_started", "in_progress", "completed"}:
                prev_status = "not_started"
            same_fp = _action_fingerprint(a) == _action_fingerprint(prev)
            if same_fp:
                src_id = int(prev.get("_probe_merge_interaction_id") or 0)
                fp_prev = _action_fingerprint(prev)
                if src_id and _probe_action_still_on_dashboard(
                    source_interaction_id=src_id,
                    dedupe_key=key,
                    fingerprint=fp_prev,
                ):
                    # Same text as a card still on the board (e.g. hourly cron, no new mail).
                    skipped_unchanged += 1
                    continue
                # Same fingerprint as a ghost row (e.g. user removed the card) — re-surface as new.
                a["status"] = "not_started"
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
        "retrieval_tools_used": sorted(list(used_tools)),
        "has_retrieval_tool_call": has_retrieval,
        "product_technical_without_retrieval": product_without_retrieval,
    }
    if product_without_retrieval > 0:
        md["csm_policy_warnings"] = (
            md.get("csm_policy_warnings") or []
        ) + [
            f"{product_without_retrieval} product_technical action(s) were produced without search_product_docs/search_rc_web tool calls."
        ]
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
