"""Tests for feedback → learning distillation, learning API, and dashboard category PATCH."""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

from src.agent.memory import (
    LEARNING_REINFORCEMENT_SYSTEM,
    MAX_LEARNING_FEEDBACK_FOR_DISTILL,
    build_learning_feedback_json_record,
    partition_learning_feedback_records,
    refresh_learning_instructions,
)


def _compact_llm_response(constraints_body: str, exemplars_body: str = "(none)") -> str:
    c = (constraints_body or "").strip()
    e = (exemplars_body if exemplars_body is not None else "(none)").strip()
    return f"===CONSTRAINTS===\n{c}\n\n===EXEMPLARS===\n{e}\n"


def _mock_llm(response_text: str, captured: dict | None = None):
    class _R:
        def __init__(self, content):
            self.content = content

    class _LLM:
        def __init__(self):
            self.calls = 0

        def invoke(self, messages):
            self.calls += 1
            if captured is not None:
                captured["messages"] = messages
            return _R(response_text)

    return _LLM()


from src.agent.prompts import render_email_agent_system
from src.db import database


class TestMemoryLearning(unittest.TestCase):
    def test_learning_system_prompts_have_no_stencil_vendor_examples(self):
        """Regression: concrete examples in the system prompt were copied by the model as fake rules."""
        lowered = LEARNING_REINFORCEMENT_SYSTEM.lower()
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
        out = refresh_learning_instructions()
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

        out_text = _compact_llm_response(
            "- Keep replies under three bullets.\n- Prefer numbered steps for runbooks."
        )
        llm = _mock_llm(out_text)
        with patch("src.agent.memory.get_chat_llm", return_value=llm):
            out = refresh_learning_instructions()
        self.assertTrue(out.get("updated"))
        self.assertEqual(out.get("llm_stages"), 1)
        self.assertEqual(llm.calls, 1)
        text = database.get_runtime_learning_instructions()
        self.assertIn("three bullets", text.lower())

    def test_refresh_learning_prompt_includes_action_dashboard_metadata(self):
        database.log_interaction(
            trigger_type="thread_probe",
            input_text="probe",
            output_text='{"skipped_note": "IGNORE_THIS_IN_DISTILL", "actions": []}',
            status="completed",
            metadata={
                "csm_actions": [
                    {
                        "title": "Quota internal",
                        "brief": "AIRIS quota exceeded",
                        "category": "internal",
                        "include_on_dashboard": True,
                        "email_subject": "Alert",
                    }
                ]
            },
        )
        row = database.get_interactions(limit=1, offset=0)[0]
        iid = int(row["id"])
        database.insert_feedback(
            interaction_id=iid,
            verdict="incorrect",
            note="Do not surface internal quota alerts as client actions.",
            correction="",
            metadata={"source": "action_dashboard", "action_index": 0},
        )

        captured: dict = {}
        out_text = _compact_llm_response("- Skip internal quota alert cards.\n")
        with patch("src.agent.memory.get_chat_llm", return_value=_mock_llm(out_text, captured)):
            refresh_learning_instructions()
        msgs = captured.get("messages") or []
        self.assertGreaterEqual(len(msgs), 2)
        human = str(getattr(msgs[1], "content", "") or "")
        self.assertIn("LEARNING_FEEDBACK_PARTITIONED_JSON", human)
        self.assertIn('"negative"', human)
        self.assertIn('"endorsed"', human)
        self.assertIn("action_dashboard", human)
        self.assertIn('"action_index": 0', human)
        self.assertIn("scoped_action_card", human)
        self.assertIn("reinforcement", human)
        self.assertIn("Quota internal", human)
        self.assertNotIn("IGNORE_THIS_IN_DISTILL", human)

    def test_action_dashboard_distill_anchors_note_not_probe_skipped_note(self):
        database.log_interaction(
            trigger_type="thread_probe",
            input_text="probe",
            output_text='{"skipped_note": "Skipped 4 threads as noise or meeting-only invites.", "actions": []}',
            status="completed",
            metadata={
                "csm_actions": [
                    {
                        "title": "AIRIS Quota Exceeded",
                        "brief": "Standard Foods exceeded quota",
                        "category": "client_technical",
                        "include_on_dashboard": True,
                        "gmail_thread_id": "tid123",
                    }
                ]
            },
        )
        row = database.get_interactions(limit=1, offset=0)[0]
        iid = int(row["id"])
        database.insert_feedback(
            interaction_id=iid,
            verdict="incorrect",
            note="not needed",
            correction="",
            metadata={"source": "action_dashboard", "action_index": 0},
        )
        captured: dict = {}
        out_text = _compact_llm_response(
            "- When operator marks AIRIS quota-style cards as not needed, omit similar dashboard rows.\n"
        )
        with patch("src.agent.memory.get_chat_llm", return_value=_mock_llm(out_text, captured)):
            refresh_learning_instructions()
        human = str(getattr((captured.get("messages") or [])[1], "content", "") or "")
        self.assertIn("not needed", human)
        self.assertIn("scoped_action_card", human)
        self.assertIn("AIRIS Quota", human)
        self.assertNotIn("Skipped 4 threads", human)
        self.assertNotIn("meeting-only invites", human.lower())

    def test_get_agent_learning_instructions_snapshot_round_trip(self):
        database.set_app_setting(database.KEY_AGENT_LEARNING_CONSTRAINTS, "- Rule A\n- Rule B")
        database.set_app_setting(database.KEY_AGENT_LEARNING_EXEMPLARS, "### Endorsed run (verdict=useful)\nx")
        snap = database.get_agent_learning_instructions_snapshot()
        self.assertIn("Rule A", snap["instructions"])
        self.assertIn("Rule A", snap.get("constraints", ""))
        self.assertIn("Endorsed run", snap.get("exemplars", ""))
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

    def test_refresh_prompt_includes_run_context_for_run_history_negative(self):
        database.log_interaction(
            trigger_type="thread_probe",
            input_text="Run an inbox probe static preamble SHOULD_NOT_APPEAR_IN_DISTILL",
            output_text='SUBJECT_LINE_UNIQUE_X9F2 {"cards": [{"title": "PROBE_JSON_SNIPPET_K3"}]}',
            status="completed",
            metadata=None,
        )
        row = database.get_interactions(limit=1, offset=0)[0]
        iid = int(row["id"])
        database.insert_feedback(
            interaction_id=iid,
            verdict="incorrect",
            note="Operator dislikes this triage",
            correction="Prefer tier_price surfaced in brief",
            metadata={"source": "run_history"},
        )
        captured: dict = {}
        out_text = _compact_llm_response(
            "- When output mentions SUBJECT_LINE_UNIQUE_X9F2, align brief with operator correction.\n"
        )
        with patch("src.agent.memory.get_chat_llm", return_value=_mock_llm(out_text, captured)):
            refresh_learning_instructions()
        msgs = captured.get("messages") or []
        human = str(getattr(msgs[1], "content", "") or "")
        self.assertIn("LEARNING_FEEDBACK_PARTITIONED_JSON", human)
        self.assertIn("model_output_excerpt", human)
        self.assertIn("reinforcement", human)
        self.assertIn("SUBJECT_LINE_UNIQUE_X9F2", human)
        self.assertIn("PROBE_JSON_SNIPPET_K3", human)
        self.assertNotIn("SHOULD_NOT_APPEAR_IN_DISTILL", human)

    def test_negative_row_distillation_payload_has_structured_operator_and_context(self):
        database.log_interaction(
            trigger_type="thread_probe",
            input_text="PROBE_IN",
            output_text="BAD_OUTPUT_SNIP_FOR_LEARN",
            status="completed",
            metadata=None,
        )
        row = database.get_interactions(limit=1, offset=0)[0]
        iid = int(row["id"])
        rec = build_learning_feedback_json_record(
            {
                "id": 1,
                "interaction_id": iid,
                "verdict": "incorrect",
                "note": "[Run history] run #9: Incorrect",
                "correction": "Always surface quota in brief",
                "metadata": json.dumps({"source": "run_history"}),
            },
            {iid: dict(row)},
        )
        dp = rec.get("distillation_payload") or {}
        self.assertEqual(dp.get("reinforcement"), "negative")
        self.assertEqual((dp.get("operator") or {}).get("correction"), "Always surface quota in brief")
        ctx = dp.get("context") or {}
        self.assertIn("BAD_OUTPUT_SNIP", str(ctx.get("model_output_excerpt", "")))

    def test_refresh_persists_partition_json_and_caps_at_five_rows(self):
        for i in range(6):
            database.insert_feedback(
                interaction_id=None,
                verdict="incorrect",
                note=f"row{i}",
                correction=None,
                metadata=None,
            )
        out_text = _compact_llm_response("- x\n", "(none)\n")
        with patch("src.agent.memory.get_chat_llm", return_value=_mock_llm(out_text)):
            out = refresh_learning_instructions()
        self.assertEqual(out.get("feedback_rows_used"), 5)
        self.assertEqual(out.get("max_feedback_cap"), MAX_LEARNING_FEEDBACK_FOR_DISTILL)
        raw = database.get_app_setting(database.KEY_AGENT_LEARNING_LAST_PARTITION, "") or ""
        data = json.loads(raw)
        total = len(data.get("negative", [])) + len(data.get("endorsed", []))
        self.assertEqual(total, 5)

    def test_refresh_includes_buried_action_dashboard_in_distill_pool(self):
        """Card feedback with low id must still reach the LLM when newer run-history rows push it out of top 5."""
        database.log_interaction(
            trigger_type="thread_probe",
            input_text="p",
            output_text="{}",
            status="completed",
            metadata={
                "csm_actions": [
                    {
                        "title": "BuriedCardTitle",
                        "brief": "brief body",
                        "category": "internal",
                        "include_on_dashboard": True,
                    }
                ]
            },
        )
        row = database.get_interactions(limit=1, offset=0)[0]
        iid = int(row["id"])
        database.insert_feedback(
            interaction_id=iid,
            verdict="incorrect",
            note="UNIQUE_BURIED_DASHBOARD_NOTE_X7",
            correction=None,
            metadata={"source": "action_dashboard", "action_index": 0},
        )
        for _ in range(6):
            database.insert_feedback(
                interaction_id=None,
                verdict="incorrect",
                note="run history noise",
                correction=None,
                metadata={"source": "run_history"},
            )
        captured: dict = {}
        out_text = _compact_llm_response("- c\n", "(none)\n")
        with patch("src.agent.memory.get_chat_llm", return_value=_mock_llm(out_text, captured)):
            refresh_learning_instructions()
        human = str(getattr((captured.get("messages") or [])[1], "content", "") or "")
        self.assertIn("UNIQUE_BURIED_DASHBOARD_NOTE_X7", human)
        self.assertIn("BuriedCardTitle", human)

    def test_refresh_normalizes_star_bullets_in_constraints(self):
        """LLM output with * bullets must not be stripped to an empty constraints column."""
        database.insert_feedback(
            interaction_id=None,
            verdict="incorrect",
            note="n",
            correction=None,
            metadata=None,
        )
        out_text = _compact_llm_response("* Asterisk bullet line for constraints.\n")
        with patch("src.agent.memory.get_chat_llm", return_value=_mock_llm(out_text)):
            refresh_learning_instructions()
        c = database.get_app_setting(database.KEY_AGENT_LEARNING_CONSTRAINTS, "") or ""
        self.assertTrue(c.strip().startswith("- "))
        self.assertIn("Asterisk bullet", c)

    def test_compaction_record_run_history_includes_output_excerpt_not_full_probe_input(self):
        database.log_interaction(
            trigger_type="thread_probe",
            input_text="LONG_PROBE_PREAMBLE_X",
            output_text="OUT_UNIQUE_T9",
            status="completed",
            metadata=None,
        )
        row = database.get_interactions(limit=1, offset=0)[0]
        iid = int(row["id"])
        rec = build_learning_feedback_json_record(
            {
                "id": 1,
                "interaction_id": iid,
                "verdict": "incorrect",
                "note": "n",
                "correction": None,
                "metadata": json.dumps({"source": "run_history"}),
            },
            {iid: dict(row)},
        )
        self.assertEqual(rec.get("reinforcement"), "negative")
        self.assertIn("OUT_UNIQUE_T9", rec.get("model_output_excerpt", ""))
        self.assertNotIn("LONG_PROBE_PREAMBLE_X", json.dumps(rec))

    def test_partition_same_interaction_id_splits_negative_and_endorsed_buckets(self):
        """Same run can have two rows; refresh payload must list them in disjoint negative vs endorsed arrays."""
        database.log_interaction(
            trigger_type="thread_probe",
            input_text="probe",
            output_text="OUT_BOTH_ROWS_222",
            status="completed",
            metadata=None,
        )
        row = database.get_interactions(limit=1, offset=0)[0]
        iid = int(row["id"])
        database.insert_feedback(
            interaction_id=iid,
            verdict="incorrect",
            note="fix triage for run",
            correction="show tier_price",
            metadata={"source": "run_history"},
        )
        database.insert_feedback(
            interaction_id=iid,
            verdict="useful",
            note="[Run history] run good",
            correction=None,
            metadata={"source": "run_history"},
        )
        captured: dict = {}
        out_text = _compact_llm_response("- c\n", "(none)\n")
        with patch("src.agent.memory.get_chat_llm", return_value=_mock_llm(out_text, captured)):
            refresh_learning_instructions()
        human = str(getattr((captured.get("messages") or [])[1], "content", "") or "")
        payload = human.split("LEARNING_FEEDBACK_PARTITIONED_JSON:\n", 1)[1]
        data = json.loads(payload)
        self.assertEqual(data.get("schema_version"), 1)
        neg = data.get("negative") or []
        end = data.get("endorsed") or []
        self.assertEqual(len(neg), 1)
        self.assertEqual(len(end), 1)
        self.assertEqual(neg[0].get("interaction_id"), iid)
        self.assertEqual(end[0].get("interaction_id"), iid)
        self.assertEqual(neg[0].get("reinforcement"), "negative")
        self.assertEqual(end[0].get("reinforcement"), "endorsed")
        self.assertIn("tier_price", (neg[0].get("constraints_grounding") or "").lower())
        self.assertIsNotNone(end[0].get("exemplars_grounding"))

    def test_action_dashboard_incorrect_includes_constraints_grounding_for_llm(self):
        """Dashboard textarea feedback is incorrect + note; must carry card context for CONSTRAINTS."""
        database.log_interaction(
            trigger_type="thread_probe",
            input_text="p",
            output_text="{}",
            status="completed",
            metadata={
                "csm_actions": [
                    {
                        "title": "CardTitleX",
                        "brief": "Brief body for card",
                        "category": "internal",
                        "include_on_dashboard": True,
                    }
                ]
            },
        )
        row = database.get_interactions(limit=1, offset=0)[0]
        iid = int(row["id"])
        rec = build_learning_feedback_json_record(
            {
                "id": 1,
                "interaction_id": iid,
                "verdict": "incorrect",
                "note": "not needed — demote similar cards",
                "correction": None,
                "metadata": json.dumps({"source": "action_dashboard", "action_index": 0}),
            },
            {iid: dict(row)},
        )
        self.assertEqual(rec.get("reinforcement"), "negative")
        cg = rec.get("constraints_grounding") or ""
        self.assertIn("CardTitleX", cg)
        self.assertIn("demote", cg.lower())
        self.assertIsNone(rec.get("exemplars_grounding"))

    def test_partition_learning_feedback_records_splits_by_reinforcement(self):
        part = partition_learning_feedback_records(
            [
                {"reinforcement": "negative", "verdict": "incorrect"},
                {"reinforcement": "endorsed", "verdict": "useful"},
            ]
        )
        self.assertEqual(len(part["negative"]), 1)
        self.assertEqual(len(part["endorsed"]), 1)

    def test_refresh_positive_only_single_llm_invocation(self):
        database.log_interaction(
            trigger_type="thread_probe",
            input_text="long shared probe preamble",
            output_text="ENDORSED_PROBE_OUTPUT_SNIPPET_Q7",
            status="completed",
            metadata=None,
        )
        row = database.get_interactions(limit=1, offset=0)[0]
        iid = int(row["id"])
        database.insert_feedback(
            interaction_id=iid,
            verdict="useful",
            note="[Run history] good",
            correction=None,
            metadata={"source": "run_history"},
        )
        out_text = _compact_llm_response(
            "",
            "Operator endorsed this run; keep probe output style like ENDORSED_PROBE_OUTPUT_SNIPPET_Q7.",
        )
        llm = _mock_llm(out_text)
        with patch("src.agent.memory.get_chat_llm", return_value=llm):
            out = refresh_learning_instructions()
        self.assertEqual(llm.calls, 1)
        self.assertGreaterEqual(out.get("exemplar_sections", 0), 1)
        text = database.get_runtime_learning_instructions()
        self.assertIn("ENDORSED_PROBE_OUTPUT_SNIPPET_Q7", text)
        self.assertNotIn("long shared probe preamble", text)

    def test_refresh_negative_distill_dedupes_identical_bullets(self):
        database.insert_feedback(
            interaction_id=None,
            verdict="incorrect",
            note="x",
            correction="y",
            metadata=None,
        )

        out_text = _compact_llm_response("- Same bullet line.\n- Same bullet line.\n- Same bullet line.\n")
        with patch("src.agent.memory.get_chat_llm", return_value=_mock_llm(out_text)):
            refresh_learning_instructions()
        c = database.get_app_setting(database.KEY_AGENT_LEARNING_CONSTRAINTS, "") or ""
        self.assertEqual(c.strip().count("\n"), 0)
        self.assertIn("Same bullet", c)

    def test_exemplars_exclude_action_dashboard_useful(self):
        """Action dashboard card feedback (incorrect+note) must not route probe output into EXEMPLARS."""
        database.log_interaction(
            trigger_type="thread_probe",
            input_text="probe",
            output_text="_ONLY_FOR_EXEMPLAR_IF_INCLUDED_",
            status="completed",
            metadata=None,
        )
        row = database.get_interactions(limit=1, offset=0)[0]
        iid = int(row["id"])
        database.insert_feedback(
            interaction_id=iid,
            verdict="incorrect",
            note="not needed",
            correction=None,
            metadata={"source": "action_dashboard", "action_index": 0},
        )

        out_text = _compact_llm_response("- Do not surface internal-only quota cards as client_technical.\n")
        with patch("src.agent.memory.get_chat_llm", return_value=_mock_llm(out_text)):
            refresh_learning_instructions()
        ex = database.get_app_setting(database.KEY_AGENT_LEARNING_EXEMPLARS, "") or ""
        self.assertNotIn("_ONLY_FOR_EXEMPLAR_IF_INCLUDED_", ex)
        c = database.get_app_setting(database.KEY_AGENT_LEARNING_CONSTRAINTS, "") or ""
        self.assertIn("quota", c.lower())


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

    def test_post_memory_feedback_dashboard_stores_action_scope_metadata(self):
        """Scoped card feedback stores incorrect verdict + action_dashboard scope (matching dashboard UI)."""
        from src.main import app

        with patch("src.api.routes.refresh_learning_instructions", return_value={"updated": True, "rules": 0}):
            with TestClient(app) as client:
                r = client.post(
                    "/memory/feedback",
                    json={
                        "interaction_id": 99,
                        "verdict": "incorrect",
                        "note": "not needed",
                        "action_index": 2,
                    },
                )
        self.assertEqual(r.status_code, 200)
        row = r.json().get("feedback") or {}
        self.assertEqual(row.get("verdict"), "incorrect")
        md_raw = row.get("metadata")
        md = json.loads(md_raw) if isinstance(md_raw, str) else (md_raw or {})
        self.assertEqual(md.get("source"), "action_dashboard")
        self.assertEqual(md.get("action_index"), 2)
        self.assertNotIn("learning_canonical", md)

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
