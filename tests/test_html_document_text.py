"""Tests for neutral HTML → excerpt text."""

import unittest

from src.agent.tools.html_document_text import html_to_document_excerpt_text, visible_text_from_html_fragment


class TestHtmlDocumentText(unittest.TestCase):
    def test_skips_sidebar_not_inside_article_readme_like(self):
        html_blob = """<body>
          <aside>SIDEBAR_MEGA_NAV_TREE</aside>
          <main>
            <nav>TOP_NAV_LINKS_ROW</nav>
            <article>
              <header><h1>Doc Title Alpha</h1></header>
              <p>Substantive body about integration steps and deadlines.</p>
            </article>
          </main></body>"""
        text = html_to_document_excerpt_text(html_blob)
        self.assertIn("Doc Title Alpha", text)
        self.assertIn("Substantive body", text)
        self.assertNotIn("SIDEBAR_MEGA_NAV_TREE", text)
        self.assertNotIn("TOP_NAV_LINKS_ROW", text)

    def test_keeps_article_header_and_aside_note(self):
        html = """<article>
          <header><h1>API limits</h1></header>
          <aside>Note: rate limit is per workspace.</aside>
          <p>Details here.</p>
        </article>"""
        t = html_to_document_excerpt_text(html)
        self.assertIn("API limits", t)
        self.assertIn("rate limit is per workspace", t)

    def test_prefers_dense_article_when_two_exist(self):
        html = """<body>
          <article id="tiny"><p>Skip</p></article>
          <article id="hero">
            <h1>Shipping guide</h1>
            """ + "<p>More copy.</p>" * 24 + """
          </article>
        </body>"""
        t = html_to_document_excerpt_text(html)
        self.assertIn("Shipping guide", t)
        self.assertNotIn("Skip", t)

    def test_json_ld_used_when_markup_is_boilerplate(self):
        html = """<html><head><title>x</title>
        <script type="application/ld+json">
        {"@type":"Article","articleBody":"LD primary paragraph with enough chars to qualify for scoring threshold here."}
        </script></head><body><nav>NAV_REPEAT</nav><p>tiny</p></body></html>"""
        t = html_to_document_excerpt_text(html)
        self.assertIn("LD primary paragraph", t)
        self.assertNotIn("NAV_REPEAT", t)

    def test_visible_fragments_fallback_on_bad_markup(self):
        # Parser should not explode; malformed closing still yields something.
        t = visible_text_from_html_fragment("<article><p>OK</article>")
        self.assertIn("OK", t)


if __name__ == "__main__":
    unittest.main()
