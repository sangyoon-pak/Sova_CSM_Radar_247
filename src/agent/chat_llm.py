"""Build ChatOpenAI instances (OpenAI-compatible: OpenRouter, OpenAI direct, etc.)."""

from langchain_openai import ChatOpenAI

from src.runtime_config import (
    effective_chat_api_key,
    effective_chat_base_url,
    effective_llm_model,
    effective_llm_provider_preset,
)


def get_chat_llm(*, model: str, temperature: float, extra_body: dict | None = None) -> ChatOpenAI:
    """Return a chat model for the given provider-specific model id."""
    resolved = (model or effective_llm_model()).strip()
    if not resolved:
        raise ValueError(
            "LLM model id is empty; set LLM_MODEL (or per-role override) in .env or Configure UI."
        )
    api_key = effective_chat_api_key()
    if not api_key:
        preset = effective_llm_provider_preset()
        if preset == "openai":
            raise ValueError(
                "Set OPENAI_API_KEY (or OPENROUTER_API_KEY) in .env or paste an API key in Configure."
            )
        raise ValueError("Set OPENROUTER_API_KEY in .env or paste an API key in Configure.")
    return ChatOpenAI(
        model=resolved,
        api_key=api_key,
        base_url=effective_chat_base_url(),
        temperature=temperature,
        extra_body=extra_body,
    )
