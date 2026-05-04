#!/usr/bin/env python3
"""
Discover same-host documentation URLs from a base RC URL.

Features:
- BFS crawl with configurable max depth and max URLs
- Uses sitemap.xml when available, then HTML anchor discovery
- Stores discovered URLs in rc_urls (enabled=False by default)
- Prints a depth-grouped tree for quick inspection

Usage:
  .venv/bin/python scripts/discover_rc_url_tree.py \
    --base-url https://docs.aiqua.appier.com/ \
    --max-urls 300 \
    --max-depth 2 \
    --store
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.db import database  # noqa: E402
from src.agent.tools.rc_url_tree_discovery import discover_url_tree, normalize_url  # noqa: E402


def _print_tree(urls: list[str], base_url: str) -> None:
    host = urlparse(base_url).netloc
    groups: dict[int, list[str]] = {}
    for u in urls:
        p = urlparse(u)
        depth = len([x for x in (p.path or "/").split("/") if x])
        groups.setdefault(depth, []).append(u)
    print(f"# Host: {host}")
    for d in sorted(groups.keys()):
        print(f"\n## Depth {d} ({len(groups[d])})")
        for u in groups[d]:
            print(u)


def main() -> int:
    ap = argparse.ArgumentParser(description="Discover RC sub-URLs for a base docs URL.")
    ap.add_argument("--base-url", required=True, help="Base documentation URL (e.g. https://docs.aiqua.appier.com/)")
    ap.add_argument("--max-urls", type=int, default=300, help="Maximum URLs to keep (default: 300)")
    ap.add_argument("--max-depth", type=int, default=2, help="BFS depth limit from base page (default: 2)")
    ap.add_argument("--timeout-s", type=int, default=10, help="Per-request timeout seconds (default: 10)")
    ap.add_argument("--store", action="store_true", help="Upsert discovered URLs into rc_urls as disabled.")
    args = ap.parse_args()

    max_urls = max(1, min(int(args.max_urls), 5000))
    max_depth = max(0, min(int(args.max_depth), 8))
    timeout_s = max(3, min(int(args.timeout_s), 30))

    nodes, by_depth = discover_url_tree(
        base_url=args.base_url,
        max_urls=max_urls,
        max_depth=max_depth,
        timeout_s=timeout_s,
    )
    urls = [str((n or {}).get("url") or "").strip() for n in nodes if str((n or {}).get("url") or "").strip()]

    if args.store:
        host = urlparse(args.base_url).netloc
        base_norm = normalize_url(args.base_url, host=host) or args.base_url
        for u in urls:
            database.upsert_rc_url(url=u, enabled=False)
        database.clear_rc_url_tree(base_norm)
        database.upsert_rc_url_tree_nodes(main_rc_url=base_norm, nodes=nodes)

    print(f"Discovered URLs: {len(urls)}")
    print(f"Depth histogram: {by_depth}")
    print(f"Stored to rc_urls: {'yes' if args.store else 'no'}")
    _print_tree(urls, args.base_url)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

