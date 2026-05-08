# Search Agent Architecture — Smarter Document Retrieval (Current)

**Goal:** Make `search_product_docs` return citations that are actually usable for the client question by combining:
1) multi-stage retrieval (RAG + exact grep + FTS),
2) product-scope aware ranking,
3) LLM rerank + sufficiency + optional refine/re-search.

---

## File Map
- Tool entry: `src/agent/email_agent.py` (`search_product_docs` → `search_with_agent_structured`)
- Orchestrator + LLM loop: `src/agent/tools/search_agent.py` (`search_with_agent` / `search_with_agent_structured` for KB callers)
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
  - `snippet` is extracted around `line_num` via `_get_snippet(window=10)` (±10 lines around the match — see **Snippet sizing knobs** below)

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

### Step E. Snippet sizing knobs (current values)

| Layer | Constant / call | Value | Where |
|---|---|---|---|
| RAG chunk size | `_RAG_CHUNK_SIZE` | **1400 chars** | `src/agent/tools/doc_search.py` |
| RAG chunk overlap | `_RAG_OVERLAP` | **250 chars** | `src/agent/tools/doc_search.py` |
| RAG snippet cap | `text[:_RAG_CHUNK_SIZE]` | tracks chunk size | `run_rag_search` |
| Grep / FTS window | `_get_snippet(window=10)` | **±10 lines** | `_get_snippet`, `search_documents` |
| Rerank prompt cap | `(snippet or line)[:1500]` | **1500 chars / candidate** | `_rerank_matches` |
| Rerank candidate cap | `all_matches[:30]` | **N=30** | `search_with_agent_structured` |
| Final tool-output cap | `format_matches_for_context(max_chars=20000)` | **20000 chars** | `search_with_agent_structured` |

The on-disk FAISS fingerprint is `registry:{count}:{digest}:{latest_mtime}:{provider}:{model}:c{chunk}o{overlap}` — the trailing `c…o…` segment makes any future chunk-size tweak auto-invalidate the index, and rebuild log entries in `data/rag/rebuild_log.jsonl` will list `chunk` in `reasons` when only the chunk knob changed.

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
- **Empty evidential set (valid rerank, all scores below threshold):** `_rerank_matches` can return **no** matches (for example every snippet scored `1` against the query). In that case the orchestrator **must not** re-inject raw `search_documents` hits: unfiltered chunks would still get `[Source: … | line …]` lines from `format_matches_for_context`, which misleads the main agent and the Workbench **citation pass** (`_extract_source_tags_from_messages` / `_add_citations_pass` in `email_agent.py`). Instead, `search_with_agent_structured` keeps **`last_evidential_matches`** (the last non-empty reranked pool), restores it when a later rerank returns empty, and **stops** the refinement loop—so the first iteration with zero evidential matches yields **no** `[Source: …]` tags and “No relevant documents found.” when appropriate.

### Step 5. Sufficiency check + optional refinement
- `_check_sufficient(query, all_matches)`
- if insufficient:
  - propose new term variants
  - run another retrieval iteration

### Step 6. Return context for the main email agent
- `format_matches_for_context()` truncates to `max_context_chars` and emits blocks like:
  `[Source: <title> — <url or path> | line <n>]\n<snippet>` (joined with `---`), or the sentence `No relevant documents found.` when the match list is empty.
- **`search_with_agent_structured`** returns `(that_string, final_matches)` for KB tooling that also needs gate decisions; `search_product_docs` uses this structured output to append mode-specific web follow-up instructions.

### Step 7. Contract with action-card creation

Retrieval output is a prerequisite for reliable action-card drafting when a thread is CSM-relevant:

- If evidence is strong, the downstream draft/card builder should include citations and grounded next steps.
- If evidence is weak or insufficient, the agent should explicitly mark a knowledge gap and avoid confident speculation.
- Card metadata should retain retrieval evidence references for downstream follow-up.
- **KB citation safety contract:** before `search_product_docs` returns to the main agent, a KB relevance gate classifies the final KB match set as relevant/irrelevant for the query. When irrelevant, KB `[Source: ...]` tags are not exposed to the final citation pass, so the assistant cannot emit false KB citations.

### KB relevance safety (irrelevant KB drop)

`search_with_agent_structured` now returns KB metadata (`kb_relevant`, `kb_reason`) in addition to formatted context + matches.

- If `kb_relevant=true`, behavior is unchanged: KB snippets and source tags flow through as normal.
- If `kb_relevant=false`, `search_product_docs` emits a KB gap marker (`KB relevance: false | reason: ...`) and does **not** pass KB source-tag blocks to the final synthesis/citation stage.
- This rule is mode-agnostic: it applies in `kb_first`, `always_augment`, and `kb_only`. In `web_only`, KB retrieval is skipped entirely.

---

