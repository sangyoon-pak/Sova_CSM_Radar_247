"""Vendor-neutral HTML → readable plain text for short excerpts (RC fetches, citations).

Strategy (no curated host lists):
- Collect candidate DOM regions: per-page ``<article>`` blocks (pick best by visible text),
  first ``[role="main"]``, ``<main>``, JSON-LD ``articleBody``, then full document.
- Convert chosen HTML → text with :mod:`html.parser`, dropping common *site chrome* tags
  (``nav``, top-level ``aside``/``footer``/``header``) while preserving the same tags *inside*
  ``<article>`` where they usually carry titles and notes—not global sidebars.

This stays stdlib-only and deterministic; it is **best-effort** for SPAs and non-semantic markup.
"""

from __future__ import annotations

import html
import json
import re
from html.parser import HTMLParser


# Candidate must contribute at least this much *visible* text to compete (skip empty shells).
_MIN_VISIBLE_CHARS = 64
# Bound work on pathological pages.
_MAX_ARTICLE_BLOCKS = 16

_JSON_LD_SCRIPT_RE = re.compile(
    r'<script[^>]+type\s*=\s*["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.I | re.DOTALL,
)


def _normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").strip())


def _extract_balanced_inner_at(html: str, open_match: re.Match, tag: str) -> tuple[str, int] | None:
    """Return (inner HTML, index after closing tag) for the element opened at ``open_match``."""
    tl = tag.lower()
    token_re = re.compile(rf"(<{re.escape(tl)}\b[^>]*>|</{re.escape(tl)}\s*>)", re.I)
    inner_start = open_match.end()
    depth = 1
    for tm in token_re.finditer(html, inner_start):
        piece = tm.group(1)
        if piece.lower().startswith(f"</{tl}"):
            depth -= 1
            if depth == 0:
                return html[inner_start : tm.start()], tm.end()
        else:
            depth += 1
    return None


def _enumerate_balanced_inners(html: str, tag: str, *, limit: int = _MAX_ARTICLE_BLOCKS) -> list[str]:
    tl = tag.lower()
    opener = re.compile(rf"<{tl}\b[^>]*>", re.I)
    out: list[str] = []
    idx = 0
    while len(out) < limit:
        m = opener.search(html, idx)
        if not m:
            break
        got = _extract_balanced_inner_at(html, m, tl)
        if got is None:
            idx = m.end()
            continue
        inner, close_end = got
        out.append(inner)
        idx = close_end
    return out


def _find_first_open_tag_match_with_role_main(html: str) -> re.Match | None:
    """Scan start tags; return the match for the opening tag whose attrs include ``role="main"``."""
    tag_open = re.compile(r"<\s*([a-zA-Z][^\s>/]*)\b([^>]*)>")
    for m in tag_open.finditer(html):
        attrs = m.group(2) or ""
        if re.search(r"""\brole\s*=\s*(['"])main\1""", attrs, re.I) or re.search(
            r"\brole\s*=\s*main\b(?=[\s/>])", attrs, re.I
        ):
            return m
    return None


def _extract_role_main_inner_html(raw: str) -> str | None:
    m = _find_first_open_tag_match_with_role_main(raw)
    if not m:
        return None
    tag = m.group(1)
    got = _extract_balanced_inner_at(raw, m, tag)
    return got[0] if got else None


def _iter_json_ld_article_bodies(raw: str) -> list[str]:
    out: list[str] = []

    def walk(o: object) -> None:
        if isinstance(o, dict):
            for k in ("articleBody", "description"):
                v = o.get(k)
                if isinstance(v, str) and len(v.strip()) >= _MIN_VISIBLE_CHARS:
                    out.append(v.strip())
            g = o.get("@graph")
            if isinstance(g, list):
                for x in g:
                    walk(x)
            for v in o.values():
                if isinstance(v, (dict, list)):
                    walk(v)
        elif isinstance(o, list):
            for x in o:
                walk(x)

    for block in _JSON_LD_SCRIPT_RE.finditer(raw or ""):
        try:
            data = json.loads(block.group(1).strip())
        except Exception:
            continue
        walk(data)
    return out


