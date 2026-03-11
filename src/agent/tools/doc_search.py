"""Grep-based document search."""
import re
import subprocess
from collections.abc import Callable
from pathlib import Path

from src.config import settings


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


def search_documents(query: str, search_terms: list[str] | None = None, llm_extract: Callable[[str], list[str]] | None = None, max_results_per_term: int = 10) -> list[dict]:
    kb = settings.kb_path_resolved
    if not kb.exists():
        return []
    if search_terms is None and llm_extract:
        search_terms = llm_extract(query)
    if not search_terms:
        search_terms = [w for w in re.findall(r"\b\w{3,}\b", query) if len(w) > 2][:5]
    all_matches = []
    seen = set()
    for term in search_terms[:5]:
        if not term or len(term) < 2:
            continue
        use_phrase = " " in term.strip()
        matches = run_grep(term, kb, max_results=max_results_per_term, fixed=use_phrase)
        for m in matches:
            key = (m["file"], m["line_num"])
            if key not in seen:
                seen.add(key)
                all_matches.append(m)
    all_matches.sort(key=lambda x: (x["file"], x["line_num"]))
    return all_matches[:30]


def format_matches_for_context(matches: list[dict], max_chars: int = 4000) -> str:
    parts = []
    total = 0
    for m in matches:
        block = f"[From {m['file']} line {m['line_num']}]\n{m['line']}"
        if total + len(block) > max_chars:
            break
        parts.append(block)
        total += len(block)
    return "\n\n---\n\n".join(parts) if parts else "No relevant documents found."
