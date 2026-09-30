import os
import sys
import time
import unittest
from unittest.mock import patch, MagicMock

# Add backend directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.watcher import scan_workspace_file_content, analyze_terminal_output
from src.core.silent_workflow_guardian import SilentWorkflowGuardian
from src.core.mobile_bridge import broadcast_proactive_event_to_mobile, connected_clients
from src.core.memory_consolidation import check_milestone_memory_consolidation
from src.core.proactive_system_guard import ProactiveSystemGuard


class TestAdvancedProactiveSuite(unittest.TestCase):

    @patch("src.core.proactive.publish_nudge_sync")
    def test_workspace_file_scanner_stray_debug_alert(self, mock_publish):
        """Verify scan_workspace_file_content fires proactive ghost alert for stray debug prints."""
        python_code = """def calculate_total():\n    print("DEBUG: entering function")\n    return 42\n"""
        alerts = scan_workspace_file_content("test_service.py", python_code)
        
        self.assertTrue(len(alerts) > 0)
        self.assertEqual(alerts[0]["type"], "stray_debug_log")
        mock_publish.assert_called()
        call_kwargs = mock_publish.call_args[1]
        self.assertEqual(call_kwargs.get("nudge_type"), "ghost_code_anomaly")
        self.assertEqual(call_kwargs.get("mascot_state"), "diagnostic")

    @patch("src.core.proactive.publish_nudge_sync")
    def test_workspace_file_scanner_syntax_error_alert(self, mock_publish):
        """Verify scan_workspace_file_content catches syntax errors on file edit."""
        broken_python = "def bad_syntax(:\n    pass"
        alerts = scan_workspace_file_content("syntax_error.py", broken_python)
        
        self.assertTrue(len(alerts) > 0)
        self.assertEqual(alerts[0]["type"], "syntax_error")
        mock_publish.assert_called()

    @patch("src.core.proactive.publish_nudge_sync")
    def test_ghost_assistant_route_mismatch_alert(self, mock_publish):
        """Verify SilentWorkflowGuardian flags route mismatches proactively."""
        content = "export const fetchUser = () => fetch('/api/user/v2');"
        guardian = SilentWorkflowGuardian(os.getcwd())
        alerts = guardian.inspect_recent_changes("src/api/user.ts", content)

        self.assertTrue(len(alerts) > 0)
        self.assertEqual(alerts[0]["type"], "route_mismatch")

    def test_mobile_companion_proactive_away_broadcast(self):
        """Verify broadcast_proactive_event_to_mobile dispatches to active mobile sockets."""
        mock_ws = MagicMock()
        mock_ws.send_text = MagicMock()

        connected_clients.add(mock_ws)
        try:
            sent_count = broadcast_proactive_event_to_mobile({
                "type": "long_task_completed",
                "title": "Build Finished",
                "message": "Desktop build completed while you were away.",
                "actions": ["review_build", "dismiss"]
            })
            self.assertEqual(sent_count, 1)
            mock_ws.send_text.assert_called()
        finally:
            connected_clients.discard(mock_ws)

    @patch("database.consolidate_memory_sleep_cycle")
    def test_milestone_autonomous_memory_consolidation(self, mock_consolidate):
        """Verify milestone memory consolidation triggers when turn threshold is reached."""
        # Under threshold (e.g. 2 turns) -> False
        triggered_early = check_milestone_memory_consolidation(current_turn=2, threshold=5)
        self.assertFalse(triggered_early)
        mock_consolidate.assert_not_called()

        # At/over threshold (e.g. 5 turns) -> True
        triggered = check_milestone_memory_consolidation(current_turn=5, threshold=5)
        self.assertTrue(triggered)
        mock_consolidate.assert_called_once()

    def test_resource_auto_healer_diagnostics(self):
        """Verify ProactiveSystemGuard auto_heal_anomalies detects hogs and proposes remedies."""
        guard = ProactiveSystemGuard(memory_threshold_mb=100.0)
        remedy = guard.auto_heal_anomalies(kill_rogue_processes=False)
        self.assertIn("status", remedy)
        self.assertIn("memory_hogs_detected", remedy)
        self.assertIn("remediation_actions", remedy)

    def test_system_guard_immunity_shield(self):
        """Verify ProactiveSystemGuard refuses to kill protected processes or self."""
        from src.core.proactive_system_guard import is_process_immune
        guard = ProactiveSystemGuard()
        self.assertTrue(is_process_immune(os.getpid()))
        self.assertTrue(is_process_immune(4, "System"))
        self.assertTrue(is_process_immune(12345, "explorer.exe"))
        self.assertTrue(is_process_immune(12346, "dwm.exe"))
        self.assertFalse(is_process_immune(99999, "random_rogue_miner.exe"))

        # Attempting to kill self or immune process must fail safely
        res = guard.kill_process(os.getpid())
        self.assertFalse(res["success"])
        self.assertIn("protected by System Immunity Shield", res["message"])


if __name__ == "__main__":
    unittest.main()

