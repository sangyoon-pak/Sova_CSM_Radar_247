"""Hosted web search via the Responses API (OpenRouter web plugin or OpenAI ``web_search``).

Originally lived in ``openrouter_web.py`` (name kept as a shim for imports).

- **openrouter** / **gemini_openrouter**: OpenRouter ``POST /v1/responses`` + ``plugins: [{id: "web"}]``.
- **openai**: OpenAI ``POST /v1/responses`` + ``tools: [{type: "web_search"}]``.

Both delegate retrieval to the provider (no local fetch to arbitrary URLs).
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlparse

import requests

from src.runtime_config import (
    effective_chat_api_key,
    effective_chat_base_url,
    effective_llm_provider_preset,
)


@dataclass(frozen=True)
class WebSearchResult:
    text: str
    citations: list[str]
    raw: dict


def _model_id_for_openai_direct(model: str) -> str:
    """Map OpenRouter-style ids (e.g. openai/gpt-4o) to OpenAI API model names."""
    m = (model or "").strip()
    if not m:
        return "gpt-4o"
    if m.startswith("openai/"):
        return m.split("/", 1)[1].strip() or "gpt-4o"
    if "/" in m:
        return "gpt-4o"
    return m


def _urls_from_url_citation_annotation(ann: dict) -> list[str]:
    """Collect URLs from flat or nested ``url_citation`` annotation objects."""
    urls: list[str] = []
    if not isinstance(ann, dict):
        return urls
    if str(ann.get("type") or "") != "url_citation":
        return urls
    u = ann.get("url")
    if u:
        urls.append(str(u).strip())
    nested = ann.get("url_citation")
    if isinstance(nested, dict) and nested.get("url"):
        urls.append(str(nested["url"]).strip())
    return urls


def _deep_collect_url_citations(obj: Any, out: list[str]) -> None:
    """Fallback: some Responses payloads nest citations outside the first ``message`` block."""
    if isinstance(obj, dict):
        if str(obj.get("type") or "") == "url_citation":
            out.extend(_urls_from_url_citation_annotation(obj))
        for v in obj.values():
            _deep_collect_url_citations(v, out)
    elif isinstance(obj, list):
        for x in obj:
            _deep_collect_url_citations(x, out)


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
                if isinstance(ann, dict):
                    cites.extend(_urls_from_url_citation_annotation(ann))
    # Deep pass catches alternate nesting / extra blocks OpenAI may emit.
    extra: list[str] = []
    _deep_collect_url_citations(payload, extra)
    cites.extend(extra)
    seen = set()
    uniq: list[str] = []
    for u in cites:
        if not u or u in seen:
            continue
        seen.add(u)
        uniq.append(u)
    return ("\n".join(texts).strip(), uniq)


def _domain_hosts(url: str | None) -> list[str] | None:
    if not url:
        return None
    host = urlparse(url).netloc
    if not host:
        return None
    return [host]


def _web_search_openrouter(
    *,
    query: str,
    model: str,
    url: str | None,
    max_results: int,
    max_output_tokens: int,
    api_key: str,
) -> WebSearchResult:
    include_domains = _domain_hosts(url)
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
            "Authorization": f"Bearer {api_key}",
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


def _web_search_openai(
    *,
    query: str,
    model: str,
    url: str | None,
    max_output_tokens: int,
    api_key: str,
) -> WebSearchResult:
    """OpenAI Responses API with built-in ``web_search`` tool (see OpenAI web search docs)."""
    base = effective_chat_base_url().rstrip("/")
    endpoint = f"{base}/responses"
    mid = _model_id_for_openai_direct(model)
    tools: list[dict] = [{"type": "web_search"}]
    hosts = _domain_hosts(url)
    if hosts:
        tools[0]["filters"] = {"allowed_domains": hosts}

    payload = {
        "model": mid,
        "input": query,
        "tools": tools,
        "max_output_tokens": int(max_output_tokens),
    }

    resp = requests.post(
        endpoint,
        headers={
            "Authorization": f"Bearer {api_key}",
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


def run_web_search(
    *,
    query: str,
    model: str,
    url: str | None = None,
    max_results: int = 5,
    max_output_tokens: int = 2000,
) -> WebSearchResult:
    """
    Run hosted web search for the current provider preset.

    OpenRouter presets use OpenRouter's Responses + web plugin; OpenAI direct uses
    OpenAI's Responses API + ``web_search`` tool.
    """
    api_key = effective_chat_api_key()
    if not api_key:
        raise ValueError(
            "API key is not set. Add a key in Configure (or set OPENROUTER_API_KEY / OPENAI_API_KEY in the environment)."
        )

    preset = effective_llm_provider_preset()
    if preset == "openai":
        return _web_search_openai(
            query=query,
            model=model,
            url=url,
            max_output_tokens=max_output_tokens,
            api_key=api_key,
        )

    return _web_search_openrouter(
        query=query,
        model=model,
        url=url,
        max_results=max_results,
        max_output_tokens=max_output_tokens,
        api_key=api_key,
    )
