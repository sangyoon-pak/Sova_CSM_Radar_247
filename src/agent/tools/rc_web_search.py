"""Hosted web search over enabled RC URLs (provider-native).

This tool is intentionally web-only: no local KB retrieval / rerank loops inside this module.
Mode-specific orchestration (always_augment vs kb_first gate decision) is handled by the caller.

**Hybrid depth:** OpenRouter/OpenAI web tools only receive *domain* filters from the ``url``
parameter — not full paths. We therefore inject **all enabled RC URLs on that host** (seed
paths, deeper pages first) into the prompt, and perform a **bounded retry** when the first
pass looks evidentially weak (short text, no citations, or explicit "not found" phrasing).
"""

from __future__ import annotations

import json
import os
import re
from html import unescape
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from langchain_core.messages import HumanMessage

from src.agent.chat_llm import get_chat_llm
from src.agent.tools.hosted_web_search import run_web_search
from src.runtime_config import effective_llm_model_main, effective_llm_provider_preset
from src.db import database

# Medium budget defaults (per search_rc_web invocation).
_MAX_SEEDS_PER_HOST = 12
_MAX_AGENTIC_STEPS_PER_HOST = 3
_MAX_FETCHED_CITATIONS_PER_HOST = 6
_MAX_DISCOVERED_URLS_PER_HOST = 16
_MAX_DISCOVERY_FETCHES_PER_HOST = 6
_MAX_DISCOVERY_SITEMAP_URLS = 120
_MAX_FETCH_CHARS_PER_URL = 4000


def _path_depth(url: str) -> int:
    path = (urlparse(url).path or "").strip("/")
    if not path:
        return 0
    return len(path.split("/"))


def _seeds_for_prompt(urls: list[str], max_seeds: int) -> list[str]:
    """Prefer deeper doc paths in the prompt so the model does not anchor only on the landing page."""
    uniq: list[str] = []
    seen: set[str] = set()
    for u in urls:
        u = (u or "").strip()
        if not u or u in seen:
            continue
        seen.add(u)
        uniq.append(u)
    uniq.sort(key=lambda u: (-_path_depth(u), -len(u), u))
    return uniq[:max_seeds]


def _group_enabled_rc_urls_by_host() -> dict[str, list[str]]:
    rows = database.list_rc_urls(limit=200, offset=0, enabled_only=True)
    by_host: dict[str, list[str]] = {}
    for r in rows:
        u = str(r.get("url") or "").strip()
        if not u.startswith(("http://", "https://")):
            continue
        host = urlparse(u).netloc
        if not host:
            continue
        by_host.setdefault(host, []).append(u)
    return by_host


def _list_rc_hosts(max_domains: int) -> tuple[list[str], dict[str, list[str]]]:
    by_host = _group_enabled_rc_urls_by_host()
    hosts = list(by_host.keys())[:max_domains]
    slim = {h: by_host[h] for h in hosts}
    return hosts, slim


def _extract_path_like_terms(user_query: str) -> list[str]:
    """Vendor-agnostic: only extract path-shaped hints (no curated token lists)."""
    q = (user_query or "").strip().lower()
    hits = re.findall(r"/[a-z0-9_./-]{2,}", q)
    # De-dupe while preserving order
    out: list[str] = []
    seen: set[str] = set()
    for h in hits:
        if h in seen:
            continue
        seen.add(h)
        out.append(h)
        if len(out) >= 8:
            break
    return out


def _query_terms(user_query: str) -> list[str]:
    """Small deterministic term set used to rank discovered URLs before any LLM sees them."""
    q = (user_query or "").lower()
    terms = re.findall(r"[a-z0-9][a-z0-9_-]{2,}", q)
    path_bits: list[str] = []
    for path in _extract_path_like_terms(q):
        path_bits.extend([x for x in re.split(r"[/._-]+", path) if len(x) >= 3])
    out: list[str] = []
    seen: set[str] = set()
    for t in path_bits + terms:
        if t in seen:
            continue
        seen.add(t)
        out.append(t)
        if len(out) >= 32:
            break
    return out


def _same_host_url(raw: str, *, base_url: str, host: str) -> str | None:
    href = (raw or "").strip()
    if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
        return None
    try:
        joined = urljoin(base_url, unescape(href))
        no_frag, _frag = urldefrag(joined)
        pu = urlparse(no_frag)
        if pu.scheme not in {"http", "https"} or pu.netloc != host:
            return None
        # Skip obviously non-document assets.
        path_l = (pu.path or "").lower()
        if re.search(r"\.(?:png|jpe?g|gif|webp|svg|ico|css|js|map|zip|tar|gz|mp4|mov|avi|woff2?|ttf)$", path_l):
            return None
        return no_frag.rstrip("/")
    except Exception:
        return None


