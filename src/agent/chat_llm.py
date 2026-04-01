"""Build ChatOpenAI instances from settings (OpenRouter-only)."""

from langchain_openai import ChatOpenAI

from src.config import settings


def get_chat_llm(*, model: str, temperature: float, extra_body: dict | None = None) -> ChatOpenAI:
    """Return a chat model for the given OpenRouter model id."""
    resolved = (model or settings.llm_model).strip()
    if not resolved:
        raise ValueError("LLM model id is empty; set LLM_MODEL or a role-specific LLM_MODEL_* in .env")
    if not settings.openrouter_api_key:
        raise ValueError("Set OPENROUTER_API_KEY in .env")
    return ChatOpenAI(
        model=resolved,
        api_key=settings.openrouter_api_key,
        base_url=settings.openrouter_base_url,
        temperature=temperature,
        extra_body=extra_body,
    )
