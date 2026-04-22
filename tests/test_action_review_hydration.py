"""Runtime hydration for action-review Workbench threads."""
from src.agent.probe_actions import (
    _format_probe_events_retrieval_digest,
    build_action_review_runtime_hydration,
)


def test_tool_digest_pairs_start_end():
    events = [
        {"type": "tool_start", "title": "Tool start: search_product_docs", "detail": '{"query": "quota"}'},
        {"type": "tool_end", "title": "Tool output", "detail": "Retrieved documents … chunk A"},
    ]
    d = _format_probe_events_retrieval_digest(events)
    assert "search_product_docs" in d
    assert "Retrieved documents" in d


def test_build_hydration_from_csm_actions():
    md = {
        "csm_actions": [
            {
                "gmail_thread_id": "threadabcd12",
                "curated_answer": "Use the API.",
                "retrieval_evidence": [{"snippet": "Rate limit is …", "path": "docs/api.md"}],
                "references": ["docs/api.md"],
            }
        ],
        "events": [
            {"type": "tool_start", "title": "Tool start: fetch_gmail_thread", "detail": "threadabcd12"},
            {"type": "tool_end", "title": "Tool output", "detail": "From: client@example.com …"},
        ],
    }
    h = build_action_review_runtime_hydration(
        interaction_metadata=md,
        action_index=0,
        source_interaction_id=42,
        probe_source_thread_id=7,
    )
    assert h is not None
    assert "Fresh context" in h
    assert "threadabcd12" in h
    assert "Rate limit" in h
    assert "fetch_gmail_thread" in h


def test_build_hydration_bad_index():
    md = {"csm_actions": [{"gmail_thread_id": "x"}]}
    assert build_action_review_runtime_hydration(
        interaction_metadata=md,
        action_index=3,
        source_interaction_id=1,
    ) is None
