"""Hosted web search over enabled RC URLs.

When a URL tree exists for the host, retrieval is **tree-first**: an LLM compares the user
query to candidate URLs (and optional titles from discovery), selects up to ``rc_web_visit_limit``
pages, fetches them, and synthesizes. If the result is **weak** or pages cannot be fetched,
the tool returns an explicit no-evidence message and does **not** fall back to provider web
search for that host (strict drop-on-weak).

If no tree is stored yet, behavior falls back to provider hosted web search (agentic loop)
for that host.
"""

from __future__ import annotations

import json
import os
import re
from urllib.parse import unquote, urlparse

import requests
from langchain_core.messages import HumanMessage

from src.agent.chat_llm import get_chat_llm
from src.agent.tools.hosted_web_search import run_web_search
from src.agent.tools.html_document_text import html_to_document_excerpt_text
from src.runtime_config import effective_llm_model_main, effective_rc_web_visit_limit
from src.db import database

# Medium budget defaults (per search_rc_web invocation).
_MAX_SEEDS_PER_HOST = 12
_MAX_RETRIES_PER_HOST = 1
_WEAK_TEXT_LEN = 140
_MAX_AGENTIC_STEPS_PER_HOST = 3
_MAX_NEW_SEEDS_FROM_CITATIONS = 8
_MAX_FETCHED_CITATIONS_PER_HOST = 6
_MAX_FETCH_CHARS_PER_URL = 12000
_WEAK_TEXT_PHRASES = (
    "i attempted to locate",
    "couldn't locate",
    "could not locate",
    "no publicly available documentation",
    "no results",
    "if you can clarify",
    "reach out to",
    "account representative",
)


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
    noisy_short = {"/ios", "/android", "/web", "/api", "/sdk", "/docs"}
    for h in hits:
        if h in noisy_short:
            continue
        # Prefer endpoint-like paths over single-token fragments.
        if h.count("/") < 2 and len(h) < 10:
            continue
        if h in seen:
            continue
        seen.add(h)
        out.append(h)
        if len(out) >= 8:
            break
    return out


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
    """Plain text excerpt for fetched HTML citations (neutral multi-strategy extractor)."""
    return html_to_document_excerpt_text(raw)


def _citation_url_quality(host: str, citations: list[str]) -> dict:
    """
    Validate citation URLs for quality diagnostics and weak-result detection.
    """
    seen: set[str] = set()
    total = 0
    valid = 0
    same_host = 0
    deep_links = 0
    for raw in citations or []:
        u = (raw or "").strip()
        if not u or u in seen:
            continue
        seen.add(u)
        total += 1
        try:
            pu = urlparse(u)
        except Exception:
            continue
        if pu.scheme not in ("http", "https") or not pu.netloc:
            continue
        valid += 1
        if pu.netloc == host:
            same_host += 1
            path = (pu.path or "").strip("/")
            if path:
                deep_links += 1
    valid_ratio = float(valid) / float(total) if total else 0.0
    deep_ratio = float(deep_links) / float(same_host) if same_host else 0.0
    return {
        "citation_total": total,
        "citation_valid": valid,
        "citation_same_host": same_host,
        "citation_deep_links": deep_links,
        "citation_valid_ratio": round(valid_ratio, 3),
        "citation_deep_ratio": round(deep_ratio, 3),
    }


def _validate_citation_urls(host: str, citations: list[str]) -> tuple[list[str], dict]:
    """
    Normalize and de-duplicate same-host citation URLs without live fetch validation.

    Rationale: provider-discovered doc URLs may reject bot fetches transiently (403/429) while
    still being valid links for user-visible follow-up. We keep them and let the bounded
    citation fetch step decide what is fetchable.
    """
    uniq: list[str] = []
    seen: set[str] = set()
    dropped = 0
    for raw in citations or []:
        u = (raw or "").strip()
        if not u:
            dropped += 1
            continue
        try:
            pu = urlparse(u)
        except Exception:
            dropped += 1
            continue
        if pu.scheme not in ("http", "https"):
            dropped += 1
            continue
        if pu.netloc != host:
            dropped += 1
            continue
        # Canonicalize trailing slash for host root to avoid noisy duplicates.
        if (pu.path or "").strip() in ("", "/"):
            u = f"{pu.scheme}://{pu.netloc}/"
        if u in seen:
            continue
        seen.add(u)
        uniq.append(u)
    stats = {
        "checked": 0,
        "input_count": len(citations or []),
        "valid_count": len(uniq),
        "dropped_count": dropped,
    }
    return uniq, stats


