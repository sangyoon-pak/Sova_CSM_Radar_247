"""Agent memory compaction and feedback distillation.

- **`compact_memory`**: summarizes older `agent_interactions` into `agent_memory` rows
  and deletes those interactions. This path does **not** populate `{learning_section}`.
- **`refresh_learning_instructions`**: (1) loads a **pool** of recent `agent_feedback` rows (`LEARNING_FEEDBACK_SAMPLE_POOL`), then selects at most **`MAX_LEARNING_FEEDBACK_FOR_DISTILL`** (5) with **action_dashboard** rows reserved so card feedback is not starved by newer run-history noise; (2) per-row JSON + **`distillation_payload`**; (3) partitions into
  `negative` / `endorsed`; (4) persists **`agent_learning_last_partition_json`**; (5) **one LLM** →
  **`agent_learning_constraints`** + **`agent_learning_exemplars`**.
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
    - `max_interactions`: maximum number of interactions to summarize in one call.
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


def _infer_surface(meta: dict[str, Any]) -> str:
    src = str(meta.get("source") or "").strip().lower()
    if src == "run_history":
        return "run_history"
    if src == "action_dashboard":
        return "action_dashboard"
    if meta.get("action_index") is not None:
        return "action_dashboard"
    if src:
        return src
    return "unknown"


def _reinforcement_label(verdict: str) -> str:
    v = (verdict or "").strip().lower()
    if v in ("correct", "useful"):
        return "endorsed"
    return "negative"


def _all_feedback_interaction_ids(samples: Sequence[dict]) -> list[int]:
    out: list[int] = []
    seen: set[int] = set()
    for s in samples:
        raw_iid = s.get("interaction_id")
        try:
            iid = int(raw_iid) if raw_iid is not None else None
        except (TypeError, ValueError):
            iid = None
        if iid is None or iid <= 0 or iid in seen:
            continue
        seen.add(iid)
        out.append(iid)
    return out


_DASHBOARD_CARD_FIELDS_FOR_LEARNING: tuple[str, ...] = (
    "title",
    "brief",
    "category",
    "include_on_dashboard",
    "gmail_thread_id",
    "email_from",
    "email_subject",
    "customer_identifier",
)

_OUT_EXCERPT_COMPACT = 1200
_IN_EXCERPT_COMPACT = 500
_GROUND_SNIP_OUTPUT = 520
_GROUND_SNIP_BRIEF = 260

# Cap rows fed to the learning LLM to bound prompt size.
MAX_LEARNING_FEEDBACK_FOR_DISTILL = 5
# Fetch this many newest eligible rows, then `_select_distillation_rows` picks up to
# `MAX_LEARNING_FEEDBACK_FOR_DISTILL`, prioritizing action_dashboard so buried card rows still distill.
LEARNING_FEEDBACK_SAMPLE_POOL = 40


def _feedback_row_id(row: dict) -> int:
    try:
        return int(row.get("id") or 0)
    except (TypeError, ValueError):
        return 0


def _select_distillation_rows(rows: list[dict], max_n: int) -> list[dict]:
    """Prefer including recent action_dashboard rows; fill with newest feedback otherwise.

    `rows` must be newest-first (as returned by `get_learning_feedback_samples`).
    """
    if max_n < 1:
        max_n = 1
    if len(rows) <= max_n:
        return rows

    seen: set[int] = set()
    out: list[dict] = []

    def add(r: dict) -> bool:
        rid = _feedback_row_id(r)
        if rid <= 0 or rid in seen:
            return False
        seen.add(rid)
        out.append(r)
        return True

    # Newest-first scan: reserve up to 2 slots for action_dashboard (card) feedback.
    dash_budget = 2
    for r in rows:
        if len(out) >= max_n:
            break
        meta = _parse_feedback_metadata(r.get("metadata"))
        if _infer_surface(meta) != "action_dashboard":
            continue
        if dash_budget <= 0:
            continue
        if add(r):
            dash_budget -= 1

    for r in rows:
        if len(out) >= max_n:
            break
        add(r)

    out.sort(key=_feedback_row_id, reverse=True)
    return out[:max_n]


def _snippet_one_line(text: str | None, max_len: int) -> str:
    if not text:
        return ""
    s = " ".join(str(text).strip().split())
    if len(s) <= max_len:
        return s
    return s[: max_len - 1] + "…"


def _attach_operator_grounding(rec: dict[str, Any]) -> None:
    """
    Deterministic text the summarizer must use so CONSTRAINTS / EXEMPLARS are not generic run-id-only bullets.

    - **constraints_grounding**: negative rows (any surface) and endorsed **action_dashboard** (card
      preferences must appear under CONSTRAINTS, not EXEMPLARS).
    - **exemplars_grounding**: endorsed **run_history** only.
    """
    surf = str(rec.get("surface") or "")
    rein = str(rec.get("reinforcement") or "")
    note = (rec.get("note") or "").strip()
    correction = (rec.get("correction") or "").strip()
    card = rec.get("scoped_action_card") if isinstance(rec.get("scoped_action_card"), dict) else {}
    m_out = (rec.get("model_output_excerpt") or "").strip()

    rec["constraints_grounding"] = None
    rec["exemplars_grounding"] = None

    if rein == "negative":
        parts: list[str] = []
        if note:
            parts.append(f"Operator note: {note[:880]}")
        if correction:
            parts.append(f"Operator correction: {correction[:880]}")
        if surf == "action_dashboard" and card:
            bt = _snippet_one_line(card.get("brief"), _GROUND_SNIP_BRIEF)
            parts.append(
                f"Card: title={card.get('title', '')!s}; category={card.get('category', '')!s}"
                + (f"; brief={bt}" if bt else "")
            )
        if m_out:
            parts.append(f"Affected probe/model output (excerpt): {_snippet_one_line(m_out, _GROUND_SNIP_OUTPUT)}")
        rec["constraints_grounding"] = "\n".join(parts) if parts else None

    elif rein == "endorsed" and surf == "action_dashboard":
        pieces = [
            "Operator card preference (endorsed useful/correct on this action card): "
            + (note[:880] if note else "(no note)")
        ]
        if card:
            bt = _snippet_one_line(card.get("brief"), _GROUND_SNIP_BRIEF)
            pieces.append(
                f"Card: title={card.get('title', '')!s}; category={card.get('category', '')!s}"
                + (f"; brief={bt}" if bt else "")
            )
        rec["constraints_grounding"] = "\n".join(pieces)

    elif rein == "endorsed" and surf == "run_history":
        ex_parts: list[str] = []
        if note:
            ex_parts.append(f"Operator endorsement: {note[:880]}")
        if m_out:
            ex_parts.append(f"Endorsed model output (excerpt): {_snippet_one_line(m_out, _GROUND_SNIP_OUTPUT)}")
        rec["exemplars_grounding"] = "\n".join(ex_parts) if ex_parts else None


def _build_distillation_payload(rec: dict[str, Any]) -> dict[str, Any]:
    """
    Single structured object per row for the final LLM (same shape for run_history and action_dashboard).
    Prefer this over echoing raw `note` lines when synthesizing CONSTRAINTS / EXEMPLARS.
    """
    meta_raw = rec.get("metadata") if isinstance(rec.get("metadata"), dict) else {}
    slim_meta: dict[str, Any] = {}
    for k in ("source", "action_index"):
        if k in meta_raw and meta_raw.get(k) is not None:
            slim_meta[k] = meta_raw.get(k)
    ctx: dict[str, Any] = {}
    if rec.get("scoped_action_card"):
        ctx["action_card"] = rec.get("scoped_action_card")
    if rec.get("model_output_excerpt"):
        ctx["model_output_excerpt"] = rec.get("model_output_excerpt")
    if rec.get("model_input_excerpt"):
        ctx["model_input_excerpt"] = rec.get("model_input_excerpt")

    return {
        "feedback_id": rec.get("feedback_id"),
        "interaction_id": rec.get("interaction_id"),
        "surface": rec.get("surface"),
        "verdict": rec.get("verdict"),
        "reinforcement": rec.get("reinforcement"),
        "metadata": slim_meta if slim_meta else None,
        "operator": {
            "note": rec.get("note"),
            "correction": rec.get("correction"),
        },
        "context": ctx if ctx else None,
        "constraints_grounding": rec.get("constraints_grounding"),
        "exemplars_grounding": rec.get("exemplars_grounding"),
    }


def _finalize_learning_record(rec: dict[str, Any]) -> None:
    _attach_operator_grounding(rec)
    rec["distillation_payload"] = _build_distillation_payload(rec)


def _scoped_action_card_dict(inter: dict | None, action_index: Any) -> dict[str, Any] | None:
    if not inter:
        return None
    try:
        idx = int(action_index) if action_index is not None else -1
    except (TypeError, ValueError):
        return None
    if idx < 0:
        return None
    md = database.parse_interaction_metadata(inter.get("metadata"))
    actions = md.get("csm_actions")
    if not isinstance(actions, list) or idx >= len(actions):
        return None
    card = actions[idx]
    if not isinstance(card, dict):
        return None
    snap: dict[str, Any] = {}
    for k in _DASHBOARD_CARD_FIELDS_FOR_LEARNING:
        v = card.get(k)
        if v is None or v == "":
            continue
        s = str(v).strip().replace("\r\n", "\n")
        if len(s) > 480:
            s = s[:480] + "…"
        snap[k] = s
    return snap or None


def build_learning_feedback_json_record(s: dict, run_ctx_by_id: dict[int, dict]) -> dict[str, Any]:
    """One JSON object per DB row: stored fields + derived surface/reinforcement + optional context."""
    meta = _parse_feedback_metadata(s.get("metadata"))
    verdict = str(s.get("verdict") or "").strip().lower()
    surface = _infer_surface(meta)
    rec: dict[str, Any] = {
        "feedback_id": s.get("id"),
        "created_at": str(s.get("created_at") or ""),
        "interaction_id": s.get("interaction_id"),
        "verdict": verdict,
        "note": (s.get("note") or "").strip()[:900] or None,
        "correction": (s.get("correction") or "").strip()[:900] or None,
        "metadata": meta,
        "surface": surface,
        "reinforcement": _reinforcement_label(verdict),
    }
    raw_iid = s.get("interaction_id")
    try:
        iid = int(raw_iid) if raw_iid is not None else None
    except (TypeError, ValueError):
        iid = None
    if iid is None:
        _finalize_learning_record(rec)
        return rec
    inter = run_ctx_by_id.get(iid)
    if not inter:
        _finalize_learning_record(rec)
        return rec
    if surface == "action_dashboard":
        ai = meta.get("action_index")
        if ai is not None:
            try:
                rec["action_index"] = int(ai)
            except (TypeError, ValueError):
                pass
        card = _scoped_action_card_dict(inter, ai)
        if card:
            rec["scoped_action_card"] = card
    else:
        trig = str(inter.get("trigger_type") or "")
        out = (inter.get("output_text") or inter.get("error_message") or "").strip()
        if out:
            rec["model_output_excerpt"] = out[:_OUT_EXCERPT_COMPACT]
        if not database.is_dashboard_probe_trigger(trig):
            inp = (inter.get("input_text") or "").strip()
            if inp:
                rec["model_input_excerpt"] = inp[:_IN_EXCERPT_COMPACT]
    _finalize_learning_record(rec)
    return rec


def partition_learning_feedback_records(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Deterministic split: classification is already on each row (`reinforcement`); no LLM."""
    negative: list[dict[str, Any]] = []
    endorsed: list[dict[str, Any]] = []
    for r in records:
        if r.get("reinforcement") == "endorsed":
            endorsed.append(r)
        else:
            negative.append(r)
    return {"schema_version": 1, "negative": negative, "endorsed": endorsed}


