"""Proactive CSM assistant (LangChain): inbox triage, KB tools, drafts on explicit request."""
import os
import re
import json
from contextlib import nullcontext
from collections.abc import Callable, Sequence

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.tools import tool
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain.agents import create_agent
from langsmith import Client as LangSmithClient
from langsmith.run_helpers import trace, tracing_context

from src.agent.chat_llm import get_chat_llm
from src.config import settings
from src.runtime_config import (
    effective_guardrail_team_guidance,
    effective_langsmith_api_key,
    effective_langsmith_project,
    effective_langsmith_tracing,
    effective_llm_model_main,
    effective_llm_model_search_json,
    effective_probe_inbox_gmail_search,
    effective_probe_inbox_max_results,
    effective_rc_web_retrieval_mode,
    effective_user_inbox_peek_max_results,
)
from src.agent.prompts import (
    get_probe_mode_system_append,
    render_email_agent_system,
)
from src.db import database
from src.scheduler import cron_manager


class AgentRunCancelled(Exception):
    """Raised when the user requests stop (cooperative cancellation between LLM/tool steps)."""


class _CancelPatrolCallback(BaseCallbackHandler):
    """Raises AgentRunCancelled when cancel_check() returns True (see run_state.request_cancel)."""

    # LangChain swallows callback exceptions unless this is True (see callbacks/manager.handle_event).
    raise_error = True

    def __init__(self, cancel_check: Callable[[], bool]):
        self._cancel_check = cancel_check

    def _maybe_cancel(self) -> None:
        try:
            if self._cancel_check():
                raise AgentRunCancelled()
        except AgentRunCancelled:
            raise
        except Exception:
            pass

    def on_chain_start(self, serialized, inputs, **kwargs):  # noqa: ARG002
        self._maybe_cancel()

    def on_chat_model_start(self, serialized, messages, **kwargs):  # noqa: ARG002
        self._maybe_cancel()

    def on_tool_start(self, serialized, input_str, **kwargs):  # noqa: ARG002
        self._maybe_cancel()


def _ensure_langsmith_env():
    """Set LangSmith env vars from runtime config so tracing works in uvicorn workers."""
    if effective_langsmith_tracing() and effective_langsmith_api_key():
        key = effective_langsmith_api_key()
        project = effective_langsmith_project()
        # Support both current and legacy env names across LangChain/LangSmith versions.
        os.environ["LANGSMITH_TRACING"] = "true"
        os.environ["LANGSMITH_API_KEY"] = key
        os.environ["LANGSMITH_PROJECT"] = project
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_API_KEY"] = key
        os.environ["LANGCHAIN_PROJECT"] = project
    else:
        os.environ.pop("LANGSMITH_TRACING", None)
        os.environ.pop("LANGSMITH_API_KEY", None)
        os.environ.pop("LANGSMITH_PROJECT", None)
        os.environ.pop("LANGCHAIN_TRACING_V2", None)
        os.environ.pop("LANGCHAIN_API_KEY", None)
        os.environ.pop("LANGCHAIN_PROJECT", None)


def _langsmith_parent_trace(*, input_text: str, probe: bool):
    """Create one parent trace run so classifier + agent calls are one trace tree."""
    try:
        if not effective_langsmith_tracing():
            return nullcontext()
        key = effective_langsmith_api_key().strip()
        if not key:
            return nullcontext()
        project = effective_langsmith_project().strip()
        client = LangSmithClient(api_key=key)
        return trace(
            "email_agent.run_agent",
            run_type="chain",
            project_name=project,
            client=client,
            inputs={"input_text": (input_text or "")[:500], "probe": bool(probe)},
            metadata={"component": "email_agent"},
        )
    except Exception:
        return nullcontext()


def _get_llm():
    return get_chat_llm(model=effective_llm_model_main(), temperature=0.3)


def _llm_intent_router():
    # Deterministic classifier for UX routing (language-agnostic).
    return get_chat_llm(model=effective_llm_model_search_json(), temperature=0.0)


INTENT_ROUTE_PROMPT = """You route the user's request to the correct action.

Return STRICT JSON ONLY:
{{
  "route": "inbox_peek" | "agent_run",
  "reason": "short"
}}

Definitions:
- inbox_peek: user is asking to show the latest/recent emails / check inbox / list emails. Do NOT draft replies. Do NOT search docs.
- agent_run: anything else (drafting, answering product questions, analysis, etc).

Be language-agnostic. Examples of inbox_peek:
- "latest email", "recent emails", "check inbox"
- "최근 이메일", "최신 이메일", "메일 확인", "받은편지함 보여줘"

User message:
{text}
"""


