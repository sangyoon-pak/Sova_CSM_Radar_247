"""URL-tree discovery helpers for RC documentation domains."""

from __future__ import annotations

import re
from collections import deque
from urllib.parse import urljoin, urlparse, urlunparse
from xml.etree import ElementTree as ET

import requests

_HREF_RE = re.compile(r'href=["\']([^"\']+)["\']', re.I)


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
    return urlunparse((pu.scheme, pu.netloc, path.rstrip("/") or "/", "", "", ""))


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


def _fetch_sitemap_urls(base_url: str, host: str, timeout_s: int) -> list[str]:
    sitemap_url = urljoin(base_url, "/sitemap.xml")
    try:
        r = requests.get(
            sitemap_url,
            timeout=timeout_s,
            headers={"User-Agent": "Mozilla/5.0 (compatible; SovaRCDiscover/1.0)"},
        )
        if r.status_code >= 400:
            return []
        text = r.text or ""
        if "<urlset" not in text and "<sitemapindex" not in text:
            return []
        root = ET.fromstring(text)
    except Exception:
        return []

    urls: list[str] = []
    ns = ""
    if root.tag.startswith("{") and "}" in root.tag:
        ns = root.tag.split("}", 1)[0] + "}"
    for loc in root.findall(f".//{ns}loc"):
        v = (loc.text or "").strip()
        n = normalize_url(v, host=host)
        if n:
            urls.append(n)
    seen: set[str] = set()
    out: list[str] = []
    for u in urls:
        if u in seen:
            continue
        seen.add(u)
        out.append(u)
    return out


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
            r = requests.get(
                cur,
                timeout=timeout_s,
                headers={"User-Agent": "Mozilla/5.0 (compatible; SovaRCDiscover/1.0)"},
            )
        except Exception:
            continue
        if r.status_code >= 400:
            continue
        ctype = (r.headers.get("Content-Type") or "").lower()
        if "text/html" not in ctype and "application/xhtml+xml" not in ctype:
            continue
        for u in _extract_same_host_links(r.text or "", page_url=cur, host=host):
            if _add(u, d + 1, cur):
                q.append((u, d + 1))
            if len(discovered) >= max_urls:
                break

    return discovered, by_depth