def _is_weak_citation_quality(host: str, citations: list[str]) -> tuple[bool, dict]:
    q = _citation_url_quality(host, citations)
    # Weak when citations are absent/invalid/shallow to the point follow-up is unlikely to help.
    weak = (
        q["citation_total"] == 0
        or q["citation_valid"] == 0
        or q["citation_same_host"] == 0
        or q["citation_valid"] < 2
        or (q["citation_same_host"] >= 2 and q["citation_deep_links"] == 0)
    )
    return weak, q


def _is_weak_web_result(host: str, text: str, citations: list[str]) -> tuple[bool, dict]:
    weak_cites, q = _is_weak_citation_quality(host, citations)
    t = (text or "").strip().lower()
    text_weak = (
        len(t) < _WEAK_TEXT_LEN
        or any(p in t for p in _WEAK_TEXT_PHRASES)
        or "not found in cited pages" in t
    )
    # Single root citation (home/reference landing) is still weak for API troubleshooting.
    one_root_only = (
        q["citation_same_host"] == 1
        and q["citation_deep_links"] == 0
    )
    weak = bool(weak_cites or text_weak or one_root_only)
    out = dict(q)
    out["text_weak"] = bool(text_weak)
    out["one_root_only"] = bool(one_root_only)
    return weak, out


def _is_weak_tree_result(host: str, text: str, citations: list[str], *, fetched_count: int) -> tuple[bool, dict]:
    """
    Strict-local tree results are based on pages we selected and fetched ourselves.
    One exact deep documentation page can be sufficient evidence, unlike provider
    hosted web search where multiple citations are a stronger quality signal.
    """
    q = _citation_url_quality(host, citations)
    t = (text or "").strip().lower()
    text_weak = (
        len(t) < _WEAK_TEXT_LEN
        or any(p in t for p in _WEAK_TEXT_PHRASES)
        or "not found in cited pages" in t
    )
    weak_cites = (
        q["citation_total"] == 0
        or q["citation_valid"] == 0
        or q["citation_same_host"] == 0
        or q["citation_deep_links"] == 0
    )
    weak = bool(weak_cites or text_weak)
    out = dict(q)
    out["text_weak"] = bool(text_weak)
    out["fetched_count"] = int(fetched_count or 0)
    out["tree_single_deep_citation_allowed"] = True
    return weak, out


def _fetch_citation_snippets(host: str, citations: list[str], *, max_pages: int = _MAX_FETCHED_CITATIONS_PER_HOST) -> list[tuple[str, str]]:
    """
    Fetch top citation URLs and extract plain text snippets.
    This makes citations actionable evidence for a second-pass synthesis.
    """
    out: list[tuple[str, str]] = []
    seen: set[str] = set()
    for u in citations:
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


def _tree_no_evidence_message(
    host: str,
    *,
    reason: str,
    selected_urls: list[str],
    fetched_count: int,
) -> str:
    n_sel = len(selected_urls or [])
    return (
        f"No verifiable documentation evidence could be produced from the stored URL tree "
        f"for **{host}** (strict quality gate).\n\n"
        f"**Reason:** {reason}\n\n"
        f"URLs selected for fetch: {n_sel}. Pages successfully fetched: {fetched_count}.\n\n"
        "Try rebuilding the URL tree (Knowledge tab), increasing **Visit limit**, or rephrasing the query. "
        "Provider web search is not used after a weak or empty tree-based pass for this host."
    )


def _synthesize_from_fetched_pages(host: str, user_query: str, fetched: list[tuple[str, str]]) -> str:
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
            config={"run_name": "search_rc_web.url_tree_synthesis", "tags": ["search_rc_web", "url_tree"]},
        )
        return str(resp.content or "").strip()
    except Exception:
        return ""


def _tree_node_metadata(node: dict) -> dict:
    raw = (node or {}).get("metadata")
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, str) and raw.strip():
        try:
            obj = json.loads(raw)
            return obj if isinstance(obj, dict) else {}
        except Exception:
            return {}
    return {}


def _url_path_text(url: str) -> str:
    """Turn a URL path into neutral text context for the LLM selector."""
    path = unquote((urlparse(url).path or "").strip("/"))
    bits = [b for b in re.split(r"[/_.-]+", path) if b]
    return " ".join(bits[:24])


