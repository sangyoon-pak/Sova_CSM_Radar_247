#!/usr/bin/env python3
"""End-to-end Search Agent test runner.

Runs `search_with_agent()` directly so we can validate full retrieval orchestration:
- term extraction
- retrieval (RAG/grep/FTS via search_documents)
- reranking
- sufficiency + refinement loop
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from dotenv import load_dotenv


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", type=str, default="")
    ap.add_argument("--query-file", type=str, default="")
    ap.add_argument("--output-file", type=str, default="")
    ap.add_argument("--max-iterations", type=int, default=2)
    ap.add_argument("--rerank-threshold", type=int, default=3)
    ap.add_argument("--max-context-chars", type=int, default=9000)
    args = ap.parse_args()

    project_root = Path(__file__).resolve().parents[1]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    load_dotenv(project_root / ".env")
    # Import after dotenv so pydantic settings read populated env.
    from src.agent.tools.search_agent import search_with_agent

    if args.query_file:
        query = Path(args.query_file).read_text(encoding="utf-8").strip()
    else:
        query = args.query.strip()

    if not query:
        raise SystemExit("Provide --query or --query-file")

    result = search_with_agent(
        query=query,
        max_iterations=args.max_iterations,
        rerank_threshold=args.rerank_threshold,
        max_context_chars=args.max_context_chars,
    )

    if args.output_file:
        out_path = Path(args.output_file)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(result, encoding="utf-8")
        print(f"saved:{out_path}")
    else:
        print(result)


if __name__ == "__main__":
    main()

