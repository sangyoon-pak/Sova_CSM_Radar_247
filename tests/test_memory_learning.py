"""Tests for feedback → learning distillation, learning API, and dashboard category PATCH."""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

from src.agent.memory import LEARNING_DISTILL_SYSTEM, refresh_learning_instructions
from src.agent.prompts import render_email_agent_system
from src.db import database


class TestMemoryLearning(unittest.TestCase):
    def test_learning_distill_system_has_no_stencil_vendor_examples(self):
        """Regression: concrete examples in the system prompt were copied by the model as fake rules."""
        lowered = LEARNING_DISTILL_SYSTEM.lower()
        self.assertNotIn("airis", lowered)
        self.assertNotIn("woopra", lowered)

    def setUp(self):
        self._tf = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self._tf.close()
        self.db_path = Path(self._tf.name)
        self._p_db = patch("src.db.database._db_path", lambda: self.db_path)
        self._p_db.start()
        database.init_db()

    def tearDown(self):
        self._p_db.stop()
        try:
            os.unlink(self.db_path)
        except OSError:
            pass

    def test_refresh_learning_instructions_empty_samples_clears_setting(self):
        database.set_app_setting("agent_learning_instructions", "old rules")
        out = refresh_learning_instructions(max_feedback=80)
        self.assertTrue(out.get("updated"))
        self.assertEqual(database.get_runtime_learning_instructions(), "")

    def test_refresh_learning_instructions_mock_llm_writes_bullets(self):
        database.insert_feedback(
            interaction_id=None,
            verdict="incorrect",
            note="Be shorter",
            correction="Max 3 bullets per reply",
            metadata=None,
        )

        class _Resp:
            content = "- Keep replies under three bullets.\n- Prefer numbered steps for runbooks."

        class _LLM:
            def invoke(self, _messages):
                return _Resp()

        with patch("src.agent.memory.get_chat_llm", return_value=_LLM()):
            out = refresh_learning_instructions(max_feedback=80)
        self.assertTrue(out.get("updated"))
        text = database.get_runtime_learning_instructions()
        self.assertIn("three bullets", text.lower())

    def test_refresh_learning_prompt_includes_action_dashboard_metadata(self):
        database.insert_feedback(
            interaction_id=1,
            verdict="incorrect",
            note="Do not surface internal quota alerts as client actions.",
            correction="",
            metadata={"source": "action_dashboard", "action_index": 0},
        )

        captured: dict = {}

        class _Resp:
            content = "- Skip internal quota alert cards.\n"

        class _LLM:
            def invoke(self, messages):
                captured["messages"] = messages
                return _Resp()

        with patch("src.agent.memory.get_chat_llm", return_value=_LLM()):
            refresh_learning_instructions(max_feedback=80)
        msgs = captured.get("messages") or []
        self.assertGreaterEqual(len(msgs), 2)
        human = str(getattr(msgs[1], "content", "") or "")
        self.assertIn("action_dashboard", human)
        self.assertIn("action_index=0", human)

    def test_get_agent_learning_instructions_snapshot_round_trip(self):
        database.set_app_setting("agent_learning_instructions", "- Rule A\n- Rule B")
        snap = database.get_agent_learning_instructions_snapshot()
        self.assertIn("Rule A", snap["instructions"])
        self.assertIsNotNone(snap.get("updated_at"))

    def test_render_email_agent_system_injects_learning(self):
        body = render_email_agent_system(
            vendor_name="V",
            product_context="P",
            role_title="R",
            learning_instructions="- Always cite KB.",
        )
        self.assertIn("Self-evolution memory", body)
        self.assertIn("Always cite KB", body)

    def test_insert_feedback_preserves_action_index_metadata(self):
        row = database.insert_feedback(
            interaction_id=42,
            verdict="useful",
            note="ok",
            correction=None,
            metadata={"source": "action_dashboard", "action_index": 3},
        )
        md_raw = row.get("metadata")
        md = json.loads(md_raw) if isinstance(md_raw, str) else (md_raw or {})
        self.assertEqual(md.get("action_index"), 3)
        self.assertEqual(md.get("source"), "action_dashboard")

    def test_learning_samples_include_run_history_verdict_only_with_note(self):
        database.insert_feedback(
            interaction_id=99,
            verdict="correct",
            note="[Run history] run #99: OK",
            correction=None,
            metadata={"source": "run_history"},
        )
        samples = database.get_learning_feedback_samples(limit=10)
        hit = next(
            (s for s in samples if s.get("verdict") == "correct" and "Run history" in str(s.get("note"))),
            None,
        )
        self.assertIsNotNone(hit)
        self.assertEqual(hit.get("interaction_id"), 99)

    def test_refresh_prompt_includes_run_context_for_run_history_useful(self):
        database.log_interaction(
            trigger_type="thread_probe",
            input_text="SUBJECT_LINE_UNIQUE_X9F2",
            output_text='{"cards": [{"title": "PROBE_JSON_SNIPPET_K3"}]}',
            status="completed",
            metadata=None,
        )
        row = database.get_interactions(limit=1, offset=0)[0]
        iid = int(row["id"])
        database.insert_feedback(
            interaction_id=iid,
            verdict="useful",
            note=f"[Run history] run #{iid}: Good",
            correction=None,
            metadata={"source": "run_history"},
        )
        captured: dict = {}

        class _Resp:
            content = "- When input resembles SUBJECT_LINE_UNIQUE_X9F2, keep surfacing probe cards like PROBE_JSON_SNIPPET_K3.\n"

        class _LLM:
            def invoke(self, messages):
                captured["messages"] = messages
                return _Resp()

        with patch("src.agent.memory.get_chat_llm", return_value=_LLM()):
            refresh_learning_instructions(max_feedback=80)
        msgs = captured.get("messages") or []
        human = str(getattr(msgs[1], "content", "") or "")
        self.assertIn("run_context", human)
        self.assertIn("SUBJECT_LINE_UNIQUE_X9F2", human)
        self.assertIn("PROBE_JSON_SNIPPET_K3", human)


