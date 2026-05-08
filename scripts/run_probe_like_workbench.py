#!/usr/bin/env python3
"""
Run the same agent path as Workbench **probe with non-empty text** (POST /threads/send
with probe=true and your pasted client body): ``run_agent(..., probe=True)``, then
``merge_csm_actions_metadata`` + ``format_probe_thread_reply`` like the API worker.

This is **not** the same as clicking **Scan inbox** (empty probe → ``get_probe_trigger_message()``).
Use this script to see structured **action cards** metadata from a pasted client email.

Requires working LLM keys (Configure / .env) and, for real inbox tools, Gmail (gog).
Optional: ``--seed-rc-url`` upserts one enabled RC URL before the run (e.g. your hosted docs root).

Usage (from repo root ``Sova_CSM_Radar_247``)::

  python scripts/run_probe_like_workbench.py --save-dir data/reports/probe_workbench_run
  python scripts/run_probe_like_workbench.py --fixture path/to/email.txt --seed-rc-url 'https://docs.example.com/'
"""
from __future__ import annotations

import argparse
import json
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
    parser = argparse.ArgumentParser(description="Probe run_agent + action-card merge like /threads/send")
    parser.add_argument(
        "--fixture",
        type=Path,
        default=ROOT / "data/reports/fixtures/client_query_kr_full.txt",
    )
    parser.add_argument(
        "--save-dir",
        type=Path,
        default=ROOT / "data/reports/probe_workbench_run",
        help="Directory for raw output, merged metadata JSON, and Workbench-style reply",
    )
    parser.add_argument(
        "--seed-rc-url",
        default="",
        help="If set, upsert this RC URL as enabled before running (empty = skip)",
    )
    parser.add_argument(
        "--ui-locale",
        choices=("ko", "en", ""),
        default="ko",
        help="Passed to merge metadata like the API (empty = omit)",
    )
    args = parser.parse_args()

    load_dotenv_simple(ROOT / ".env")
    sys.path.insert(0, str(ROOT))

    from src.agent.email_agent import run_agent
    from src.agent.probe_actions import format_probe_thread_reply, merge_csm_actions_metadata
    from src.db import database
    from src.runtime_config import (
        effective_customer_email_domains,
        effective_guardrail_exclude_intent_keywords,
        effective_guardrail_exclude_sender_domains,
        effective_guardrail_include_intent_keywords,
        effective_guardrail_include_sender_domains,
        effective_guardrail_strictness,
    )

    body = args.fixture.read_text(encoding="utf-8").strip()
    if not body:
        print("Fixture empty", file=sys.stderr)
        return 1

    if (args.seed_rc_url or "").strip():
        u = args.seed_rc_url.strip()
        database.upsert_rc_url(url=u, enabled=True)
        print(f"Seeded RC URL (enabled): {u}", file=sys.stderr)

    metadata: dict = {
        "tools_used": [],
        "events": [],
        "guardrail_include_sender_domains": effective_guardrail_include_sender_domains(),
        "guardrail_exclude_sender_domains": effective_guardrail_exclude_sender_domains(),
        "guardrail_include_intent_keywords": effective_guardrail_include_intent_keywords(),
        "guardrail_exclude_intent_keywords": effective_guardrail_exclude_intent_keywords(),
        "guardrail_strictness": effective_guardrail_strictness(),
        "customer_email_domains": effective_customer_email_domains(),
    }
    loc = (args.ui_locale or "").strip().lower()
    if loc in ("ko", "en"):
        metadata["ui_locale"] = loc

    print("Running run_agent(probe=True) … (Gmail + tools may take a while)", file=sys.stderr)
    output = run_agent(body, probe=True)
    existing = database.latest_dashboard_actions_by_gmail_thread()
    merged = merge_csm_actions_metadata(output, metadata, existing_by_thread=existing)
    reply = format_probe_thread_reply(output, merged)

    out_dir = args.save_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "raw_model_output.txt").write_text(output or "", encoding="utf-8")
    (out_dir / "workbench_thread_reply.txt").write_text(reply or "", encoding="utf-8")
    # Compact JSON: actions + diagnostics + parse errors
    slim = {
        "csm_actions": merged.get("csm_actions"),
        "csm_skipped_note": merged.get("csm_skipped_note"),
        "csm_actions_parse_error": merged.get("csm_actions_parse_error"),
        "csm_probe_diagnostics": merged.get("csm_probe_diagnostics"),
        "csm_policy_warnings": merged.get("csm_policy_warnings"),
    }
    (out_dir / "merged_action_metadata.json").write_text(
        json.dumps(slim, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote:\n  {out_dir / 'raw_model_output.txt'}\n  {out_dir / 'workbench_thread_reply.txt'}\n  {out_dir / 'merged_action_metadata.json'}", file=sys.stderr)
    print("\n--- workbench_thread_reply (preview) ---\n")
    print(reply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