def _extract_links_from_html(base_url: str, host: str, raw: str) -> list[str]:
    urls: list[str] = []
    seen: set[str] = set()
    for m in re.finditer(r"""(?is)<a\b[^>]*?\bhref\s*=\s*["']([^"']+)["']""", raw or ""):
        u = _same_host_url(m.group(1), base_url=base_url, host=host)
        if not u or u in seen:
            continue
        seen.add(u)
        urls.append(u)
    return urls


def _sitemap_urls(host: str, seed_urls: list[str]) -> list[str]:
    scheme = "https"
    for u in seed_urls:
        pu = urlparse(u)
        if pu.scheme in {"http", "https"} and pu.netloc == host:
            scheme = pu.scheme
            break
    candidates = [f"{scheme}://{host}/sitemap.xml", f"{scheme}://{host}/sitemap_index.xml"]
    urls: list[str] = []
    seen: set[str] = set()
    for sm in candidates:
        try:
            resp = requests.get(
                sm,
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0 (compatible; SovaRCWeb/1.0)"},
            )
            if resp.status_code >= 400:
                continue
            for loc in re.findall(r"(?is)<loc>\s*(.*?)\s*</loc>", resp.text or ""):
                u = _same_host_url(loc, base_url=sm, host=host)
                if not u or u in seen:
                    continue
                seen.add(u)
                urls.append(u)
                if len(urls) >= _MAX_DISCOVERY_SITEMAP_URLS:
                    return urls
        except Exception:
            continue
    return urls


def _score_discovered_url(url: str, user_query: str, seed_urls: list[str]) -> int:
    pu = urlparse(url)
    hay = f"{pu.path} {pu.query}".lower()
    terms = _query_terms(user_query)
    score = 0
    if url in seed_urls:
        score += 40
    score += min(_path_depth(url), 6) * 3
    for term in terms:
        if term in hay:
            score += 8
    for path_term in _extract_path_like_terms(user_query):
        if path_term.strip("/").lower() in hay:
            score += 20
    if any(x in hay for x in ("api", "reference", "docs", "guide", "integration", "developer", "webhook", "endpoint")):
        score += 6
    if pu.query:
        score -= 4
    if re.search(r"/(?:blog|news|press|careers|legal|privacy|terms)(?:/|$)", pu.path.lower()):
        score -= 10
    return score


def _discover_same_host_candidate_urls(host: str, seed_urls: list[str], user_query: str) -> list[str]:
    """
    Deterministically shrink a large site/link surface into a small same-host shortlist.

    Some hosted web plugins follow useful child pages from a base URL. OpenAI's
    hosted web_search can be less reliable for that traversal, so we provide concrete
    candidate URLs from sitemaps and first-hop links rather than asking a model to sort
    hundreds of raw crawler URLs.
    """
    candidates: list[str] = []
    seen: set[str] = set()

    def add(url: str | None) -> None:
        if not url or url in seen:
            return
        seen.add(url)
        candidates.append(url)

    for u in seed_urls:
        add(_same_host_url(u, base_url=u, host=host))
    for u in _sitemap_urls(host, seed_urls):
        add(u)

    fetches = 0
    for seed in seed_urls[: _MAX_DISCOVERY_FETCHES_PER_HOST]:
        if fetches >= _MAX_DISCOVERY_FETCHES_PER_HOST:
            break
        try:
            resp = requests.get(
                seed,
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0 (compatible; SovaRCWeb/1.0)"},
            )
            fetches += 1
            if resp.status_code >= 400:
                continue
            ctype = (resp.headers.get("Content-Type") or "").lower()
            if "text/html" not in ctype and ctype:
                continue
            for u in _extract_links_from_html(seed, host, resp.text or ""):
                add(u)
        except Exception:
            continue

    candidates.sort(key=lambda u: (-_score_discovered_url(u, user_query, seed_urls), -_path_depth(u), u))
    return candidates[:_MAX_DISCOVERED_URLS_PER_HOST]


