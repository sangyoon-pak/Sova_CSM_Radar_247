"""Tests for the customer-email picker + card "From" anchoring used by the action dashboard.

Covers:
- `_pick_external_customer_email` prefers a curated `customer_email_domains` over the
  generic "non-internal" fallback even when the curated address is listed after an
  external-but-unrelated one.
- The picker still resolves an external sender when the curated registry is empty.
- `_maybe_anchor_email_from_to_customer` rewrites the displayed `email_from` to the
  customer when the literal From line is internal but a customer was identified.
- `_maybe_anchor_email_from_to_customer` is a no-op when the From is already external,
  when the customer is internal, or when no customer was resolved.
- `merge_csm_actions_metadata` overrides a model-emitted internal `customer_email` with
  the registry-backed answer surfaced by the inbox tool.
- `merge_csm_actions_metadata` refreshes existing card identity in-place via
  `database.update_dashboard_action_identity_inplace` when the new probe has the same body
  fingerprint as the prior card but identity changed (e.g. operator updated the registry).
"""

from __future__ import annotations

import json
import unittest
from unittest.mock import patch

from src.agent.probe_actions import (
    _maybe_anchor_email_from_to_customer,
    _pick_external_customer_email,
    merge_csm_actions_metadata,
)


class CustomerEmailPickerTest(unittest.TestCase):
    def test_curated_customer_domain_wins_over_generic_external(self):
        # Curated registry includes amorepacific.com — picker should prefer it even when an
        # internal you-address appears first AND another external address appears in between.
        with patch(
            "src.runtime_config.effective_customer_email_domains",
            return_value="amorepacific.com, partner.example.org",
        ):
            picked = _pick_external_customer_email(
                "Sangyoon Park <sangyoon.park@appier.com>",
                "Outsider <random@external.test>, Hangyu Kim <Hangyu10@amorepacific.com>",
            )
        self.assertEqual(picked, "hangyu10@amorepacific.com")

    def test_falls_back_to_first_non_internal_when_registry_empty(self):
        with patch(
            "src.runtime_config.effective_customer_email_domains",
            return_value="",
        ):
            picked = _pick_external_customer_email(
                "Sangyoon Park <sangyoon.park@appier.com>",
                "Hangyu Kim <Hangyu10@amorepacific.com>",
            )
        self.assertEqual(picked, "hangyu10@amorepacific.com")

    def test_anchors_email_from_to_customer_when_from_is_internal(self):
        action = {
            "email_from": "Sangyoon Park <sangyoon.park@appier.com>",
            "customer_email": "Hangyu10@amorepacific.com",
            "customer_identifier": "Hangyu Kim",
            "customer_domain": "appier.com",
        }
        _maybe_anchor_email_from_to_customer(action)
        self.assertEqual(action["email_from"], "Hangyu Kim <Hangyu10@amorepacific.com>")
        self.assertEqual(action["customer_domain"], "amorepacific.com")

    def test_does_not_anchor_when_from_is_already_external(self):
        action = {
            "email_from": "Hangyu Kim <Hangyu10@amorepacific.com>",
            "customer_email": "Hangyu10@amorepacific.com",
            "customer_identifier": "Hangyu Kim",
            "customer_domain": "amorepacific.com",
        }
        _maybe_anchor_email_from_to_customer(action)
        self.assertEqual(action["email_from"], "Hangyu Kim <Hangyu10@amorepacific.com>")
        self.assertEqual(action["customer_domain"], "amorepacific.com")

    def test_does_not_anchor_when_customer_is_also_internal(self):
        action = {
            "email_from": "Sangyoon Park <sangyoon.park@appier.com>",
            "customer_email": "teammate@appier.com",
            "customer_identifier": "Teammate",
            "customer_domain": "appier.com",
        }
        _maybe_anchor_email_from_to_customer(action)
        self.assertEqual(action["email_from"], "Sangyoon Park <sangyoon.park@appier.com>")

    def test_does_not_anchor_when_no_customer_resolved(self):
        action = {
            "email_from": "Sangyoon Park <sangyoon.park@appier.com>",
            "customer_email": "",
            "customer_identifier": "",
            "customer_domain": "appier.com",
        }
        _maybe_anchor_email_from_to_customer(action)
        self.assertEqual(action["email_from"], "Sangyoon Park <sangyoon.park@appier.com>")


_INBOX_BLOB = """id\tmsg_zzz999
thread_id\t19e019bce6f1f6c3
label_ids\tINBOX,IMPORTANT
from\tSangyoon Park <sangyoon.park@appier.com>
to\tHangyu Kim <Hangyu10@amorepacific.com>
subject\tRe: Time Frame 역할 문의
date\tFri, 08 May 2026 09:59:00 +0900

Reply body.
"""