PROBE_THREAD_INTENT_PROMPT = """Classify one user turn (Workbench).

Return STRICT JSON ONLY:
{{
  "run_full_inbox_probe": true | false,
  "reason": "short english"
}}

true = user wants the full inbox probe pipeline now (Gmail triage → JSON → Action dashboard merge). Same intent as Scan inbox: includes inbox scan/probe/triage and requests to create/update/refresh/regenerate/sync action cards or the dashboard from inbox data (any language).

false = definitions/how-it-works only; single-thread email work; light peek at a few messages only; cron job ops; KB/general chat unrelated to running that pipeline.

User message:
{text}
"""


def _parse_json_object_from_llm_content(raw: str) -> dict | None:
    s = (raw or "").strip()
    if not s:
        return None
    if "```" in s:
        s = s.split("```")[1]
        if s.lstrip().startswith("json"):
            s = s[4:].lstrip()
    try:
        data = json.loads(s.strip())
        return data if isinstance(data, dict) else None
    except Exception:
        return None


def _probe_thread_intent_llm_enabled() -> bool:
    """When False, chat never auto-promotes to probe (no classifier call)."""
    ex = (os.environ.get("PROBE_THREAD_INTENT_CLASSIFIER") or "").strip().lower()
    if ex in ("heuristic", "0", "false", "off", "regex", "disabled"):
        return False
    if ex in ("llm", "1", "true", "on"):
        return True
    v = (getattr(settings, "probe_thread_intent_classifier", "llm") or "llm").strip().lower()
    return v not in ("heuristic", "0", "false", "off", "regex", "disabled")


def _classify_full_inbox_probe_intent_llm(text: str) -> bool | None:
    """Returns None on parse / transport failure (caller may fall back)."""
    t = (text or "").strip()
    if not t:
        return None
    llm = _llm_intent_router()
    prompt = PROBE_THREAD_INTENT_PROMPT.format(text=t[:2000])
    try:
        resp = llm.invoke(
            [HumanMessage(content=prompt)],
            config={"run_name": "email_agent.probe_thread_intent"},
        )
        data = _parse_json_object_from_llm_content(str(resp.content or ""))
        if not data:
            return None
        v = data.get("run_full_inbox_probe")
        if isinstance(v, bool):
            return v
        if isinstance(v, str):
            low = v.strip().lower()
            if low in ("true", "yes", "1", "y"):
                return True
            if low in ("false", "no", "0", "n"):
                return False
        return None
    except Exception:
        return None


def _route_user_request(text: str, *, callbacks: Sequence | None = None) -> str:
    t = (text or "").strip()
    if not t:
        return "agent_run"
    llm = _llm_intent_router()
    prompt = INTENT_ROUTE_PROMPT.format(text=t[:2000])
    base_cfg = {"run_name": "email_agent.route_intent"}
    cbs = list(callbacks) if callbacks else []
    if cbs:
        # Keep UI trace callbacks for local run history, but avoid explicit LangSmith
        # tracer on classifier side-calls so Workbench appears as one LangGraph trace.
        base_cfg["callbacks"] = cbs

    def _parse_route(resp_content: str) -> str | None:
        raw = (resp_content or "").strip()
        if "```" in raw:
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        data = json.loads(raw.strip())
        route = str(data.get("route") or "").strip()
        if route in ("inbox_peek", "agent_run"):
            return route
        return None

    try:
        resp = llm.invoke([HumanMessage(content=prompt)], config=base_cfg)
        parsed = _parse_route(str(resp.content or ""))
        if parsed:
            return parsed
    except Exception:
        pass
    return "agent_run"


_CRON_NAME_RE = re.compile(r"[A-Za-z0-9._:-]{3,80}")
_CRON_EXPR_RE = re.compile(
    r"(?<!\S)([\d*/,\-]+\s+[\d*/,\-]+\s+[\d*/,\-]+\s+[\d*/,\-]+\s+[\d*/,\-]+)(?!\S)"
)


def _recent_user_text(conversation_messages: list[dict] | None, *, limit: int = 6) -> str:
    if not conversation_messages:
        return ""
    vals: list[str] = []
    for row in reversed(conversation_messages):
        if (row.get("role") or "").strip().lower() != "user":
            continue
        c = str(row.get("content") or "").strip()
        if c:
            vals.append(c)
        if len(vals) >= limit:
            break
    vals.reverse()
    return "\n".join(vals)


