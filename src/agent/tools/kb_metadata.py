"""KB metadata extraction and normalization.

Goal: keep this solution-agnostic. We only parse structured frontmatter and
return a normalized schema for retrieval/routing and UI display.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from src.config import settings


_FRONTMATTER_MAX = 12000


@dataclass(frozen=True)
class KBDocMeta:
    title: str | None = None
    tags: list[str] | None = None
    language: str | None = None
    scope: str | None = None
    last_updated: str | None = None
    url: str | None = None
    source: str | None = None


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()


def _normalize_label(x: str | None) -> str | None:
    if not x:
        return None
    s = str(x).strip().strip('"').strip("'")
    return s or None


def _normalize_scope(x: str | None) -> str | None:
    if not x:
        return None
    s = x.strip().strip('"').strip("'").lower()
    s = " ".join(s.split()).replace(" ", "_")
    return s or None


def _parse_frontmatter(raw: str) -> dict:
    """
    Minimal YAML-ish parser for key: value lines in the first frontmatter block.
    Avoids adding a YAML dependency.
    """
    if not raw.lstrip().startswith("---"):
        return {}
    lines = raw.splitlines()
    out: dict[str, object] = {}
    for ln in lines[1:]:
        if ln.strip() == "---":
            break
        if ":" not in ln:
            continue
        k, v = ln.split(":", 1)
        key = k.strip().lower()
        val = v.strip()
        if not key:
            continue
        # list-ish forms: [a, b] or a,b
        if key in {"tags", "guide_keywords"}:
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                parts = [p.strip().strip('"').strip("'") for p in inner.split(",") if p.strip()]
                out[key] = parts
            else:
                parts = [p.strip() for p in val.split(",") if p.strip()]
                out[key] = [p.strip('"').strip("'") for p in parts]
            continue
        out[key] = val.strip().strip('"').strip("'")
    return out


def extract_kb_metadata_from_text(text: str) -> KBDocMeta:
    fm = _parse_frontmatter(text[:_FRONTMATTER_MAX])
    scope_field = (settings.rc_scope_field or "product").strip().lower()

    title = _normalize_label(fm.get("title") or fm.get("filename") or fm.get("doc_title"))  # type: ignore[arg-type]
    tags_raw = fm.get("tags") or fm.get("guide_keywords")
    tags: list[str] | None = None
    if isinstance(tags_raw, list):
        tags = [t for t in (_normalize_label(x) for x in tags_raw) if t]  # type: ignore[arg-type]
    language = _normalize_label(fm.get("language"))  # type: ignore[arg-type]
    url = _normalize_label(fm.get("url") or fm.get("source_url"))  # type: ignore[arg-type]
    last_updated = _normalize_label(fm.get("last_updated") or fm.get("updated_at") or fm.get("date"))  # type: ignore[arg-type]
    scope_val = fm.get(scope_field)
    scope = _normalize_scope(scope_val if isinstance(scope_val, str) else None)
    source = _normalize_label(fm.get("source"))  # type: ignore[arg-type]

    return KBDocMeta(
        title=title,
        tags=tags,
        language=language,
        scope=scope,
        last_updated=last_updated,
        url=url,
        source=source,
    )


def detect_language_simple(text: str) -> str:
    """
    Lightweight language guess for response control.
    - returns 'ko' when Hangul is present
    - else 'en'
    """
    if re.search(r"[\uAC00-\uD7A3]", text or ""):
        return "ko"
    return "en"


def build_uploaded_markdown(*, filename: str, body: str, meta: KBDocMeta) -> str:
    """Wrap content with a normalized frontmatter block."""
    fm: dict[str, object] = {}
    if meta.title:
        fm["title"] = meta.title
    if meta.tags:
        fm["tags"] = meta.tags
    if meta.language:
        fm["language"] = meta.language
    if meta.scope:
        fm[(settings.rc_scope_field or "product").strip()] = meta.scope
    if meta.url:
        fm["url"] = meta.url
    fm["ingested_at"] = datetime.utcnow().isoformat()

    fm_lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, list):
            fm_lines.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
        else:
            fm_lines.append(f"{k}: {v}")
    fm_lines.append("---")
    fm_block = "\n".join(fm_lines)

    header = f"# {meta.title or filename}\n\n"
    return f"{fm_block}\n\n{header}{body}".strip() + "\n"

