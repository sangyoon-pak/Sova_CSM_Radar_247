"""
Search Agent: re-ranks results, checks sufficiency, optionally refines and re-searches.
Wraps doc_search with a "brain" for smarter retrieval.
"""
import copy
import json
import re

from langchain_core.messages import HumanMessage

from src.agent.chat_llm import get_chat_llm
from src.config import settings
from src.runtime_config import effective_llm_model_search_json, effective_llm_model_search_rerank
from src.agent.tools.doc_search import (
    _single_scope_exclusive_query,
    _extract_product_hints,
    format_matches_for_context,
    search_documents,
)
from src.agent.search_terms_extractor import extract_search_terms

# Set by enable_retrieval_logging(); each search_with_agent call appends one record.
# Off by default so production / API runs are unchanged.
_retrieval_log: list[dict] | None = None


def enable_retrieval_logging() -> None:
    """Start capturing search_with_agent results (query, matches, context string to the LLM)."""
    global _retrieval_log
    _retrieval_log = []


def take_retrieval_log() -> list[dict]:
    """Return captured records and stop capturing."""
    global _retrieval_log
    out = list(_retrieval_log or [])
    _retrieval_log = None
    return out


def _split_focus_subqueries(query: str) -> list[str]:
    """
    Split a long inquiry into focus questions.

    Primary path: ask the LLM to interpret and split (language/format agnostic).
    Fallback path: use lightweight regex heuristics when LLM output is unavailable.
    """
    text = (query or "").strip()
    if not text:
        return []

    # LLM-based split (preferred). If anything goes wrong, we fall back to heuristics.
    try:
        llm = _llm_search_json()
        prompt = (
            "Split the following customer inquiry into up to 6 focused sub-questions to improve document retrieval.\n"
            "Rules:\n"
            "- Be language-agnostic and format-agnostic (do not rely on specific headings/keywords).\n"
            "- Preserve the original language of each sub-question.\n"
            "- If the inquiry already contains numbered questions, keep each numbered item as a separate sub-question.\n"
            "- If it's a single coherent question, return a single-item list.\n"
            "- Return STRICT JSON only (no markdown, no prose): {\"subqueries\": [\"...\", ...]}\n"
            "\n"
            f"Inquiry:\n{text}\n"
        )
        response = llm.invoke(
            [HumanMessage(content=prompt)],
            config={
                "run_name": "search_agent.split_focus_subqueries",
                "tags": ["search_agent", "subquery_split"],
                "metadata": {"max_subqueries": 6},
            },
        )
        raw = (response.content or "").strip()
        if "```" in raw:
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        data = json.loads(raw.strip())
        subqueries = data.get("subqueries", [])
        cleaned: list[str] = []
        for sq in subqueries:
            s = " ".join(str(sq).split()).strip()
            if not s:
                continue
            if s.lower() in {c.lower() for c in cleaned}:
                continue
            cleaned.append(s)
        if cleaned:
            return cleaned[:6]
    except Exception:
        pass

    # Fallback: sentence split
    sentences = [s.strip() for s in re.split(r"(?<=[?.!])\s+", text.replace("\n", " ")) if s.strip()]
    return sentences[:6]


def _extract_hard_terms(query: str) -> list[str]:
    """
    Extract exact tokens likely to appear verbatim in docs:
    URLs, endpoint paths, event names, and common field names.
    """
    hard: list[str] = []
    # URLs
    hard.extend(re.findall(r"https?://\\S+", query))
    # Endpoint-like paths
    # Put '-' at end of class to avoid range parsing issues.
    hard.extend(re.findall(r"/[A-Za-z0-9_./\\-]+/?", query))
    # snake_case tokens (event names, params)
    hard.extend(re.findall(r"\\b[a-z]+(?:_[a-z0-9]+){1,}\\b", query))
    # Common auth/fields
    for token in ["appId", "appSecret", "identifier", "identifier_value", "user_id", "device"]:
        if token in query:
            hard.append(token)
    # Dedup preserve order
    seen: set[str] = set()
    out: list[str] = []
    for t in hard:
        k = t.strip()
        if not k:
            continue
        lk = k.lower()
        if lk in seen:
            continue
        seen.add(lk)
        out.append(k)
    return out[:12]


