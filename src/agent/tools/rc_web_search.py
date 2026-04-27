"""Web search across enabled RC URLs (solution-agnostic).

This tool is only used when the user has enabled RC URLs in the UI.
Hosted web retrieval follows **Configure → provider preset**:
OpenRouter presets use OpenRouter's Responses + web plugin; **openai** uses
OpenAI's Responses API + ``web_search`` tool (same entrypoint: ``run_web_search`` in ``hosted_web_search``).

After KB retrieval, ``kb_first`` mode runs an LLM gate (see ``kb_web_gate``) on the final
match list to decide whether hosted web should still run. ``always_augment`` skips the gate
and always runs web after non-empty KB (higher cost); configure under **Knowledge → RC URLs**.
"""

from __future__ import annotations

from urllib.parse import urlparse

from src.agent.tools.hosted_web_search import run_web_search
from src.agent.tools.kb_web_gate import evaluate_kb_web_gate
from src.agent.tools.search_agent import search_with_agent_structured
from src.runtime_config import effective_llm_model_main, effective_rc_web_retrieval_mode
from src.db import database

_NO_DOCS_SENTINEL = "No relevant documents found."


def _list_rc_hosts(max_domains: int) -> tuple[list[str], dict[str, str]]:
    urls = database.list_rc_urls(limit=200, offset=0, enabled_only=True)
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
    return hosts, url_by_host


def _run_hosted_web_aggregate(
    query: str,
    url_by_host: dict[str, str],
    hosts: list[str],
    *,
    max_results_per_domain: int,
) -> str:
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
        return "Web search returned no usable results from enabled RC URLs."
    cite_block = ""
    if citations:
        cite_block = "\n\n## Citations\n" + "\n".join(f"- {c}" for c in citations[:30])
    return "\n\n---\n\n".join(parts) + cite_block


def _merge_kb_and_web(*, kb_block: str, web_block: str, weak_kb_signal: bool) -> str:
    """Single tool string: optional KB section + web section."""
    segments: list[str] = []
    kb = (kb_block or "").strip()
    web = (web_block or "").strip()
    if kb:
        if weak_kb_signal:
            segments.append(
                "## Local KB (below confidence threshold — verify with web)\n\n" + kb
            )
        else:
            segments.append("## Local KB\n\n" + kb)
    if web:
        segments.append(web)
    if not segments:
        return ""
    return "\n\n---\n\n".join(segments)


def search_rc_web(query: str, max_domains: int = 5, max_results_per_domain: int = 5) -> str:
    kb_formatted, final_matches = search_with_agent_structured(query=query)
    kb_formatted = (kb_formatted or "").strip()
    mode = effective_rc_web_retrieval_mode()

    hosts, url_by_host = _list_rc_hosts(max_domains)
    kb_is_emptyish = (not kb_formatted) or (_NO_DOCS_SENTINEL in kb_formatted) or not final_matches

    if not hosts:
        if kb_is_emptyish:
            return kb_formatted or "No RC URLs are enabled."
        return kb_formatted

    # Empty / unusable KB → hosted web when RC domains exist.
    if kb_is_emptyish:
        web_only = _run_hosted_web_aggregate(
            query, url_by_host, hosts, max_results_per_domain=max_results_per_domain
        )
        if kb_formatted and web_only and not web_only.startswith("Web search returned no"):
            return _merge_kb_and_web(kb_block=kb_formatted, web_block=web_only, weak_kb_signal=True)
        return web_only if web_only else (kb_formatted or "Web search returned no usable results from enabled RC URLs.")

    # Non-empty KB: RC URLs required for any web branch (already checked hosts).

    if mode == "always_augment":
        web_block = _run_hosted_web_aggregate(
            query, url_by_host, hosts, max_results_per_domain=max_results_per_domain
        )
        return _merge_kb_and_web(kb_block=kb_formatted, web_block=web_block, weak_kb_signal=False)

    # kb_first — LLM gate on final matches
    proceed_web, _reason = evaluate_kb_web_gate(query, final_matches)
    if not proceed_web:
        return kb_formatted

    web_block = _run_hosted_web_aggregate(
        query, url_by_host, hosts, max_results_per_domain=max_results_per_domain
    )
    return _merge_kb_and_web(kb_block=kb_formatted, web_block=web_block, weak_kb_signal=True)
