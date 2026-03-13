"""Local email draft agent using LangChain."""
import os

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import AIMessage, HumanMessage
from langchain.agents import create_agent

from src.config import settings
from src.agent.prompts import EMAIL_AGENT_SYSTEM


def _ensure_langsmith_env():
    """Set LangSmith env vars from settings so tracing works in uvicorn workers."""
    if settings.langsmith_api_key:
        os.environ["LANGSMITH_TRACING"] = "true"
        os.environ["LANGSMITH_API_KEY"] = settings.langsmith_api_key
        os.environ["LANGSMITH_PROJECT"] = settings.langsmith_project


def _get_llm():
    api_key = settings.openrouter_api_key or settings.openai_api_key
    if not api_key:
        raise ValueError("Set OPENAI_API_KEY or OPENROUTER_API_KEY in .env")
    if settings.openrouter_api_key:
        return ChatOpenAI(
            model=settings.llm_model,
            api_key=settings.openrouter_api_key,
            base_url=settings.openrouter_base_url,
            temperature=0.3,
        )
    return ChatOpenAI(
        model=settings.llm_model,
        api_key=settings.openai_api_key,
        temperature=0.3,
    )


@tool
def fetch_inbox_emails(search: str = "in:inbox category:primary newer_than:2d", max_results: int = 10) -> str:
    """Fetch recent emails from Gmail Primary inbox. Use for probing new messages."""
    from src.agent.tools.gmail_tool import fetch_inbox_emails as _fetch_emails
    return _fetch_emails(search=search, max_results=max_results)


@tool
def search_appier_docs(query: str) -> str:
    """Search Appier documentation for relevant context. Use when the email asks about Appier products (AIRIS, AIQUA, BotBonnie, etc.)."""
    from src.agent.tools.search_agent import search_with_agent
    return search_with_agent(query=query, max_context_chars=8000)


def create_agent_executor():
    llm = _get_llm()
    tools = [fetch_inbox_emails, search_appier_docs]
    system_prompt = EMAIL_AGENT_SYSTEM
    return create_agent(model=llm, tools=tools, system_prompt=system_prompt)


def run_agent(input_text: str) -> str:
    _ensure_langsmith_env()
    agent = create_agent_executor()
    result = agent.invoke({"messages": [HumanMessage(content=input_text)]})
    messages = result.get("messages", [])
    for m in reversed(messages):
        if isinstance(m, AIMessage) and m.content:
            return str(m.content)
    return str(result)