LEARNING_REINFORCEMENT_SYSTEM = """You are the **learning reinforcement** summarizer for a CSM inbox assistant.

The user message is **LEARNING_FEEDBACK_PARTITIONED_JSON**: one JSON object with `schema_version`, **`negative`**, and **`endorsed`** arrays.

**Primary source for every row:** the object **`distillation_payload`** (structured JSON). It contains:
- `operator.note` / `operator.correction` — free text from the operator.
- `metadata` — e.g. `source`, `action_index`.
- `context` — **`action_card`** (title, brief, category, …) for dashboard rows; **`model_output_excerpt`** / **`model_input_excerpt`** for probe runs.
- `constraints_grounding` / `exemplars_grounding` — pre-joined hints (use together with `distillation_payload`, not instead of it).

**Section routing (do not re-classify verdicts):**

1. **===CONSTRAINTS===**  
   For **`negative`** rows (including **action_dashboard** card text such as “not needed” — stored as **`incorrect`** with a note) and any legacy **`endorsed`** + **`action_dashboard`** rows: synthesize actionable bullets **from `distillation_payload`**, especially `operator`, `context.action_card`, and `context.model_output_excerpt`.  
   When `operator.note` is only a template like “[Run history] run #N: Incorrect” with little substance, **you must** infer what went wrong using **`context.model_output_excerpt`** (quote or paraphrase the problematic part) and any **`operator.correction`**.

2. **===EXEMPLARS===**  
   Only **`endorsed`** + **`surface` `run_history`**, using `distillation_payload`. Never put **`action_dashboard`** in EXEMPLARS.

**EXEMPLARS must not invent praise:** Paraphrase **only** what the operator actually signalled in `distillation_payload.operator.note` (and matching lines in `exemplars_grounding`). Do **not** spin long narratives from `model_output_excerpt` alone (e.g. quota math, client names, alert bodies) unless the operator note clearly praises that specific handling. Prefer **2–4 short sentences** tied to the endorsement wording. If the note is a thin template, say **(none)** rather than elaborating the excerpt.

**Quality bar (non-negotiable):**
- **Never** emit CONSTRAINT bullets that only repeat the raw `note` string or start with labels like “Operator note:” / “Operator card preference”. Rewrite into **specific** triage rules (what to change, what pattern to avoid, which card shapes or categories).
- Each negative bullet must tie to **concrete content**: card title/category/brief, correction text, or a **short quoted phrase** from `model_output_excerpt` so a future run has context.
- **Forbidden:** a CONSTRAINT bullet that is only “run #N was incorrect” without describing the failure mode using `distillation_payload.context`.

**Output format (exact markers, nothing before the first marker):**

===CONSTRAINTS===
- Only lines starting with "- ".

===EXEMPLARS===
- Short text (markdown allowed, max ~1500 characters). If there is no qualifying `run_history` endorsement, output exactly: (none)

**Anti-duplication:** Same `interaction_id` in both arrays — CONSTRAINTS use the negative `distillation_payload`; EXEMPLARS use the endorsed run_history row.

**Rules:**
- Do not invent vendors, products, or scenarios absent from the JSON.
- CONSTRAINTS may be empty only if no record has usable constraint signal.
- No preamble outside the two sections."""


