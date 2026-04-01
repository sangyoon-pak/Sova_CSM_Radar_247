"""OpenRouter web search via Responses API (Option A).

This bypasses local HTTP fetching (TLS/CA issues) by delegating web search to OpenRouter's plugin.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from urllib.parse import urlparse

import requests

from src.config import settings


@dataclass(frozen=True)
class WebSearchResult:
    text: str
    citations: list[str]
    raw: dict


def _extract_output_text_and_citations(payload: dict) -> tuple[str, list[str]]:
    out = payload.get("output") or []
    texts: list[str] = []
    cites: list[str] = []
    for item in out:
        if not isinstance(item, dict):
            continue
        if item.get("type") != "message":
            continue
        for c in item.get("content") or []:
            if not isinstance(c, dict):
                continue
            if c.get("type") != "output_text":
                continue
            txt = str(c.get("text") or "")
            if txt:
                texts.append(txt)
            for ann in c.get("annotations") or []:
                if isinstance(ann, dict) and ann.get("type") == "url_citation" and ann.get("url"):
                    cites.append(str(ann["url"]))
    # Dedup citations preserve order
    seen = set()
    uniq: list[str] = []
    for u in cites:
        if u in seen:
            continue
        seen.add(u)
        uniq.append(u)
    return ("\n".join(texts).strip(), uniq)


def run_web_search(
    *,
    query: str,
    model: str,
    url: str | None = None,
    max_results: int = 5,
    max_output_tokens: int = 2000,
) -> WebSearchResult:
    """
    Run a web-enabled response using OpenRouter Responses API + web plugin.
    If url is provided, we restrict to that domain.
    """
    if not settings.openrouter_api_key:
        raise ValueError("OPENROUTER_API_KEY is not set")
    if not settings.openrouter_base_url:
        raise ValueError("OPENROUTER_BASE_URL is not set")

    include_domains = None
    if url:
        host = urlparse(url).netloc
        if host:
            include_domains = [host]

    plugins: list[dict] = [{"id": "web", "max_results": int(max_results)}]
    if include_domains:
        plugins[0]["include_domains"] = include_domains

    payload = {
        "model": model,
        "input": query,
        "plugins": plugins,
        "max_output_tokens": int(max_output_tokens),
    }

    resp = requests.post(
        "https://openrouter.ai/api/v1/responses",
        headers={
            "Authorization": f"Bearer {settings.openrouter_api_key}",
            "Content-Type": "application/json",
        },
        data=json.dumps(payload),
        timeout=120,
    )
    if resp.status_code >= 400:
        raise ValueError(resp.text[:2000])
    data = resp.json()
    text, citations = _extract_output_text_and_citations(data)
    return WebSearchResult(text=text, citations=citations, raw=data)

