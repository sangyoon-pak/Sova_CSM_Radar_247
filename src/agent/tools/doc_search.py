"""NotebookLM-style hybrid RAG document search."""
# macOS: FAISS + PyTorch can each link libomp; duplicate init can hang or error.
import os

os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
os.environ.setdefault("OMP_NUM_THREADS", "1")

import re
import json
import sqlite3
import subprocess
from collections.abc import Callable
from pathlib import Path
from typing import Any

from src.config import settings

try:
    from langchain_community.vectorstores import FAISS
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_openai import OpenAIEmbeddings
except Exception:  # pragma: no cover - optional dependency path
    FAISS = None
    HuggingFaceEmbeddings = None
    OpenAIEmbeddings = None


_SCOPE_FIELD = (settings.rc_scope_field or "product").strip()
_METADATA_LINE_RE = re.compile(
    rf"^\s*(guide_keywords|guide_summary|doc_type|{re.escape(_SCOPE_FIELD)}|content_type|language|source|file_id|filename)\s*:",
    re.IGNORECASE,
)

_FTS_DB_PATH = (Path(__file__).resolve().parents[3] / "data" / "kb_fts.db").resolve()
_FRONTMATTER_SCOPE_CACHE: dict[str, str | None] = {}
# Backward-compatible alias for older helper names in this module.
_FRONTMATTER_PRODUCT_CACHE = _FRONTMATTER_SCOPE_CACHE
_FRONTMATTER_META_CACHE: dict[str, dict] = {}
_LAST_FTS_STATE: tuple[int, int] | None = None  # (file_count, latest_mtime)
_RAG_DIR = (Path(__file__).resolve().parents[3] / "data" / "rag").resolve()
_RAG_INDEX_DIR = (_RAG_DIR / "faiss_index").resolve()
_RAG_STATE_PATH = (_RAG_DIR / "state.txt").resolve()
_RAG_TOMBSTONES_PATH = (_RAG_DIR / "tombstones.json").resolve()
_RAG_EMBED_MODEL_LOCAL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
_RAG_CHUNK_SIZE = 900
_RAG_OVERLAP = 150
_EMBEDDINGS = None
_EMBED_CFG: tuple[str, str] | None = None
_VECTORSTORE = None
_VECTORSTORE_FP: str | None = None


def run_grep(pattern: str, base_path: Path, max_results: int = 20, fixed: bool = False) -> list[dict]:
    """Run ripgrep. Use fixed=True for phrase search (literal match, no regex)."""
    base_path = Path(base_path)
    if not base_path.exists():
        return []
    base_args = ["--max-count", str(max_results), "--line-number", "--no-heading", "--color", "never", "-S"]
    try:
        args = ["rg"] + base_args + (["-F", pattern] if fixed else [pattern]) + [str(base_path)]
        result = subprocess.run(
            args,
            capture_output=True, text=True, timeout=30,
        )
    except FileNotFoundError:
        try:
            grep_args = ["grep", "-r", "-n", "-i", "-m", str(max_results)]
            if fixed:
                grep_args.extend(["-F", pattern])
            else:
                grep_args.append(pattern)
            grep_args.append(str(base_path))
            result = subprocess.run(
                grep_args,
                capture_output=True, text=True, timeout=30,
            )
        except FileNotFoundError:
            return []
    if result.returncode not in (0, 1):
        return []
    out = []
    for line in (result.stdout or "").strip().split("\n"):
        if ":" not in line:
            continue
        parts = line.split(":", 2)
        if len(parts) >= 3:
            out.append({"file": Path(parts[0]).name, "line_num": int(parts[1]) if parts[1].isdigit() else 0, "line": parts[2].strip(), "path": parts[0]})
    return out[:max_results]


def _kb_files(base_path: Path) -> list[Path]:
    return sorted(base_path.rglob("*.md"))


def _kb_state(base_path: Path) -> tuple[int, int]:
    files = _kb_files(base_path)
    if not files:
        return (0, 0)
    latest_mtime = int(max(f.stat().st_mtime for f in files))
    return (len(files), latest_mtime)


def _kb_fingerprint(base_path: Path) -> str:
    count, latest = _kb_state(base_path)
    provider = (settings.rag_embedding_provider or "openrouter").strip().lower()
    model = (settings.rag_embedding_model or "").strip()
    return f"{count}:{latest}:{provider}:{model}"


