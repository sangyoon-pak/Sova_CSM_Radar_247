"""Web search across enabled RC URLs (solution-agnostic).

This tool is only used when the user has enabled RC URLs in the UI.
Hosted web retrieval follows **Configure → provider preset**:
OpenRouter presets use OpenRouter's Responses + web plugin; **openai** uses
OpenAI's Responses API + ``web_search`` tool (same entrypoint: ``run_web_search``).
"""

from __future__ import annotations

from urllib.parse import urlparse

from src.agent.tools.openrouter_web import run_web_search
from src.runtime_config import effective_llm_model_main
from src.db import database


def _kb_context_insufficient(kb_text: str) -> bool:
    t = (kb_text or "").strip()
    if not t:
        return True
    if "No relevant documents found." in t:
        return True
    if "## Retrieved documents" not in t:
        return True
    return False


def search_rc_web(query: str, max_domains: int = 5, max_results_per_domain: int = 5) -> str:
    # Fundamental retrieval policy (global):
    # 1) Search uploaded KB docs first
    # 2) Run RC URL web search only when KB evidence is insufficient
    from src.agent.tools.search_agent import search_with_agent

    kb = search_with_agent(query=query, max_context_chars=14000)
    if not _kb_context_insufficient(kb):
        return (
            "Used uploaded KB documents first (search_product_docs).\n"
            "RC URL web fallback not needed because KB evidence is sufficient.\n\n"
            f"{kb}"
        )

    urls = database.list_rc_urls(limit=200, offset=0, enabled_only=True)
    if not urls:
        return (
            "KB retrieval was insufficient and no RC URLs are enabled in Knowledge > RC URLs.\n\n"
            "[KB retrieval result]\n"
            f"{kb}"
        )

    # Deduplicate by host; keep up to max_domains to control cost/latency.
    hosts: list[str] = []
    url_by_host: dict[str, str] = {}
    for r in urls:
        u = str(r.get("url") or "").strip()
        if not u:
            continue
        host = urlparse(u).netloc
        if not host or host in url_by_host:
            continue
        url_by_host[host] = u
        hosts.append(host)
        if len(hosts) >= max_domains:
            break

    parts: list[str] = []
    citations: list[str] = []
    for host in hosts:
        base_url = url_by_host[host]
        prompt = (
            "Use web search results ONLY from this documentation domain to answer the user query. "
            "Prefer the most relevant pages and cite them.\n"
            f"User query:\n{query}\n"
            f"Documentation domain: {host}\n"
        )
        res = run_web_search(
            query=prompt,
            model=effective_llm_model_main(),
            url=base_url,
            max_results=max_results_per_domain,
            max_output_tokens=1400,
        )
        if res.text:
            parts.append(f"## Web results from {host}\n{res.text}")
        for c in res.citations or []:
            if c not in citations:
                citations.append(c)

    if not parts:
        return (
            "KB retrieval was insufficient, but RC URL web search returned no usable results.\n\n"
            "[KB retrieval result]\n"
            f"{kb}"
        )
    cite_block = ""
    if citations:
        cite_block = "\n\n## Citations\n" + "\n".join(f"- {c}" for c in citations[:30])
    web_block = "\n\n---\n\n".join(parts) + cite_block
    return (
        "[KB retrieval result]\n"
        f"{kb}\n\n"
        "---\n\n"
        "[RC URL web retrieval fallback]\n"
        f"{web_block}"
    )