def _extract_cron_name(text: str) -> str | None:
    t = (text or "").strip()
    if not t:
        return None
    m = re.search(r"(?:named|name)\s+[`'\"]?([A-Za-z0-9._:-]{3,80})[`'\"]?", t, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r"(?:create|add|update|adjust)\s+(?:a\s+)?cron(?:\s+job)?\s+([A-Za-z0-9._:-]{3,80})", t, re.IGNORECASE)
    if m:
        cand = m.group(1).strip()
        if cand.lower() not in {"job", "cron"}:
            return cand
    m = re.search(r"`([^`]{3,80})`", t)
    if m and _CRON_NAME_RE.fullmatch(m.group(1).strip() or ""):
        return m.group(1).strip()
    # Quoted free-form name (allows spaces for manually created jobs).
    m = re.search(r"[\"']([^\"']{3,120})[\"']", t)
    if m:
        return m.group(1).strip()
    return None


def _extract_cron_expr(text: str) -> str | None:
    t = " ".join((text or "").split())
    if not t:
        return None
    # Explicit 5-field numeric/wildcard expression
    m = _CRON_EXPR_RE.search(t)
    if m:
        expr = m.group(1).strip()
        parts = expr.split()
        if len(parts) == 5:
            return expr

    low = t.lower()
    every_h = re.search(r"every\s+(\d{1,2})\s*hours?", low)
    if every_h:
        n = int(every_h.group(1))
        if 1 <= n <= 23:
            dow = "1-5" if re.search(r"week\s*days?|weekdays?", low) else "*"
            return f"0 */{n} * * {dow}"

    if re.search(r"\bdaily\b", low):
        hh = 9
        mm = 0
        tm = re.search(r"(?:at\s+)?(\d{1,2})(?::(\d{2}))?\s*(am|pm)?", low)
        if tm:
            hh = int(tm.group(1))
            mm = int(tm.group(2) or "0")
            ap = (tm.group(3) or "").lower()
            if ap == "pm" and hh < 12:
                hh += 12
            if ap == "am" and hh == 12:
                hh = 0
            hh = max(0, min(23, hh))
            mm = max(0, min(59, mm))
        dow = "1-5" if re.search(r"week\s*days?|weekdays?", low) else "*"
        return f"{mm} {hh} * * {dow}"
    return None


