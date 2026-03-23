"""Doc upload ingestion helpers.

The knowledge base is searched via grep over plain text/markdown files.
So for now we normalize uploads into UTF-8 markdown files under knowledge-base/.
"""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

from fastapi import UploadFile


_SAFE_NAME_RE = re.compile(r"[^a-zA-Z0-9._-]+")


def _safe_filename(name: str) -> str:
    name = name.strip()
    name = name.replace(" ", "_")
    name = _SAFE_NAME_RE.sub("_", name)
    return name or "uploaded_doc"


def normalize_uploaded_text(filename: str, content: bytes) -> tuple[str, str]:
    """Return (normalized_filename, normalized_markdown_text)."""
    # Try UTF-8 first; fall back to latin1 to avoid hard failures on odd encodings.
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        text = content.decode("latin1", errors="replace")

    # Normalize extension to .md
    norm_name = _safe_filename(filename)
    ext = Path(norm_name).suffix.lower()
    if ext in (".md", ".markdown"):
        norm_name = str(Path(norm_name).with_suffix(".md"))
        header = f"# Uploaded Document ({norm_name})\n\n"
        return norm_name, header + text
    if ext in (".txt", ".text"):
        norm_name = str(Path(norm_name).with_suffix(".md"))
        header = f"# Uploaded Text ({norm_name})\n\n"
        return norm_name, header + text

    # For any other extension, still wrap as markdown to keep grep working.
    norm_name = str(Path(norm_name).with_suffix(".md"))
    header = f"# Uploaded Document ({norm_name})\n\n"
    return norm_name, header + text


async def ingest_upload(file: UploadFile, kb_path: Path, max_bytes: int = 5_000_000) -> dict:
    """
    Ingest uploaded text/markdown into the knowledge base directory.

    Returns metadata used by the UI.
    """
    if not file.filename:
        raise ValueError("Missing filename.")

    raw = await file.read()
    if len(raw) > max_bytes:
        raise ValueError(f"File too large. Max {max_bytes} bytes.")

    kb_path.mkdir(parents=True, exist_ok=True)
    normalized_name, normalized_md = normalize_uploaded_text(file.filename, raw)

    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    out_name = f"uploaded_{ts}_{normalized_name}"
    out_path = kb_path / out_name
    out_path.write_text(normalized_md, encoding="utf-8")

    return {
        "saved": True,
        "filename": out_name,
        "chars": len(normalized_md),
    }

