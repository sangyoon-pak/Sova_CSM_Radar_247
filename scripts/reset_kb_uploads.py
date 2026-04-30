#!/usr/bin/env python3
"""
Remove all uploaded knowledge-base documents and derived search indexes.

This does **not** delete conversation history, prompts, or `rc_urls` (hosted RC URLs).
Stop the API server before running so SQLite files are not locked.

Clears:
  - All rows in `kb_documents`
  - Every file under `KNOWLEDGE_BASE_PATH` (default `data/user_kb/files`)
  - `data/kb_fts.db` (FTS; recreated on next search)
  - `data/rag/` (FAISS index, tombstones, state, rebuild log)

Usage:
  python scripts/reset_kb_uploads.py --yes
"""
from __future__ import annotations

import argparse
import shutil
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _rm_sqlite_family(path: Path) -> None:
    if not path.exists():
        return
    path.unlink()
    for suffix in ("-wal", "-shm", "-journal"):
        side = Path(str(path) + suffix)
        if side.exists():
            side.unlink()


def _clear_dir_contents(d: Path) -> None:
    if not d.is_dir():
        return
    for child in d.iterdir():
        if child.is_file() or child.is_symlink():
            child.unlink()
        elif child.is_dir():
            shutil.rmtree(child)


def main() -> int:
    ap = argparse.ArgumentParser(description="Reset KB uploads + FTS/FAISS (keeps agent.db threads/settings).")
    ap.add_argument("--yes", action="store_true", help="Required confirmation.")
    args = ap.parse_args()
    if not args.yes:
        print("Refusing to run without --yes.", file=sys.stderr)
        return 2

    from src.config import settings

    data = ROOT / "data"
    db_path = Path(settings.database_path)
    if not db_path.is_absolute():
        db_path = (ROOT / db_path).resolve()
    else:
        db_path = db_path.resolve()

    kb_fts = (data / "kb_fts.db").resolve()
    rag_dir = (data / "rag").resolve()
    kb_files = Path(settings.knowledge_base_path)
    if not kb_files.is_absolute():
        kb_files = (ROOT / kb_files).resolve()
    else:
        kb_files = kb_files.resolve()

    print("Clearing kb_documents in:", db_path)
    conn = sqlite3.connect(str(db_path), timeout=30)
    try:
        conn.execute("DELETE FROM kb_documents")
        conn.commit()
    finally:
        conn.close()

    print("Emptying KB directory:", kb_files)
    kb_files.mkdir(parents=True, exist_ok=True)
    _clear_dir_contents(kb_files)

    print("Removing FTS:", kb_fts)
    _rm_sqlite_family(kb_fts)

    print("Removing RAG dir:", rag_dir)
    if rag_dir.is_dir():
        shutil.rmtree(rag_dir)

    print("Done. Restart the server; uploads will rebuild indexes on first use / reindex.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