def discover_same_host_candidate_urls(base_url: str, user_query: str = "", max_urls: int = 10) -> list[str]:
    """Public helper for RC URL discovery without relying on provider-hosted traversal."""
    base = (base_url or "").strip()
    limit = max(1, int(max_urls or 10))
    pu = urlparse(base)
    if pu.scheme not in {"http", "https"} or not pu.netloc:
        return []
    candidates = _discover_same_host_candidate_urls(pu.netloc, [base], user_query or base)
    if base.rstrip("/") not in candidates:
        candidates.insert(0, base.rstrip("/"))
    return candidates[:limit]


def _parse_json_object(raw: str) -> dict | None:
    s = (raw or "").strip()
    if not s:
        return None
    if "```" in s:
        s = s.split("```")[1]
        if s.lstrip().startswith("json"):
            s = s[4:].lstrip()
    try:
        obj = json.loads(s.strip())
        return obj if isinstance(obj, dict) else None
    except Exception:
        return None


def _agentic_plan_prompt(
    *,
    host: str,
    user_query: str,
    seed_urls: list[str],
    prior_citations: list[str],
    last_answer: str,
    step: int,
) -> str:
    """Ask the hosted-web model to propose the next best focused query + target pages."""
    seed_block = "\n".join(f"- {u}" for u in seed_urls) if seed_urls else "(none)"
    cite_block = "\n".join(f"- {u}" for u in prior_citations[:20]) if prior_citations else "(none yet)"
    path_terms = _extract_path_like_terms(user_query)
    path_block = "\n".join(f"- {p}" for p in path_terms) if path_terms else "(none)"
    return (
        "You are an agent controlling hosted web search restricted to ONE documentation domain.\n"
        "Your job: propose the best *next* search step to maximize finding authoritative API/spec evidence.\n\n"
        "Return STRICT JSON ONLY:\n"
        "{\n"
        '  "next_query": "string",\n'
        '  "target_urls": ["https://..."],\n'
        '  "stop": false,\n'
        '  "reason": "short"\n'
        "}\n\n"
        "Constraints:\n"
        "- Domain must be the provided host.\n"
        "- Prefer deep API/reference pages over the homepage.\n"
        "- Use the *current* evidence (prior citations + last_answer) to decide whether to stop.\n"
        "- If you are not confident you have authoritative evidence yet, set stop=false and propose a next_query.\n"
        "- If the user query contains path-like terms, prefer to include them verbatim in next_query.\n\n"
        f"Host: {host}\n"
        f"Step: {step}\n"
        f"Seed URLs:\n{seed_block}\n\n"
        f"User query:\n{(user_query or '').strip()[:2000]}\n\n"
        f"Path-like terms from user query:\n{path_block}\n\n"
        f"Prior citations (if any):\n{cite_block}\n\n"
        f"Last answer snippet (may be empty):\n{(last_answer or '').strip()[:1200]}\n"
    )


def _agentic_answer_prompt(*, host: str, user_query: str, seed_urls: list[str]) -> str:
    """Ask for a tight, evidence-first answer (still produced by hosted web)."""
    seed_block = "\n".join(f"- {u}" for u in seed_urls) if seed_urls else "(none)"
    return (
        "Answer the user using hosted web search restricted to this domain.\n"
        "Be evidence-first: cite the exact URLs you used.\n"
        "If you cannot find authoritative documentation after searching, say so briefly and list what you tried.\n\n"
        f"Host: {host}\n"
        f"Seed URLs:\n{seed_block}\n\n"
        f"User query:\n{user_query}\n"
    )


