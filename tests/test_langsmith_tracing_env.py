"""Regression: Configure-driven LangSmith env must bypass langsmith.utils getenv LRU cache."""

from __future__ import annotations

import os
import unittest


class TestLangsmithTracingEnv(unittest.TestCase):
    def test_invalidate_langsmith_utils_caches_refreshes_tracing_v2(self):
        from langsmith.utils import get_env_var

        get_env_var.cache_clear()
        os.environ.pop("LANGCHAIN_TRACING_V2", None)
        os.environ.pop("LANGSMITH_TRACING_V2", None)
        self.assertEqual(get_env_var("TRACING_V2", default=""), "")
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        self.assertEqual(
            get_env_var("TRACING_V2", default=""),
            "",
            "langsmith caches getenv; stale read without cache_clear",
        )
        from src.agent.email_agent import _invalidate_langsmith_utils_caches

        _invalidate_langsmith_utils_caches()
        self.assertEqual(get_env_var("TRACING_V2", default=""), "true")
