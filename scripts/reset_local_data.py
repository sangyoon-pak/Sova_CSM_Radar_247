#!/usr/bin/env python3
"""
Destructive local reset: application SQLite, KB FTS, FAISS/RAG artifacts, and uploaded KB files.

To wipe **only** KB uploads + search indexes while keeping threads and settings, use
`scripts/reset_kb_uploads.py` instead.

Stop the server before running (otherwise DB files may be locked).

Usage:
  python scripts/reset_local_data.py --yes
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

# Project root = parent of scripts/
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _rm_sqlite_family(path: Path) -> None:
    """Remove main DB and SQLite sidecar files (-wal, -shm, -journal)."""
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
    ap = argparse.ArgumentParser(description="Reset local app data (destructive).")
    ap.add_argument(
        "--yes",
        action="store_true",
        help="Required: confirm you want to delete all local data.",
    )
    args = ap.parse_args()
    if not args.yes:
        print("Refusing to run without --yes (destructive).", file=sys.stderr)
        return 2

    data = ROOT / "data"
    from src.config import settings

    db_path = Path(settings.database_path)
    if not db_path.is_absolute():
        db_path = (ROOT / db_path).resolve()
    else:
        db_path = db_path.resolve()

    kb_fts = (data / "kb_fts.db").resolve()
    rag_dir = (data / "rag").resolve()
    kb_files = (data / "user_kb" / "files").resolve()
    # Legacy/orphan filename sometimes seen under data/; not used by src (canonical is agent.db).
    orphan_app_db = (data / "app.db").resolve()

    print("Removing:", db_path, kb_fts, rag_dir, f"{kb_files}/*", sep="\n  ")
    if orphan_app_db.exists():
        print("  (also)", orphan_app_db)
    _rm_sqlite_family(db_path)
    _rm_sqlite_family(kb_fts)
    _rm_sqlite_family(orphan_app_db)
    if rag_dir.is_dir():
        shutil.rmtree(rag_dir)
    kb_files.mkdir(parents=True, exist_ok=True)
    _clear_dir_contents(kb_files)

    from src.db.database import init_db

    init_db()
    print("Done. Empty schema recreated (init_db). Restart the server.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
