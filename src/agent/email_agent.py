"""Proactive CSM assistant (LangChain): inbox triage, KB tools, drafts on explicit request."""
import os
import re
import json
from collections.abc import Callable, Sequence

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.tools import tool
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain.agents import create_agent

from src.agent.chat_llm import get_chat_llm
from src.config import settings
from src.runtime_config import (
    effective_guardrail_team_guidance,
    effective_llm_model_main,
    effective_llm_model_search_json,
)
from src.agent.prompts import (
    get_probe_mode_system_append,
    render_email_agent_system,
)
from src.db import database


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
    """Set LangSmith env vars from settings so tracing works in uvicorn workers."""
    if settings.langsmith_api_key:
        os.environ["LANGSMITH_TRACING"] = "true"
        os.environ["LANGSMITH_API_KEY"] = settings.langsmith_api_key
        os.environ["LANGSMITH_PROJECT"] = settings.langsmith_project


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


def _route_user_request(text: str) -> str:
    t = (text or "").strip()
    if not t:
        return "agent_run"
    llm = _llm_intent_router()
    prompt = INTENT_ROUTE_PROMPT.format(text=t[:2000])
    try:
        resp = llm.invoke([HumanMessage(content=prompt)], config={"run_name": "email_agent.route_intent"})
        raw = (resp.content or "").strip()
        if "```" in raw:
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        data = json.loads(raw.strip())
        route = str(data.get("route") or "").strip()
        if route in ("inbox_peek", "agent_run"):
            return route
    except Exception:
        pass
    return "agent_run"

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
    Second-pass enforcement: append citations to each numbered item.
    """
    if not draft or not source_tags:
        return draft
    if cancel_check and cancel_check():
        raise AgentRunCancelled()
    llm = get_chat_llm(model=effective_llm_model_main(), temperature=0.0)
    tags = "\n".join(f"- {t}" for t in source_tags)
    prompt = (
        "You are post-processing a draft email.\n"
        "Task: Add citations to EVERY numbered answer item (1., 2., 3., ...).\n"
        "Rules:\n"
        "- Do NOT rewrite the content beyond adding citations.\n"
        "- For each numbered item, append exactly one parenthetical at the end: (출처: <tag>) or (출처: <tag1>; <tag2>).\n"
        "- Use ONLY the provided source tags. Copy them exactly, including the full `| line <number>` part—never shorten to `line ...`.\n"
        "- If an item already has (출처: ...), keep it as-is.\n"
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
def fetch_inbox_emails(search: str = "in:inbox category:primary newer_than:2d", max_results: int = 10) -> str:
    """Fetch recent emails from Gmail Primary inbox. Use for probing new messages."""
    from src.agent.tools.gmail_tool import fetch_inbox_emails as _fetch_emails
    return _fetch_emails(search=search, max_results=max_results)


@tool
def fetch_gmail_thread(thread_id: str) -> str:
    """Fetch the full Gmail thread (all messages) by Gmail thread id. Id appears as `thread_id` in fetch_inbox_emails output; use when discussing one dashboard action."""
    from src.agent.tools.gmail_tool import fetch_gmail_thread as _fetch_thread
    return _fetch_thread(thread_id)


@tool
def search_product_docs(query: str) -> str:
    """Search product documentation for relevant context."""
    from src.agent.tools.search_agent import search_with_agent
    return search_with_agent(query=query, max_context_chars=20000)


@tool
def search_rc_web(query: str) -> str:
    """Search enabled RC URLs on the web for relevant context (with citations)."""
    from src.agent.tools.rc_web_search import search_rc_web as _search
    return _search(query=query)

def create_agent_executor(
    *,
    probe: bool = False,
    system_append: str | None = None,
):
    llm = _get_llm()
    tools = [fetch_inbox_emails, fetch_gmail_thread, search_product_docs, search_rc_web]
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
    _peek = _route_user_request(route_text) == "inbox_peek"
    _action_review = thread_is_action_review or (input_text or "").lstrip().startswith("[Action review")
    if _peek and not _action_review:
        from src.agent.tools.gmail_tool import fetch_inbox_emails as _fetch
        # Emit trace events (tool_start/tool_end) so the UI Trace inspector stays useful.
        cbs = list(callbacks) if callbacks else []
        if cancel_check:
            cbs.append(_CancelPatrolCallback(cancel_check))
        for cb in cbs:
            try:
                cb.on_tool_start({"name": "fetch_inbox_emails"}, f"max_results=5 search=default")  # type: ignore[attr-defined]
            except AgentRunCancelled:
                raise
            except Exception:
                pass
        if cancel_check and cancel_check():
            raise AgentRunCancelled()
        out = _fetch(max_results=5)
        for cb in cbs:
            try:
                cb.on_tool_end(out)  # type: ignore[attr-defined]
            except AgentRunCancelled:
                raise
            except Exception:
                pass
        return out

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
