"""Doc upload ingestion helpers.

The knowledge base is searched via grep over plain text/markdown files.
Uploads are normalized into UTF-8 markdown under the configured user KB path.
"""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from threading import Thread
from io import BytesIO
from uuid import uuid4

from fastapi import UploadFile
from pypdf import PdfReader
from docx import Document

from src.agent.tools.kb_metadata import KBDocMeta, build_uploaded_markdown, extract_kb_metadata_from_text, sha256_text
from src.db import database


_SAFE_NAME_RE = re.compile(r"[^a-zA-Z0-9._-]+")


def _safe_filename(name: str) -> str:
    name = name.strip()
    name = name.replace(" ", "_")
    name = _SAFE_NAME_RE.sub("_", name)
    return name or "uploaded_doc"


def _extract_pdf_text(content: bytes) -> str:
    reader = PdfReader(BytesIO(content))
    pages: list[str] = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n\n".join(pages).strip()


def _extract_docx_text(content: bytes) -> str:
    doc = Document(BytesIO(content))
    lines = [p.text for p in doc.paragraphs if (p.text or "").strip()]
    return "\n".join(lines).strip()


def normalize_uploaded_text(filename: str, content: bytes) -> tuple[str, str]:
    """Return (normalized_filename, normalized_markdown_text)."""
    # Normalize extension to .md
    norm_name = _safe_filename(filename)
    ext = Path(norm_name).suffix.lower()
    text = ""

    # Structured formats: extract text before wrapping into markdown.
    if ext == ".pdf":
        try:
            text = _extract_pdf_text(content)
        except Exception as e:
            raise ValueError(f"Could not parse PDF: {e}") from e
    elif ext == ".docx":
        try:
            text = _extract_docx_text(content)
        except Exception as e:
            raise ValueError(f"Could not parse DOCX: {e}") from e
    else:
        # Try UTF-8 first; fall back to latin1 to avoid hard failures on odd encodings.
        try:
            text = content.decode("utf-8")
        except UnicodeDecodeError:
            text = content.decode("latin1", errors="replace")

    if not text.strip():
        raise ValueError("Uploaded document has no extractable text.")

    if ext in (".md", ".markdown"):
        norm_name = str(Path(norm_name).with_suffix(".md"))
        return norm_name, text
    if ext in (".txt", ".text"):
        norm_name = str(Path(norm_name).with_suffix(".md"))
        return norm_name, text
    if ext in (".pdf", ".docx"):
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

    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S_%f")
    nonce = uuid4().hex[:8]
    out_name = f"uploaded_{ts}_{nonce}_{normalized_name}"
    out_path = kb_path / out_name
    meta = extract_kb_metadata_from_text(normalized_md)
    # Keep uploaded-doc metadata minimal: language is not used by core retrieval/runtime logic.
    meta = KBDocMeta(
        title=meta.title or f"Uploaded: {normalized_name}",
        tags=meta.tags,
        language=None,
        scope=meta.scope,
        last_updated=meta.last_updated,
        url=meta.url,
        source=meta.source,
    )
    md = build_uploaded_markdown(filename=normalized_name, body=normalized_md, meta=meta)
    out_path.write_text(md, encoding="utf-8")

    row = database.upsert_kb_document(
        source_type="file_upload",
        path=str(out_path.resolve()),
        content_sha256=sha256_text(md),
        title=meta.title,
        tags=meta.tags,
        language=meta.language,
        scope=meta.scope,
        last_updated=meta.last_updated,
        metadata={"filename": out_name, "index_status": "pending"},
    )

    doc_id = int(row.get("id")) if isinstance(row, dict) and row.get("id") else None
    if doc_id:
        database.update_kb_document_metadata(doc_id, {"index_status": "indexing"})

    def _index_worker():
        try:
            from src.agent.tools import doc_search
            doc_search.index_files([out_path])
            if doc_id:
                database.update_kb_document_metadata(doc_id, {"index_status": "indexed"})
        except Exception as e:
            if doc_id:
                database.update_kb_document_metadata(doc_id, {"index_status": "failed", "index_error": str(e)[:500]})

    Thread(target=_index_worker, daemon=True).start()

    return {
        "saved": True,
        "filename": out_name,
        "chars": len(md),
        "doc_id": doc_id,
    }

