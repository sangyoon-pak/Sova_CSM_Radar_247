"""LLM-based extraction of search terms from an email/query."""
import json

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from src.config import settings


SYSTEM_PROMPT = """You analyze emails or questions about Appier products and extract search terms for document search.

Given an email body or question, output a JSON array of 3-8 search terms or short PHRASES that would help find relevant content in Appier documentation. Prefer 2-4 word phrases over single generic words.

Include:
- Product names: AIRIS, AIQUA, BotBonnie, AI Agent, AIXON, AiDeal
- Technical terms: API, SDK, integration, data warehouse, recommendation
- Feature names, acronyms, or specific phrases from the question (e.g. "user schema formula", "create user schema", "AIRIS formula")

Output ONLY a valid JSON array of strings, e.g. ["AIRIS", "user schema formula", "create user schema"]. No other text."""


def get_extractor_llm():
    api_key = settings.openrouter_api_key or settings.openai_api_key
    if not api_key:
        raise ValueError("Set OPENAI_API_KEY or OPENROUTER_API_KEY in .env")
    if settings.openrouter_api_key:
        return ChatOpenAI(
            model=settings.llm_model,
            api_key=settings.openrouter_api_key,
            base_url=settings.openrouter_base_url,
            temperature=0,
        )
    return ChatOpenAI(
        model=settings.llm_model,
        api_key=settings.openai_api_key,
        temperature=0,
    )


def extract_search_terms(query: str) -> list[str]:
    llm = get_extractor_llm()
    msg = HumanMessage(content=query[:2000])
    response = llm.invoke([SystemMessage(content=SYSTEM_PROMPT), msg])
    text = response.content.strip()
    if "```" in text:
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    text = text.strip()
    try:
        terms = json.loads(text)
        if isinstance(terms, list):
            return [str(t) for t in terms if t]
    except json.JSONDecodeError:
        pass
    return []
