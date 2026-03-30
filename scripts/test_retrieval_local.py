#!/usr/bin/env python3
"""Local retrieval tester (no LLM/API calls).

Usage examples:
  python scripts/test_retrieval_local.py --query "your long query"
  python scripts/test_retrieval_local.py --query-file /tmp/query.txt

This script:
1) Splits long queries into sub-queries
2) Extracts hard tokens (URLs, paths, snake_case fields)
3) Runs local grep/FTS retrieval only (no search_with_agent, no OpenRouter)
4) Prints coverage of hard tokens and top snippets
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.agent.tools.doc_search import search_documents, format_matches_for_context


STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "that",
    "this",
    "what",
    "when",
    "where",
    "which",
    "from",
    "then",
    "into",
    "through",
    "using",
    "please",
}


def split_subqueries(text: str) -> list[str]:
    anchor = text.find("확인 요청 사항")
    scoped = text[anchor:] if anchor >= 0 else text
    lines = [ln.strip() for ln in scoped.splitlines() if ln.strip()]
    out: list[str] = []

    # Prefer numbered bullet blocks if present.
    cur: list[str] = []
    for ln in lines:
        if re.match(r"^\d+\.", ln):
            if cur:
                out.append(" ".join(cur).strip())
                cur = []
            cur.append(ln)
        else:
            cur.append(ln)
    if cur:
        out.append(" ".join(cur).strip())

    # If not meaningful, fallback to sentence chunks.
    if len(out) <= 1:
        sentences = re.split(r"(?<=[?.!])\s+", text.replace("\n", " ").strip())
        out = [s.strip() for s in sentences if s.strip()]

    # Keep top 6 subqueries to limit noise.
    return out[:6]


def extract_hard_tokens(text: str) -> list[str]:
    hard: list[str] = []
    hard.extend(re.findall(r"https?://\S+", text))
    hard.extend(re.findall(r"/[A-Za-z0-9_./\-]+/?", text))
    hard.extend(re.findall(r"\b[a-z]+(?:_[a-z0-9]+){1,}\b", text))
    for token in ["appId", "appSecret", "identifier", "identifier_value", "user_id", "device"]:
        if token in text:
            hard.append(token)

    seen = set()
    out = []
    for t in hard:
        k = t.strip()
        if not k:
            continue
        lk = k.lower()
        if lk in seen:
            continue
        seen.add(lk)
        out.append(k)
    return out


def extract_soft_terms(text: str) -> list[str]:
    toks = re.findall(r"[A-Za-z0-9_]{2,}|[가-힣]{2,}", text)
    seen = set()
    out = []
    for t in toks:
        lk = t.lower()
        if lk in STOPWORDS:
            continue
        if lk in seen:
            continue
        seen.add(lk)
        out.append(t)
    return out[:10]


def run_local_retrieval(query: str) -> dict:
    subqueries = split_subqueries(query)
    global_hard = extract_hard_tokens(query)
    global_soft = extract_soft_terms(query)

    all_matches: list[dict] = []
    seen = set()
    by_subq: dict[str, int] = {}

    for sq in subqueries:
        # Preserve global intent across subqueries to avoid drift.
        terms = extract_hard_tokens(sq) + global_hard + extract_soft_terms(sq) + global_soft[:8]
        matches = search_documents(
            query=sq,
            search_terms=terms,
            llm_extract=None,
            max_results_per_term=8,
        )
        by_subq[sq] = len(matches)
        for m in matches:
            key = (m.get("file"), m.get("line_num"))
            if key in seen:
                continue
            seen.add(key)
            all_matches.append(m)

    # Hard-token coverage on retrieved text.
    token_hits = defaultdict(int)
    combined = "\n".join((m.get("snippet") or m.get("line") or "") for m in all_matches).lower()
    for tok in global_hard:
        token_hits[tok] = 1 if tok.lower() in combined else 0

    # Consolidated ranking for report readability.
    def _diag_score(m: dict) -> tuple[int, int, int]:
        src = str(m.get("source", "grep"))
        src_score = 3 if src == "rag" else (2 if src == "grep" else 1)
        text = (m.get("snippet") or m.get("line") or "").lower()
        hard = 1 if any(t.lower() in text for t in global_hard) else 0
        aiqua = 1 if "aiqua" in str(m.get("file", "")).lower() or "aiqua" in text else 0
        return (aiqua, hard, src_score)

    all_matches.sort(key=lambda m: (_diag_score(m)[0], _diag_score(m)[1], _diag_score(m)[2]), reverse=True)

    return {
        "subqueries": subqueries,
        "by_subq_count": by_subq,
        "global_hard_tokens": global_hard,
        "token_hits": dict(token_hits),
        "matches": all_matches,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", type=str, default="")
    ap.add_argument("--query-file", type=str, default="")
    ap.add_argument("--max-context-chars", type=int, default=5000)
    args = ap.parse_args()

    if args.query_file:
        with open(args.query_file, "r", encoding="utf-8") as f:
            query = f.read().strip()
    else:
        query = args.query.strip()

    if not query:
        raise SystemExit("Provide --query or --query-file")

    result = run_local_retrieval(query)

    print("=== Sub-queries ===")
    for i, sq in enumerate(result["subqueries"], start=1):
        print(f"{i}. {sq[:180]}")

    print("\n=== Matches per sub-query ===")
    for sq, c in result["by_subq_count"].items():
        print(f"- {c:>2} : {sq[:120]}")

    print("\n=== Hard-token coverage ===")
    if not result["global_hard_tokens"]:
        print("(no hard tokens detected)")
    else:
        for tok in result["global_hard_tokens"]:
            status = "HIT" if result["token_hits"].get(tok) else "MISS"
            print(f"- {status:4} {tok}")

    print("\n=== Retrieved context ===")
    print(format_matches_for_context(result["matches"], max_chars=args.max_context_chars))


if __name__ == "__main__":
    main()