def _probe_output_with_internal_customer_email() -> str:
    return (
        "Here is the dashboard JSON.\n\n"
        "```json\n"
        + json.dumps(
            {
                "skipped_note": "",
                "actions": [
                    {
                        "include_on_dashboard": True,
                        "category": "client_technical",
                        "title": "Re: Time Frame 역할 문의",
                        "brief": "김한규님이 Timeframe 기능에 대해 문의하셨습니다.",
                        "curated_answer": "Timeframe explanation here.",
                        "client_query_digest": "Timeframe 역할 문의",
                        "thread_summary": "Customer asks about Timeframe behavior.",
                        "gmail_thread_id": "19e019bce6f1f6c3",
                        # Model picked the latest message → mistakenly identified the operator
                        # as the customer. The merge step must override this from the inbox
                        # tool when the registry resolves a real external customer.
                        "email_from": "Sangyoon Park <sangyoon.park@appier.com>",
                        "email_subject": "Re: Time Frame 역할 문의",
                        "customer_email": "sangyoon.park@appier.com",
                        "customer_identifier": "Sangyoon Park",
                        "customer_domain": "appier.com",
                    }
                ],
            }
        )
        + "\n```\n"
    )


class CustomerEmailRegistryMergeOverrideTest(unittest.TestCase):
    def test_registry_overrides_model_internal_customer_email(self):
        base = {
            "events": [
                {
                    "type": "tool_end",
                    "title": "fetch_inbox_emails Tool output",
                    "detail": _INBOX_BLOB,
                }
            ],
            "tools_used": ["fetch_inbox_emails"],
        }
        with patch(
            "src.runtime_config.effective_customer_email_domains",
            return_value="amorepacific.com",
        ):
            merged = merge_csm_actions_metadata(_probe_output_with_internal_customer_email(), base)
        actions = merged.get("csm_actions") or []
        self.assertEqual(len(actions), 1, msg="card should not be filtered out by guardrails")
        a = actions[0]
        self.assertEqual(a["customer_email"], "hangyu10@amorepacific.com")
        self.assertEqual(a["customer_domain"], "amorepacific.com")
        # Anchor should also rewrite the displayed From to the customer.
        self.assertIn("amorepacific.com", a["email_from"].lower())
        self.assertIn("hangyu", a["email_from"].lower())

    def test_no_override_when_registry_empty(self):
        base = {
            "events": [
                {
                    "type": "tool_end",
                    "title": "fetch_inbox_emails Tool output",
                    "detail": _INBOX_BLOB,
                }
            ],
            "tools_used": ["fetch_inbox_emails"],
        }
        with patch(
            "src.runtime_config.effective_customer_email_domains",
            return_value="",
        ):
            merged = merge_csm_actions_metadata(_probe_output_with_internal_customer_email(), base)
        actions = merged.get("csm_actions") or []
        self.assertEqual(len(actions), 1)
        a = actions[0]
        # With no registry and `a` already populated, identity stays as the model emitted.
        self.assertEqual(a["customer_email"], "sangyoon.park@appier.com")
        self.assertEqual(a["customer_domain"], "appier.com")


