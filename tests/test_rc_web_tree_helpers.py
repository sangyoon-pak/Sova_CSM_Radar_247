"""Unit tests for RC URL-tree helper behavior."""

import unittest
from unittest.mock import Mock, patch

from src.agent.tools.rc_url_tree_discovery import discover_url_tree
from src.agent.tools.rc_web_search import (
    _format_tree_candidate_lines,
    _is_weak_tree_result,
    _select_tree_urls,
    _strip_html_to_text,
    _tree_no_evidence_message,
)


class TestRcWebTreeHelpers(unittest.TestCase):
    def test_format_tree_candidate_lines_includes_title(self):
        rows = [
            {
                "url": "https://docs.example.com/ref/foo",
                "title": "Foo API",
                "depth": 2,
                "parent_url": "https://docs.example.com/ref",
                "metadata": {"h1": "Foo endpoint", "description": "Create and update Foo objects."},
            }
        ]
        lines = _format_tree_candidate_lines(rows)
        self.assertEqual(len(lines), 1)
        self.assertIn("https://docs.example.com/ref/foo", lines[0])
        self.assertIn("title=Foo API", lines[0])
        self.assertIn("h1=Foo endpoint", lines[0])
        self.assertIn("description=Create and update Foo objects.", lines[0])
        self.assertIn("path_terms=ref foo", lines[0])
        self.assertIn("depth=2", lines[0])

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

    def test_tree_quality_allows_single_deep_fetched_citation(self):
        weak, meta = _is_weak_tree_result(
            "docs.example.com",
            (
                "This documentation page directly answers the question with concrete behavior, parameter "
                "semantics, return behavior, and warnings that are specific enough for a CSM to cite safely "
                "when responding to a customer."
            ),
            ["https://docs.example.com/reference/users"],
            fetched_count=1,
        )
        self.assertFalse(weak)
        self.assertEqual(meta["citation_deep_links"], 1)
        self.assertTrue(meta["tree_single_deep_citation_allowed"])

    def test_strip_html_prefers_article_body_over_sidebar(self):
        # ReadMe-style layout: TOC/nav live outside <article>; excerpt must not be sidebar soup.
        html_blob = """<body>
          <aside>TOC Analytics Campaigns SEGMENTS FAQs SDK FULL TREE TEXT</aside>
          <main>
            <nav>Home Guides Announcements 한국어홈</nav>
            <article class="rm-Article">
              <header><h1>iOS Push Campaigns</h1></header>
              <p>Note that push opt-in &#x2014; users who opt out won't receive pushes.</p>
              <table><tr><td>Configure credentials</td><td>Use .p8 or .p12 with APNs.</td></tr></table>
            </article>
          </main></body>"""
        text = _strip_html_to_text(html_blob)
        self.assertIn("iOS Push Campaigns", text)
        self.assertIn(".p8", text)
        self.assertIn("won't receive", text)
        self.assertNotIn("FULL TREE TEXT", text)
        self.assertNotIn("SEGMENTS FAQs SDK", text)

    def test_strip_html_falls_back_when_no_article(self):
        html_blob = '<html><body><p>No article tag, plain body only.</p></body></html>'
        text = _strip_html_to_text(html_blob)
        self.assertIn("plain body only", text)

    def test_discover_url_tree_reads_sitemap_index_metadata_and_filters_assets(self):
        def fake_get(url, **_kwargs):
            resp = Mock()
            resp.status_code = 200
            resp.headers = {"Content-Type": "text/xml"}
            if url == "https://docs.example.com/robots.txt":
                resp.text = "Sitemap: https://docs.example.com/sitemap-index.xml\n"
            elif url == "https://docs.example.com/sitemap.xml":
                resp.status_code = 404
                resp.text = ""
            elif url == "https://docs.example.com/sitemap_index.xml":
                resp.status_code = 404
                resp.text = ""
            elif url == "https://docs.example.com/sitemap-index.xml":
                resp.text = """<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
                <sitemap><loc>https://docs.example.com/reference-sitemap.xml</loc></sitemap>
                </sitemapindex>"""
            elif url == "https://docs.example.com/reference-sitemap.xml":
                resp.text = """<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
                <url><loc>https://docs.example.com/reference/users</loc></url>
                <url><loc>https://docs.example.com/assets/logo.png</loc></url>
                </urlset>"""
            elif url == "https://docs.example.com/":
                resp.headers = {"Content-Type": "text/html"}
                resp.text = """<html><head><title>Docs Home</title><meta name="description" content="Developer docs"></head>
                <body><h1>Documentation</h1><a href="/reference/users/create">Create users</a>
                <a href="/assets/app.js">Asset</a></body></html>"""
            elif url == "https://docs.example.com/reference/users/create":
                resp.headers = {"Content-Type": "text/html"}
                resp.text = "<html><head><title>Create users</title></head><body></body></html>"
            else:
                resp.status_code = 404
                resp.text = ""
            return resp

        with patch("src.agent.tools.rc_url_tree_discovery.requests.get", side_effect=fake_get):
            nodes, by_depth = discover_url_tree(
                base_url="https://docs.example.com/",
                max_urls=20,
                max_depth=1,
                timeout_s=1,
            )

        urls = {n["url"] for n in nodes}
        self.assertIn("https://docs.example.com/reference/users", urls)
        self.assertIn("https://docs.example.com/reference/users/create", urls)
        self.assertNotIn("https://docs.example.com/assets/logo.png", urls)
        self.assertNotIn("https://docs.example.com/assets/app.js", urls)
        root = next(n for n in nodes if n["url"] == "https://docs.example.com/")
        self.assertEqual(root.get("title"), "Docs Home")
        self.assertEqual(root.get("metadata", {}).get("h1"), "Documentation")
        self.assertEqual(root.get("metadata", {}).get("description"), "Developer docs")
        self.assertGreaterEqual(int(by_depth.get("1") or 0), 1)

    def test_select_tree_urls_retains_first_pass_when_final_arbitration_empty(self):
        calls = []

        def fake_pick(*, user_query, batch_lines, allowed_urls, pick_n):
            calls.append(list(batch_lines))
            if len(calls) == 1:
                return [
                    {
                        "url": "https://docs.example.com/reference/users",
                        "reason": "users reference",
                        "confidence": 0.91,
                    }
                ]
            return []

        nodes = [
            {"url": "https://docs.example.com/reference/users", "title": "Users API"},
            {"url": "https://docs.example.com/guides/intro", "title": "Intro"},
        ]
        with patch("src.agent.tools.rc_web_search._llm_pick_urls_for_batch", side_effect=fake_pick):
            selected, ranked, final_pick = _select_tree_urls("How do I create users?", nodes, visit_limit=2)

        self.assertEqual(selected, ["https://docs.example.com/reference/users"])
        self.assertEqual(ranked[0]["url"], "https://docs.example.com/reference/users")
        self.assertIn("Retained from first-pass", final_pick[0]["reason"])


if __name__ == "__main__":
    unittest.main()
