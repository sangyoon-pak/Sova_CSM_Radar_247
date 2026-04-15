import importlib.util
import unittest
from pathlib import Path

_PROBE_ACTIONS_PATH = Path(__file__).resolve().parents[1] / "src" / "agent" / "probe_actions.py"
_SPEC = importlib.util.spec_from_file_location("probe_actions", _PROBE_ACTIONS_PATH)
assert _SPEC and _SPEC.loader
_MOD = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MOD)
merge_csm_actions_metadata = _MOD.merge_csm_actions_metadata


def _probe_output(actions: list[dict]) -> str:
    return '{"actions": ' + __import__("json").dumps(actions) + "}"


def test_guardrail_excludes_internal_notice_in_balanced_mode():
    output = _probe_output(
        [
            {
                "title": "Quota exceeded alert",
                "brief": "internal alert for quota exceeded in monitoring",
                "email_from": "alerts@internal.company.com",
                "gmail_thread_id": "thread12345",
            }
        ]
    )
    md = merge_csm_actions_metadata(
        output,
        {
            "guardrail_strictness": "balanced",
            "guardrail_exclude_sender_domains": "internal.company.com",
        },
    )
    assert md.get("csm_actions") == []


def test_guardrail_permissive_keeps_informational_card():
    output = _probe_output(
        [
            {
                "title": "Monthly newsletter",
                "brief": "newsletter and monthly update",
                "email_from": "news@customer.com",
                "gmail_thread_id": "thread12345",
            }
        ]
    )
    md = merge_csm_actions_metadata(
        output,
        {
            "guardrail_strictness": "permissive",
            "guardrail_include_sender_domains": "",
            "guardrail_exclude_sender_domains": "",
            "guardrail_include_intent_keywords": "",
            "guardrail_exclude_intent_keywords": "",
        },
    )
    acts = md.get("csm_actions") or []
    assert len(acts) == 1
    assert acts[0]["relevance_outcome"] == "requires_csm_action"
    assert acts[0]["relevance_reason"] == "permissive_ambiguous_intent"


def test_action_contract_includes_required_fields():
    output = _probe_output(
        [
            {
                "title": "Need help with API error",
                "brief": "customer blocked by API error",
                "email_from": "ops@customer.com",
                "email_subject": "API issue",
                "gmail_thread_id": "thread12345",
                "include_on_dashboard": True,
                "category": "product_technical",
            }
        ]
    )
    md = merge_csm_actions_metadata(
        output,
        {
            "guardrail_strictness": "balanced",
            "guardrail_include_sender_domains": "",
            "guardrail_exclude_sender_domains": "",
            "guardrail_include_intent_keywords": "",
            "guardrail_exclude_intent_keywords": "",
        },
    )
    action = (md.get("csm_actions") or [])[0]
    for key in (
        "thread_title",
        "customer_identifier",
        "customer_domain",
        "priority",
        "confidence_label",
        "owner",
        "feedback_notes",
        "relevance_outcome",
        "relevance_reason",
    ):
        assert key in action
    assert "csm_decision_summary" in md
    assert "csm_probe_diagnostics" in md


class TestExplicitDashboardTrustsModel(unittest.TestCase):
    """When include_on_dashboard is true, server heuristics must not drop except Configure excludes."""

    def test_quota_text_kept_when_model_flags_dashboard(self):
        output = _probe_output(
            [
                {
                    "title": "AIRIS quota exceeded",
                    "brief": "Client quota exceeded; requires attention.",
                    "email_from": "alerts@woopra.com",
                    "email_subject": "[AIRIS QUOTA EXCEEDED]: Client X",
                    "gmail_thread_id": "threadquota1",
                    "include_on_dashboard": True,
                }
            ]
        )
        md = merge_csm_actions_metadata(
            output,
            {
                "guardrail_strictness": "balanced",
                "guardrail_include_sender_domains": "",
                "guardrail_exclude_sender_domains": "",
                "guardrail_include_intent_keywords": "",
                "guardrail_exclude_intent_keywords": "",
            },
        )
        acts = md.get("csm_actions") or []
        self.assertEqual(len(acts), 1)
        self.assertEqual(acts[0]["relevance_outcome"], "requires_csm_action")
        self.assertEqual(acts[0]["relevance_reason"], "model_include_dashboard")

    def test_exclude_intent_quota_drops_even_when_model_includes_dashboard(self):
        output = _probe_output(
            [
                {
                    "title": "AIRIS Quota Exceeded",
                    "brief": "Quota exceeded for client.",
                    "email_from": "alerts@woopra.com",
                    "gmail_thread_id": "tidq",
                    "include_on_dashboard": True,
                }
            ]
        )
        md = merge_csm_actions_metadata(
            output,
            {
                "guardrail_strictness": "balanced",
                "guardrail_include_sender_domains": "",
                "guardrail_exclude_sender_domains": "",
                "guardrail_include_intent_keywords": "",
                "guardrail_exclude_intent_keywords": "quota, exceeded",
            },
        )
        self.assertEqual(md.get("csm_actions"), [])

    def test_configure_exclude_domain_still_drops_even_if_include_true(self):
        output = _probe_output(
            [
                {
                    "title": "Internal",
                    "brief": "Something",
                    "email_from": "x@internal.company.com",
                    "gmail_thread_id": "t1",
                    "include_on_dashboard": True,
                }
            ]
        )
        md = merge_csm_actions_metadata(
            output,
            {
                "guardrail_strictness": "balanced",
                "guardrail_exclude_sender_domains": "internal.company.com",
            },
        )
        self.assertEqual(md.get("csm_actions"), [])