def _maybe_handle_cron_request(
    *,
    input_text: str,
    conversation_messages: list[dict] | None = None,
    callbacks: Sequence | None = None,
) -> str | None:
    """
    Deterministic Workbench cron ops path (independent of prompt overrides).
    Handles create/update/delete/enable/disable/list and asks for missing details.
    """
    latest = (input_text or "").strip()
    low = latest.lower()
    hist = _recent_user_text(conversation_messages)
    low_hist = hist.lower()

    if "cron" not in low and "cron" not in low_hist:
        return None

    op = ""
    if re.search(r"\b(list|show)\b.*\bcron\b", low):
        op = "list"
    elif re.search(r"\b(delete|remove)\b", low) and "cron" in low:
        op = "delete"
    elif re.search(r"\b(disable|pause|turn off|stop)\b", low) and "cron" in low:
        op = "disable"
    elif re.search(r"\b(enable|resume|turn on|start)\b", low) and "cron" in low:
        op = "enable"
    elif re.search(r"\b(create|add|make|update|adjust)\b", low) and "cron" in low:
        op = "upsert"
    elif re.search(r"\b(yes|ok|sure|please)\b", low) and re.search(r"\b(create|add|do it)\b", low) and "cron" in low_hist:
        op = "upsert"
    else:
        return None

    def _emit_tool_start(name: str, payload: str) -> None:
        for cb in (callbacks or []):
            try:
                cb.on_tool_start({"name": name}, payload)  # type: ignore[attr-defined]
            except Exception:
                pass

    def _emit_tool_end(output: str) -> None:
        for cb in (callbacks or []):
            try:
                cb.on_tool_end(output)  # type: ignore[attr-defined]
            except Exception:
                pass

    if op == "list":
        _emit_tool_start("list_cron_jobs", "list")
        jobs = database.get_cron_jobs()
        if not jobs:
            out = "No cron jobs configured yet."
            _emit_tool_end(out)
            return out
        lines = []
        for j in jobs:
            name = str(j.get("name") or "").strip() or "(unnamed)"
            expr = str(j.get("cron_expression") or "").strip() or "-"
            tz = str(j.get("timezone") or "").strip() or "Asia/Seoul"
            enabled = bool(j.get("enabled"))
            lines.append(f"- `{name}`: `{expr}` ({tz}) — {'enabled' if enabled else 'disabled'}")
        out = "Current cron jobs:\n" + "\n".join(lines)
        _emit_tool_end(out)
        return out

    source_text = f"{hist}\n{latest}".strip()
    jobs = database.get_cron_jobs()
    name = _extract_cron_name(source_text)
    # Resolve against existing cron jobs, including names with spaces/manual naming.
    if jobs:
        text_low = source_text.lower()
        by_exact = {str(j.get("name") or ""): j for j in jobs}
        if name:
            for n in by_exact:
                if n.lower() == name.lower():
                    name = n
                    break
        if not name:
            for n in by_exact:
                if n and n.lower() in text_low:
                    name = n
                    break
        if not name and op in {"delete", "enable", "disable"} and len(jobs) == 1:
            only = str(jobs[0].get("name") or "").strip()
            if only:
                name = only
    if not name:
        if op in {"delete", "enable", "disable"} and jobs:
            names = ", ".join(f"`{str(j.get('name') or '').strip()}`" for j in jobs[:12] if str(j.get("name") or "").strip())
            return (
                "I can do that, but I couldn't identify which cron job you meant. "
                f"Please specify one of: {names}"
            )
        return (
            "I can do that. Please provide the cron job name first "
            "(e.g. `weekday_4h_probe`)."
        )

    if op == "delete":
        _emit_tool_start("delete_cron_job", f"name={name}")
        try:
            cron_manager.remove_job(name)
            out = f"Deleted cron job `{name}`."
            _emit_tool_end(out)
            return out
        except Exception as e:
            out = f"Could not delete cron job `{name}`: {e}"
            _emit_tool_end(out)
            return out
    if op == "disable":
        _emit_tool_start("set_cron_job_enabled", f"name={name} enabled=false")
        try:
            cron_manager.toggle_job(name, False)
            out = f"Disabled cron job `{name}`."
            _emit_tool_end(out)
            return out
        except Exception as e:
            out = f"Could not disable cron job `{name}`: {e}"
            _emit_tool_end(out)
            return out
    if op == "enable":
        _emit_tool_start("set_cron_job_enabled", f"name={name} enabled=true")
        try:
            cron_manager.toggle_job(name, True)
            out = f"Enabled cron job `{name}`."
            _emit_tool_end(out)
            return out
        except Exception as e:
            out = f"Could not enable cron job `{name}`: {e}"
            _emit_tool_end(out)
            return out

    expr = _extract_cron_expr(source_text)
    if not expr:
        return (
            "I can create/update it, but I still need the schedule. "
            "Tell me a cadence (e.g. `every 4 hours on weekdays`) or a 5-field cron expression."
        )
    tz = "Asia/Seoul"
    _emit_tool_start("upsert_cron_job", f"name={name} cron_expression={expr} timezone={tz}")
    try:
        cron_manager.add_job(name, expr, tz)
        human = cron_manager.describe_cron_expression(expr)
        upcoming = cron_manager.preview_next_runs(expr, tz, count=3)
        if upcoming:
            nxt = ", ".join(upcoming)
            out = (
                f"Saved cron job `{name}`.\n"
                f"- Schedule: `{expr}` ({tz})\n"
                f"- Meaning: {human}\n"
                f"- Next runs: {nxt}"
            )
            _emit_tool_end(out)
            return out
        out = (
            f"Saved cron job `{name}`.\n"
            f"- Schedule: `{expr}` ({tz})\n"
            f"- Meaning: {human}"
        )
        _emit_tool_end(out)
        return out
    except Exception as e:
        out = (
            f"I understood name `{name}` and schedule `{expr}`, but creation failed: {e}. "
            "Please provide a 5-field cron expression if you want exact control."
        )
        _emit_tool_end(out)
        return out


def is_cron_management_request(
    input_text: str,
    *,
    conversation_messages: list[dict] | None = None,
) -> bool:
    t = (input_text or "").strip().lower()
    hist = _recent_user_text(conversation_messages).lower()
    if "cron" not in t and "cron" not in hist:
        return False
    if re.search(r"\b(list|show|create|add|make|update|adjust|delete|remove|disable|pause|enable|resume)\b", t):
        return True
    if re.search(r"\b(yes|ok|sure|please)\b", t) and "cron" in hist:
        return True
    return False


