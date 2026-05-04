"""URL-tree discovery helpers for RC documentation domains."""

from __future__ import annotations

import html as html_lib
import re
from collections import deque
from urllib.parse import urljoin, urlparse, urlunparse
from xml.etree import ElementTree as ET

import requests

_HREF_RE = re.compile(r'href=["\']([^"\']+)["\']', re.I)
_TITLE_RE = re.compile(r"(?is)<title[^>]*>(.*?)</title>")
_META_DESC_RE = re.compile(
    r"""(?is)<meta\b(?=[^>]*\bname\s*=\s*["']description["'])(?=[^>]*\bcontent\s*=\s*["']([^"']+)["'])[^>]*>"""
)
_H1_RE = re.compile(r"(?is)<h1\b[^>]*>(.*?)</h1>")
_TAG_RE = re.compile(r"(?s)<[^>]+>")
_ASSET_EXT_RE = re.compile(
    r"\.(?:png|jpe?g|gif|webp|svg|ico|css|js|mjs|map|zip|tar|gz|tgz|bz2|7z|"
    r"mp4|mov|avi|webm|mp3|wav|pdf|woff2?|ttf|eot)(?:$|[?#])",
    re.I,
)
_SITEMAP_RE = re.compile(r"(?im)^\s*sitemap:\s*(\S+)\s*$")


def normalize_url(raw: str, *, host: str) -> str | None:
    u = (raw or "").strip()
    if not u:
        return None
    pu = urlparse(u)
    if pu.scheme not in ("http", "https"):
        return None
    if pu.netloc != host:
        return None
    path = pu.path or "/"
    if not path.startswith("/"):
        path = "/" + path
    low_path = path.lower()
    if "http://" in low_path or "https://" in low_path:
        return None
    if _ASSET_EXT_RE.search(low_path):
        return None
    return urlunparse((pu.scheme, pu.netloc, path.rstrip("/") or "/", "", "", ""))


def _clean_html_text(raw: str, max_chars: int = 240) -> str:
    text = html_lib.unescape(_TAG_RE.sub(" ", raw or ""))
    text = re.sub(r"\s+", " ", text).strip()
    return text[:max_chars]


def _extract_page_metadata(html: str) -> dict:
    """Extract neutral page metadata to help downstream agentic URL selection."""
    title = ""
    desc = ""
    h1 = ""
    mt = _TITLE_RE.search(html or "")
    if mt:
        title = _clean_html_text(mt.group(1), max_chars=180)
    md = _META_DESC_RE.search(html or "")
    if md:
        desc = _clean_html_text(md.group(1), max_chars=260)
    mh = _H1_RE.search(html or "")
    if mh:
        h1 = _clean_html_text(mh.group(1), max_chars=180)
    meta: dict[str, str] = {}
    if desc:
        meta["description"] = desc
    if h1:
        meta["h1"] = h1
    return {"title": title, "metadata": meta}


def _extract_same_host_links(html: str, *, page_url: str, host: str) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for m in _HREF_RE.finditer(html or ""):
        href = (m.group(1) or "").strip()
        if not href or href.startswith(("mailto:", "javascript:", "#")):
            continue
        abs_u = urljoin(page_url, href)
        n = normalize_url(abs_u, host=host)
        if not n or n in seen:
            continue
        seen.add(n)
        out.append(n)
    return out


def _parse_sitemap_locs(text: str) -> tuple[list[str], bool]:
    """Return (<loc> values, is_sitemap_index)."""
    root = ET.fromstring(text)
    is_index = root.tag.endswith("sitemapindex")
    ns = ""
    if root.tag.startswith("{") and "}" in root.tag:
        ns = root.tag.split("}", 1)[0] + "}"
    locs = [(loc.text or "").strip() for loc in root.findall(f".//{ns}loc")]
    return [x for x in locs if x], is_index


def _fetch_text(url: str, timeout_s: int) -> tuple[str, str, int]:
    r = requests.get(
        url,
        timeout=timeout_s,
        headers={"User-Agent": "Mozilla/5.0 (compatible; SovaRCDiscover/1.0)"},
    )
    return (r.text or "", (r.headers.get("Content-Type") or "").lower(), int(r.status_code))