class TestRelevanceHeuristic(unittest.TestCase):
    """Structured LLM fields + Configure; no server keyword intent lists."""

    def test_model_category_product_technical_without_include_flag(self):
        """`category: product_technical` alone is enough for dashboard intent."""
        output = _probe_output(
            [
                {
                    "title": "업데이트 안내",
                    "brief": "고객사 속성 반영 관련 후속.",
                    "email_from": "c@client.kr",
                    "email_subject": "마케팅활용동의 회원 속성 업데이트",
                    "gmail_thread_id": "threadcat1",
                    "category": "product_technical",
                }
            ]
        )
        md = merge_csm_actions_metadata(
            output,
            {
                "guardrail_strictness": "balanced",
                "guardrail_include_sender_domains": "",
                "guardrail_exclude_sender_domains": "",
                "guardrail_include_intent_keywords": "",
                "guardrail_exclude_intent_keywords": "",
            },
        )
        acts = md.get("csm_actions") or []
        self.assertEqual(len(acts), 1)
        self.assertEqual(acts[0]["relevance_outcome"], "requires_csm_action")
        self.assertEqual(acts[0]["relevance_reason"], "model_category:product_technical")

    def test_model_include_dashboard_requires_action(self):
        """Explicit model_include_dashboard keeps the row without server keyword heuristics."""
        output = _probe_output(
            [
                {
                    "title": "Journey issues",
                    "brief": "Client is experiencing issues with journey triggers.",
                    "email_from": "c@client.com",
                    "gmail_thread_id": "threadabc123",
                    "include_on_dashboard": True,
                }
            ]
        )
        md = merge_csm_actions_metadata(
            output,
            {
                "guardrail_strictness": "balanced",
                "guardrail_include_sender_domains": "",
                "guardrail_exclude_sender_domains": "",
                "guardrail_include_intent_keywords": "",
                "guardrail_exclude_intent_keywords": "",
            },
        )
        acts = md.get("csm_actions") or []
        self.assertEqual(len(acts), 1)
        self.assertEqual(acts[0]["relevance_outcome"], "requires_csm_action")
        self.assertEqual(acts[0]["relevance_reason"], "model_include_dashboard")

    def test_configure_include_intent_keyword_surfaces_without_llm_flags(self):
        """UI include-intent keywords are the operator’s lever — not Python regex lists."""
        output = _probe_output(
            [
                {
                    "title": "Newsletter",
                    "brief": "Monthly digest",
                    "email_from": "news@acme.com",
                    "gmail_thread_id": "tidnews",
                }
            ]
        )
        md = merge_csm_actions_metadata(
            output,
            {
                "guardrail_strictness": "balanced",
                "guardrail_include_sender_domains": "",
                "guardrail_exclude_sender_domains": "",
                "guardrail_include_intent_keywords": "newsletter, digest",
                "guardrail_exclude_intent_keywords": "",
            },
        )
        acts = md.get("csm_actions") or []
        self.assertEqual(len(acts), 1)
        self.assertEqual(acts[0]["relevance_reason"], "user_include_intent_phrase")

    def test_balanced_drops_ambiguous_without_dashboard_signals(self):
        output = _probe_output(
            [{"title": "T", "brief": "Help with API", "gmail_thread_id": "threadxyz"}]
        )
        md = merge_csm_actions_metadata(
            output,
            {
                "guardrail_strictness": "balanced",
                "guardrail_include_sender_domains": "",
                "guardrail_exclude_sender_domains": "",
                "guardrail_include_intent_keywords": "",
                "guardrail_exclude_intent_keywords": "",
            },
        )
        d = md.get("csm_probe_diagnostics")
        self.assertIsInstance(d, dict)
        self.assertEqual(d.get("raw_action_count"), 1)
        self.assertEqual(d.get("kept_after_normalization"), 0)
        self.assertIn("normalization_dropped", d)
        self.assertIn("kept_after_merge", d)


