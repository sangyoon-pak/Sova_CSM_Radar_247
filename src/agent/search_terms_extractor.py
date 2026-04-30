"""LLM-based extraction of search terms from an email/query."""
import json
import re

from langchain_core.messages import HumanMessage, SystemMessage

from src.agent.chat_llm import get_chat_llm
from src.runtime_config import effective_llm_model_search_json


SYSTEM_PROMPT = """You analyze emails or user questions and extract search terms for document search.

Given an email body or question, output a JSON array of 3-8 search terms or short PHRASES that would help find relevant content in product documentation. Prefer 2-4 word phrases over single generic words.

Include:
- Product names if present in the question
- Technical terms (for example): API, SDK, integration, schema, authentication, webhook, troubleshooting
- Feature names, acronyms, or specific phrases from the question (e.g. "user schema formula", "create user schema")

Guidance:
- Prefer combinations of product + feature (e.g. "<product> user schema", "<product> event schema") when possible.
- Avoid generic single words like "work", "create", "how" by themselves.
- Expand shorthand only when unambiguous from context (e.g. a product acronym defined in the same message).
- If the query includes any of the following, ALWAYS include them as exact search terms:
  - URLs / endpoint paths (e.g. "/v1/events", "https://docs.example.com/api")
  - event or action names (e.g. "price_drop_event")
  - parameter / field names (e.g. "client_id", "identifier_value", "auth_token")
  - UI menu paths mentioned by the user (e.g. "Settings > Activity", "Trigger rule dropdown")

Output ONLY a valid JSON array of strings, e.g. ["product_x", "user schema formula", "create user schema"]. No other text."""


def _deterministic_fallback_terms(query: str, limit: int = 8) -> list[str]:
    """
    Deterministic extraction for robustness when LLM JSON parse fails.
    Same input -> same terms.
    """
    q = (query or "").strip()
    if not q:
        return []
    candidates: list[str] = []
    # Keep exact literals first.
    candidates.extend(re.findall(r"https?://\S+", q))
    candidates.extend(re.findall(r"/[A-Za-z0-9_./-]{2,}", q))
    candidates.extend(re.findall(r"\b[a-z][a-z0-9]+(?:_[a-z0-9]+)+\b", q))
    candidates.extend(re.findall(r"\b[A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)+\b", q))
    # Menu path style text.
    candidates.extend(re.findall(r"[A-Za-z가-힣][^:\n]{0,40}\s>\s[^:\n]{1,40}", q))
    # Upper acronyms / API-family tokens.
    candidates.extend(re.findall(r"\b[A-Z]{2,}[A-Z0-9_-]*\b", q))

    out: list[str] = []
    seen: set[str] = set()
    for raw in candidates:
        s = " ".join(str(raw).split()).strip(" ,.;:")
        if not s:
            continue
        lk = s.lower()
        if lk in seen:
            continue
        seen.add(lk)
        out.append(s)
        if len(out) >= limit:
            break
    return out


def extract_search_terms(query: str) -> list[str]:
    llm = get_chat_llm(model=effective_llm_model_search_json(), temperature=0)
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
            cleaned = [" ".join(str(t).split()).strip() for t in terms if str(t).strip()]
            dedup: list[str] = []
            seen: set[str] = set()
            for t in cleaned:
                lk = t.lower()
                if lk in seen:
                    continue
                seen.add(lk)
                dedup.append(t)
            if dedup:
                return dedup[:8]
    except json.JSONDecodeError:
        pass
    return _deterministic_fallback_terms(query, limit=8)