def _candidate_sitemap_urls(base_url: str, timeout_s: int) -> list[str]:
    out = [urljoin(base_url, "/sitemap.xml"), urljoin(base_url, "/sitemap_index.xml")]
    robots_url = urljoin(base_url, "/robots.txt")
    try:
        text, _ctype, status = _fetch_text(robots_url, timeout_s)
        if status < 400:
            out.extend(m.group(1).strip() for m in _SITEMAP_RE.finditer(text or ""))
    except Exception:
        pass
    seen: set[str] = set()
    uniq: list[str] = []
    for u in out:
        if not u or u in seen:
            continue
        seen.add(u)
        uniq.append(u)
    return uniq


def _fetch_sitemap_urls(base_url: str, host: str, timeout_s: int, max_sitemaps: int = 20) -> list[str]:
    queue = deque(_candidate_sitemap_urls(base_url, timeout_s))
    seen_sitemaps: set[str] = set()
    urls: list[str] = []
    seen_urls: set[str] = set()

    while queue and len(seen_sitemaps) < max_sitemaps:
        sitemap_url = queue.popleft()
        if sitemap_url in seen_sitemaps:
            continue
        seen_sitemaps.add(sitemap_url)
        pu = urlparse(sitemap_url)
        if pu.scheme not in ("http", "https") or pu.netloc != host:
            continue
        try:
            text, _ctype, status = _fetch_text(sitemap_url, timeout_s)
            if status >= 400:
                continue
            if "<urlset" not in text and "<sitemapindex" not in text:
                continue
            locs, is_index = _parse_sitemap_locs(text)
        except Exception:
            continue

        for loc in locs:
            if is_index:
                if loc not in seen_sitemaps:
                    queue.append(loc)
                continue
            n = normalize_url(loc, host=host)
            if not n or n in seen_urls:
                continue
            seen_urls.add(n)
            urls.append(n)
    return urls


def discover_url_tree(
    *,
    base_url: str,
    max_urls: int,
    max_depth: int,
    timeout_s: int,
) -> tuple[list[dict], dict[str, int]]:
    """
    Discover same-host URLs and return tree nodes:
    [{url, depth, parent_url}, ...], plus depth histogram.
    """
    pu = urlparse(base_url)
    if pu.scheme not in ("http", "https") or not pu.netloc:
        raise ValueError("base_url must be an absolute http(s) URL")
    host = pu.netloc
    base_norm = normalize_url(base_url, host=host)
    if not base_norm:
        raise ValueError("base_url host/scheme invalid")

    discovered: list[dict] = []
    seen: set[str] = set()
    by_depth: dict[str, int] = {}
    parent_map: dict[str, str | None] = {base_norm: None}

    def _add(u: str, d: int, parent_url: str | None) -> bool:
        if u in seen:
            return False
        if len(discovered) >= max_urls:
            return False
        seen.add(u)
        discovered.append({"url": u, "depth": d, "parent_url": parent_url})
        by_depth[str(d)] = by_depth.get(str(d), 0) + 1
        parent_map[u] = parent_url
        return True

    q: deque[tuple[str, int]] = deque()
    _add(base_norm, 0, None)
    q.append((base_norm, 0))

    for su in _fetch_sitemap_urls(base_norm, host, timeout_s):
        if len(discovered) >= max_urls:
            break
        path_depth = len([p for p in (urlparse(su).path or "/").split("/") if p])
        logical_depth = min(max_depth, max(1, path_depth))
        _add(su, logical_depth, base_norm)

    while q and len(discovered) < max_urls:
        cur, d = q.popleft()
        if d >= max_depth:
            continue
        try:
            body, ctype, status = _fetch_text(cur, timeout_s)
        except Exception:
            continue
        if status >= 400:
            continue
        if "text/html" not in ctype and "application/xhtml+xml" not in ctype:
            continue
        page_meta = _extract_page_metadata(body)
        if page_meta.get("title") or page_meta.get("metadata"):
            for node in discovered:
                if node.get("url") == cur:
                    node.update({k: v for k, v in page_meta.items() if v})
                    break
        for u in _extract_same_host_links(body, page_url=cur, host=host):
            if _add(u, d + 1, cur):
                q.append((u, d + 1))
            if len(discovered) >= max_urls:
                break

    return discovered, by_depth