class InPlaceIdentityRefreshTest(unittest.TestCase):
    def test_same_fingerprint_refreshes_identity_when_registry_changes(self):
        base = {
            "events": [
                {
                    "type": "tool_end",
                    "title": "fetch_inbox_emails Tool output",
                    "detail": _INBOX_BLOB,
                }
            ],
            "tools_used": ["fetch_inbox_emails"],
        }
        # Existing card on the dashboard, fingerprint will match this run's output.
        prev_card = {
            "title": "Re: Time Frame 역할 문의",
            "brief": "김한규님이 Timeframe 기능에 대해 문의하셨습니다.",
            "client_query_digest": "Timeframe 역할 문의",
            "thread_summary": "Customer asks about Timeframe behavior.",
            "curated_answer": "Timeframe explanation here.",
            "gmail_thread_id": "19e019bce6f1f6c3",
            "email_from": "Sangyoon Park <sangyoon.park@appier.com>",
            "email_subject": "Re: Time Frame 역할 문의",
            "customer_email": "sangyoon.park@appier.com",
            "customer_identifier": "Sangyoon Park",
            "customer_domain": "appier.com",
            "_probe_merge_interaction_id": 20,
        }
        existing_by_thread = {"gid:19e019bce6f1f6c3": prev_card}
        captured: dict = {}

        def _fake_inplace(interaction_id, *, gmail_thread_id, email_from, email_subject, identity):
            captured.update(
                {
                    "interaction_id": interaction_id,
                    "gmail_thread_id": gmail_thread_id,
                    "match_email_from": email_from,
                    "match_email_subject": email_subject,
                    "identity": dict(identity or {}),
                }
            )
            return True

        with patch(
            "src.runtime_config.effective_customer_email_domains",
            return_value="amorepacific.com",
        ), patch(
            "src.agent.probe_actions._probe_action_still_on_dashboard",
            return_value=True,
        ), patch(
            "src.db.database.update_dashboard_action_identity_inplace",
            side_effect=_fake_inplace,
        ):
            merged = merge_csm_actions_metadata(
                _probe_output_with_internal_customer_email(),
                base,
                existing_by_thread=existing_by_thread,
            )

        # Skipped because fingerprint matched a still-on-dashboard card → no new csm_actions row.
        self.assertEqual(len(merged.get("csm_actions") or []), 0)
        # In-place refresh was called against the source interaction with the new identity.
        self.assertEqual(captured.get("interaction_id"), 20)
        self.assertEqual(captured.get("gmail_thread_id"), "19e019bce6f1f6c3")
        self.assertEqual(captured.get("match_email_from"), "Sangyoon Park <sangyoon.park@appier.com>")
        self.assertEqual(captured.get("match_email_subject"), "Re: Time Frame 역할 문의")
        ident = captured.get("identity") or {}
        self.assertEqual(ident.get("customer_email"), "hangyu10@amorepacific.com")
        self.assertEqual(ident.get("customer_domain"), "amorepacific.com")
        self.assertIn("amorepacific.com", str(ident.get("email_from") or "").lower())


class ProductionShapedEventDetailTest(unittest.TestCase):
    """Defensive coverage: in production, `_UITraceCallback.on_tool_end` used to call
    `str(output)` on a LangChain `ToolMessage`, producing `content='...'` Python repr with
    embedded `\\n`/`\\t` escapes — which silently broke identity extraction. Now the
    callback unwraps `.content` first; this test pins both that the parser handles the
    historical escaped shape AND that the registry override still fires through it.
    """

    def test_merge_handles_repr_wrapped_inbox_with_escapes(self):
        # Simulate the historical shape: `content='...'` wrapper with `\n` / `\t` escaped.
        wrapped = (
            "content='id\\t19e019bce6f1f6c3\\n"
            "thread_id\\t19e019bce6f1f6c3\\n"
            "label_ids\\tINBOX\\n"
            "from\\t김한규/글로벌커머스 개발팀/Hankyu Kim Hangyu10@amorepacific.com\\n"
            "to\\t\"Sangyoon.Park\" sangyoon.park@appier.com\\n"
            "subject\\tTime Frame 역할 문의\\n"
            "date\\tThu, 07 May 2026 08:44:03 +0000\\n\\n"
            "Body of message 1.\\n'"
        )
        probe_output = (
            "OK.\n\n```json\n"
            + json.dumps(
                {
                    "skipped_note": "",
                    "actions": [
                        {
                            "include_on_dashboard": True,
                            "category": "client_technical",
                            "title": "Re: Time Frame 역할 문의",
                            "brief": "Customer asks about Timeframe.",
                            "curated_answer": "Explanation.",
                            "client_query_digest": "Timeframe 역할 문의",
                            "thread_summary": "Customer asks about Timeframe behavior.",
                            "gmail_thread_id": "19e019bce6f1f6c3",
                            "email_from": "Sangyoon Park <sangyoon.park@appier.com>",
                            "email_subject": "Re: Time Frame 역할 문의",
                            "customer_email": "sangyoon.park@appier.com",
                            "customer_identifier": "Sangyoon Park",
                            "customer_domain": "appier.com",
                        }
                    ],
                }
            )
            + "\n```\n"
        )
        base = {
            "events": [{"type": "tool_end", "title": "Tool output", "detail": wrapped}],
            "tools_used": ["fetch_inbox_emails"],
        }
        with patch(
            "src.runtime_config.effective_customer_email_domains",
            return_value="amorepacific.com",
        ):
            merged = merge_csm_actions_metadata(probe_output, base)
        actions = merged.get("csm_actions") or []
        self.assertEqual(len(actions), 1)
        a = actions[0]
        self.assertEqual(a["customer_email"], "hangyu10@amorepacific.com")
        self.assertEqual(a["customer_domain"], "amorepacific.com")
        self.assertIn("amorepacific.com", a["email_from"].lower())


if __name__ == "__main__":
    unittest.main()