class TestMemoryLearningApi(unittest.TestCase):
    def setUp(self):
        self._tf = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self._tf.close()
        self.db_path = Path(self._tf.name)
        self._p_db = patch("src.db.database._db_path", lambda: self.db_path)
        self._p_db.start()
        database.init_db()

    def tearDown(self):
        self._p_db.stop()
        try:
            os.unlink(self.db_path)
        except OSError:
            pass

    def test_get_memory_learning(self):
        database.set_app_setting("agent_learning_instructions", "- From API test")
        from src.main import app

        with TestClient(app) as client:
            r = client.get("/memory/learning")
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertIn("From API test", data.get("instructions", ""))

    def test_delete_memory_learning_clears_distilled_text(self):
        database.set_app_setting("agent_learning_instructions", "- Old rule")
        database.insert_feedback(
            interaction_id=1,
            verdict="useful",
            note="run note",
            metadata={"source": "run_history"},
        )
        database.insert_feedback(
            interaction_id=1,
            verdict="incorrect",
            note="card note",
            correction="fix",
            metadata={"source": "action_dashboard", "action_index": 0},
        )
        self.assertEqual(len(database.list_feedback(limit=10, offset=0)), 2)
        from src.main import app

        with TestClient(app) as client:
            r = client.delete("/memory/learning")
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertTrue(data.get("cleared"))
        self.assertEqual(data.get("feedback_deleted"), 2)
        self.assertEqual((data.get("instructions") or "").strip(), "")
        self.assertEqual(database.get_runtime_learning_instructions(), "")
        self.assertEqual(database.list_feedback(limit=10, offset=0), [])

    def test_post_memory_feedback_persists_run_history_metadata(self):
        from src.main import app

        with patch("src.api.routes.refresh_learning_instructions", return_value={"updated": True, "rules": 1}):
            with TestClient(app) as client:
                r = client.post(
                    "/memory/feedback",
                    json={
                        "interaction_id": 5,
                        "verdict": "useful",
                        "note": "[Run history] run #5: Good",
                        "metadata": {"source": "run_history"},
                    },
                )
        self.assertEqual(r.status_code, 200)
        row = r.json().get("feedback") or {}
        md_raw = row.get("metadata")
        md = json.loads(md_raw) if isinstance(md_raw, str) else (md_raw or {})
        self.assertEqual(md.get("source"), "run_history")

    def test_patch_dashboard_action_category(self):
        database.log_interaction(
            trigger_type="thread_probe",
            input_text="x",
            output_text="{}",
            status="completed",
            metadata={
                "csm_actions": [
                    {
                        "title": "T",
                        "include_on_dashboard": True,
                        "category": "client_non_technical",
                        "gmail_thread_id": "abc12345",
                    }
                ]
            },
        )
        row = database.list_probe_interactions(limit=1, offset=0, source="all", status_filter=None)[0]
        iid = int(row["id"])
        from src.main import app

        with TestClient(app) as client:
            bad = client.patch(
                f"/dashboard/probe-runs/{iid}/actions/0/category",
                json={"category": "nope"},
            )
            self.assertEqual(bad.status_code, 404)
            ok = client.patch(
                f"/dashboard/probe-runs/{iid}/actions/0/category",
                json={"category": "internal"},
            )
        self.assertEqual(ok.status_code, 200)
        fresh = database.get_interaction_by_id(iid)
        md = database.parse_interaction_metadata(fresh.get("metadata"))
        actions = md.get("csm_actions")
        self.assertEqual(actions[0].get("category"), "internal")
