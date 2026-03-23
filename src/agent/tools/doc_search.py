"""Grep-based document search."""
import re
import subprocess
from collections.abc import Callable
from pathlib import Path

from src.config import settings


_METADATA_LINE_RE = re.compile(
    r"^\s*(guide_keywords|guide_summary|doc_type|product|content_type|language|source|file_id|filename)\s*:",
    re.IGNORECASE,
)


def run_grep(pattern: str, base_path: Path, max_results: int = 20, fixed: bool = False) -> list[dict]:
    """Run ripgrep. Use fixed=True for phrase search (literal match, no regex)."""
    base_path = Path(base_path)
    if not base_path.exists():
        return []
    base_args = ["--max-count", str(max_results), "--line-number", "--no-heading", "--color", "never", "-S"]
    try:
        args = ["rg"] + base_args + (["-F", pattern] if fixed else [pattern]) + [str(base_path)]
        result = subprocess.run(
            args,
            capture_output=True, text=True, timeout=30,
        )
    except FileNotFoundError:
        try:
            grep_args = ["grep", "-r", "-n", "-i", "-m", str(max_results)]
            if fixed:
                grep_args.extend(["-F", pattern])
            else:
                grep_args.append(pattern)
            grep_args.append(str(base_path))
            result = subprocess.run(
                grep_args,
                capture_output=True, text=True, timeout=30,
            )
        except FileNotFoundError:
            return []
    if result.returncode not in (0, 1):
        return []
    out = []
    for line in (result.stdout or "").strip().split("\n"):
        if ":" not in line:
            continue
        parts = line.split(":", 2)
        if len(parts) >= 3:
            out.append({"file": Path(parts[0]).name, "line_num": int(parts[1]) if parts[1].isdigit() else 0, "line": parts[2].strip(), "path": parts[0]})
    return out[:max_results]


def _is_metadata_line(text: str) -> bool:
    t = (text or "").strip()
    return t == "---" or bool(_METADATA_LINE_RE.match(t))


def _get_snippet(path: str, line_num: int, window: int = 3) -> str:
    """
    Return +/- window lines around the matched line.
    Keeps retrieval more actionable than single-line keyword matches.
    """
    p = Path(path)
    if not p.exists() or line_num <= 0:
        return ""
    try:
        lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception:
        return ""
    start = max(1, line_num - window)
    end = min(len(lines), line_num + window)
    snippet_lines = []
    for idx in range(start, end + 1):
        marker = ">>" if idx == line_num else "  "
        snippet_lines.append(f"{marker} L{idx}: {lines[idx - 1]}")
    return "\n".join(snippet_lines).strip()


def _expand_alias_terms(query: str, terms: list[str]) -> list[str]:
    """
    Expand common shorthand so retrieval doesn't miss obvious docs.
    Examples: AQ -> AIQUA, RC -> reference card.
    """
    expanded = list(terms)
    q = query.lower()
    if "aq" in q or "aiqua" in q:
        expanded.extend(["AIQUA", "AIQUA RC", "AIQUA reference card", "AIQUA web"])
    if "rc" in q:
        expanded.extend(["reference card", "rc part", "integration"])
    if "web" in q:
        expanded.extend(["web integration", "web sdk", "javascript", "js sdk"])
    # Deduplicate while preserving order
    seen = set()
    out = []
    for t in expanded:
        key = t.strip().lower()
        if key and key not in seen:
            seen.add(key)
            out.append(t.strip())
    return out


def search_documents(query: str, search_terms: list[str] | None = None, llm_extract: Callable[[str], list[str]] | None = None, max_results_per_term: int = 10) -> list[dict]:
    kb = settings.kb_path_resolved
    if not kb.exists():
        return []
    if search_terms is None and llm_extract:
        search_terms = llm_extract(query)
    if not search_terms:
        search_terms = [w for w in re.findall(r"\b\w{3,}\b", query) if len(w) > 2][:5]
    search_terms = _expand_alias_terms(query, search_terms)
    all_matches = []
    seen = set()
    for term in search_terms[:8]:
        if not term or len(term) < 2:
            continue
        use_phrase = " " in term.strip()
        matches = run_grep(term, kb, max_results=max_results_per_term, fixed=use_phrase)
        for m in matches:
            if _is_metadata_line(m.get("line", "")):
                # Skip YAML/frontmatter-like hits that often cause weak answers.
                continue
            m["snippet"] = _get_snippet(m.get("path", ""), m.get("line_num", 0), window=3)
            key = (m["file"], m["line_num"])
            if key not in seen:
                seen.add(key)
                all_matches.append(m)
    all_matches.sort(key=lambda x: (x["file"], x["line_num"]))
    return all_matches[:40]


def format_matches_for_context(matches: list[dict], max_chars: int = 4000) -> str:
    parts = []
    total = 0
    for m in matches:
        snippet = m.get("snippet") or m.get("line", "")
        block = f"[From {m['file']} line {m['line_num']}]\n{snippet}"
        if total + len(block) > max_chars:
            break
        parts.append(block)
        total += len(block)
    return "\n\n---\n\n".join(parts) if parts else "No relevant documents found."
