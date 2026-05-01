"""Unit tests for RC URL-tree helper behavior (no LLM calls)."""

import unittest

from src.agent.tools.rc_web_search import _format_tree_candidate_lines, _tree_no_evidence_message


class TestRcWebTreeHelpers(unittest.TestCase):
    def test_format_tree_candidate_lines_includes_title(self):
        rows = [{"url": "https://docs.example.com/ref/foo", "title": "Foo API"}]
        lines = _format_tree_candidate_lines(rows)
        self.assertEqual(len(lines), 1)
        self.assertIn("https://docs.example.com/ref/foo", lines[0])
        self.assertIn("Foo API", lines[0])

    def test_format_tree_candidate_lines_skips_empty_url(self):
        rows = [{"url": "", "title": "x"}, {"url": "https://docs.example.com/a", "title": ""}]
        lines = _format_tree_candidate_lines(rows)
        self.assertEqual(len(lines), 1)
        self.assertIn("https://docs.example.com/a", lines[0])

    def test_tree_no_evidence_message_contains_reason(self):
        msg = _tree_no_evidence_message(
            "docs.example.com",
            reason="Test reason",
            selected_urls=["https://docs.example.com/a"],
            fetched_count=0,
        )
        self.assertIn("docs.example.com", msg)
        self.assertIn("Test reason", msg)
        self.assertIn("strict quality gate", msg.lower())


if __name__ == "__main__":
    unittest.main()