def is_inbox_probe_chat_intent(text: str) -> bool:
    """
    True when the user wants a full inbox probe (same as probe=True / Scan inbox).

    Decided only by the JSON classifier on LLM_MODEL_SEARCH_JSON. Returns false if that is disabled
    (PROBE_THREAD_INTENT_CLASSIFIER=off) or the call fails.

    Set PROBE_THREAD_INTENT_CLASSIFIER=off to disable auto-probe from chat (no classifier call).
    """
    raw = (text or "").strip()
    if not raw:
        return False
    if not _probe_thread_intent_llm_enabled():
        return False
    # This pre-run classifier executes before the main Workbench trace exists.
    # Keep it out of LangSmith to avoid a separate top-level trace thread.
    with tracing_context(enabled=False):
        try:
            return bool(_classify_full_inbox_probe_intent_llm(raw[:2000]))
        except Exception:
            # Never fail /threads/send due to pre-route classifier issues
            # (for example missing provider API keys).
            return False


_SOURCE_TAG_RE = re.compile(r"^\[Source:\s*(.+?)\s*\|\s*line\s*\d+\]\s*$", re.MULTILINE)


def _flatten_ai_content(content) -> str:
    """LangChain may use str or list of blocks for AIMessage.content."""
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict):
                if block.get("type") == "text":
                    parts.append(str(block.get("text") or ""))
                elif "text" in block:
                    parts.append(str(block["text"]))
            else:
                parts.append(str(block))
        return "".join(parts)
    return str(content)


def db_conversation_to_langchain(rows: list[dict]) -> list:
    """
    Map persisted thread rows to LangChain messages. Only this thread's rows should be passed —
    the agent then sees that thread as its conversational context (no cross-thread mixing).
    """
    out: list = []
    for row in rows or []:
        role = (row.get("role") or "").strip().lower()
        content = row.get("content")
        if content is None:
            continue
        text = str(content).strip()
        if not text:
            continue
        if role == "system":
            out.append(SystemMessage(content=text))
        elif role == "user":
            out.append(HumanMessage(content=text))
        elif role == "assistant":
            out.append(AIMessage(content=text))
    return out


def _collect_probe_assistant_output(messages: list) -> str:
    """
    In probe mode the model may emit valid ```json``` in an earlier assistant turn and then
    paste raw inbox text in the last turn — parsing only the last AIMessage misses the JSON.
    Join all assistant text so parse_probe_dashboard_json can find the fenced block.
    """
    chunks: list[str] = []
    for m in messages:
        if isinstance(m, AIMessage):
            t = _flatten_ai_content(m.content).strip()
            if t:
                chunks.append(t)
    return "\n\n".join(chunks)


def _extract_source_tags_from_messages(messages: list) -> list[str]:
    """
    Pull NotebookLM-style chunk tags from any tool outputs.
    We avoid relying on ToolMessage types; we just scan all message contents.
    """
    tags: list[str] = []
    seen: set[str] = set()
    for m in messages or []:
        content = getattr(m, "content", None)
        if not content:
            continue
        text = str(content)
        for match in _SOURCE_TAG_RE.finditer(text):
            # Keep the full tag including the numeric line (do not replace with "line ...").
            tag = match.group(0).strip()
            if tag in seen:
                continue
            seen.add(tag)
            tags.append(tag)
    return tags[:40]


def _draft_needs_citations(draft: str) -> bool:
    """
    If there's a numbered list, require citations for each item.
    """
    if not draft:
        return False
    has_numbered = bool(re.search(r"(?m)^\s*\d+\.\s*\*\*", draft))
    if not has_numbered:
        return False
    # If any numbered item block doesn't contain "(출처:" we do a citation pass.
    blocks = re.split(r"(?m)^(?=\s*\d+\.\s)", draft)
    for b in blocks:
        if re.match(r"(?m)^\s*\d+\.\s", b) and "(출처:" not in b:
            return True
    return False