def _split_into_chunks(text: str, chunk_size: int = _RAG_CHUNK_SIZE, overlap: int = _RAG_OVERLAP) -> list[tuple[int, str]]:
    """
    Split docs into overlapping chunks and track approximate starting line.
    """
    lines = text.splitlines()
    chunks: list[tuple[int, str]] = []
    if not lines:
        return chunks
    step = max(1, chunk_size - overlap)
    joined = "\n".join(lines)
    if len(joined) <= chunk_size:
        return [(1, joined)]

    offsets = []
    pos = 0
    while pos < len(joined):
        offsets.append(pos)
        pos += step
    for start in offsets:
        end = min(len(joined), start + chunk_size)
        chunk = joined[start:end].strip()
        if not chunk:
            continue
        approx_line = joined[:start].count("\n") + 1
        chunks.append((approx_line, chunk))
    return chunks


def _get_embeddings():
    global _EMBEDDINGS, _EMBED_CFG
    provider = (settings.rag_embedding_provider or "openrouter").strip().lower()
    model_name = (settings.rag_embedding_model or "").strip()
    cfg = (provider, model_name)
    if _EMBEDDINGS is not None and _EMBED_CFG == cfg:
        return _EMBEDDINGS

    if provider == "openrouter":
        if OpenAIEmbeddings is None or not settings.openrouter_api_key:
            return None
        _EMBEDDINGS = OpenAIEmbeddings(
            model=model_name or "openai/text-embedding-3-large",
            api_key=settings.openrouter_api_key,
            base_url=settings.openrouter_base_url,
        )
        _EMBED_CFG = cfg
        return _EMBEDDINGS

    if provider == "local":
        if HuggingFaceEmbeddings is None:
            return None
        _EMBEDDINGS = HuggingFaceEmbeddings(
            model_name=model_name or _RAG_EMBED_MODEL_LOCAL,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )
        _EMBED_CFG = cfg
        return _EMBEDDINGS

    return None


def _ensure_rag_index(base_path: Path):
    if FAISS is None:
        return
    _RAG_DIR.mkdir(parents=True, exist_ok=True)
    fingerprint = _kb_fingerprint(base_path)
    old = _RAG_STATE_PATH.read_text(encoding="utf-8").strip() if _RAG_STATE_PATH.exists() else ""
    if old == fingerprint and _RAG_INDEX_DIR.exists():
        return

    embeddings = _get_embeddings()
    if embeddings is None:
        return

    texts: list[str] = []
    metadatas: list[dict[str, Any]] = []
    for p in _kb_files(base_path):
        try:
            content = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for line_start, chunk in _split_into_chunks(content):
            if _is_metadata_line(chunk[:120]):
                continue
            texts.append(chunk)
            metadatas.append(
                {
                    "path": str(p),
                    "file": p.name,
                    "line_num": line_start,
                    "source": "rag",
                }
            )
    if not texts:
        return
    vs = FAISS.from_texts(texts=texts, embedding=embeddings, metadatas=metadatas)
    vs.save_local(str(_RAG_INDEX_DIR))
    _RAG_STATE_PATH.write_text(fingerprint, encoding="utf-8")


def _ensure_fts_index(base_path: Path):
    global _LAST_FTS_STATE
    state = _kb_state(base_path)
    if _LAST_FTS_STATE == state:
        return
    _FTS_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(_FTS_DB_PATH))
    conn.execute(
        "CREATE VIRTUAL TABLE IF NOT EXISTS fts_docs USING fts5(path UNINDEXED, file UNINDEXED, content, tokenize='unicode61')"
    )
    conn.execute("DELETE FROM fts_docs")
    for p in _kb_files(base_path):
        try:
            content = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        conn.execute(
            "INSERT INTO fts_docs(path, file, content) VALUES (?, ?, ?)",
            (str(p), p.name, content),
        )
    conn.commit()
    conn.close()
    _LAST_FTS_STATE = state


def _load_tombstones() -> set[str]:
    try:
        if _RAG_TOMBSTONES_PATH.exists():
            data = json.loads(_RAG_TOMBSTONES_PATH.read_text(encoding="utf-8"))
            if isinstance(data, list):
                return set(str(x) for x in data)
    except Exception:
        return set()
    return set()


