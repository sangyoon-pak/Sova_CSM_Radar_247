"""Local email draft agent using LangChain."""
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import AIMessage, HumanMessage
from langchain.agents import create_agent

from src.config import settings
from src.agent.prompts import EMAIL_AGENT_SYSTEM
from src.agent.search_terms_extractor import extract_search_terms


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
    from src.agent.tools.doc_search import search_documents as _search, format_matches_for_context
    matches = _search(query=query, search_terms=None, llm_extract=extract_search_terms, max_results_per_term=10)
    return format_matches_for_context(matches)


def create_agent_executor():
    llm = _get_llm()
    tools = [fetch_inbox_emails, search_appier_docs]
    system_prompt = EMAIL_AGENT_SYSTEM.format(client_domains=", ".join(settings.allowlist))
    return create_agent(model=llm, tools=tools, system_prompt=system_prompt)


def run_agent(input_text: str) -> str:
    agent = create_agent_executor()
    result = agent.invoke({"messages": [HumanMessage(content=input_text)]})
    messages = result.get("messages", [])
    for m in reversed(messages):
        if isinstance(m, AIMessage) and m.content:
            return str(m.content)
    return str(result)
