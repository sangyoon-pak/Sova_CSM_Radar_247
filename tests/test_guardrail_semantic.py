"""Unit tests for NL phrase parsing and fallback matching."""
import importlib.util
from pathlib import Path

_GS = Path(__file__).resolve().parents[1] / "src" / "guardrail_semantic.py"
_SPEC = importlib.util.spec_from_file_location("guardrail_semantic", _GS)
assert _SPEC and _SPEC.loader
_MOD = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MOD)
parse_intent_phrases_blob = _MOD.parse_intent_phrases_blob
_fallback_phrase_match = _MOD._fallback_phrase_match


def test_parse_json_array():
    assert parse_intent_phrases_blob('["a", "b"]') == ["a", "b"]


def test_parse_newline_and_comma_legacy():
    assert parse_intent_phrases_blob("x,y\nz") == ["x", "y", "z"]


def test_fallback_substring():
    assert _fallback_phrase_match("quota exceeded", "Client QUOTA exceeded alert") is True


def test_fallback_token_overlap():
    assert _fallback_phrase_match("monthly newsletter digest", "Our monthly digest for partners") is True
