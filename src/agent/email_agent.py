"""Local email draft agent using LangChain."""
import os
import re
import json
from collections.abc import Sequence

from langchain_core.tools import tool
from langchain_core.messages import AIMessage, HumanMessage
from langchain.agents import create_agent

from src.agent.chat_llm import get_chat_llm
from src.config import settings
from src.agent.prompts import render_email_agent_system
from src.db import database


def _ensure_langsmith_env():
    """Set LangSmith env vars from settings so tracing works in uvicorn workers."""
    if settings.langsmith_api_key:
        os.environ["LANGSMITH_TRACING"] = "true"
        os.environ["LANGSMITH_API_KEY"] = settings.langsmith_api_key
        os.environ["LANGSMITH_PROJECT"] = settings.langsmith_project


def _get_llm():
    return get_chat_llm(model=settings.llm_model_for_main, temperature=0.3)

def _llm_intent_router():
    # Deterministic classifier for UX routing (language-agnostic).
    return get_chat_llm(model=settings.llm_model_for_search_json, temperature=0.0)


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
            tag = f"[Source: {match.group(1)} | line ...]"
            if tag.lower() in seen:
                continue
            seen.add(tag.lower())
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


def _add_citations_pass(*, draft: str, source_tags: list[str]) -> str:
    """
    Second-pass enforcement: append citations to each numbered item.
    """
    if not draft or not source_tags:
        return draft
    llm = get_chat_llm(model=settings.llm_model_for_main, temperature=0.0)
    tags = "\n".join(f"- {t}" for t in source_tags)
    prompt = (
        "You are post-processing a draft email.\n"
        "Task: Add citations to EVERY numbered answer item (1., 2., 3., ...).\n"
        "Rules:\n"
        "- Do NOT rewrite the content beyond adding citations.\n"
        "- For each numbered item, append exactly one parenthetical at the end: (출처: <tag>) or (출처: <tag1>; <tag2>).\n"
        "- Use ONLY the provided source tags. Copy them exactly.\n"
        "- If an item already has (출처: ...), keep it as-is.\n"
        "- Keep the original language and formatting.\n"
        "\n"
        f"Available source tags:\n{tags}\n"
        "\n"
        f"Draft:\n{draft}\n"
        "\n"
        "Return the updated draft only."
    )
    resp = llm.invoke([HumanMessage(content=prompt)])
    out = (resp.content or "").strip()
    return out or draft


@tool
def fetch_inbox_emails(search: str = "in:inbox category:primary newer_than:2d", max_results: int = 10) -> str:
    """Fetch recent emails from Gmail Primary inbox. Use for probing new messages."""
    from src.agent.tools.gmail_tool import fetch_inbox_emails as _fetch_emails
    return _fetch_emails(search=search, max_results=max_results)


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

def create_agent_executor():
    llm = _get_llm()
    tools = [fetch_inbox_emails, search_product_docs, search_rc_web]
    profile = database.get_agent_profile_settings()
    learning = database.get_runtime_learning_instructions()
    system_prompt = render_email_agent_system(
        vendor_name=profile["vendor_name"],
        product_context=profile["product_context"],
        role_title=profile["role_title"],
        learning_instructions=learning,
    )
    return create_agent(model=llm, tools=tools, system_prompt=system_prompt)


def run_agent(
    input_text: str,
    callbacks: Sequence | None = None,
) -> str:
    _ensure_langsmith_env()

    # If the user is just asking to see recent/latest emails, do that directly.
    # This avoids accidental doc retrieval + drafting on short inbox-peek queries (Korean/English/etc).
    if _route_user_request(input_text) == "inbox_peek":
        from src.agent.tools.gmail_tool import fetch_inbox_emails as _fetch
        # Emit trace events (tool_start/tool_end) so the UI Trace inspector stays useful.
        cbs = list(callbacks) if callbacks else []
        for cb in cbs:
            try:
                cb.on_tool_start({"name": "fetch_inbox_emails"}, f"max_results=5 search=default")  # type: ignore[attr-defined]
            except Exception:
                pass
        out = _fetch(max_results=5)
        for cb in cbs:
            try:
                cb.on_tool_end(out)  # type: ignore[attr-defined]
            except Exception:
                pass
        return out

    agent = create_agent_executor()
    config = {"callbacks": list(callbacks)} if callbacks else None
    result = agent.invoke({"messages": [HumanMessage(content=input_text)]}, config=config)
    messages = result.get("messages", [])
    draft = None
    for m in reversed(messages):
        if isinstance(m, AIMessage) and m.content:
            draft = str(m.content)
            break
    if not draft:
        return str(result)

    # NotebookLM-style enforcement: ensure each numbered item has citations.
    if _draft_needs_citations(draft):
        source_tags = _extract_source_tags_from_messages(messages)
        if source_tags:
            draft = _add_citations_pass(draft=draft, source_tags=source_tags)
    return draft