def _split_compacted_learning_response(text: str) -> tuple[str, str]:
    raw = (text or "").strip()
    if "===EXEMPLARS===" in raw:
        left, right = raw.split("===EXEMPLARS===", 1)
        constraints = left.replace("===CONSTRAINTS===", "").strip()
        exemplars = right.strip()
    else:
        constraints = raw.replace("===CONSTRAINTS===", "").strip()
        exemplars = ""
    return constraints, exemplars


def _normalize_distilled_constraint_line(line: str) -> str:
    """Map common LLM bullets (*, •) to hyphen bullets so dedupe keeps them."""
    s = line.strip()
    if s.startswith("•"):
        return "- " + s[1:].lstrip()
    if s.startswith("*"):
        return "- " + s[1:].lstrip()
    return s


def _dedupe_distilled_bullet_lines(rules: str) -> str:
    bullets: list[str] = []
    seen_norm: set[str] = set()
    for ln in (rules or "").splitlines():
        s = _normalize_distilled_constraint_line(ln)
        if not s.startswith("-"):
            continue
        low = " ".join(s.lower().split())[:200]
        if low in seen_norm:
            continue
        seen_norm.add(low)
        bullets.append(s)
    return "\n".join(bullets).strip()


def clear_distilled_learning_instructions() -> dict:
    """Clear learning memory artifacts and all stored feedback (Run history + Action dashboard).

    Clears `agent_learning_constraints`, `agent_learning_exemplars`, legacy
    `agent_learning_instructions`, and deletes every row in `agent_feedback`.
    """
    feedback_deleted = database.delete_all_agent_feedback()
    database.set_app_setting(database.KEY_AGENT_LEARNING_CONSTRAINTS, "")
    database.set_app_setting(database.KEY_AGENT_LEARNING_EXEMPLARS, "")
    database.set_app_setting(database.KEY_AGENT_LEARNING_LEGACY, "")
    database.set_app_setting(database.KEY_AGENT_LEARNING_LAST_PARTITION, "")
    snap = database.get_agent_learning_instructions_snapshot()
    return {
        "cleared": True,
        "feedback_deleted": feedback_deleted,
        "instructions": snap["instructions"],
        "constraints": snap.get("constraints", ""),
        "exemplars": snap.get("exemplars", ""),
        "updated_at": snap["updated_at"],
    }


