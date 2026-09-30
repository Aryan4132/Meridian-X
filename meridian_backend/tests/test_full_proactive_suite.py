import os
import sys
import time
import unittest
from unittest.mock import patch, MagicMock

# Add backend directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core import proactive
from src.core.presence_briefing import PresenceBriefingEngine
from src.core.predictive_engine import PredictiveContextPrewarmer, get_prewarmed_context
from src.core.commit_whisperer import CommitWhisperer
from src.core.what_broke_detective import WhatBrokeDetective
from src.core.self_evolving_tooling import SelfEvolvingToolingManager
from src.core.tool_regression_sentinel import ToolRegressionSentinel


class TestFullProactiveSuite(unittest.TestCase):

    def setUp(self):
        proactive.game_mode_active = False

    def test_presence_arrival_briefing_engine(self):
        """Verify PresenceBriefingEngine formats 15-second arrival briefing."""
        engine = PresenceBriefingEngine()
        briefing = engine.generate_presence_briefing(
            user_name="Aryan",
            context_data={"weather": "75°F and sunny", "schedule": "3 meetings today", "unread_alerts": 2}
        )
        self.assertIn("Aryan", briefing["text"])
        self.assertIn("75°F and sunny", briefing["text"])
        self.assertTrue(briefing["duration_seconds"] <= 20)

    @patch("src.core.proactive.publish_nudge_sync")
    def test_presence_arrival_nudge_trigger(self, mock_publish):
        """Verify check_presence_arrival triggers proactive arrival briefing when returning after idle."""
        # Simulate user being away for 6 minutes (360 seconds)
        now = time.time()
        proactive._last_activity_time = now - 360
        proactive._last_arrival_briefing = now - 700  # past cooldown

        briefing_sent = proactive.check_presence_arrival(user_name="Aryan")
        self.assertTrue(briefing_sent)
        mock_publish.assert_called()
        call_kwargs = mock_publish.call_args[1]
        self.assertEqual(call_kwargs.get("nudge_type"), "room_arrival_briefing")
        self.assertIn("Aryan", call_kwargs.get("message", ""))

    @patch("src.core.commit_whisperer.CommitWhisperer.inspect_staged_commit")
    @patch("src.core.proactive.publish_nudge_sync")
    def test_proactive_commit_whisperer(self, mock_publish, mock_inspect):
        """Verify check_proactive_commits pushes commit recommendation when changes are staged."""
        mock_inspect.return_value = {
            "has_staged": True,
            "staged_files": ["api.py", "proactive.py"],
            "suggested_message": "feat(core): enhance proactive intelligence pipeline",
            "needs_version_bump": False
        }

        proactive._last_commit_whisper_time = 0  # reset cooldown
        nudged = proactive.check_proactive_commits(workspace_root=os.getcwd())
        self.assertTrue(nudged)
        mock_publish.assert_called()
        call_kwargs = mock_publish.call_args[1]
        self.assertEqual(call_kwargs.get("nudge_type"), "commit_suggestion")
        self.assertIn("proactive", call_kwargs.get("message", "").lower())

    @patch("src.core.what_broke_detective.WhatBrokeDetective.diagnose_failures")
    @patch("src.core.proactive.publish_nudge_sync")
    def test_proactive_what_broke_detective(self, mock_publish, mock_diagnose):
        """Verify trigger_what_broke_auto_fix pushes actionable patch nudge."""
        mock_diagnose.return_value = {
            "breakage_detected": True,
            "error_summary": "ImportError: cannot import name 'xyz'",
            "recommended_patch": {
                "file_path": "src/core/test.py",
                "original": "from x import xyz",
                "proposed": "from x import abc as xyz",
                "error_message": "ImportError: cannot import name 'xyz'"
            }
        }

        nudged = proactive.trigger_what_broke_auto_fix(
            error_text="ImportError: cannot import name 'xyz'",
            workspace_root=os.getcwd()
        )
        self.assertTrue(nudged)
        mock_publish.assert_called()
        call_kwargs = mock_publish.call_args[1]
        self.assertEqual(call_kwargs.get("nudge_type"), "what_broke_patch")
        self.assertIn("patch", call_kwargs)

    def test_predictive_context_prewarmer(self):
        """Verify PredictiveContextPrewarmer pre-warms context and stores in cache."""
        prewarmer = PredictiveContextPrewarmer()
        res = prewarmer.prewarm_context_for_app("Code.exe", "api.py - Meridian-X")
        self.assertTrue(res.get("prewarmed", False))
        self.assertEqual(res.get("target_app"), "Code.exe")

        cached = get_prewarmed_context("Code.exe")
        self.assertIsNotNone(cached)
        self.assertIn("target_app", cached)

    @patch("src.core.proactive.publish_nudge_sync")
    def test_continuous_work_ergonomics_tracker(self, mock_publish):
        """Verify check_continuous_work_ergonomics pushes stretch nudge after 45m active work."""
        now = time.time()
        # Set work start to 50 minutes ago
        proactive._continuous_work_start_time = now - (50 * 60)
        proactive._last_ergonomics_nudge_time = 0

        nudged = proactive.check_continuous_work_ergonomics()
        self.assertTrue(nudged)
        mock_publish.assert_called()
        call_kwargs = mock_publish.call_args[1]
        self.assertEqual(call_kwargs.get("nudge_type"), "pomodoro_stretch_nudge")

    @patch("src.core.proactive.publish_nudge_sync")
    def test_self_evolving_tool_synthesizer_sequence(self, mock_publish):
        """Verify SelfEvolvingToolingManager detects recurring sequences and proposes synthesis."""
        manager = SelfEvolvingToolingManager(tools_dir=os.path.join(os.getcwd(), "temp_tools"))
        
        # Simulate running a 2-step sequence 3 times
        seq = ["read_file", "search_codebase"]
        for _ in range(3):
            manager.record_tool_call(seq[0], {"path": "test.txt"})
            manager.record_tool_call(seq[1], {"query": "def run"})

        proposal = manager.detect_sequence_opportunity(min_occurrences=3)
        self.assertIsNotNone(proposal)
        self.assertEqual(proposal["sequence"], tuple(seq))

    def test_tool_regression_sentinel_validation(self):
        """Verify ToolRegressionSentinel executes scenarios and validates heuristic matching."""
        sentinel = ToolRegressionSentinel()
        report = sentinel.check_regressions()
        self.assertIn("total_scenarios", report)
        self.assertIn("passed", report)
        self.assertTrue(report["passed"] > 0)
        self.assertEqual(report["failed"], 0)


if __name__ == "__main__":
    unittest.main()