def _add_citations_pass(
    *,
    draft: str,
    source_tags: list[str],
    cancel_check: Callable[[], bool] | None = None,
) -> str:
    """
    Optional second pass: add (출처: …) only where a numbered line is clearly
    supported by a provided ``[Source: … | line …]`` tag; skip lines that disclaim
    KB/web evidence or lack grounding (see prompt rules).
    """
    if not draft or not source_tags:
        return draft
    if cancel_check and cancel_check():
        raise AgentRunCancelled()
    llm = get_chat_llm(model=effective_llm_model_main(), temperature=0.0)
    tags = "\n".join(f"- {t}" for t in source_tags)
    prompt = (
        "You are post-processing a draft email.\n"
        "Task: Add optional inline citations only where a numbered item (1., 2., 3., …) "
        "makes a factual claim that is clearly supported by one of the source tags below.\n"
        "Rules:\n"
        "- Do NOT rewrite the substantive wording; you may only append parenthetical citations.\n"
        "- Citation form when used: (출처: <tag>) or (출처: <tag1>; <tag2>). "
        "Use ONLY the provided source tags; copy exactly, including the full `| line <number>` segment.\n"
        "- If an item already has (출처: ...), keep it as-is.\n"
        "- **No false citations:** If a numbered line says documentation/KB/web found **no** relevant results, "
        "only recommends internal verification, or is clearly not grounded in the snippets below, "
        "leave that line **without** (출처: …).\n"
        "- If no tag below genuinely supports a numbered line, do **not** invent a citation for that line.\n"
        "- Keep the original language and formatting.\n"
        "\n"
        f"Available source tags:\n{tags}\n"
        "\n"
        f"Draft:\n{draft}\n"
        "\n"
        "Return the updated draft only."
    )
    if cancel_check and cancel_check():
        raise AgentRunCancelled()
    resp = llm.invoke([HumanMessage(content=prompt)])
    out = (resp.content or "").strip()
    return out or draft


@tool
def fetch_inbox_emails(search: str | None = None, max_results: int = 10) -> str:
    """Fetch Gmail threads using the server's default inbox search (Configure: probe Gmail query), or pass `search` to override."""
    from src.agent.tools.gmail_tool import fetch_inbox_emails as _fetch_emails
    return _fetch_emails(search=search, max_results=max_results)


@tool
def fetch_gmail_thread(thread_id: str) -> str:
    """Fetch the full Gmail thread (all messages) by Gmail thread id. Id appears as `thread_id` in fetch_inbox_emails output; use when discussing one dashboard action."""
    from src.agent.tools.gmail_tool import fetch_gmail_thread as _fetch_thread
    return _fetch_thread(thread_id)


@tool
def search_product_docs(query: str) -> str:
    """Search local product documentation (KB only) for relevant context."""
    from src.agent.tools.search_agent import search_with_agent_structured

    out, final_matches = search_with_agent_structured(query=query, max_context_chars=20000)
    out = (out or "").strip()

    # Enforce mode-specific explicit web follow-up as a separate tool call.
    try:
        has_enabled_rc = bool(database.list_rc_urls(limit=1, offset=0, enabled_only=True))
        mode = effective_rc_web_retrieval_mode()
        should_force_web_followup = (
            mode == "always_augment"
            and has_enabled_rc
        )
        should_gate_web_followup = (
            mode == "kb_first"
            and has_enabled_rc
            and bool(final_matches)
        )
    except Exception:
        should_force_web_followup = False
        should_gate_web_followup = False

    if should_force_web_followup:
        return (
            out.rstrip()
            + "\n\n[TOOL RULE] RC web retrieval mode is always_augment and enabled RC URLs exist. "
            "Before finalizing your answer, call tool `search_rc_web` with the same query."
        )
    if should_gate_web_followup:
        try:
            from src.agent.tools.kb_web_gate import evaluate_kb_web_gate

            proceed_web, reason = evaluate_kb_web_gate(query, final_matches)
            if proceed_web:
                reason_text = f" Reason: {reason}" if reason else ""
                return (
                    out.rstrip()
                    + "\n\n[TOOL RULE] RC web retrieval mode is kb_first and the KB→web gate decided web follow-up is needed."
                    + reason_text
                    + " Before finalizing your answer, call tool `search_rc_web` with the same query."
                )
        except Exception:
            # Fail-open in kb_first: if gate call fails, keep KB-only output.
            pass
    return out


@tool
def search_rc_web(query: str) -> str:
    """Search enabled RC URLs on the web for relevant context (with citations)."""
    from src.agent.tools.rc_web_search import search_rc_web as _search
    return _search(query=query)


@tool
def list_cron_jobs() -> str:
    """List cron jobs (name, expression, timezone, enabled). Use before editing/deleting when job name is uncertain."""
    jobs = database.get_cron_jobs()
    if not jobs:
        return "No cron jobs configured."
    lines = []
    for j in jobs:
        name = str(j.get("name") or "").strip() or "(unnamed)"
        expr = str(j.get("cron_expression") or "").strip() or "-"
        tz = str(j.get("timezone") or "").strip() or "Asia/Seoul"
        enabled = bool(j.get("enabled"))
        lines.append(f"- {name} | {expr} | {tz} | {'enabled' if enabled else 'disabled'}")
    return "\n".join(lines)


