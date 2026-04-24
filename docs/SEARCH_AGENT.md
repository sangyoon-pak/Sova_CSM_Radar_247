# Search Agent Architecture — Smarter Document Retrieval (Current)

**Goal:** Make `search_product_docs` return citations that are actually usable for the client question by combining:
1) multi-stage retrieval (RAG + exact grep + FTS),
2) product-scope aware ranking,
3) LLM rerank + sufficiency + optional refine/re-search.

---

## File Map
- Tool entry: `src/agent/email_agent.py` (`search_product_docs` → `search_with_agent`)
- Orchestrator + LLM loop: `src/agent/tools/search_agent.py` (`search_with_agent` / `search_with_agent_structured` for RC callers)
- Retrieval + candidate ranking: `src/agent/tools/doc_search.py` (`search_documents`)

Related behavior docs:
- Guardrails: [AGENT_GUARDRAILS.md](AGENT_GUARDRAILS.md)
- Action cards: [ACTION_CARD_SPEC.md](ACTION_CARD_SPEC.md)
- Troubleshooting: [OPERATIONS_RUNBOOK.md](OPERATIONS_RUNBOOK.md)

### LLM models (OpenRouter / OpenAI-compatible)
Search-related LLM calls use **`LLM_MODEL_SEARCH_JSON`** (split, sufficiency, refine) and **`LLM_MODEL_SEARCH_RERANK`** (policy-aware reranking). Term extraction in `search_terms_extractor.py` uses **`LLM_MODEL_SEARCH_JSON`**. The **same** `LLM_MODEL_SEARCH_JSON` stack also drives small **JSON intent routers** in `email_agent.py` (Workbench `inbox_peek` vs `agent_run`, and optional full-inbox-probe classifier)—see the **JSON intent routers** section in [LLM_MODELS.md](LLM_MODELS.md). The **RC KB→web gate** uses **`LLM_MODEL_KB_WEB_GATE`** (`kb_web_gate.py`) — intentionally **separate** from `LLM_MODEL_SEARCH_JSON`. Rerank policy itself is configured via **`RETRIEVAL_RANKING_POLICY`** (Configure/runtime JSON). All roles fall back to **`LLM_MODEL`** when unset (gate: see `effective_llm_model_kb_web_gate()`).

### Scope routing (config-driven)
When `RC_SCOPE_ENABLE=true` and `RC_SCOPE_LABELS` is set, the search agent first runs an LLM-based scope inference step to decide whether the inquiry is **exclusive to one scope** or **multi-scope/ambiguous**. If exclusive, cross-scope docs are strongly down-ranked and routed behind in-scope docs. The exclusivity decision is controlled by `RC_SCOPE_EXCLUSIVE_THRESHOLD`.

---

## 1) Retrieval Stack (`doc_search.search_documents`)

`search_documents(query, search_terms=...)` builds a candidate list from multiple retrieval strategies, then applies a local sort.

### Step A. RAG recall (FAISS / embeddings)
- `run_rag_search()` returns chunks from the FAISS index
- Each match is annotated with:
  - `source: "rag"`
  - `score: <vector similarity relevance score>`

### Step B. Exact/phrase lexical recall (grep / ripgrep)
- For each term, `run_grep()` is called
  - phrase-like terms (contains spaces / `/` / `:`) use fixed-string match (`fixed=True`)
- Each hit is annotated as:
  - `source` is treated as `"grep"` (there is no explicit `"source":"grep"` field; default logic shows up without `| rag |` in the report)
  - `snippet` is extracted around `line_num` via `_get_snippet()`

### Step C. FTS augmentation (SQLite FTS5 + BM25)
- If the merged candidate list is still small (`len(all_matches) < 40`),
  `run_fts_search()` adds more lexical hits using SQLite FTS.
- FTS ranking inside SQLite uses **BM25**:
  - BM25 is a scoring function used to rank full-text search results.
  - It is *math/scoring*, not a different retrieval type (FTS is the search engine; BM25 ranks its output).
- Matches from this step are annotated:
  - `source: "fts"` (and `line/snip` around an approximate match line)

### Step D. Deterministic candidate ordering (no hardcoded boosts)
Before LLM rerank, candidates are ordered deterministically using:
- optional policy-defined `source_order` from `RETRIEVAL_RANKING_POLICY` (for example `["rag","grep","fts"]`)
- stable tie-breakers (`file`, `line_num`)
- optional config-driven cross-scope penalty when an exclusive scope is inferred (`RC_SCOPE_*`)

There are no hardcoded vendor-specific keyword boosts in this stage.

Final return from `search_documents`: top candidates (currently capped at `[:50]`) with `snippet/line_num/path`.

### Uploaded documents behavior

Uploaded `.md/.txt` and other indexed knowledge artifacts are expected to participate in the same retrieval path after indexing/reindexing.  
If a product-related thread does not produce uploaded-document evidence, treat it as an operational issue and follow [OPERATIONS_RUNBOOK.md](OPERATIONS_RUNBOOK.md).

---

## 2) Search Orchestration (`search_agent.search_with_agent`)

This is an iterative loop around `search_documents()` plus LLM decisions.

### Step 1. Focus split
- `_split_focus_subqueries(query)` uses an LLM to split a long inquiry into focused sub-questions
- language-agnostic, format-agnostic, and resilient to different numbering styles.