def _llm_search_json():
    """LLM for structured JSON outputs: subquery split, sufficiency, refine."""
    return get_chat_llm(model=effective_llm_model_search_json(), temperature=0)


def _llm_search_rerank():
    """LLM for snippet scoring (rerank)."""
    return get_chat_llm(model=effective_llm_model_search_rerank(), temperature=0)


def _doc_key(m: dict) -> str:
    meta = m.get("meta") or {}
    url = str(meta.get("url") or m.get("url") or "").strip().lower()
    if url:
        return f"url:{url}"
    path = str(m.get("path") or "").strip().lower()
    if path:
        return f"path:{path}"
    return f"file:{str(m.get('file') or '').strip().lower()}"


def _distinct_doc_count(matches: list[dict]) -> int:
    if not matches:
        return 0
    return len({_doc_key(m) for m in matches})


def _diversify_matches(matches: list[dict], max_per_doc: int = 4, keep_limit: int = 30) -> list[dict]:
    """
    Keep ranking signal, but avoid context being dominated by one document.
    Round-robin across docs while capping per-doc entries.
    """
    if not matches:
        return []
    buckets: dict[str, list[dict]] = {}
    order: list[str] = []
    for m in matches:
        k = _doc_key(m)
        if k not in buckets:
            buckets[k] = []
            order.append(k)
        if len(buckets[k]) < max_per_doc:
            buckets[k].append(m)
    out: list[dict] = []
    while len(out) < keep_limit:
        advanced = False
        for k in order:
            if buckets[k]:
                out.append(buckets[k].pop(0))
                advanced = True
                if len(out) >= keep_limit:
                    break
        if not advanced:
            break
    return out


def _augment_with_unseen_docs(primary: list[dict], fallback_pool: list[dict], target_docs: int = 3) -> list[dict]:
    """
    If rerank becomes too single-source, inject top candidates from unseen docs.
    """
    out = list(primary)
    seen_docs = {_doc_key(m) for m in out}
    if len(seen_docs) >= target_docs:
        return out
    for m in fallback_pool:
        k = _doc_key(m)
        if k in seen_docs:
            continue
        out.append(m)
        seen_docs.add(k)
        if len(seen_docs) >= target_docs:
            break
    return out


SCOPE_INFER_PROMPT = """You infer which documentation scope(s) a customer inquiry belongs to.

You will be given:
- a list of allowed scope labels
- the inquiry text

Return STRICT JSON ONLY (no markdown, no prose):
{{
  "scopes": ["label1", "label2"],   // 0-3 items, from allowed labels only
  "primary": "label1" | null,       // one of scopes, or null if ambiguous
  "confidence": 0.0                 // 0.0-1.0 confidence that primary is correct and the inquiry is mostly about that scope
}}

Rules:
- Be language-agnostic (the inquiry may be Korean/English/etc.).
- If the inquiry clearly concerns a single product/scope, output one scope and high confidence (>= 0.8).
- If the inquiry spans multiple scopes, output multiple scopes and lower confidence (<= 0.7).
- If you cannot determine, output empty scopes, primary null, confidence 0.0.

Allowed labels: {labels}
Inquiry:
{query}
"""