def _save_tombstones(paths: set[str]) -> None:
    try:
        _RAG_DIR.mkdir(parents=True, exist_ok=True)
        _RAG_TOMBSTONES_PATH.write_text(json.dumps(sorted(paths)), encoding="utf-8")
    except Exception:
        pass


def _extract_query_tokens(query: str) -> list[str]:
    # Keep words from multiple scripts, plus underscore terms.
    tokens = re.findall(r"[A-Za-z0-9_]{2,}|[가-힣]{2,}", query)
    # Remove extremely generic tokens.
    stop = {"the", "and", "for", "with", "this", "that", "how", "what", "where", "when"}
    out = []
    seen = set()
    for t in tokens:
        lk = t.lower()
        if lk in stop or lk in seen:
            continue
        seen.add(lk)
        out.append(t)
    return out[:14]


def _approx_line_num(content: str, tokens: list[str]) -> int:
    lines = content.splitlines()
    lowered = [ln.lower() for ln in lines]
    for token in tokens:
        tk = token.lower()
        for i, ln in enumerate(lowered, start=1):
            if tk in ln:
                return i
    return 1


def run_fts_search(query: str, base_path: Path, max_results: int = 20) -> list[dict]:
    """
    FTS fallback/augment search over full document text.
    Useful when exact line-grep misses but docs still contain related terms.
    """
    _ensure_fts_index(base_path)
    tokens = _extract_query_tokens(query)
    if not tokens:
        return []
    match_expr = " OR ".join(tokens[:10])
    conn = sqlite3.connect(str(_FTS_DB_PATH))
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT path, file, content, snippet(fts_docs, 2, '', '', ' ... ', 28) as snip, bm25(fts_docs) as score
        FROM fts_docs
        WHERE fts_docs MATCH ?
        ORDER BY score
        LIMIT ?
        """,
        (match_expr, max_results),
    ).fetchall()
    conn.close()
    out = []
    for r in rows:
        content = r["content"] or ""
        line_num = _approx_line_num(content, tokens)
        snip = (r["snip"] or "").strip()
        if not snip:
            lines = content.splitlines()
            start = max(1, line_num - 2)
            end = min(len(lines), line_num + 2)
            snip = "\n".join(lines[start - 1 : end])
        out.append(
            {
                "file": r["file"],
                "line_num": line_num,
                "line": snip,
                "path": r["path"],
                "snippet": snip,
                "source": "fts",
            }
        )
    return out


def run_rag_search(query: str, base_path: Path, max_results: int = 20) -> list[dict]:
    """
    Vector retrieval over chunked KB (NotebookLM-like RAG retrieval).
    Uses local HuggingFace embeddings + FAISS index, no OpenRouter usage.
    """
    if FAISS is None:
        return []
    _ensure_rag_index(base_path)
    if not _RAG_INDEX_DIR.exists():
        return []
    global _VECTORSTORE, _VECTORSTORE_FP
    embeddings = _get_embeddings()
    if embeddings is None:
        return []
    current_fp = _kb_fingerprint(base_path)
    if _VECTORSTORE is None or _VECTORSTORE_FP != current_fp:
        try:
            _VECTORSTORE = FAISS.load_local(
                str(_RAG_INDEX_DIR),
                embeddings,
                allow_dangerous_deserialization=True,
            )
            _VECTORSTORE_FP = current_fp
        except Exception:
            return []
    store = _VECTORSTORE

    try:
        docs = store.similarity_search_with_relevance_scores(query, k=max_results)
    except Exception:
        docs = []
    tomb = _load_tombstones()
    out: list[dict] = []
    for item in docs:
        if len(item) != 2:
            continue
        doc, score = item
        md = doc.metadata or {}
        p = str(md.get("path") or "")
        if p and p in tomb:
            continue
        file_name = str(md.get("file", Path(md.get("path", "")).name))
        text = (doc.page_content or "").strip()
        if not text:
            continue
        out.append(
            {
                "file": file_name,
                "line_num": int(md.get("line_num", 1)),
                "line": text.splitlines()[0][:240],
                "path": md.get("path", ""),
                "snippet": text[:900],
                "source": "rag",
                "score": float(score),
            }
        )
    return out


def reindex_kb(base_path: Path) -> dict:
    """
    Force rebuild of local KB derived indexes (FTS + RAG).
    This is intentionally coarse-grained (full rebuild) for simplicity.
    """
    global _LAST_FTS_STATE, _VECTORSTORE, _VECTORSTORE_FP
    _LAST_FTS_STATE = None
    _VECTORSTORE = None
    _VECTORSTORE_FP = None
    try:
        _RAG_STATE_PATH.unlink(missing_ok=True)
    except Exception:
        pass
    _ensure_fts_index(base_path)
    _ensure_rag_index(base_path)
    return {"fts_db": str(_FTS_DB_PATH), "rag_dir": str(_RAG_INDEX_DIR)}


def index_files(paths: list[Path]) -> dict:
    """
    Incrementally index only the given files into FTS and (if available) FAISS.
    """
    # FTS upsert
    _FTS_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(_FTS_DB_PATH))
    conn.execute(
        "CREATE VIRTUAL TABLE IF NOT EXISTS fts_docs USING fts5(path UNINDEXED, file UNINDEXED, content, tokenize='unicode61')"
    )
    for p in paths:
        try:
            content = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        conn.execute("DELETE FROM fts_docs WHERE path = ?", (str(p),))
        conn.execute(
            "INSERT INTO fts_docs(path, file, content) VALUES (?, ?, ?)",
            (str(p), p.name, content),
        )
    conn.commit()
    conn.close()

    # RAG incremental add
    if FAISS is not None:
        embeddings = _get_embeddings()
        if embeddings is not None:
            _RAG_DIR.mkdir(parents=True, exist_ok=True)
            global _VECTORSTORE, _VECTORSTORE_FP
            if _RAG_INDEX_DIR.exists():
                try:
                    _VECTORSTORE = FAISS.load_local(
                        str(_RAG_INDEX_DIR),
                        embeddings,
                        allow_dangerous_deserialization=True,
                    )
                except Exception:
                    _VECTORSTORE = None
            texts: list[str] = []
            metadatas: list[dict] = []
            for p in paths:
                try:
                    content = p.read_text(encoding="utf-8", errors="replace")
                except Exception:
                    continue
                for line_start, chunk in _split_into_chunks(content):
                    if _is_metadata_line(chunk[:120]):
                        continue
                    texts.append(chunk)
                    metadatas.append({"path": str(p), "file": p.name, "line_num": line_start, "source": "rag"})
            if texts:
                if _VECTORSTORE is None:
                    _VECTORSTORE = FAISS.from_texts(texts=texts, embedding=embeddings, metadatas=metadatas)
                else:
                    _VECTORSTORE.add_texts(texts=texts, metadatas=metadatas)
                _VECTORSTORE.save_local(str(_RAG_INDEX_DIR))
                _VECTORSTORE_FP = None

    # remove from tombstones if re-indexed
    tomb = _load_tombstones()
    before = len(tomb)
    for p in paths:
        tomb.discard(str(p))
    if len(tomb) != before:
        _save_tombstones(tomb)

    return {"indexed_files": [str(p) for p in paths]}


def tombstone_files(paths: list[Path]) -> dict:
    """
    Mark files as deleted for vector retrieval (FAISS doesn't support easy deletes).
    Also remove from FTS table.
    """
    # FTS delete
    _FTS_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(_FTS_DB_PATH))
    try:
        conn.execute(
            "CREATE VIRTUAL TABLE IF NOT EXISTS fts_docs USING fts5(path UNINDEXED, file UNINDEXED, content, tokenize='unicode61')"
        )
        for p in paths:
            conn.execute("DELETE FROM fts_docs WHERE path = ?", (str(p),))
        conn.commit()
    finally:
        conn.close()

    tomb = _load_tombstones()
    for p in paths:
        tomb.add(str(p))
    _save_tombstones(tomb)
    return {"tombstoned": [str(p) for p in paths]}

def _is_metadata_line(text: str) -> bool:
    t = (text or "").strip()
    return t == "---" or bool(_METADATA_LINE_RE.match(t))


def _get_snippet(path: str, line_num: int, window: int = 3) -> str:
    """
    Return +/- window lines around the matched line.
    Keeps retrieval more actionable than single-line keyword matches.
    """
    p = Path(path)
    if not p.exists() or line_num <= 0:
        return ""
    try:
        lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception:
        return ""
    start = max(1, line_num - window)
    end = min(len(lines), line_num + window)
    snippet_lines = []
    for idx in range(start, end + 1):
        marker = ">>" if idx == line_num else "  "
        snippet_lines.append(f"{marker} L{idx}: {lines[idx - 1]}")
    return "\n".join(snippet_lines).strip()


def _expand_alias_terms(query: str, terms: list[str]) -> list[str]:
    """
    Expand common shorthand so retrieval doesn't miss obvious docs.

    Keep this function product-neutral so the search core can be shared
    across industries/solutions.
    """
    # Default: no alias expansion (only deduplication).
    expanded = list(terms)
    seen: set[str] = set()
    out: list[str] = []
    for t in expanded:
        key = (t or "").strip().lower()
        if key and key not in seen:
            seen.add(key)
            out.append((t or "").strip())
    return out


def _read_frontmatter_product(path_str: str) -> str | None:
    """
    Parse a scope/category label from YAML frontmatter (authoritative for KB files).

    Field name is controlled by `settings.rc_scope_field` (default: `product`).
    """
    if path_str in _FRONTMATTER_PRODUCT_CACHE:
        return _FRONTMATTER_PRODUCT_CACHE[path_str]

    field = (settings.rc_scope_field or "product").strip()
    p = Path(path_str)
    scope_val: str | None = None
    try:
        raw = p.read_text(encoding="utf-8", errors="replace")[:8000]
    except OSError:
        _FRONTMATTER_PRODUCT_CACHE[path_str] = None
        return None
    if not raw.lstrip().startswith("---"):
        _FRONTMATTER_PRODUCT_CACHE[path_str] = None
        return None

    lines = raw.splitlines()
    for ln in lines[1:]:
        s = ln.strip()
        if s == "---":
            break
        m = re.match(rf"{re.escape(field)}\s*:\s*\"([^\"]+)\"", ln, re.I)
        if m:
            scope_val = m.group(1).strip()
            break
        m2 = re.match(rf"{re.escape(field)}\s*:\s*(\S+)", ln, re.I)
        if m2:
            v = m2.group(1).strip().rstrip(",")
            if not v.startswith('"'):
                scope_val = v
                break

    normalized = _normalize_kb_product_label(scope_val) if scope_val else None
    _FRONTMATTER_PRODUCT_CACHE[path_str] = normalized
    return normalized


def _read_frontmatter_meta(path_str: str) -> dict:
    """
    Parse a small set of frontmatter metadata for retrieval/routing display:
    title, tags, language, url, scope field.
    """
    if path_str in _FRONTMATTER_META_CACHE:
        return _FRONTMATTER_META_CACHE[path_str]
    p = Path(path_str)
    try:
        raw = p.read_text(encoding="utf-8", errors="replace")[:8000]
    except OSError:
        _FRONTMATTER_META_CACHE[path_str] = {}
        return {}
    if not raw.lstrip().startswith("---"):
        _FRONTMATTER_META_CACHE[path_str] = {}
        return {}
    field = (settings.rc_scope_field or "product").strip()
    meta: dict[str, object] = {}
    for ln in raw.splitlines()[1:]:
        s = ln.strip()
        if s == "---":
            break
        if ":" not in ln:
            continue
        k, v = ln.split(":", 1)
        key = k.strip().lower()
        val = v.strip().strip('"').strip("'")
        if key in {"title", "language", "url", "source_url"}:
            meta[key] = val
        if key in {"tags", "guide_keywords"}:
            meta["tags"] = val
        if key == field.lower():
            meta["scope"] = _normalize_kb_product_label(val)
    _FRONTMATTER_META_CACHE[path_str] = meta
    return meta


def _normalize_kb_product_label(label: str | None) -> str | None:
    if not label:
        return None
    s = label.strip().strip('"').lower()
    # Normalize whitespace and use underscore as a stable delimiter.
    s = " ".join(s.split())
    s = s.replace(" ", "_")
    return s


def _filename_product_guess(file_name: str) -> str | None:
    """Infer a scope label from crawler-style filenames like 060_<scope>_part_6.md."""
    stem = Path(file_name).stem.lower()
    m = re.match(r"^\d+_([a-z0-9]+)_", stem)
    if not m:
        return None
    return _normalize_kb_product_label(m.group(1))


def _match_primary_product(m: dict) -> str | None:
    """Single canonical product for routing / cross-product penalty."""
    path_str = str(m.get("path") or "")
    file_name = str(m.get("file") or "")
    if path_str:
        fp = _read_frontmatter_product(path_str)
        if fp:
            return fp
    return _filename_product_guess(file_name)


def _single_scope_exclusive_query(scope_hints: set[str]) -> bool:
    """
    Return True only when a single exclusive scope/category is inferred.

    The inferred scope comes from `settings.rc_scope_labels` via `_extract_product_hints()`.
    """
    if not settings.rc_scope_enable:
        return False
    return len(scope_hints) == 1


def _cross_product_penalty_weight(exclusive_scope: str | None, doc_primary: str | None) -> int:
    """Config-driven cross-scope penalty when the question is unambiguously scoped."""
    if not settings.rc_scope_enable or not exclusive_scope or not doc_primary:
        return 0
    if doc_primary == exclusive_scope:
        return 0
    return int(settings.rc_scope_penalty or 0)


def _extract_product_hints(text: str) -> set[str]:
    """
    Infer possible scope/category labels from the query text using config.
    Returns empty set when `settings.rc_scope_labels` is not provided.
    """
    labels = [
        _normalize_kb_product_label(x)
        for x in (settings.rc_scope_labels or "").split(",")
    ]
    labels = [x for x in labels if x]
    if not labels:
        return set()

    q = (text or "").lower()
    q_norm = " ".join(q.split())
    out: set[str] = set()
    for lbl in labels:
        if " " in lbl:
            # multi-token labels
            if lbl in q_norm:
                out.add(lbl)
        else:
            if re.search(rf"\b{re.escape(lbl)}\b", q):
                out.add(lbl)
    return out


def _detect_doc_products(file_name: str, text: str) -> set[str]:
    # Generic detection based on configured scope labels.
    labels = [
        _normalize_kb_product_label(x)
        for x in (settings.rc_scope_labels or "").split(",")
    ]
    labels = [x for x in labels if x]
    if not labels:
        return set()

    x = f"{file_name} {text}".lower()
    out: set[str] = set()
    for lbl in labels:
        if " " in lbl:
            if lbl in x:
                out.add(lbl)
        else:
            if re.search(rf"\b{re.escape(lbl)}\b", x):
                out.add(lbl)
    return out


def _hard_tokens_from_inputs(query: str, terms: list[str]) -> set[str]:
    toks = set(re.findall(r"https?://\S+|/[A-Za-z0-9_./\-]+/?|\b[a-z]+(?:_[a-z0-9]+){1,}\b", query))
    for t in terms:
        s = (t or "").strip()
        if "/" in s or ":" in s or "_" in s:
            toks.add(s)
    # lowercase for membership checks
    return {t.lower() for t in toks if t}


def search_documents(
    query: str,
    search_terms: list[str] | None = None,
    llm_extract: Callable[[str], list[str]] | None = None,
    max_results_per_term: int = 10,
    scope_hints: set[str] | None = None,
    exclusive_scope: str | None = None,
) -> list[dict]:
    kb = settings.kb_path_resolved
    if not kb.exists():
        return []
    if search_terms is None and llm_extract:
        search_terms = llm_extract(query)
    if not search_terms:
        search_terms = [w for w in re.findall(r"\b\w{3,}\b", query) if len(w) > 2][:5]
    search_terms = _expand_alias_terms(query, search_terms)
    all_matches: list[dict] = []
    seen = set()

    # 1) Vector retrieval first (NotebookLM-like semantic recall).
    rag_matches = run_rag_search(query, kb, max_results=24)
    for m in rag_matches:
        key = (m.get("file"), m.get("line_num"), "rag")
        if key in seen:
            continue
        seen.add(key)
        all_matches.append(m)

    # 2) Lexical term-based retrieval for exact token coverage.
    for term in search_terms[:12]:
        if not term or len(term) < 2:
            continue
        # Use fixed-string matching for phrases and for URL/path-like tokens.
        t = term.strip()
        use_phrase = (" " in t) or ("/" in t) or (":" in t)
        matches = run_grep(term, kb, max_results=max_results_per_term, fixed=use_phrase)
        for m in matches:
            if _is_metadata_line(m.get("line", "")):
                # Skip YAML/frontmatter-like hits that often cause weak answers.
                continue
            m["snippet"] = _get_snippet(m.get("path", ""), m.get("line_num", 0), window=3)
            key = (m["file"], m["line_num"])
            if key not in seen:
                seen.add(key)
                all_matches.append(m)

    # 3) FTS augmentation for broader lexical recall.
    if len(all_matches) < 40:
        fts_matches = run_fts_search(query, kb, max_results=20)
        for m in fts_matches:
            key = (m["file"], m["line_num"], "fts")
            if key not in seen:
                seen.add(key)
                all_matches.append(m)

    product_hints = set(scope_hints or _extract_product_hints(query + " " + " ".join(search_terms)))
    hard_tokens = _hard_tokens_from_inputs(query, search_terms)
    is_exclusive = bool(exclusive_scope) if settings.rc_scope_enable else False
    if not exclusive_scope:
        is_exclusive = _single_scope_exclusive_query(product_hints)
        exclusive_scope = next(iter(product_hints)) if is_exclusive and product_hints else None

    # Prefer semantic + actionable snippets with soft product alignment and hard-token matches.
    def _score(m: dict) -> tuple[int, int, int, int, int]:
        src = str(m.get("source", "grep"))
        src_score = 3 if src == "rag" else (2 if src == "grep" else 1)
        file_name = str(m.get("file", "")).lower()
        text = (m.get("snippet") or m.get("line") or "").lower()
        actionable = 1 if any(w in text for w in ["api", "sdk", "event", "trigger", "identifier", "appid"]) else 0
        product_align = 0
        product_mismatch = 0
        if product_hints:
            doc_products = _detect_doc_products(file_name, text)
            product_align = len(product_hints & doc_products)
            # Soft penalty: query has clear products, doc has other product labels only.
            if doc_products and product_align == 0:
                product_mismatch = 1
        hard_hit = 0
        if hard_tokens:
            hard_hit = 1 if any(tok in text for tok in hard_tokens) else 0
        return (product_mismatch, product_align, hard_hit, src_score, actionable)

    def _sort_key(m: dict) -> tuple:
        s = _score(m)
        cross = _cross_product_penalty_weight(exclusive_scope, _match_primary_product(m))
        # Ascending: lower cross-penalty first, fewer mismatches, stronger align / hard hits first.
        return (
            cross,
            s[0],
            -s[1],
            -s[2],
            -s[3],
            -s[4],
            str(m.get("file", "")),
            int(m.get("line_num", 0)),
        )

    all_matches.sort(key=_sort_key)

    # Attach structured metadata for downstream LLM planning (best effort).
    for m in all_matches:
        path_str = str(m.get("path") or "")
        if path_str:
            fm = _read_frontmatter_meta(path_str)
            if fm:
                m.setdefault("meta", fm)
    if product_hints:
        aligned = []
        others = []
        exclusive_label = exclusive_scope
        for m in all_matches:
            file_name = str(m.get("file", "")).lower()
            text = (m.get("snippet") or m.get("line") or "").lower()
            doc_products = _detect_doc_products(file_name, text)
            primary = _match_primary_product(m)
            if is_exclusive and exclusive_label and primary and primary != exclusive_label:
                others.append(m)
            elif doc_products and (doc_products & product_hints):
                aligned.append(m)
            else:
                others.append(m)
        # Soft routing: keep aligned docs first, but still allow fallback docs.
        all_matches = aligned + others
    return all_matches[:50]


def format_matches_for_context(matches: list[dict], max_chars: int = 4000) -> str:
    parts = []
    total = 0
    for m in matches:
        snippet = m.get("snippet") or m.get("line", "")
        meta = m.get("meta") or {}
        title = (meta.get("title") or "").strip() or str(m.get("file") or "Document").strip()
        url = (meta.get("url") or "").strip() or str(m.get("url") or "").strip()
        if url:
            src = f"{title} — {url}"
        else:
            path = str(m.get("path") or "").strip()
            src = f"{title} — {path}" if path else title
        # Keep a consistent, easy-to-cite source tag per chunk.
        block = f"[Source: {src} | line {m['line_num']}]\n{snippet}"
        if total + len(block) > max_chars:
            break
        parts.append(block)
        total += len(block)
    return "\n\n---\n\n".join(parts) if parts else "No relevant documents found."