def _strip_html_to_text(raw: str) -> str:
    text = re.sub(r"(?is)<script.*?>.*?</script>", " ", raw)
    text = re.sub(r"(?is)<style.*?>.*?</style>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _fetch_same_host_snippets(host: str, urls: list[str], *, max_pages: int) -> list[tuple[str, str]]:
    """
    Fetch top same-host URLs and extract plain text snippets.
    This makes citations/candidate URLs actionable evidence for second-pass synthesis.
    """
    out: list[tuple[str, str]] = []
    seen: set[str] = set()
    for u in urls:
        url = (u or "").strip()
        if not url or url in seen:
            continue
        seen.add(url)
        pu = urlparse(url)
        if pu.netloc != host:
            continue
        try:
            resp = requests.get(
                url,
                timeout=12,
                headers={"User-Agent": "Mozilla/5.0 (compatible; SovaRCWeb/1.0)"},
            )
            if resp.status_code >= 400:
                continue
            ctype = (resp.headers.get("Content-Type") or "").lower()
            body = resp.text or ""
            if "text/html" in ctype:
                text = _strip_html_to_text(body)
            elif "text/plain" in ctype or "application/json" in ctype or not ctype:
                text = re.sub(r"\s+", " ", body).strip()
            else:
                continue
            if not text:
                continue
            out.append((url, text[:_MAX_FETCH_CHARS_PER_URL]))
            if len(out) >= max_pages:
                break
        except Exception:
            continue
    return out


def _fetch_citation_snippets(host: str, citations: list[str]) -> list[tuple[str, str]]:
    """Fetch top citation URLs and extract plain text snippets."""
    return _fetch_same_host_snippets(host, citations, max_pages=_MAX_FETCHED_CITATIONS_PER_HOST)


def _synthesize_from_cited_pages(host: str, user_query: str, fetched: list[tuple[str, str]]) -> str:
    if not fetched:
        return ""
    blocks = []
    for i, (u, t) in enumerate(fetched, start=1):
        blocks.append(f"[Doc {i}] URL: {u}\nExcerpt:\n{t}\n")
    prompt = (
        "You are synthesizing an answer from fetched documentation excerpts.\n"
        "Return concise, evidence-grounded findings only.\n"
        "- Do not ask the user for more information.\n"
        "- If the excerpts do not answer a point, explicitly say 'Not found in cited pages'.\n"
        "- Keep references by URL inline where used.\n\n"
        f"Host: {host}\n"
        f"User query:\n{(user_query or '').strip()[:2200]}\n\n"
        "Fetched citation pages:\n"
        f"{''.join(blocks)[:18000]}\n"
    )
    try:
        llm = get_chat_llm(model=effective_llm_model_main(), temperature=0.0)
        resp = llm.invoke(
            [HumanMessage(content=prompt)],
            config={"run_name": "search_rc_web.citation_followup_synthesis", "tags": ["search_rc_web", "citation_followup"]},
        )
        return str(resp.content or "").strip()
    except Exception:
        return ""


def _base_web_prompt(*, user_query: str, host: str, seed_urls: list[str]) -> str:
    seed_block = "\n".join(f"- {u}" for u in seed_urls) if seed_urls else "(no extra seed URLs)"
    paths = _extract_path_like_terms(user_query)
    path_block = "\n".join(f"- {p}" for p in paths) if paths else "- (none)"
    return (
        "You are answering using **hosted web search** restricted to this documentation domain.\n"
        "The domain filter is already applied; your job is to retrieve **concrete, citeable facts** "
        "(endpoints, parameters, field names, limits, defaults, error codes, examples).\n\n"
        "**Prioritize** pages whose URLs match or extend these **seed documentation URLs** "
        "(especially deeper paths — do not stop at the site home/landing page if a seed points further in):\n"
        f"{seed_block}\n\n"
        "Rules:\n"
        "- Every factual claim must be backed by a retrieved URL you cite (same domain).\n"
        "- If the user asks about a specific API or resource, **search for that exact path or keyword** "
        "within the domain, not only generic marketing pages.\n"
        "- Do NOT ask the user for more details. Do NOT include generic coaching text. "
        "Return only retrieval-grounded findings.\n"
        "- If evidence is missing, output a short machine-like gap note with what was searched.\n\n"
        "Path-like terms from user query:\n"
        f"{path_block}\n\n"
        "- If you truly cannot find authoritative docs for this domain, say so explicitly and suggest what "
        "doc section is missing.\n\n"
        f"Documentation domain: {host}\n"
        f"User query:\n{user_query}\n"
    )


def _retry_web_prompt(*, user_query: str, host: str, seed_urls: list[str]) -> str:
    seeds = "\n".join(f"- {u}" for u in seed_urls) if seed_urls else "(no seed URLs)"
    path_terms = ", ".join(_extract_path_like_terms(user_query)) or "(none)"
    return (
        "Your **first** web search pass for this domain looked **too shallow or non-evidential** "
        "(missing citations, too vague, or only generic landing-page content).\n"
        "**Search again**, focusing on **API / integration / reference** sections implied by the user question.\n"
        "Use exact endpoint/path terms, then adjacent aliases and related key names.\n\n"
        "Mandatory focus — treat these as primary targets (open equivalent child pages if needed):\n"
        f"{seeds}\n\n"
        f"Path terms: {path_terms}\n"
        "\n"
        "Return:\n"
        "1) Direct answer with **specific** facts (names, types, endpoints, payloads).\n"
        "2) **Citations**: list the exact doc URLs you used (same domain).\n\n"
        "Prohibited:\n"
        "- Asking user to provide more context.\n"
        "- Generic support escalation advice unless no evidence is found after this retry.\n\n"
        f"Documentation domain: {host}\n"
        f"User query:\n{user_query}\n"
    )


def _run_hosted_web_for_host(
    *,
    user_query: str,
    host: str,
    primary_url: str,
    all_urls_on_host: list[str],
    max_results_per_domain: int,
    max_output_tokens: int,
) -> tuple[str, list[str], dict]:
    seeds = _seeds_for_prompt(all_urls_on_host, _MAX_SEEDS_PER_HOST)
    provider_preset = effective_llm_provider_preset()
    discovered_urls: list[str] = []
    if provider_preset == "openai":
        discovered_urls = _discover_same_host_candidate_urls(host, seeds or [primary_url], user_query)
        # Promote deterministic candidates to seed URLs so hosted search has exact child pages to consider.
        for u in discovered_urls:
            if u not in seeds:
                seeds.append(u)
        seeds = _seeds_for_prompt(seeds, _MAX_SEEDS_PER_HOST)
    diag: dict = {
        "host": host,
        "primary_url": primary_url,
        "seed_count": len(seeds),
        "deterministic_discovered_count": len(discovered_urls),
        "attempts": [],
    }

    def _one_call(label: str, prompt: str) -> tuple[str, list[str]]:
        res = run_web_search(
            query=prompt,
            model=effective_llm_model_main(),
            url=primary_url,
            max_results=max_results_per_domain,
            max_output_tokens=max_output_tokens,
        )
        text = (res.text or "").strip()
        cites = list(res.citations or [])
        diag["attempts"].append(
            {
                "label": label,
                "text_len": len(text),
                "citation_count": len(cites),
                # Vendor-agnostic: only track whether the step produced any citations.
                "weak": (len(cites) == 0),
            }
        )
        return text, cites

    # Agentic loop: plan → search/answer → (optionally) refine, bounded by budget.
    citations: list[str] = []
    text = ""
    diag["retry_used"] = False

    step = 0
    while step < _MAX_AGENTIC_STEPS_PER_HOST:
        step += 1
        diag["step"] = step

        # 1) Ask for the next best query + target URLs (agentic planning).
        plan_prompt = _agentic_plan_prompt(
            host=host,
            user_query=user_query,
            seed_urls=seeds,
            prior_citations=citations,
            last_answer=text,
            step=step,
        )
        plan_raw, plan_cites = _one_call(f"plan_{step}", plan_prompt)
        plan_obj = _parse_json_object(plan_raw)
        if plan_cites:
            for c in plan_cites:
                if c not in citations:
                    citations.append(c)

        stop = False
        next_query = ""
        target_urls: list[str] = []
        if plan_obj:
            stop = bool(plan_obj.get("stop"))
            next_query = str(plan_obj.get("next_query") or "").strip()
            tu = plan_obj.get("target_urls") or []
            if isinstance(tu, list):
                target_urls = [str(u).strip() for u in tu if str(u).strip().startswith(("http://", "https://"))]

        # Promote cited deep URLs to seeds (agent discovers subpages via citations).
        new_seeds: list[str] = []
        for c in (plan_cites or []):
            if urlparse(c).netloc == host:
                new_seeds.append(c)
        for u in target_urls:
            if urlparse(u).netloc == host:
                new_seeds.append(u)
        for u in new_seeds:
            if u not in seeds:
                seeds.append(u)
        seeds = _seeds_for_prompt(seeds, _MAX_SEEDS_PER_HOST)

        if stop:
            break

        # 2) Execute an evidence-focused answer search. Use next_query if provided, else original.
        q = next_query or user_query
        answer_prompt = _agentic_answer_prompt(host=host, user_query=q, seed_urls=seeds)
        t, c = _one_call(f"answer_{step}", answer_prompt)
        if t:
            text = t
        if c:
            for u in c:
                if u not in citations:
                    citations.append(u)

    # Citation URL follow-up: fetch cited pages directly and synthesize from page contents.
    fetched = _fetch_citation_snippets(host, citations)
    diag["fetched_citation_pages"] = len(fetched)
    if fetched:
        synth = _synthesize_from_cited_pages(host, user_query, fetched)
        if synth:
            text = (
                (text or "").strip()
                + "\n\n### Citation URL follow-up\n"
                + synth.strip()
            ).strip()

    # OpenAI mitigation: if hosted search did not traverse to the right child pages, use the
    # deterministic same-host shortlist directly. This avoids handing 300+ URLs to an LLM.
    deterministic_fetched: list[tuple[str, str]] = []
    if provider_preset == "openai" and discovered_urls:
        already = set(citations)
        candidate_urls = [u for u in discovered_urls if u not in already]
        deterministic_fetched = _fetch_same_host_snippets(
            host,
            candidate_urls,
            max_pages=_MAX_FETCHED_CITATIONS_PER_HOST,
        )
        diag["fetched_deterministic_pages"] = len(deterministic_fetched)
        if deterministic_fetched:
            synth = _synthesize_from_cited_pages(host, user_query, deterministic_fetched)
            if synth:
                text = (
                    (text or "").strip()
                    + "\n\n### Deterministic URL follow-up\n"
                    + synth.strip()
                ).strip()
            for u, _snippet in deterministic_fetched:
                if u not in citations:
                    citations.append(u)
    else:
        diag["fetched_deterministic_pages"] = 0

    # Back-compat: single additional retry flag for meta line (true when >1 step).
    diag["retry_used"] = bool(step > 1)

    # Minimal, vendor-agnostic signal: "weak" only means we ended with zero citations.
    diag["final_weak"] = (len(citations) == 0)
    diag["final_citation_count"] = len(citations)
    return text, citations, diag


def _run_hosted_web_aggregate(
    query: str,
    hosts: list[str],
    urls_by_host: dict[str, list[str]],
    *,
    max_results_per_domain: int,
) -> tuple[str, list[dict]]:
    parts: list[str] = []
    citations: list[str] = []
    diags: list[dict] = []
    max_out = 1400

    for host in hosts:
        urls = urls_by_host.get(host) or []
        if not urls:
            continue
        primary = urls[0]
        text, cites, d = _run_hosted_web_for_host(
            user_query=query,
            host=host,
            primary_url=primary,
            all_urls_on_host=urls,
            max_results_per_domain=max_results_per_domain,
            max_output_tokens=max_out,
        )
        diags.append(d)
        if text:
            parts.append(f"## Web results from {host}\n{text}")
        for c in cites:
            if c not in citations:
                citations.append(c)

    if not parts:
        body = "Web search returned no usable results from enabled RC URLs."
    else:
        body = "\n\n---\n\n".join(parts)
        cite_block = ""
        if citations:
            cite_block = "\n\n## Citations\n" + "\n".join(f"- {c}" for c in citations[:40])
        body = body + cite_block

    # Compact, always-on trace line for debugging weak web passes (kept short for the main LLM).
    if diags:
        bits: list[str] = []
        for d in diags:
            attempts = d.get("attempts") or []
            n_att = len(attempts)
            bits.append(
                f"{d.get('host')}:n={n_att},cites={d.get('final_citation_count')},"
                f"retry={bool(d.get('retry_used'))},weak={bool(d.get('final_weak'))}"
            )
        body = body + "\n\n---\n_RC web meta:_ " + "; ".join(bits)

    show_diag = (os.environ.get("RC_WEB_DIAGNOSTICS", "") or "").strip().lower() in ("1", "true", "yes")
    if show_diag and diags:
        lines = [
            "## RC web diagnostics (RC_WEB_DIAGNOSTICS=1)",
            f"- hosts queried: {len(hosts)}",
        ]
        for d in diags:
            attempts = d.get("attempts") or []
            ac = " → ".join(
                f"{a.get('label')}:len={a.get('text_len')},cites={a.get('citation_count')},weak={a.get('weak')}"
                for a in attempts
            )
            lines.append(
                f"- `{d.get('host')}`: seeds={d.get('seed_count')}, retry={d.get('retry_used')}, "
                f"final_cites={d.get('final_citation_count')}, final_weak={d.get('final_weak')} | {ac}"
            )
        body = body + "\n\n" + "\n".join(lines)

    return body, diags


def search_rc_web(query: str, max_domains: int = 5, max_results_per_domain: int = 5) -> str:
    hosts, urls_by_host = _list_rc_hosts(max_domains)
    if not hosts:
        return "No RC URLs are enabled."

    body, _diags = _run_hosted_web_aggregate(
        query,
        hosts,
        urls_by_host,
        max_results_per_domain=max_results_per_domain,
    )
    return body
