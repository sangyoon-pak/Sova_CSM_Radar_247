"""Local email draft agent using LangChain."""
import os
from collections.abc import Sequence

from langchain_core.tools import tool
from langchain_core.messages import AIMessage, HumanMessage
from langchain.agents import create_agent

from src.agent.chat_llm import get_chat_llm
from src.config import settings
from src.agent.prompts import EMAIL_AGENT_SYSTEM


def _ensure_langsmith_env():
    """Set LangSmith env vars from settings so tracing works in uvicorn workers."""
    if settings.langsmith_api_key:
        os.environ["LANGSMITH_TRACING"] = "true"
        os.environ["LANGSMITH_API_KEY"] = settings.langsmith_api_key
        os.environ["LANGSMITH_PROJECT"] = settings.langsmith_project


def _get_llm():
    return get_chat_llm(model=settings.llm_model_for_main, temperature=0.3)


@tool
def fetch_inbox_emails(search: str = "in:inbox category:primary newer_than:2d", max_results: int = 10) -> str:
    """Fetch recent emails from Gmail Primary inbox. Use for probing new messages."""
    from src.agent.tools.gmail_tool import fetch_inbox_emails as _fetch_emails
    return _fetch_emails(search=search, max_results=max_results)


@tool
def search_appier_docs(query: str) -> str:
    """Search Appier documentation for relevant context. Use when the email asks about Appier products (AIRIS, AIQUA, BotBonnie, etc.)."""
    from src.agent.tools.search_agent import search_with_agent
    return search_with_agent(query=query, max_context_chars=20000)


def create_agent_executor():
    llm = _get_llm()
    tools = [fetch_inbox_emails, search_appier_docs]
    system_prompt = EMAIL_AGENT_SYSTEM
    return create_agent(model=llm, tools=tools, system_prompt=system_prompt)


def run_agent(input_text: str, callbacks: Sequence | None = None) -> str:
    _ensure_langsmith_env()
    agent = create_agent_executor()
    config = {"callbacks": list(callbacks)} if callbacks else None
    result = agent.invoke({"messages": [HumanMessage(content=input_text)]}, config=config)
    messages = result.get("messages", [])
    for m in reversed(messages):
        if isinstance(m, AIMessage) and m.content:
            return str(m.content)
    return str(result)
