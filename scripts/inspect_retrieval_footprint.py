#!/usr/bin/env python3
"""
Inspect three signals related to RAG cost / full reindex vs query embeds:

1) Run history: count search_product_docs and search_rc_web from agent_interactions.metadata
   (tools_used + tool_start events). Optional: --id <interaction_id> for one turn.

2) data/rag/rebuild_log.jsonl: list rebuild_start / rebuild_done / skip_* lines with timestamps.

3) data/rag/faiss_index + state.txt: existence, sizes, mtimes (cold start vs steady state).

Usage:
  python scripts/inspect_retrieval_footprint.py
  python scripts/inspect_retrieval_footprint.py --id 42
  python scripts/inspect_retrieval_footprint.py --last 20
"""
from __future__ import annotations

import argparse
import json
import sqlite3
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "agent.db"
RAG = ROOT / "data" / "rag"
LOG = RAG / "rebuild_log.jsonl"
STATE = RAG / "state.txt"
FAISS_DIR = RAG / "faiss_index"


def _fmt_ts(p: Path) -> str:
    if not p.exists():
        return "(missing)"
    try:
        return datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    except OSError:
        return "?"


def analyze_metadata(meta: dict | None) -> tuple[int, int, list[str], list[str]]:
    """Returns (invocations_product_docs, invocations_rc_web, tools_used dedup list, tool_start titles)."""
    if not meta:
        return 0, 0, [], []
    sp = rc = 0
    tools = [str(t).strip() for t in (meta.get("tools_used") or [])]
    ev_titles: list[str] = []
    # Invocation counts: one per tool_start event (matches Run trace).
    for e in meta.get("events") or []:
        if not isinstance(e, dict) or e.get("type") != "tool_start":
            continue
        title = str(e.get("title") or "")
        ev_titles.append(title)
        if "search_product_docs" in title:
            sp += 1
        if "search_rc_web" in title:
            rc += 1
    return sp, rc, tools, ev_titles


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", type=int, default=None, help="Single agent_interactions.id")
    ap.add_argument("--last", type=int, default=15, help="How many recent interactions to show")
    args = ap.parse_args()

    print("=== (3) FAISS / cold start vs steady state ===")
    print(f"  data/rag/faiss_index/  exists: {FAISS_DIR.is_dir()}")
    idx = FAISS_DIR / "index.faiss"
    pkl = FAISS_DIR / "index.pkl"
    if idx.exists():
        print(f"  index.faiss size: {idx.stat().st_size:,} bytes  mtime: {_fmt_ts(idx)}")
    if pkl.exists():
        print(f"  index.pkl   size: {pkl.stat().st_size:,} bytes  mtime: {_fmt_ts(pkl)}")
    print(f"  state.txt   exists: {STATE.exists()}  mtime: {_fmt_ts(STATE)}")
    if STATE.exists():
        print(f"  fingerprint: {(STATE.read_text(encoding='utf-8') or '').strip()!r}")

    print("\n=== (2) data/rag/rebuild_log.jsonl ===")
    if not LOG.exists():
        print("  (file missing — no logged rebuild events)")
    else:
        lines = LOG.read_text(encoding="utf-8").strip().splitlines()
        print(f"  lines: {len(lines)}")
        phases: dict[str, int] = {}
        for line in lines:
            try:
                o = json.loads(line)
                phases[o.get("phase", "?")] = phases.get(o.get("phase", "?"), 0) + 1
            except json.JSONDecodeError:
                pass
        print(f"  phase counts: {phases}")
        for line in lines[-30:]:
            try:
                o = json.loads(line)
            except json.JSONDecodeError:
                continue
            ts = o.get("ts", "")
            ph = o.get("phase", "")
            base = str(o.get("base_path", ""))[-60:]
            print(f"  {ts}  {ph:28}  …{base}")

        starts = done = skips = 0
        for line in lines:
            try:
                o = json.loads(line)
            except json.JSONDecodeError:
                continue
            p = o.get("phase", "")
            if p == "rebuild_start":
                starts += 1
            elif p == "rebuild_done":
                done += 1
            elif p and "skip" in p:
                skips += 1
        print(f"\n  rebuild_start: {starts}  rebuild_done: {done}  skip_*: {skips}")
        if starts > done:
            print("  NOTE: more rebuild_start than rebuild_done — interrupted run or log truncated.")

    print("\n=== (1) Run history — search_product_docs / search_rc_web ===")
    if not DB.exists():
        print(f"  No database at {DB}")
        return

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    if args.id is not None:
        rows = conn.execute(
            "SELECT id, created_at, trigger_type, metadata FROM agent_interactions WHERE id = ?",
            (args.id,),
        ).fetchall()
    else:
        rows = conn.execute(
            f"""SELECT id, created_at, trigger_type, metadata FROM agent_interactions
                ORDER BY id DESC LIMIT {int(args.last)}"""
        ).fetchall()

    if not rows:
        print("  (no rows)")
        conn.close()
        return

    for r in rows:
        try:
            md = json.loads(r["metadata"]) if r["metadata"] else {}
        except json.JSONDecodeError:
            md = {}
        sp, rc, tools, evs = analyze_metadata(md)
        print(
            f"  id={r['id']}  {str(r['created_at'])[:19]}  {str(r['trigger_type'] or ''):18}  "
            f"search_product_docs≈{sp}  search_rc_web≈{rc}"
        )
        if tools:
            print(f"      tools_used: {tools}")
        if evs:
            print(f"      tool_start: {evs}")

    conn.close()
    print("\nTip: Workbench turns are logged as trigger_type=thread_message (async). Expand Run history in UI or use --id after noting id from /interactions.")


if __name__ == "__main__":
    main()