@tool
def upsert_cron_job(name: str, cron_expression: str, timezone: str = "Asia/Seoul") -> str:
    """Create or update a cron probe job. cron_expression must be 5 fields: minute hour day month weekday."""
    nm = (name or "").strip()
    expr = " ".join((cron_expression or "").split())
    tz = (timezone or "Asia/Seoul").strip() or "Asia/Seoul"
    if not nm:
        return "Error: name is required."
    parts = expr.split()
    if len(parts) != 5:
        return "Error: cron_expression must have 5 fields (minute hour day month weekday)."
    cron_manager.add_job(nm, expr, tz)
    return f"Saved cron job '{nm}' with schedule '{expr}' ({tz})."


@tool
def set_cron_job_enabled(name: str, enabled: bool) -> str:
    """Enable/disable one cron job by exact name."""
    nm = (name or "").strip()
    if not nm:
        return "Error: name is required."
    cron_manager.toggle_job(nm, bool(enabled))
    return f"Cron job '{nm}' is now {'enabled' if enabled else 'disabled'}."


@tool
def delete_cron_job(name: str) -> str:
    """Delete one cron job by exact name."""
    nm = (name or "").strip()
    if not nm:
        return "Error: name is required."
    cron_manager.remove_job(nm)
    return f"Deleted cron job '{nm}'."

def create_agent_executor(
    *,
    probe: bool = False,
    system_append: str | None = None,
):
    llm = _get_llm()
    tools = [
        fetch_inbox_emails,
        fetch_gmail_thread,
        search_product_docs,
        search_rc_web,
        list_cron_jobs,
        upsert_cron_job,
        set_cron_job_enabled,
        delete_cron_job,
    ]
    profile = database.get_agent_profile_settings()
    learning = database.get_runtime_learning_instructions()
    system_prompt = render_email_agent_system(
        vendor_name=profile["vendor_name"],
        product_context=profile["product_context"],
        role_title=profile["role_title"],
        learning_instructions=learning,
    )
    team_g = (effective_guardrail_team_guidance() or "").strip()
    if team_g:
        system_prompt = system_prompt.rstrip() + "\n\n## Team guidance (Configure)\n" + team_g
    if probe:
        system_prompt = system_prompt.rstrip() + "\n\n" + get_probe_mode_system_append()
    extra = (system_append or "").strip()
    if extra:
        system_prompt = system_prompt.rstrip() + "\n\n" + extra
    return create_agent(model=llm, tools=tools, system_prompt=system_prompt)


def run_agent(
    input_text: str,
    callbacks: Sequence | None = None,
    *,
    probe: bool = False,
    system_append: str | None = None,
    conversation_messages: list[dict] | None = None,
    thread_is_action_review: bool = False,
    cancel_check: Callable[[], bool] | None = None,
) -> str:
    _ensure_langsmith_env()
    with _langsmith_parent_trace(input_text=input_text, probe=probe):
        return _run_agent_impl(
            input_text=input_text,
            callbacks=callbacks,
            probe=probe,
            system_append=system_append,
            conversation_messages=conversation_messages,
            thread_is_action_review=thread_is_action_review,
            cancel_check=cancel_check,
        )