### Step 2. Term variants (iteration 0 vs refined iteration)
- Iteration 0:
  - `extract_search_terms(query)` (general terms)
  - `_extract_hard_terms(query)` (endpoint paths, event names, identifiers like `user_id`, `device`, etc.)
  - combines them into a single term-variant list
- Iteration > 0:
  - LLM sufficiency check decides if more retrieval is needed
  - if not sufficient, LLM proposes refined term lists (`_refine_search_terms`)

### Step 3. Retrieve per focus sub-query
For each term variant and each focus sub-query:
- `search_documents(query=sq, search_terms=terms + _extract_hard_terms(sq))`
- candidates are merged + deduped by `(file, line_num)`.

### Step 4. Policy-aware LLM rerank + threshold filter
- `_rerank_matches(query, matches, threshold=3)` calls the rerank model with:
  - user query
  - candidate snippets
  - runtime `RETRIEVAL_RANKING_POLICY` JSON
  - optional scope guidance note (when exclusive scope is inferred)
- Output contract is strict JSON with `ranked_indices` + `scores`.
- Tracing metadata includes policy name/version (`search_agent.policy_rerank`).
- **Neutral fallback:** if rerank fails (timeout/error/invalid JSON/invalid permutation), the system uses deterministic policy-order sorting (no hardcoded vendor heuristics).

### Step 5. Sufficiency check + optional refinement
- `_check_sufficient(query, all_matches)`
- if insufficient:
  - propose new term variants
  - run another retrieval iteration

### Step 6. Return context for the main email agent
- `format_matches_for_context()` truncates to `max_context_chars` and returns a string like:
  `[From <file> line <line_num>] ...`
- **`search_with_agent_structured`** returns `(that_string, final_matches)` for RC tooling (`search_rc_web` + gate); **`search_product_docs`** keeps calling **`search_with_agent`** (string only).

### Step 7. Contract with action-card creation

Retrieval output is a prerequisite for reliable action-card drafting when a thread is CSM-relevant:

- If evidence is strong, the downstream draft/card builder should include citations and grounded next steps.
- If evidence is weak or insufficient, the agent should explicitly mark a knowledge gap and avoid confident speculation.
- Card metadata should retain retrieval evidence references for downstream follow-up.

---

## 3) RC web tool (`search_rc_web`)

`search_rc_web` is **not** another orchestrator: it calls **`search_with_agent_structured`** to reuse the full KB pipeline, then applies RC-only policy:

1. **Structured KB result** — `(formatted_context, final_matches)` after the same diversify step as `search_with_agent` (see `search_agent.py`).
2. **`rc_web_retrieval_mode`** — `kb_first` (default): run **`evaluate_kb_web_gate`** on `(query, final_matches)` when KB text is non-empty and not the “no relevant documents” sentinel; if `proceed_web` is false, return KB only. `always_augment`: skip the gate and always invoke hosted web after KB (merge sections; higher cost). Persisted via **Knowledge → RC URLs** and `effective_rc_web_retrieval_mode()`.
3. **Hosted web** — `run_web_search` per enabled RC URL host; merged with KB using clear `## Local KB` / web headings (when web runs after a weak KB signal, the KB block is labeled as below-confidence — see `rc_web_search.py`).
4. **Gate JSON failure** — treated as **`proceed_web: true`** so web is not silently skipped.

Details and operator controls: [ARCHITECTURE.md](ARCHITECTURE.md) (retrieval section), [LLM_MODELS.md](LLM_MODELS.md) (`LLM_MODEL_KB_WEB_GATE`).

---

## 4) Scope Rules (Scope citations)

Search/ranking tries to infer the user’s primary scope/category from:
- the query text (`RC_SCOPE_LABELS`), and
- KB metadata when available,
then enforces a “scope scoped” citation style:

- Prefer KB chunks whose primary documentation scope matches the inferred scope.
- Penalize (or down-rank) chunks from other scopes (cross-scope hubs), even if they contain overlapping words.
- If the question is ambiguous (no clear scope), do not hard-block other docs;
  instead, rely on reranking/actionability to pick the most relevant passages.

This is enforced at 2 layers:
1. heuristic candidate sorting in `doc_search.py` (cross-scope penalty)
2. rerank prompt in `search_agent.py` (scope note)
3. email system prompt guidance in `src/agent/prompts.py` (citation rules)

If there are no relevant passages (or retrieved snippets do not substantively answer the numbered questions),
the agent should state KB gaps and recommend the customer contact your team/support (no guessing).

This keeps retrieval behavior aligned with guardrail policy in [AGENT_GUARDRAILS.md](AGENT_GUARDRAILS.md).

---

## 5) Debugging: why you see `rag` vs `fts` vs “plain grep”

When inspecting retrieval (logs, traces, or temporary prints in `doc_search.py` / `search_agent.py`), candidate lines are often tagged as:

- `| rag | score=...` → FAISS vector retrieval
- `| fts` (or similar) → SQLite FTS search (ranked by BM25 internally)
- no `| rag |` marker → typically grep-based hits (ripgrep exact match)

---

## References
- Retrieval: `src/agent/tools/doc_search.py`
- Orchestration: `src/agent/tools/search_agent.py`
- Tool wiring: `src/agent/email_agent.py` (`search_product_docs`, `search_rc_web`)
- Architecture: [ARCHITECTURE.md](ARCHITECTURE.md)
