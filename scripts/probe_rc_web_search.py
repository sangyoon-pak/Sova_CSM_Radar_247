#!/usr/bin/env python3
"""
Compare hosted web search (OpenRouter vs OpenAI) for a long prompt + single RC domain.

Loads repo .env into os.environ before importing app settings. Does not use DB overrides
for keys (reads OPENROUTER_* / OPENAI_* / LLM_MODEL* from env only).

Usage (from repo root email_draft_agent):
  python scripts/probe_rc_web_search.py --preset openrouter --max-results 10
  python scripts/probe_rc_web_search.py --preset openai
  python scripts/probe_rc_web_search.py --preset both --max-results 5
  python scripts/probe_rc_web_search.py --preset both --save-outputs
  python scripts/probe_rc_web_search.py --preset both --save-outputs --output-dir /tmp/rc_probe
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_dotenv_simple(path: Path) -> None:
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip()
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
        if key and key not in os.environ:
            os.environ[key] = val


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--fixture",
        type=Path,
        default=ROOT / "data/reports/fixtures/client_query_kr_full.txt",
        help="Prompt file (default: client_query_kr_full.txt)",
    )
    parser.add_argument(
        "--url",
        default="https://docs.aiqua.appier.com/",
        help="Documentation base URL (domain filter for hosted search)",
    )
    parser.add_argument("--preset", choices=("openrouter", "openai", "both"), default="both")
    parser.add_argument("--max-results", type=int, default=10, help="OpenRouter web plugin max_results only")
    parser.add_argument("--max-output-tokens", type=int, default=4000)
    parser.add_argument(
        "--save-outputs",
        action="store_true",
        help="Write full model answers (+ citations) under --output-dir",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "data/reports/probe_rc_web_search",
        help="Directory for --save-outputs (default: data/reports/probe_rc_web_search)",
    )
    args = parser.parse_args()

    load_dotenv_simple(ROOT / ".env")
    sys.path.insert(0, str(ROOT))

    from src.agent.tools.hosted_web_search import _web_search_openai, _web_search_openrouter
    from src.config import settings

    query = args.fixture.read_text(encoding="utf-8").strip()
    if not query:
        print("Fixture empty", file=sys.stderr)
        return 1

    model = settings.llm_model_for_main
    print("=== probe_rc_web_search ===")
    print(f"fixture: {args.fixture}")
    print(f"url:     {args.url}")
    print(f"model:   {model}")
    print(f"prompt chars: {len(query)}")
    print()

    def format_report(label: str, res, *, max_cite_lines: int | None = 25) -> str:
        text = (res.text or "").strip()
        cites = list(res.citations or [])
        lines = [
            label,
            "",
            f"answer_chars: {len(text)}",
            f"citations: {len(cites)}",
            "",
            "## Citations",
            "",
        ]
        if max_cite_lines is None:
            cite_enum = cites
        else:
            cite_enum = cites[: max_cite_lines or len(cites)]
        for i, u in enumerate(cite_enum, 1):
            lines.append(f"{i}. {u}")
        if max_cite_lines is not None and len(cites) > len(cite_enum):
            lines.append(f"... +{len(cites) - len(cite_enum)} more")
        lines.extend(["", "## Answer", "", text, ""])
        return "\n".join(lines)

    def summarize(label: str, res) -> None:
        text = (res.text or "").strip()
        cites = list(res.citations or [])
        print(f"--- {label} ---")
        print(f"answer chars: {len(text)}")
        print(f"citations:    {len(cites)}")
        for i, u in enumerate(cites[:25], 1):
            print(f"  {i}. {u}")
        if len(cites) > 25:
            print(f"  ... +{len(cites) - 25} more")
        print()
        preview = text[:6000]
        print(preview)
        if len(text) > len(preview):
            print(f"\n... [{len(text) - len(preview)} more chars]")
        print()

    presets = ("openrouter", "openai") if args.preset == "both" else (args.preset,)
    out_dir = args.output_dir.resolve()
    if args.save_outputs:
        out_dir.mkdir(parents=True, exist_ok=True)

    for p in presets:
        if p == "openrouter":
            key = (settings.openrouter_api_key or "").strip()
            if not key:
                print("OPENROUTER_API_KEY missing; skip openrouter", file=sys.stderr)
                continue
            res = _web_search_openrouter(
                query=query,
                model=model,
                url=args.url,
                max_results=args.max_results,
                max_output_tokens=args.max_output_tokens,
                api_key=key,
            )
            label = f"OpenRouter (max_results={args.max_results})"
            summarize(label, res)
            if args.save_outputs:
                path = out_dir / "openrouter_full.txt"
                path.write_text(
                    format_report(label, res, max_cite_lines=None),
                    encoding="utf-8",
                )
                print(f"Wrote {path}", file=sys.stderr)
        else:
            key = (settings.openai_api_key or "").strip()
            if not key:
                print("OPENAI_API_KEY missing; skip openai", file=sys.stderr)
                continue
            res = _web_search_openai(
                query=query,
                model=model,
                url=args.url,
                max_output_tokens=args.max_output_tokens,
                api_key=key,
            )
            label = "OpenAI web_search (no max_results knob in client)"
            summarize(label, res)
            if args.save_outputs:
                path = out_dir / "openai_full.txt"
                path.write_text(
                    format_report(label, res, max_cite_lines=None),
                    encoding="utf-8",
                )
                print(f"Wrote {path}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