def _format_tree_candidate_lines(nodes_batch: list[dict]) -> list[str]:
    """One line per candidate for the URL selector LLM with neutral local metadata."""
    lines: list[str] = []
    for n in nodes_batch:
        u = str((n or {}).get("url") or "").strip()
        if not u:
            continue
        parts = [u]
        title = str((n or {}).get("title") or "").strip()
        if title:
            parts.append(f"title={title[:200]}")
        meta = _tree_node_metadata(n if isinstance(n, dict) else {})
        h1 = str(meta.get("h1") or "").strip()
        if h1 and h1 != title:
            parts.append(f"h1={h1[:180]}")
        desc = str(meta.get("description") or "").strip()
        if desc:
            parts.append(f"description={desc[:260]}")
        path_text = _url_path_text(u)
        if path_text:
            parts.append(f"path_terms={path_text[:220]}")
        try:
            depth = int((n or {}).get("depth") or 0)
            parts.append(f"depth={depth}")
        except Exception:
            pass
        parent = str((n or {}).get("parent_url") or "").strip()
        if parent:
            parts.append(f"parent={parent[:180]}")
        lines.append("- " + " | ".join(parts))
    return lines


def _llm_pick_urls_for_batch(*, user_query: str, batch_lines: list[str], allowed_urls: set[str], pick_n: int) -> list[dict]:
    if not batch_lines:
        return []
    prompt = (
        "You are selecting documentation URLs for evidence retrieval.\n"
        "Each candidate line is: URL plus neutral local metadata when available "
        "(title, h1, description, URL path terms, depth, parent URL).\n"
        "Compare the **full user query** (all questions and constraints) to each candidate. "
        "Choose only URLs whose content is likely to help answer those asks.\n"
        "Use the metadata as hints only: prefer semantic fit across URL path, title/heading, and description. "
        "Do not pick URLs just because they share one generic word with the query.\n"
        "Return STRICT JSON ONLY:\n"
        "{\n"
        '  "selected": [\n'
        '    {"url":"https://...", "reason":"short reason", "confidence":0.0}\n'
        "  ]\n"
        "}\n"
        f"Select up to {int(max(1, pick_n))} URLs. confidence must be in [0,1].\n\n"
        f"User query:\n{(user_query or '').strip()[:2800]}\n\n"
        "Candidates:\n"
        + "\n".join(batch_lines)
    )
    try:
        llm = get_chat_llm(model=effective_llm_model_main(), temperature=0.0)
        resp = llm.invoke([HumanMessage(content=prompt)])
        obj = _parse_json_object(str(resp.content or ""))
        sel = (obj or {}).get("selected") or []
        if not isinstance(sel, list):
            return []
        out: list[dict] = []
        for it in sel:
            if not isinstance(it, dict):
                continue
            u = str(it.get("url") or "").strip()
            if u not in allowed_urls:
                continue
            reason = str(it.get("reason") or "").strip()
            try:
                conf = float(it.get("confidence") or 0.0)
            except Exception:
                conf = 0.0
            out.append({"url": u, "reason": reason, "confidence": conf})
        return out
    except Exception:
        return []


