"""Natural-language guardrail phrases: semantic match + safe fallbacks.

Uses the same embedding stack as RAG when available; otherwise substring / token overlap.
"""
from __future__ import annotations

import json
import math
import re
from functools import lru_cache
from typing import Any

from src.config import settings


def parse_intent_phrases_blob(raw: str) -> list[str]:
    """
    Accepts JSON array string, newline-separated phrases, or legacy comma-separated text.
    """
    s = (raw or "").strip()
    if not s:
        return []
    if s.startswith("["):
        try:
            v = json.loads(s)
            if isinstance(v, list):
                return [str(x).strip() for x in v if str(x).strip()]
        except json.JSONDecodeError:
            pass
    parts: list[str] = []
    for line in re.split(r"[\n,]", s):
        t = line.strip()
        if t:
            parts.append(t)
    return parts


def _action_text_blob(a: dict[str, Any]) -> str:
    return " ".join(
        [
            str(a.get("title") or ""),
            str(a.get("brief") or ""),
            str(a.get("client_query_digest") or ""),
            str(a.get("thread_summary") or ""),
            str(a.get("email_subject") or ""),
        ]
    ).strip()


def _cosine_sim(a: list[float], b: list[float]) -> float:
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na <= 0 or nb <= 0:
        return 0.0
    return dot / (na * nb)


@lru_cache(maxsize=256)
def _embed_one_cached(model_cfg: tuple[str, ...], text: str) -> tuple[float, ...] | None:
    """Returns tuple for hashability in lru_cache."""
    from src.agent.tools.doc_search import _get_embeddings

    emb = _get_embeddings()
    if emb is None:
        return None
    try:
        v = emb.embed_query(text[:8000])
        if not v:
            return None
        return tuple(float(x) for x in v)
    except Exception:
        return None


def _effective_embed_cfg() -> tuple[str, ...]:
    from src.runtime_config import effective_rag_embedding_model, effective_rag_embedding_provider

    return (
        (effective_rag_embedding_provider() or "").strip().lower(),
        (effective_rag_embedding_model() or "").strip(),
    )


def nl_phrase_matches_thread_text(phrase: str, action: dict[str, Any]) -> bool:
    """
    True if the natural-language phrase applies to this action row (exclude/include).
    """
    p = (phrase or "").strip()
    if not p:
        return False
    text = _action_text_blob(action)
    if not text:
        return False
    thr = float(getattr(settings, "guardrail_nl_similarity_threshold", 0.66) or 0.66)
    cfg = _effective_embed_cfg()
    pv = _embed_one_cached(cfg, p)
    tv = _embed_one_cached(cfg, text[:8000])
    if pv is not None and tv is not None:
        sim = _cosine_sim(list(pv), list(tv))
        if sim >= thr:
            return True
    # Embeddings can miss short phrases vs. titles; substring/token overlap still counts.
    return _fallback_phrase_match(p, text)


def _fallback_phrase_match(phrase: str, text: str) -> bool:
    """When embeddings are unavailable: substring + light token overlap."""
    pl = phrase.lower().strip()
    tl = text.lower()
    if len(pl) >= 2 and pl in tl:
        return True
    pw = [w for w in re.split(r"\s+", pl) if len(w) >= 2]
    if not pw:
        return False
    hits = sum(1 for w in pw if w in tl)
    return hits >= max(1, len(pw) // 2)


def thread_text_matches_any_phrase(phrases: list[str], action: dict[str, Any]) -> bool:
    for ph in phrases:
        if nl_phrase_matches_thread_text(ph, action):
            return True
    return False