class _VisibleTextExtractor(HTMLParser):
    """Extract visible text, skipping scripts and common *site* chrome (not in-article headers/asides)."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._article_depth = 0
        self._suppress: list[bool] = []
        self._parts: list[str] = []

    def _attrs_dict(self, attrs: list[tuple[str, str | None]]) -> dict[str, str]:
        return {k.lower(): (v or "").strip() for k, v in attrs}

    def _enter_silent(self, silent: bool) -> None:
        self._suppress.append(silent)

    def _leave_silent(self) -> None:
        if self._suppress:
            self._suppress.pop()

    def _silent_now(self) -> bool:
        return any(self._suppress)

    def _chrome_start(self, tag: str, attrs_d: dict[str, str]) -> bool:
        if tag in {"script", "style", "noscript", "template"}:
            return True
        role = attrs_d.get("role", "").strip().strip("\"'").lower()
        if attrs_d.get("aria-hidden", "").strip().strip("\"'").lower() == "true":
            return True
        if tag == "nav" or role == "navigation":
            return True
        # Landmark roles usually wrap site chrome; inside <article> they can annotate real headings — only strip at root.
        if role in {"banner", "contentinfo", "complementary", "search"}:
            return self._article_depth == 0
        # Sidebars/top-level wrappers: outside articles only (keep in-article asides/callouts/headers).
        if self._article_depth == 0 and tag in {"aside", "footer", "header"}:
            return True
        return False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_d = self._attrs_dict(attrs)
        if tag == "article":
            self._article_depth += 1
        silent = self._chrome_start(tag, attrs_d)
        self._enter_silent(silent)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_d = self._attrs_dict(attrs)
        silent = self._chrome_start(tag, attrs_d)
        self._enter_silent(silent)
        self._leave_silent()

    def handle_endtag(self, tag: str) -> None:
        if self._suppress:
            self._leave_silent()
        if tag == "article":
            self._article_depth = max(0, self._article_depth - 1)

    def handle_data(self, data: str) -> None:
        if self._silent_now():
            return
        t = data.strip()
        if t:
            self._parts.append(t)

    def text(self) -> str:
        return _normalize_ws(html.unescape(" ".join(self._parts)))


def visible_text_from_html_fragment(fragment: str) -> str:
    parser = _VisibleTextExtractor()
    try:
        parser.feed(fragment or "")
        parser.close()
    except Exception:
        return _normalize_ws(html.unescape(re.sub(r"(?s)<[^>]+>", " ", fragment or "")))
    return parser.text()


def _score_fragment(html: str) -> int:
    return len(visible_text_from_html_fragment(html))


def _pick_best_html_fragment(raw: str) -> tuple[str, str]:
    """
    Return (source_label, html_fragment).

    ``source_label`` is for debugging only; behavior is determined by visible-text score.
    """
    s = raw or ""
    semantic: list[tuple[int, int, str, str]] = []

    articles = _enumerate_balanced_inners(s, "article")
    best_article_inner = ""
    best_article_score = 0
    for inner in articles:
        sc = _score_fragment(inner)
        if sc > best_article_score:
            best_article_score = sc
            best_article_inner = inner
    if best_article_inner:
        semantic.append((best_article_score, 0, "article", best_article_inner))

    role_main = _extract_role_main_inner_html(s) or ""
    if role_main:
        semantic.append((_score_fragment(role_main), 1, "role_main", role_main))

    main_open = re.search(r"<main\b[^>]*>", s, re.I)
    main_inner = ""
    if main_open:
        got = _extract_balanced_inner_at(s, main_open, "main")
        main_inner = got[0] if got else ""
    if main_inner:
        semantic.append((_score_fragment(main_inner), 2, "main", main_inner))

    for body in _iter_json_ld_article_bodies(s):
        lg = len(_normalize_ws(html.unescape(body)))
        semantic.append((lg, 3, "json_ld", body))

    viable_semantic = [(sc, pr, lbl, frag) for sc, pr, lbl, frag in semantic if sc >= _MIN_VISIBLE_CHARS]
    if viable_semantic:
        max_score = max(c[0] for c in viable_semantic)
        epsilon = max(250, max_score // 8)
        top = [c for c in viable_semantic if c[0] + epsilon >= max_score]
        top.sort(key=lambda c: (-c[0], c[1]))
        return (top[0][2], top[0][3])

    return ("full", s)


def html_to_document_excerpt_text(raw_html: str) -> str:
    """
    Neutral main-content excerpt: pick a structural region, then visible-text extraction.

    ``raw_html`` should be server-rendered HTML. Client-only SPAs often return shells; nothing can fix that
    without a headless browser.
    """
    label, fragment = _pick_best_html_fragment(raw_html)
    if label == "json_ld":
        return _normalize_ws(html.unescape(fragment))
    return visible_text_from_html_fragment(fragment)


__all__ = ["html_to_document_excerpt_text", "visible_text_from_html_fragment"]
