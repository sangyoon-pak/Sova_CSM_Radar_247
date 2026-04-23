"""Tests for chat-triggered full-inbox probe intent (LLM classifier, mocked in unit tests)."""

from src.agent.email_agent import is_inbox_probe_chat_intent


def test_off_never_probes_and_skips_llm(monkeypatch):
    called: list[str] = []

    def boom(text: str):
        called.append(text)
        return True

    monkeypatch.setenv("PROBE_THREAD_INTENT_CLASSIFIER", "off")
    monkeypatch.setattr("src.agent.email_agent._classify_full_inbox_probe_intent_llm", boom)
    assert not is_inbox_probe_chat_intent("scan inbox")
    assert called == []


def test_empty_message_false(monkeypatch):
    monkeypatch.setenv("PROBE_THREAD_INTENT_CLASSIFIER", "llm")
    assert not is_inbox_probe_chat_intent("")
    assert not is_inbox_probe_chat_intent("   ")


def test_llm_true_when_classifier_returns_true(monkeypatch):
    monkeypatch.setenv("PROBE_THREAD_INTENT_CLASSIFIER", "llm")
    monkeypatch.setattr(
        "src.agent.email_agent._classify_full_inbox_probe_intent_llm",
        lambda text: True,
    )
    assert is_inbox_probe_chat_intent("scan inbox")
    assert is_inbox_probe_chat_intent("anything at all")


def test_llm_false_when_classifier_returns_false(monkeypatch):
    monkeypatch.setenv("PROBE_THREAD_INTENT_CLASSIFIER", "llm")
    monkeypatch.setattr(
        "src.agent.email_agent._classify_full_inbox_probe_intent_llm",
        lambda text: False,
    )
    assert not is_inbox_probe_chat_intent("scan inbox")
    assert not is_inbox_probe_chat_intent("what is an inbox probe")


def test_llm_false_when_classifier_returns_none(monkeypatch):
    monkeypatch.setenv("PROBE_THREAD_INTENT_CLASSIFIER", "llm")
    monkeypatch.setattr(
        "src.agent.email_agent._classify_full_inbox_probe_intent_llm",
        lambda text: None,
    )
    assert not is_inbox_probe_chat_intent("hello")


def test_llm_respects_classifier_per_message(monkeypatch):
    monkeypatch.setenv("PROBE_THREAD_INTENT_CLASSIFIER", "llm")
    monkeypatch.setattr(
        "src.agent.email_agent._classify_full_inbox_probe_intent_llm",
        lambda text: text.strip().lower().startswith("probe:"),
    )
    assert is_inbox_probe_chat_intent("probe: refresh dashboard")
    assert not is_inbox_probe_chat_intent("just chatting")