def _infer_scope(query: str) -> tuple[set[str], str | None]:
    """
    Infer likely scope labels and an optional exclusive scope for routing.

    Returns:
    - scope_hints: set of labels (may be empty)
    - exclusive_scope: a single label when confident and unambiguous, else None
    """
    if not settings.rc_scope_enable:
        return set(), None
    labels = [x.strip() for x in (settings.rc_scope_labels or "").split(",") if x.strip()]
    if not labels:
        return set(), None

    llm = _llm_search_json()
    prompt = SCOPE_INFER_PROMPT.format(labels=", ".join(labels), query=(query or "").strip()[:6000])
    try:
        resp = llm.invoke(
            [HumanMessage(content=prompt)],
            config={"run_name": "search_agent.infer_scope", "tags": ["search_agent", "scope_infer"]},
        )
        raw = (resp.content or "").strip()
        if "```" in raw:
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        data = json.loads(raw.strip())
        scopes = {str(s).strip().lower() for s in (data.get("scopes") or []) if str(s).strip()}
        scopes = {s for s in scopes if s in {l.strip().lower() for l in labels}}
        primary = data.get("primary")
        primary_s = str(primary).strip().lower() if primary else None
        if primary_s and primary_s not in scopes:
            primary_s = None
        conf = float(data.get("confidence", 0.0) or 0.0)
        exclusive = None
        if primary_s and conf >= float(settings.rc_scope_exclusive_threshold or 0.75) and len(scopes) <= 1:
            exclusive = primary_s
        return scopes, exclusive
    except Exception:
        return set(), None


RERANK_PROMPT = """You score how relevant and actionable each document snippet is to the user's question.

{product_scope}
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
- If the question is clearly scoped to a specific category/scope (see Product scope above), strongly penalize snippets from other categories/scopes unless the snippet alone directly answers the same behavior the user asked about.
- Prefer snippets that contain exact technical entities from the question (endpoint paths, event names, parameter names).

Output a JSON object: {{ "scores": [5, 3, 1, ...] }} with one score per snippet, in the same order.
Snippets are numbered 1 to N. Output ONLY the JSON object."""

SUFFICIENCY_PROMPT = """Given the user's question and the retrieved document snippets, is there enough relevant information to answer the question?

Question: {query}

Snippets (truncated): {snippet_preview}

Answer with a JSON object: {{ "sufficient": true/false, "reason": "brief reason" }}
Rules:
- Set sufficient=true only if the snippets include actionable/helpful content (instructions, steps, configuration details, or relevant technical context).
- If snippets are mostly metadata/keywords or don't include actual integration/how-to details, set sufficient=false.
- If most snippets are irrelevant (wrong topic/category), or are from the wrong scope line for the question when the user clearly scoped the question, set sufficient=false.
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
- Include the main category/scope label if the question is category-specific
- Avoid generic terms like "work", "create", "how" alone
- Each variant should output 3-5 terms.
- Prefer including at least one variant that is more "how-to/actionable" (contains verbs like configure/install/integrate/click/set) and one variant that is more "entity-focused" (product + feature name).
- Output ONLY the JSON object."""


def _rerank_product_scope_note(query: str, exclusive_scope: str | None = None) -> str:
    if exclusive_scope:
        exclusive = exclusive_scope
    else:
        hints = _extract_product_hints(query)
        if not _single_scope_exclusive_query(hints):
            return ""
        exclusive = next(iter(hints))
    if not exclusive:
        return ""
    return (
        f"Product scope: The user is asking about **{exclusive}**. Down-rank (scores 1–2) snippets from files whose primary "
        f"documentation scope differs from **{exclusive}** (when detected from KB frontmatter/filename). Favor snippets that directly "
        f"match the same behavior the user asked about.\n"
    )


