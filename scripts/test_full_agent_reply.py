#!/usr/bin/env python3
"""Run the main email agent end-to-end on a saved query (no Gmail).

Export ``OPENROUTER_API_KEY`` (and related vars) in your shell before running, or save keys in Configure and use the app DB.

Example:
  .venv/bin/python scripts/test_full_agent_reply.py \\
    --query-file data/reports/fixtures/client_query_kr_full.txt \\
    --output-file data/reports/full_agent_reply_latest.txt

Include retrieval ( what search_product_docs returned to the model ) for RAG tuning:
  .venv/bin/python scripts/test_full_agent_reply.py \\
    --query-file data/reports/fixtures/client_query_kr_full.txt \\
    --output-file data/reports/full_agent_reply_latest.txt \\
    --with-retrieval \\
    --retrieval-json data/reports/full_agent_retrieval_latest.json

This consumes OpenRouter (or OpenAI) credits: term extract, rerank, sufficiency,
refine inside search_with_agent, plus the main agent turns.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def _format_retrieval_section(log: list[dict]) -> str:
    """Human-readable block to append after the draft reply."""
    lines = [
        "",
        "=" * 72,
        "# Retrieval — search_product_docs (what the model received)",
        "",
    ]
    for i, entry in enumerate(log, 1):
        lines.append(f"## Tool call {i}")
        lines.append("")
        lines.append("### Query")
        lines.append(entry.get("query", ""))
        lines.append("")
        subs = entry.get("focus_subqueries") or []
        lines.append(f"### Focus sub-queries ({len(subs)})")
        for j, sq in enumerate(subs, 1):
            lines.append(f"{j}. {sq}")
        lines.append("")
        matches = entry.get("matches") or []
        lines.append(f"### Matches after rerank ({len(matches)} chunks)")
        for m in matches:
            fn = m.get("file", "")
            ln = m.get("line_num", 0)
            bits = [f"{fn} L{ln}"]
            if m.get("source"):
                bits.append(str(m["source"]))
            if m.get("score") is not None:
                bits.append(f"score={m['score']}")
            lines.append(f"- {' | '.join(bits)}")
        lines.append("")
        lines.append("### Formatted context (capped by max_context_chars in search_with_agent)")
        lines.append(entry.get("context_passed_to_llm") or "")
        lines.append("")
        lines.append("---")
        lines.append("")
    if len(log) == 0:
        lines.append("_(No search_product_docs calls recorded — logging was enabled but tool was not used.)_")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", type=str, default="")
    ap.add_argument("--query-file", type=str, default="")
    ap.add_argument("--output-file", type=str, default="")
    ap.add_argument(
        "--with-retrieval",
        action="store_true",
        help="Append retrieval section (queries + chunks + formatted context) to output / stdout.",
    )
    ap.add_argument(
        "--retrieval-json",
        type=str,
        default="",
        help="Write structured log (matches + context_passed_to_llm) as JSON.",
    )
    args = ap.parse_args()

    if args.query_file:
        body = Path(args.query_file).read_text(encoding="utf-8").strip()
    else:
        body = args.query.strip()

    if not body:
        raise SystemExit("Provide --query or --query-file")

    instruction = """다음은 고객 메일 본문입니다.
- Gmail(fetch_inbox_emails)는 호출하지 마세요.
- AIQUA/Appier 기술 문의이므로 search_product_docs를 반드시 사용해, 위 메일 전체(또는 핵심 질문)로 문서를 검색하고 근거를 수집하세요. 가능하면 첫 검색에 본문 전체(특히 번호 질문)를 넣으세요.
- 고객 메일이 AIQUA만 다루는 경우(AV API, quantumgraph, AIQUA 콘솔 등) 출처는 AIQUA 문서(파일명에 aiqua 등)만 인용하고, AIRIS·BotBonnie·Enterprise 허브 문서는 인용하지 마세요.
- 확인 요청 사항이 번호로 나열되어 있으면 1, 2, 3… 순서로 한국어 답변 초안을 작성하세요.
- 검색 결과로 근거를 확보하지 못한 항목은 추측하지 말고, KB에 관련 문서가 없음을 밝히고 Appier CSM/지원팀 확인을 권하세요.
- 메일 초안만 작성하고 발송은 하지 마세요.

--- 고객 메일 ---
"""

    from src.agent.email_agent import run_agent
    from src.agent.tools.search_agent import enable_retrieval_logging, take_retrieval_log

    log_retrieval = args.with_retrieval or bool(args.retrieval_json)
    if log_retrieval:
        enable_retrieval_logging()
    retrieval_log: list[dict] = []
    try:
        reply = run_agent(instruction + body)
    finally:
        if log_retrieval:
            retrieval_log = take_retrieval_log()

    if args.retrieval_json:
        jpath = Path(args.retrieval_json)
        jpath.parent.mkdir(parents=True, exist_ok=True)
        jpath.write_text(
            json.dumps(retrieval_log, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"retrieval_json:{jpath.resolve()}")

    out_text = reply
    if args.with_retrieval:
        out_text = reply + _format_retrieval_section(retrieval_log)

    if args.output_file:
        out = Path(args.output_file)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(out_text, encoding="utf-8")
        print(f"saved:{out.resolve()}")
    else:
        print(out_text)


if __name__ == "__main__":
    main()