def refresh_learning_instructions(max_feedback: int | None = None) -> dict:
    """
    Per-row JSON → deterministic negative/endorsed partition → one LLM → constraints + exemplars.

    Uses at most `max_learning_feedback_for_distill` (default **5**) feedback rows selected from a
    larger newest-first pool so action_dashboard rows are not dropped when many run-history notes exist.
    """
    cap = max_feedback if max_feedback is not None else MAX_LEARNING_FEEDBACK_FOR_DISTILL
    if cap < 1:
        cap = 1
    if cap > MAX_LEARNING_FEEDBACK_FOR_DISTILL:
        cap = MAX_LEARNING_FEEDBACK_FOR_DISTILL

    pool = database.get_learning_feedback_samples(limit=LEARNING_FEEDBACK_SAMPLE_POOL)
    samples = _select_distillation_rows(pool, cap)
    if not samples:
        database.set_app_setting(database.KEY_AGENT_LEARNING_CONSTRAINTS, "")
        database.set_app_setting(database.KEY_AGENT_LEARNING_EXEMPLARS, "")
        database.set_app_setting(database.KEY_AGENT_LEARNING_LEGACY, "")
        database.set_app_setting(database.KEY_AGENT_LEARNING_LAST_PARTITION, "")
        return {
            "updated": True,
            "rules": 0,
            "constraints_bullets": 0,
            "exemplar_sections": 0,
            "llm_stages": 0,
            "feedback_rows_used": 0,
            "max_feedback_cap": cap,
        }

    run_ctx_by_id = database.get_interactions_by_ids(_all_feedback_interaction_ids(samples))
    records = [build_learning_feedback_json_record(s, run_ctx_by_id) for s in samples]
    partitioned = partition_learning_feedback_records(records)
    bundle_json = json.dumps(partitioned, ensure_ascii=False, indent=2)
    max_chars = 120_000
    if len(bundle_json) > max_chars:
        bundle_json = bundle_json[:max_chars] + "\n… (truncated for token limit)\n"

    database.set_app_setting(database.KEY_AGENT_LEARNING_LAST_PARTITION, bundle_json)

    llm = _get_llm()
    response = llm.invoke(
        [
            SystemMessage(content=LEARNING_REINFORCEMENT_SYSTEM),
            HumanMessage(content="LEARNING_FEEDBACK_PARTITIONED_JSON:\n" + bundle_json),
        ]
    )
    raw_out = str(response.content or "").strip()
    constraints, exemplars = _split_compacted_learning_response(raw_out)
    constraints = _dedupe_distilled_bullet_lines(constraints)
    database.set_app_setting(database.KEY_AGENT_LEARNING_CONSTRAINTS, constraints)
    database.set_app_setting(database.KEY_AGENT_LEARNING_EXEMPLARS, exemplars.strip())
    database.set_app_setting(database.KEY_AGENT_LEARNING_LEGACY, "")
    bullet_count = len([ln for ln in constraints.splitlines() if ln.strip().startswith("-")])
    ex_sections = 0 if not exemplars.strip() or exemplars.strip().lower() == "(none)" else 1
    return {
        "updated": True,
        "rules": bullet_count,
        "constraints_bullets": bullet_count,
        "exemplar_sections": ex_sections,
        "llm_stages": 1,
        "feedback_rows_used": len(samples),
        "max_feedback_cap": cap,
    }