def _rerank_matches(
    query: str,
    matches: list[dict],
    threshold: int = 3,
    exclusive_scope: str | None = None,
) -> list[dict]:
    """Score each match 1-5, filter by threshold."""
    if not matches:
        return []
    llm = _llm_search_rerank()
    # Build snippet list for prompt (truncate long lines)
    snippets = []
    for m in matches:
        text = (m.get("snippet") or m.get("line", ""))[:500]
        snippets.append(f"[{m['file']} L{m['line_num']}] {text}")
    snippet_text = "\n".join(f"{i+1}. {s}" for i, s in enumerate(snippets))
    scope = _rerank_product_scope_note(query, exclusive_scope=exclusive_scope)
    prompt = RERANK_PROMPT.format(query=query, product_scope=scope) + "\n\nSnippets:\n" + snippet_text
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
    llm = _llm_search_json()
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
    llm = _llm_search_json()
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
    max_context_chars: int = 20000,
) -> str:
    """
    Orchestrated search: grep → re-rank → sufficiency check → optional refined search.
    Returns formatted context for the main agent.
    """
    all_matches: list[dict] = []
    fallback_candidates: list[dict] = []
    seen = set()

    scope_hints, exclusive_scope = _infer_scope(query)

    focus_subqueries = _split_focus_subqueries(query)
    if not focus_subqueries:
        focus_subqueries = [query]

    for iteration in range(max_iterations):
        if iteration == 0:
            base_terms = extract_search_terms(query)
            hard_terms = _extract_hard_terms(query)
            terms_variants = [hard_terms + base_terms]
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
            # Retrieve per focus sub-query, then merge.
            for sq in focus_subqueries:
                found = search_documents(
                    query=sq,
                    search_terms=terms + _extract_hard_terms(sq),
                    llm_extract=None,
                    max_results_per_term=10,
                    scope_hints=scope_hints if scope_hints else None,
                    exclusive_scope=exclusive_scope,
                )
                matches.extend(found)

        for m in matches:
            key = (m["file"], m["line_num"])
            if key not in seen:
                seen.add(key)
                all_matches.append(m)
                fallback_candidates.append(m)

        if not matches:
            break

        # Re-rank and filter (cap candidates to keep cost bounded).
        all_matches = _rerank_matches(
            query,
            all_matches[:30],
            threshold=rerank_threshold,
            exclusive_scope=exclusive_scope,
        )
        if not all_matches:
            all_matches = matches[:15]  # Fallback
        elif _distinct_doc_count(all_matches) < 2:
            # Recover source diversity when rerank over-focuses on one large document.
            all_matches = _augment_with_unseen_docs(all_matches, fallback_candidates, target_docs=3)

    all_matches = _diversify_matches(all_matches, max_per_doc=4, keep_limit=30)

    formatted = format_matches_for_context(all_matches, max_chars=max_context_chars)

    def _format_retrieved_documents(matches: list[dict], max_items: int = 12) -> str:
        """
        Provide a compact, de-duplicated list of retrieved documents for the main agent
        to cite/mention as references in the final answer.
        """
        if not matches:
            return ""
        docs: list[tuple[str, str, str | None]] = []
        seen_doc: set[str] = set()
        for m in matches:
            meta = m.get("meta") or {}
            title = (meta.get("title") or "").strip() or str(m.get("file") or "Document").strip()
            url = (meta.get("url") or "").strip() or str(m.get("url") or "").strip()
            path = str(m.get("path") or "").strip()
            key = (url or path or title).strip().lower()
            if not key or key in seen_doc:
                continue
            seen_doc.add(key)
            docs.append((title, url or path or title, url or None))
            if len(docs) >= max_items:
                break
        if not docs:
            return ""
        lines = ["## Retrieved documents"]
        for title, ref, url in docs:
            if url and url.startswith("http"):
                lines.append(f"- {title}: {url}")
            else:
                lines.append(f"- {title}: {ref}")
        return "\n".join(lines)

    retrieved_docs = _format_retrieved_documents(all_matches)
    if retrieved_docs and formatted and formatted != "No relevant documents found.":
        formatted = f"{formatted}\n\n---\n\n{retrieved_docs}"
    if _retrieval_log is not None:
        _retrieval_log.append(
            {
                "query": query,
                "focus_subqueries": list(focus_subqueries),
                "match_count": len(all_matches),
                "matches": [copy.deepcopy(m) for m in all_matches],
                "context_passed_to_llm": formatted,
            }
        )
    return formatted
