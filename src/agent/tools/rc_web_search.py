"""Hosted web search over enabled RC URLs (provider-native).

This tool is intentionally web-only: no local KB retrieval / rerank loops inside this module.
Mode-specific orchestration (always_augment vs kb_first gate decision) is handled by the caller.
"""

from __future__ import annotations

from urllib.parse import urlparse

from src.agent.tools.hosted_web_search import run_web_search
from src.runtime_config import effective_llm_model_main
from src.db import database

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


def search_rc_web(query: str, max_domains: int = 5, max_results_per_domain: int = 5) -> str:
    hosts, url_by_host = _list_rc_hosts(max_domains)
    if not hosts:
        return "No RC URLs are enabled."

    return _run_hosted_web_aggregate(
        query, url_by_host, hosts, max_results_per_domain=max_results_per_domain
    )
