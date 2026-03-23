"""
Search Agent: re-ranks results, checks sufficiency, optionally refines and re-searches.
Wraps doc_search with a "brain" for smarter retrieval.
"""
import json

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from src.config import settings
from src.agent.tools.doc_search import search_documents, format_matches_for_context
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
            temperature=0,
        )
    return ChatOpenAI(
        model=settings.llm_model,
        api_key=settings.openai_api_key,
        temperature=0,
    )


RERANK_PROMPT = """You score how relevant and actionable each document snippet is to the user's question.

Question: {query}

For each snippet, output a relevance score 1-5:
- 5: Directly answers the question
- 4: Highly relevant, strong overlap
- 3: Somewhat relevant
- 2: Tangentially related
- 1: Not relevant

Scoring guidance:
- Prefer snippets containing concrete implementation steps (e.g. "go to", "click", "configure", "SDK", "web", "JavaScript", "API").
- Penalize metadata-only snippets (keywords/frontmatter) even if product names match.

Output a JSON object: {{ "scores": [5, 3, 1, ...] }} with one score per snippet, in the same order.
Snippets are numbered 1 to N. Output ONLY the JSON object."""

SUFFICIENCY_PROMPT = """Given the user's question and the retrieved document snippets, is there enough relevant information to answer the question?

Question: {query}

Snippets (truncated): {snippet_preview}

Answer with a JSON object: {{ "sufficient": true/false, "reason": "brief reason" }}
Rules:
- Set sufficient=true only if the snippets include actionable/helpful content (instructions, steps, configuration details, or relevant technical context).
- If snippets are mostly metadata/keywords or don't include actual integration/how-to details, set sufficient=false.
- If most snippets are irrelevant (wrong product, wrong topic), set sufficient=false.
Output ONLY the JSON object."""

REFINE_PROMPT = """The initial search did not find enough relevant content. Refine and propose alternative search terms.

Original question: {query}
Reason insufficient: {reason}

Output a JSON object with 2-3 alternative term lists:
{{
  "variants": [
    {{ "terms": ["phrase1", "phrase2", "..."] }},
    {{ "terms": ["alt phrase1", "alt phrase2", "..."] }}
  ]
}}

- Use 2-4 word PHRASES (e.g. "user schema formula", "create user schema") not single generic words
- Include the main product name (AIRIS, AIQUA, etc.) if the question is product-specific
- Avoid generic terms like "work", "create", "how" alone
- Each variant should output 3-5 terms.
- Prefer including at least one variant that is more "how-to/actionable" (contains verbs like configure/install/integrate/click/set) and one variant that is more "entity-focused" (product + feature name).
- Output ONLY the JSON object."""


def _rerank_matches(query: str, matches: list[dict], threshold: int = 3) -> list[dict]:
    """Score each match 1-5, filter by threshold."""
    if not matches:
        return []
    llm = _get_llm()
    # Build snippet list for prompt (truncate long lines)
    snippets = []
    for m in matches:
        text = (m.get("snippet") or m.get("line", ""))[:500]
        snippets.append(f"[{m['file']} L{m['line_num']}] {text}")
    snippet_text = "\n".join(f"{i+1}. {s}" for i, s in enumerate(snippets))
    prompt = RERANK_PROMPT.format(query=query) + "\n\nSnippets:\n" + snippet_text
    response = llm.invoke([HumanMessage(content=prompt)])
    text = response.content.strip()
    if "```" in text:
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    text = text.strip()
    try:
        data = json.loads(text)
        scores = data.get("scores", [])
    except json.JSONDecodeError:
        return matches[:15]  # Fallback: keep first 15
    if len(scores) != len(matches):
        return matches[:15]
    scored = [(m, scores[i] if i < len(scores) else 1) for i, m in enumerate(matches)]
    filtered = [(m, s) for m, s in scored if s >= threshold]
    filtered.sort(key=lambda x: (-x[1], x[0]["file"], x[0]["line_num"]))
    result = [m for m, s in filtered]
    return result if result else [m for m, s in scored if s >= 2][:15]


def _check_sufficient(query: str, matches: list[dict]) -> tuple[bool, str]:
    """LLM decides if results are sufficient."""
    if not matches:
        return False, "No matches found"
    llm = _get_llm()
    preview = "\n".join((m.get("snippet") or m.get("line", ""))[:300] for m in matches[:10])
    prompt = SUFFICIENCY_PROMPT.format(query=query, snippet_preview=preview[:1500])
    response = llm.invoke([HumanMessage(content=prompt)])
    text = response.content.strip()
    if "```" in text:
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    try:
        data = json.loads(text.strip())
        return bool(data.get("sufficient", False)), str(data.get("reason", ""))
    except json.JSONDecodeError:
        return True, "Could not parse"  # Assume sufficient to avoid loop


def _refine_search_terms(query: str, reason: str) -> list[list[str]]:
    """LLM produces alternative term variants for a follow-up grep pass."""
    llm = _get_llm()
    prompt = REFINE_PROMPT.format(query=query, reason=reason)
    response = llm.invoke([HumanMessage(content=prompt)])
    text = response.content.strip()
    if "```" in text:
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    try:
        data = json.loads(text.strip())
        variants = data.get("variants", [])
        out: list[list[str]] = []
        for v in variants:
            terms = v.get("terms", [])
            cleaned = [str(t) for t in terms if t]
            if cleaned:
                out.append(cleaned)
        return out
    except json.JSONDecodeError:
        return []


def search_with_agent(
    query: str,
    max_iterations: int = 2,
    rerank_threshold: int = 3,
    max_context_chars: int = 8000,
) -> str:
    """
    Orchestrated search: grep → re-rank → sufficiency check → optional refined search.
    Returns formatted context for the main agent.
    """
    all_matches: list[dict] = []
    seen = set()

    for iteration in range(max_iterations):
        if iteration == 0:
            terms_variants = [extract_search_terms(query)]
        else:
            sufficient, reason = _check_sufficient(query, all_matches)
            if sufficient:
                break
            terms_variants = _refine_search_terms(query, reason)
            if not terms_variants:
                break

        matches: list[dict] = []
        for terms in terms_variants:
            if not terms:
                continue
            found = search_documents(
                query=query,
                search_terms=terms,
                llm_extract=None,
                max_results_per_term=10,
            )
            matches.extend(found)

        for m in matches:
            key = (m["file"], m["line_num"])
            if key not in seen:
                seen.add(key)
                all_matches.append(m)

        if not matches:
            break

        # Re-rank and filter
        all_matches = _rerank_matches(query, all_matches, threshold=rerank_threshold)
        if not all_matches:
            all_matches = matches[:15]  # Fallback

    return format_matches_for_context(all_matches, max_chars=max_context_chars)
