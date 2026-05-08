"""Tests for the early-skip preflight that lets the probe agent avoid retrieval on
unchanged Gmail threads.

Covers:
- `parse_inbox_tool_output_thread_message_ids` parses a realistic inbox blob.
- `_extract_latest_message_id_by_thread_from_events` reads the same data from a UI trace event.
- `merge_csm_actions_metadata` persists `gmail_latest_message_id` on each action so the next
  probe can compare against it.
- `_build_probe_preflight_trailer` emits `PROBE_PREFLIGHT` only for threads whose latest
  message id matches a previously persisted dashboard card.
"""

from __future__ import annotations

import json
import unittest
from unittest.mock import patch

from src.agent.probe_actions import (
    _extract_latest_message_id_by_thread_from_events,
    merge_csm_actions_metadata,
    parse_inbox_tool_output_thread_message_ids,
)
from src.agent.tools.gmail_tool import (
    _PROBE_PREFLIGHT_SKIP_KEY,
    _PROBE_PREFLIGHT_TRAILER_HEADER,
    _build_probe_preflight_trailer,
)


_INBOX_BLOB = """id\tmsg_aaa111
thread_id\t199e90fa3a8c2bd1
label_ids\tINBOX,IMPORTANT
from\tAlice <alice@customer.com>
to\tcsm@vendor.com
subject\tQuestion about API rate limits
date\tWed, 06 May 2026 09:11:00 +0000

We hit a rate limit yesterday.

============================================================

id\tmsg_bbb222
thread_id\t199e7777ffff0001
label_ids\tINBOX
from\tBob <bob@another.com>
to\tcsm@vendor.com
subject\tQuota exceeded warning
date\tWed, 06 May 2026 12:00:00 +0000

Daily quota report.
"""


class TestPreflightParsers(unittest.TestCase):
    def test_parse_inbox_tool_output_thread_message_ids(self):
        out = parse_inbox_tool_output_thread_message_ids(_INBOX_BLOB)
        self.assertEqual(
            out,
            {
                "199e90fa3a8c2bd1": "msg_aaa111",
                "199e7777ffff0001": "msg_bbb222",
            },
        )

    def test_parse_handles_escaped_event_detail(self):
        # UI trace events sometimes serialize tool output with escaped \n / \t.
        escaped = _INBOX_BLOB.replace("\n", "\\n").replace("\t", "\\t")
        out = parse_inbox_tool_output_thread_message_ids(escaped)
        self.assertIn("199e90fa3a8c2bd1", out)
        self.assertEqual(out["199e90fa3a8c2bd1"], "msg_aaa111")

    def test_extract_latest_message_id_by_thread_from_events(self):
        md = {
            "events": [
                {"type": "tool_start", "title": "Tool start: fetch_inbox_emails", "detail": ""},
                {
                    "type": "tool_end",
                    "title": "fetch_inbox_emails Tool output",
                    "detail": _INBOX_BLOB,
                },
            ]
        }
        out = _extract_latest_message_id_by_thread_from_events(md)
        self.assertEqual(out["199e90fa3a8c2bd1"], "msg_aaa111")
        self.assertEqual(out["199e7777ffff0001"], "msg_bbb222")


class TestMergeStampsLatestMessageId(unittest.TestCase):
    def test_gmail_latest_message_id_is_persisted_on_each_action(self):
        probe_output = (
            "Here you go.\n\n"
            "```json\n"
            + json.dumps(
                {
                    "skipped_note": "",
                    "actions": [
                        {
                            "include_on_dashboard": True,
                            "category": "client_technical",
                            "title": "Investigate API rate limit",
                            "brief": "Customer hit limits yesterday and needs a confirmed quota.",
                            "curated_answer": "Confirm tier and burst window.",
                            "client_query_digest": "Why is my account hitting rate limits?",
                            "thread_summary": "Alice asks about rate limits on production keys.",
                            "gmail_thread_id": "199e90fa3a8c2bd1",
                            "email_from": "Alice <alice@customer.com>",
                            "email_subject": "Question about API rate limits",
                        }
                    ],
                }
            )
            + "\n```\n"
        )
        base = {
            "events": [
                {
                    "type": "tool_end",
                    "title": "fetch_inbox_emails Tool output",
                    "detail": _INBOX_BLOB,
                }
            ],
            "tools_used": ["fetch_inbox_emails", "search_product_docs"],
        }
        merged = merge_csm_actions_metadata(probe_output, base)
        actions = merged.get("csm_actions") or []
        self.assertEqual(len(actions), 1)
        self.assertEqual(actions[0].get("gmail_latest_message_id"), "msg_aaa111")


class TestPreflightTrailer(unittest.TestCase):
    def test_trailer_lists_only_threads_with_matching_message_id(self):
        prev_by_thread = {
            # Same latest message id → should be skipped.
            "gid:199e90fa3a8c2bd1": {"gmail_latest_message_id": "msg_aaa111"},
            # Different latest message id → must NOT be skipped.
            "gid:199e7777ffff0001": {"gmail_latest_message_id": "msg_old_xyz"},
        }
        with patch(
            "src.db.database.latest_dashboard_actions_by_gmail_thread",
            return_value=prev_by_thread,
        ):
            trailer = _build_probe_preflight_trailer(_INBOX_BLOB)
        self.assertIn(_PROBE_PREFLIGHT_TRAILER_HEADER, trailer)
        skip_line = next(
            (ln for ln in trailer.splitlines() if ln.startswith(_PROBE_PREFLIGHT_SKIP_KEY + "=")),
            "",
        )
        self.assertTrue(skip_line, msg="Expected RETRIEVAL_SKIP_THREAD_IDS line in trailer")
        ids = skip_line.split("=", 1)[1].split(",")
        self.assertEqual(ids, ["199e90fa3a8c2bd1"])

    def test_trailer_empty_when_no_prior_card(self):
        with patch(
            "src.db.database.latest_dashboard_actions_by_gmail_thread",
            return_value={},
        ):
            trailer = _build_probe_preflight_trailer(_INBOX_BLOB)
        self.assertEqual(trailer, "")

    def test_trailer_empty_when_inbox_blob_empty(self):
        with patch(
            "src.db.database.latest_dashboard_actions_by_gmail_thread",
            return_value={"gid:199e90fa3a8c2bd1": {"gmail_latest_message_id": "msg_aaa111"}},
        ):
            trailer = _build_probe_preflight_trailer("")
        self.assertEqual(trailer, "")


if __name__ == "__main__":
    unittest.main()
