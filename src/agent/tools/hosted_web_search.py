"""Hosted web search via the Responses API (OpenRouter web plugin or OpenAI ``web_search``).

Originally lived in ``openrouter_web.py`` (name kept as a shim for imports).

- **openrouter** / **gemini_openrouter**: OpenRouter ``POST /v1/responses`` + ``plugins: [{id: "web"}]``.
- **openai**: OpenAI ``POST /v1/responses`` + ``tools: [{type: "web_search"}]``.

Both delegate retrieval to the provider (no local fetch to arbitrary URLs).
"""

from __future__ import annotations

import json
import re
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
    provider: str
    raw_meta: dict

    @property
    def raw(self) -> dict:
        """Backward-compat shim for older call sites expecting `raw`."""
        return self.raw_meta


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


def _openai_web_search_supports_allowed_domains(resolved_model_id: str) -> bool:
    """
    Some OpenAI models reject ``web_search`` tool ``filters.allowed_domains``.
    Example: gpt-4o-mini returns invalid_request_error for ``filters``.
    Domain restriction then relies on the prompt (RC web already injects seeds).
    """
    mid = (resolved_model_id or "").strip().lower()
    if "gpt-4o-mini" in mid:
        return False
    return True


def _openai_response_implies_filters_unsupported(body: str) -> bool:
    try:
        data = json.loads(body)
        err = data.get("error") or {}
        msg = str(err.get("message") or "").lower()
        if "filters" in msg and "not supported" in msg:
            return True
        if err.get("param") == "tools" and "filter" in msg:
            return True
    except Exception:
        pass
    return False


def _openai_response_implies_include_unsupported(body: str) -> bool:
    try:
        data = json.loads(body)
        err = data.get("error") or {}
        msg = str(err.get("message") or "").lower()
        param = str(err.get("param") or "").lower()
        if "include" in param:
            return True
        if "include" in msg and any(x in msg for x in ("unknown", "unsupported", "invalid", "unexpected")):
            return True
    except Exception:
        pass
    return False


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


_URL_IN_TEXT_RE = re.compile(r"https?://[^\s\)\]<>\"']+", re.I)


def _host_matches_allowed(url: str, allowed_hosts: list[str]) -> bool:
    h = urlparse(url).netloc.lower()
    if not h:
        return False
    for a in allowed_hosts:
        al = (a or "").strip().lower()
        if not al:
            continue
        if h == al or h.endswith("." + al):
            return True
    return False


def _urls_from_plain_text_and_markdown(text: str, *, allowed_hosts: list[str]) -> list[str]:
    """When OpenAI omits url_citation annotations (common on smaller models), recover same-host links from prose."""
    if not text.strip() or not allowed_hosts:
        return []
    out: list[str] = []
    seen: set[str] = set()
    for m in _URL_IN_TEXT_RE.finditer(text):
        u = (m.group(0) or "").strip().rstrip(".,;:)}]")
        if not u or u in seen:
            continue
        if not _host_matches_allowed(u, allowed_hosts):
            continue
        seen.add(u)
        out.append(u)
    return out


def _extract_web_search_tool_source_urls(payload: dict) -> list[str]:
    """
    OpenAI may omit ``output_text.annotations`` but still attach consulted URLs under
    ``web_search_call`` items. Request ``include: ['web_search_call.action.sources']``
    when calling the Responses API so ``action.sources`` is populated.

    Supports list of strings, list of {url: ...}, or nested shapes via light recursion.
    """
    urls: list[str] = []
    seen: set[str] = set()

    def _take_url_obj(obj: Any) -> None:
        if isinstance(obj, str) and obj.startswith(("http://", "https://")):
            u = obj.strip()
            if u not in seen:
                seen.add(u)
                urls.append(u)
            return
        if isinstance(obj, dict):
            u = obj.get("url") or obj.get("uri")
            if u:
                _take_url_obj(str(u))

    def _consume_sources(src: Any) -> None:
        if src is None:
            return
        if isinstance(src, list):
            for x in src:
                _consume_sources(x)
            return
        _take_url_obj(src)

    output_items = payload.get("output") or []
    stack: list[Any] = [output_items]
    while stack:
        cur = stack.pop()
        if isinstance(cur, dict):
            if str(cur.get("type") or "") == "web_search_call":
                action = cur.get("action") or {}
                _consume_sources(action.get("sources"))
                # open_page / similar
                if isinstance(action, dict) and action.get("url"):
                    _take_url_obj(str(action["url"]))
            for v in cur.values():
                if isinstance(v, (dict, list)):
                    stack.append(v)
        elif isinstance(cur, list):
            stack.extend(cur)
    return urls


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
    seen: set[str] = set()
    uniq: list[str] = []
    for u in cites:
        if not u or u in seen:
            continue
        seen.add(u)
        uniq.append(u)

    for u in _extract_web_search_tool_source_urls(payload):
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
    return WebSearchResult(
        text=text,
        citations=citations,
        provider="openrouter",
        raw_meta=data,
    )


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
    hosts = _domain_hosts(url)

    def _post(*, with_domain_filters: bool, include_web_search_sources: bool) -> requests.Response:
        tools: list[dict] = [{"type": "web_search"}]
        if with_domain_filters and hosts:
            tools[0]["filters"] = {"allowed_domains": hosts}
        payload: dict[str, Any] = {
            "model": mid,
            "input": query,
            "tools": tools,
            "max_output_tokens": int(max_output_tokens),
        }
        if include_web_search_sources:
            payload["include"] = ["web_search_call.action.sources"]
        return requests.post(
            endpoint,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            data=json.dumps(payload),
            timeout=120,
        )

    use_filters = bool(hosts) and _openai_web_search_supports_allowed_domains(mid)
    wf = use_filters
    resp = _post(with_domain_filters=wf, include_web_search_sources=True)
    if resp.status_code >= 400 and wf and _openai_response_implies_filters_unsupported(resp.text):
        wf = False
        resp = _post(with_domain_filters=False, include_web_search_sources=True)
    if resp.status_code >= 400 and _openai_response_implies_include_unsupported(resp.text):
        resp = _post(with_domain_filters=wf, include_web_search_sources=False)
    if resp.status_code >= 400:
        raise ValueError(resp.text[:2000])
    data = resp.json()
    text, citations = _extract_output_text_and_citations(data)
    if hosts:
        seen_c = set(citations)
        for u in _urls_from_plain_text_and_markdown(text, allowed_hosts=hosts):
            if u not in seen_c:
                seen_c.add(u)
                citations.append(u)
    return WebSearchResult(
        text=text,
        citations=citations,
        provider="openai",
        raw_meta=data,
    )


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
