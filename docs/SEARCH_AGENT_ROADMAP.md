# Search Agent Roadmap — Smarter Document Retrieval

**Goal:** Give the doc search tool a "brain" so it can re-rank results and optionally run refined searches when the first pass is insufficient.

---

## Status (Implemented)

| Component | Status | Location |
|-----------|--------|----------|
| Re-ranker | Done | `src/agent/tools/search_agent.py` |
| Phrase search | Done | `doc_search.run_grep(fixed=True)` for terms with spaces |
| Sufficiency check + refined search | Done | `search_agent.search_with_agent()` |
| Wire into email agent | Done | `search_appier_docs` → `search_with_agent` |

Context limit increased to 8,000 chars. Max 2 iterations for refined search.

---

## Current Flow (Single Pass)

```
Query → LLM extract terms → Grep (5 terms × 10 matches) → Dedupe → Sort by file/line → Truncate 4K chars → Return
```

**Problems:** Many irrelevant matches (generic terms like "formula", "work"); no quality check; no refinement.

---

## Proposed: Search Agent as a Tool

Wrap the existing grep search inside a **sub-agent** that can:

1. **Re-rank** retrieved texts by relevance to the query
2. **Decide** if results are sufficient
3. **Refine and re-search** with a better query if needed (e.g. more specific terms, phrases)

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Main Email Agent                                                        │
│  (calls search_appier_docs for email drafting)                           │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Search Agent (sub-agent / tool with brain)                              │
│                                                                          │
│  1. Initial search: query → extract terms → grep → raw matches           │
│  2. Re-rank: LLM scores each match (1-5) for relevance to query         │
│  3. Filter: keep only matches above threshold (e.g. score ≥ 3)           │
│  4. Sufficiency check: LLM decides "enough?" or "need more?"             │
│  5. If insufficient → refine query (e.g. add phrases, exclude terms)     │
│     → run another grep with refined terms                                 │
│     → re-rank new matches → merge with previous → dedupe                  │
│  6. Return top-N by score, truncate to context limit                     │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Components

| Component | Purpose |
|-----------|---------|
| **Re-ranker** | LLM scores each match (1–5) given (query, match_text). Filter by threshold. |
| **Sufficiency checker** | LLM answers: "Is this enough to answer the query?" Yes / No + reason. |
| **Query refiner** | If insufficient, LLM produces refined search terms (phrases, exclusions). |
| **Search loop** | Max 2–3 iterations to avoid runaway. Merge results, dedupe, re-rank. |

---

## Implementation Options

### Option A: Sub-agent (LangGraph / LangChain)

- Search agent has tools: `grep_search`, `rerank`, (internal)
- Uses `create_agent` with a search-specific system prompt
- Main agent calls `search_appier_docs` → that invokes the search agent

### Option B: Orchestrator function (simpler)

- Single Python function that:
  1. Runs grep (existing `search_documents`)
  2. Calls LLM to re-rank (batch or one-by-one)
  3. Calls LLM to check sufficiency
  4. If insufficient, refines query and repeats 1–2
  5. Returns merged, ranked, truncated context

### Option C: Tool that returns a "search plan"

- LLM first outputs: `{ "terms": [...], "phrases": [...], "exclude": [...] }`
- Grep uses that directly
- Post-grep: re-rank only (no iterative search)

---

## Suggested Phasing

| Phase | Scope | Effort |
|-------|-------|--------|
| **1** | Re-rank only — add LLM scoring after grep, filter low scores | Low |
| **2** | Phrase search — improve term extractor to output phrases, grep for quoted strings | Low |
| **3** | Sufficiency check + refined search — one optional second pass | Medium |
| **4** | Full search agent — sub-agent with loop, max 2–3 iterations | Medium–High |

---

## Cost / Latency Trade-offs

| Addition | Extra LLM calls | Latency |
|----------|-----------------|---------|
| Re-rank (batch) | 1 (batch of matches) | +2–5 s |
| Sufficiency check | 1 | +1–2 s |
| Refined search | 1 (extract) + 1 (sufficiency) | +3–5 s |
| **Total (2 passes)** | ~3–4 | +6–12 s |

---

## References

- Current search: `src/agent/tools/doc_search.py`
- Term extraction: `src/agent/search_terms_extractor.py`
- Tool wiring: `src/agent/email_agent.py` (search_appier_docs)