## 3) RC web tool (`search_rc_web`)

`search_rc_web` uses **URL-tree-first retrieval** when a tree exists for the host; otherwise it uses **provider-hosted web search** per host.

### When `rc_url_tree` has rows for the host

1. Resolve **enabled** RC URLs and **group by host** as before.
2. Load stored tree nodes (`url`, optional `title`, depth) for that host.
3. **Semantic URL selection (LLM):** the model compares the user query to batched candidates (URL + optional title), shortlists, then picks up to **`rc_web_visit_limit`** URLs. There is no separate heuristic URL ranker; empty LLM output does not fall back to URL substring scoring.
4. **Fetch + synthesize:** selected pages are fetched; an LLM synthesizes an answer from excerpts.
5. **Strict drop-on-weak:** if no URLs were selected, fetch fails for all selections, or the post-synthesis **weak** gate fires, the tool returns an explicit **no-evidence** message and **does not** call provider web search for that host (no citation list on that weak drop path).

### When no tree exists yet

1. Same host grouping.
2. **Agentic hosted web:** plan → `run_web_search` → bounded steps with seed URLs in prompts, then validated citations.

Output is web-only (no KB merge inside this tool). **Diagnostics:** `_RC web meta:_` plus optional **`RC_WEB_DIAGNOSTICS=1`** block (includes `weak_drop_reason`, `selector_final_pick`, and strict-tree flag when applicable).

Mode policy is orchestrated by `search_product_docs` in `email_agent.py`:
- **`always_augment`**: after KB retrieval, emit a tool rule to call `search_rc_web` as a second explicit tool call.
- **`kb_first`**: run `evaluate_kb_web_gate(query, final_matches)` on KB evidence from the same KB retrieval call; only emit web follow-up rule if gate says proceed.
- **`kb_only`**: run KB retrieval only; never emit web follow-up.
- **`web_only`**: skip KB retrieval and force `search_rc_web`. If no enabled RC URLs exist, return a clear unavailability message.
- **Gate JSON failure** remains fail-open (`proceed_web: true`) to avoid silently skipping web fallback.

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

### Wrong product family in retrieval (separate from chunk size)

When a query about **product A** (e.g. AIRIS Time Frame) returns snippets dominated by **product B** docs (e.g. AIQUA), the fix is **not** larger chunks — it's scope routing. Larger chunks just make a wrong-family hit *also* longer. Levers, in order of effort:

1. **`RC_SCOPE_ENABLE=true` + `RC_SCOPE_LABELS=AIRIS,AIQUA,...`** — turns on the LLM-based scope inference step that down-ranks cross-scope docs (`RC_SCOPE_PENALTY`) and can hard-route when the query is exclusive to one scope (`RC_SCOPE_EXCLUSIVE_THRESHOLD`).
2. **Frontmatter** (`RC_SCOPE_FIELD`, default `product`) — give each KB markdown an authoritative scope label, e.g. `product: "AIRIS"`. The cross-scope penalty in `doc_search.py` reads this; without it scope detection falls back to filename heuristics (`RC_SCOPE_FILENAME_REGEX`), which is brittle.
3. **KB folder organization** — physically separating `AIRIS/` and `AIQUA/` markdown under `data/user_kb/files/` makes filename-based scope hints reliable and lets operators load only the relevant subset per probe campaign.

Tracked as a follow-up rather than a blocker for this snippet-sizing change. Suggested next step: enable `RC_SCOPE_*` for the AIRIS/AIQUA pair and backfill `product:` frontmatter on at least the top 10 most-cited KB files.

---

## 5) Debugging: why you see `rag` vs `fts` vs “plain grep”

When inspecting retrieval (logs, traces, or temporary prints in `doc_search.py` / `search_agent.py`), candidate lines are often tagged as:

- `| rag | score=...` → FAISS vector retrieval
- `| fts` (or similar) → SQLite FTS search (ranked by BM25 internally)
- no `| rag |` marker → typically grep-based hits (ripgrep exact match)

### Retrieval miss diagnostics

When `enable_retrieval_logging()` is on, each retrieval record now includes:
- `rerank_debug`: per-iteration pre/post counts and whether balanced fallback (`score>=2`) was used.
- `top_doc_keys`: top document ids after final diversify.
- `indexing_summary`: current KB indexing state counts (`pending`, `indexing`, `failed`).

At runtime, if uploads are still indexing, `search_with_agent_structured` prepends:
- `[Indexing note] ...` to explain that very recent uploads may not be retrievable yet.

---

## References
- Retrieval: `src/agent/tools/doc_search.py`
- Orchestration: `src/agent/tools/search_agent.py`
- Tool wiring: `src/agent/email_agent.py` (`search_product_docs`, `search_rc_web`)
- Architecture: [ARCHITECTURE.md](ARCHITECTURE.md)
