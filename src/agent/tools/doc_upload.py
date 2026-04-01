"""Doc upload ingestion helpers.

The knowledge base is searched via grep over plain text/markdown files.
So for now we normalize uploads into UTF-8 markdown files under knowledge-base/.
"""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

from fastapi import UploadFile

from src.agent.tools.kb_metadata import KBDocMeta, build_uploaded_markdown, detect_language_simple, extract_kb_metadata_from_text, sha256_text
from src.db import database


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
        return norm_name, text
    if ext in (".txt", ".text"):
        norm_name = str(Path(norm_name).with_suffix(".md"))
        return norm_name, text

    # For any other extension, still wrap as markdown to keep grep working.
    norm_name = str(Path(norm_name).with_suffix(".md"))
    return norm_name, text


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
    lang = detect_language_simple(normalized_md)
    meta = extract_kb_metadata_from_text(normalized_md)
    # Ensure we always tag language for later routing/LLM planning.
    meta = KBDocMeta(
        title=meta.title or f"Uploaded: {normalized_name}",
        tags=meta.tags,
        language=meta.language or lang,
        scope=meta.scope,
        last_updated=meta.last_updated,
        url=meta.url,
        source=meta.source,
    )
    md = build_uploaded_markdown(filename=normalized_name, body=normalized_md, meta=meta)
    out_path.write_text(md, encoding="utf-8")

    database.upsert_kb_document(
        source_type="file_upload",
        path=str(out_path.resolve()),
        content_sha256=sha256_text(md),
        title=meta.title,
        tags=meta.tags,
        language=meta.language,
        scope=meta.scope,
        last_updated=meta.last_updated,
        metadata={"filename": out_name},
    )

    return {
        "saved": True,
        "filename": out_name,
        "chars": len(md),
        "language": meta.language,
    }