def _select_tree_urls(user_query: str, nodes: list[dict], *, visit_limit: int) -> tuple[list[str], list[dict], list[dict]]:
    """
    Two-pass agent-only URL selection from tree nodes (URL + optional title).
    Returns (selected_urls, ranked_meta_for_diagnostics, final_pick_items_with_reason).
    """
    if not nodes:
        return [], [], []

    uniq_nodes: list[dict] = []
    seen_u: set[str] = set()
    for n in nodes:
        u = str((n or {}).get("url") or "").strip()
        if not u or u in seen_u:
            continue
        seen_u.add(u)
        uniq_nodes.append(n if isinstance(n, dict) else {"url": u})

    batch_size = 120
    pick_each = max(4, min(12, visit_limit * 2))
    first_pass: list[dict] = []
    for i in range(0, len(uniq_nodes), batch_size):
        batch_nodes = uniq_nodes[i : i + batch_size]
        lines = _format_tree_candidate_lines(batch_nodes)
        allowed = {str((x or {}).get("url") or "").strip() for x in batch_nodes}
        allowed.discard("")
        first_pass.extend(
            _llm_pick_urls_for_batch(
                user_query=user_query,
                batch_lines=lines,
                allowed_urls=allowed,
                pick_n=pick_each,
            )
        )

    best_by_url: dict[str, dict] = {}
    for it in first_pass:
        u = str(it.get("url") or "").strip()
        if not u:
            continue
        prev = best_by_url.get(u)
        if prev is None or float(it.get("confidence") or 0.0) > float(prev.get("confidence") or 0.0):
            best_by_url[u] = it
    shortlist = list(best_by_url.values())
    shortlist.sort(key=lambda x: float(x.get("confidence") or 0.0), reverse=True)
    shortlist_nodes = shortlist[: max(visit_limit * 8, 24)]
    shortlist_lines = []
    shortlist_allowed: set[str] = set()
    for it in shortlist_nodes:
        u = str(it.get("url") or "").strip()
        if not u:
            continue
        shortlist_allowed.add(u)
        reason = str(it.get("reason") or "").strip()
        conf = float(it.get("confidence") or 0.0)
        shortlist_lines.append(f"- {u} | prior_confidence={conf:.3f} | prior_pick_reason={reason[:160]}")

    final_pick = _llm_pick_urls_for_batch(
        user_query=user_query,
        batch_lines=shortlist_lines,
        allowed_urls=shortlist_allowed,
        pick_n=visit_limit,
    )
    if not final_pick and shortlist:
        # Still agentic: retain the strongest URLs the first LLM pass selected when the
        # final arbitration pass returns empty or unparsable JSON.
        final_pick = [
            {
                "url": str(it.get("url") or "").strip(),
                "reason": "Retained from first-pass LLM URL selection after empty final arbitration. "
                + str(it.get("reason") or "").strip(),
                "confidence": float(it.get("confidence") or 0.0),
            }
            for it in shortlist[:visit_limit]
            if str(it.get("url") or "").strip()
        ]
    selected = [str(it.get("url") or "").strip() for it in final_pick if str(it.get("url") or "").strip()]

    ranked_meta: list[dict] = []
    for it in shortlist[: min(len(shortlist), max(visit_limit * 8, 24))]:
        ranked_meta.append(
            {
                "url": str(it.get("url") or "").strip(),
                "score": {
                    "confidence": float(it.get("confidence") or 0.0),
                    "reason": str(it.get("reason") or "").strip(),
                },
            }
        )
    return selected, ranked_meta, final_pick


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
    visit_limit = max(1, min(int(effective_rc_web_visit_limit()), 50))
    diag: dict = {
        "host": host,
        "primary_url": primary_url,
        "seed_count": len(seeds),
        "attempts": [],
    }

    # URL-tree-first path: LLM semantic URL selection + fetch + synthesis. Strict drop-on-weak: no provider fallback.
    tree_nodes = database.list_rc_url_tree_by_host(host, enabled_main_only=True, limit=10000)
    tree_urls = [str((n or {}).get("url") or "").strip() for n in tree_nodes if str((n or {}).get("url") or "").strip()]
    if tree_urls:
        diag["tree_strict_no_provider_fallback"] = True
        selected_urls, ranked_urls, final_pick_items = _select_tree_urls(
            user_query, tree_nodes, visit_limit=visit_limit
        )
        diag["tree_url_count"] = len(tree_urls)
        diag["selected_url_count"] = len(selected_urls)
        diag["selected_urls"] = list(selected_urls)
        diag["selector_final_pick"] = [
            {
                "url": str(it.get("url") or "").strip(),
                "reason": str(it.get("reason") or "").strip(),
                "confidence": float(it.get("confidence") or 0.0),
            }
            for it in (final_pick_items or [])
            if isinstance(it, dict)
        ]
        diag["top_ranked_urls"] = ranked_urls[: min(len(ranked_urls), 20)]
        diag["retry_used"] = False

        if not selected_urls:
            diag["weak_drop_reason"] = (
                "Semantic URL selector returned no candidates from the tree "
                "(empty final pick and no non-LLM fallback)."
            )
            diag["final_weak"] = True
            diag["final_citation_count"] = 0
            diag["final_citation_quality"] = {}
            diag["fetched_citation_pages"] = 0
            diag["attempts"].append(
                {
                    "label": "url_tree",
                    "text_len": 0,
                    "citation_count": 0,
                    "citation_quality": {},
                    "weak": True,
                    "weak_drop_reason": diag["weak_drop_reason"],
                }
            )
            msg = _tree_no_evidence_message(
                host,
                reason=diag["weak_drop_reason"],
                selected_urls=[],
                fetched_count=0,
            )
            return msg, [], diag

        fetched = _fetch_citation_snippets(host, selected_urls, max_pages=visit_limit)
        diag["fetched_citation_pages"] = len(fetched)

        if not fetched:
            diag["weak_drop_reason"] = (
                "No selected pages could be fetched successfully "
                "(HTTP errors, empty body, or unsupported content type)."
            )
            diag["final_weak"] = True
            diag["final_citation_count"] = 0
            diag["final_citation_quality"] = {}
            diag["attempts"].append(
                {
                    "label": "url_tree",
                    "text_len": 0,
                    "citation_count": 0,
                    "citation_quality": {"citation_total": len(selected_urls), "citation_valid": 0},
                    "weak": True,
                    "weak_drop_reason": diag["weak_drop_reason"],
                }
            )
            msg = _tree_no_evidence_message(
                host,
                reason=diag["weak_drop_reason"],
                selected_urls=selected_urls,
                fetched_count=0,
            )
            return msg, [], diag

        text = _synthesize_from_fetched_pages(host, user_query, fetched)
        citations = [u for (u, _t) in fetched]
        final_weak, final_quality = _is_weak_tree_result(host, text, citations, fetched_count=len(fetched))
        diag["final_citation_quality"] = final_quality
        diag["final_weak"] = final_weak
        diag["final_citation_count"] = len(citations)

        if final_weak:
            diag["weak_drop_reason"] = (
                "Evidence quality gate marked the tree-based answer as weak "
                "(e.g. too short, generic 'not found' phrasing, or shallow citations)."
            )
            diag["attempts"].append(
                {
                    "label": "url_tree",
                    "text_len": len(text or ""),
                    "citation_count": len(citations),
                    "citation_quality": final_quality,
                    "weak": True,
                    "weak_drop_reason": diag["weak_drop_reason"],
                }
            )
            msg = _tree_no_evidence_message(
                host,
                reason=diag["weak_drop_reason"],
                selected_urls=selected_urls,
                fetched_count=len(fetched),
            )
            return msg, [], diag

        diag["attempts"].append(
            {
                "label": "url_tree",
                "text_len": len(text or ""),
                "citation_count": len(citations),
                "citation_quality": final_quality,
                "weak": False,
            }
        )
        return text, citations, diag

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
        weak_result, q = _is_weak_web_result(host, text, cites)
        diag["attempts"].append(
            {
                "label": label,
                "text_len": len(text),
                "citation_count": len(cites),
                "citation_quality": q,
                "weak": weak_result,
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
            weak_now, _ = _is_weak_web_result(host, text, citations)
            # Override early stop once when citation quality is still weak.
            if weak_now and step < _MAX_AGENTIC_STEPS_PER_HOST:
                stop = False
            else:
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

    # Provider fallback path: keep citations and metadata; no citation-followup synthesis.
    validated_citations, vstats = _validate_citation_urls(host, citations)
    diag["citation_validation"] = vstats
    citations = validated_citations
    diag["fetched_citation_pages"] = 0

    # Back-compat: single additional retry flag for meta line (true when >1 step).
    diag["retry_used"] = bool(step > 1)

    final_weak, final_quality = _is_weak_web_result(host, text, citations)
    diag["final_citation_quality"] = final_quality
    diag["final_weak"] = final_weak
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
            if d.get("tree_strict_no_provider_fallback"):
                lines.append("  tree_mode: strict (no provider fallback after tree pass for this host)")
            wdr = d.get("weak_drop_reason")
            if wdr:
                lines.append(f"  weak_drop_reason: {wdr}")
            sfp = d.get("selector_final_pick") or []
            if sfp:
                pick_bits = [
                    f"{p.get('url')} (conf={p.get('confidence')})"
                    for p in sfp[:8]
                    if isinstance(p, dict)
                ]
                lines.append("  selector_final_pick: " + "; ".join(pick_bits))
            sel = d.get("selected_urls") or []
            if sel and not sfp:
                lines.append("  selected_urls: " + "; ".join(str(u) for u in sel[:8]))
            fq = d.get("final_citation_quality") or {}
            if fq:
                lines.append(
                    f"  citation_quality: total={fq.get('citation_total')}, valid={fq.get('citation_valid')}, "
                    f"same_host={fq.get('citation_same_host')}, deep_links={fq.get('citation_deep_links')}, "
                    f"valid_ratio={fq.get('citation_valid_ratio')}, deep_ratio={fq.get('citation_deep_ratio')}"
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