def _run_agent_impl(
    *,
    input_text: str,
    callbacks: Sequence | None,
    probe: bool,
    system_append: str | None,
    conversation_messages: list[dict] | None,
    thread_is_action_review: bool,
    cancel_check: Callable[[], bool] | None,
) -> str:

    # Deterministic cron-management fast path for Workbench chat.
    # This keeps create/adjust/delete behavior available even if prompt overrides are stale.
    if not probe and not thread_is_action_review:
        cron_reply = _maybe_handle_cron_request(
            input_text=input_text or "",
            conversation_messages=conversation_messages,
            callbacks=callbacks,
        )
        if cron_reply is not None:
            return cron_reply

    # Latest user utterance (for routing) when using thread history
    route_text = (input_text or "").strip()
    if conversation_messages and not probe:
        for row in reversed(conversation_messages):
            if (row.get("role") or "").strip().lower() == "user":
                c = row.get("content")
                if c is not None and str(c).strip():
                    route_text = str(c).strip()
                    break

    # If the user is just asking to see recent/latest emails, do that directly.
    # This avoids accidental doc retrieval + drafting on short inbox-peek queries (Korean/English/etc).
    # Action-review threads always run the full agent (fetch_gmail_thread, etc.).
    _peek = (not probe) and (_route_user_request(route_text, callbacks=callbacks) == "inbox_peek")
    _action_review = thread_is_action_review or (input_text or "").lstrip().startswith("[Action review")
    if _peek and not _action_review:
        from src.agent.tools.gmail_tool import fetch_inbox_emails as _fetch
        try:
            max_results = int(effective_user_inbox_peek_max_results())
        except Exception:
            max_results = 5
        if max_results < 1:
            max_results = 1
        if max_results > 100:
            max_results = 100
        # Emit trace events (tool_start/tool_end) so the UI Trace inspector stays useful.
        cbs = list(callbacks) if callbacks else []
        if cancel_check:
            cbs.append(_CancelPatrolCallback(cancel_check))
        for cb in cbs:
            try:
                cb.on_tool_start({"name": "fetch_inbox_emails"}, f"max_results={max_results} search=default")  # type: ignore[attr-defined]
            except AgentRunCancelled:
                raise
            except Exception:
                pass
        if cancel_check and cancel_check():
            raise AgentRunCancelled()
        out = _fetch(max_results=max_results)
        for cb in cbs:
            try:
                cb.on_tool_end(out)  # type: ignore[attr-defined]
            except AgentRunCancelled:
                raise
            except Exception:
                pass
        return out

    if probe:
        probe_limit = effective_probe_inbox_max_results()
        probe_gmail_q = effective_probe_inbox_gmail_search()
        probe_hint = (
            "**Probe JSON vs. UI language:** Workbench EN/KR is only for app chrome — it does **not** pick the language "
            "of `actions` text. After Gmail tools, each block ends with `csm_output_language` (**ko** or **inferred**) and a note. "
            "When the tag is **ko**, write **every** string field for that thread's action in **Korean** — no English dashboard prose. "
            "When **inferred**, choose language from the **customer's substantive email** (main ask / body), not from UI.\n"
            f"**Gmail slice:** When the tool omits `search`, the server uses this query: `{probe_gmail_q}`. "
            "Threads outside that slice never appear in `fetch_inbox_emails` (and `category:primary` hides other tabs). "
            "Widen `newer_than:` or drop `category:primary` in `search` if needed, or use `fetch_gmail_thread` when the id is known.\n"
            f"For `fetch_inbox_emails`, use max_results={probe_limit} unless the user explicitly asks otherwise.\n"
            "If any action is `product_technical`, you MUST call `search_product_docs` before final JSON. "
            "If docs are truly unavailable, keep `references` and `retrieval_evidence` empty rather than fabricating sources.\n"
            "Language: follow the inferred-language note per thread. Do not default to English for dashboard strings "
            "just because the latest reply is an internal English ping — read who actually asked for help and in which language."
        )
        if system_append and system_append.strip():
            system_append = system_append.rstrip() + "\n\n" + probe_hint
        else:
            system_append = probe_hint

    agent = create_agent_executor(probe=probe, system_append=system_append)
    cbs = list(callbacks) if callbacks else []
    if cancel_check:
        cbs.append(_CancelPatrolCallback(cancel_check))
    config = {"callbacks": cbs} if cbs else None
    if conversation_messages is not None and not probe:
        lc_messages = db_conversation_to_langchain(conversation_messages)
        if not lc_messages:
            lc_messages = [HumanMessage(content=input_text or "(no message)")]
        invoke_messages = lc_messages
    else:
        invoke_messages = [HumanMessage(content=input_text)]
    try:
        result = agent.invoke({"messages": invoke_messages}, config=config)
    except Exception as e:
        ex: BaseException | None = e
        while ex is not None:
            if isinstance(ex, AgentRunCancelled):
                raise ex
            ex = ex.__cause__
        raise
    messages = result.get("messages", [])
    draft = None
    for m in reversed(messages):
        if isinstance(m, AIMessage) and m.content:
            draft = _flatten_ai_content(m.content)
            break
    if not draft:
        return str(result)

    # Probe output should stay bullet-oriented; citation pass encourages formal numbered replies.
    if probe:
        collected = _collect_probe_assistant_output(messages)
        return collected if collected.strip() else draft

    # NotebookLM-style enforcement: ensure each numbered item has citations.
    if _draft_needs_citations(draft):
        source_tags = _extract_source_tags_from_messages(messages)
        if source_tags:
            draft = _add_citations_pass(
                draft=draft, source_tags=source_tags, cancel_check=cancel_check
            )
    return draft
