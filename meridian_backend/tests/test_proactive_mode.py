import os
import sys
import json
import unittest
from unittest.mock import patch, MagicMock

# Add backend directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.mode import (
    classify_mode,
    MODE_DIRECTIVES,
    get_proactive_mode,
    set_proactive_mode,
    build_system_prompt
)
from src.core.loop_parser import process_final_response


class TestProactiveModeAndSuggestions(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        # Reset proactive mode to False before each test
        set_proactive_mode(False)

    def tearDown(self):
        set_proactive_mode(False)

    def test_proactive_mode_directive_registered(self):
        """Verify PROACTIVE mode exists in MODE_DIRECTIVES with autonomous instructions."""
        self.assertIn("PROACTIVE", MODE_DIRECTIVES)
        directive = MODE_DIRECTIVES["PROACTIVE"]
        self.assertIn("proactive", directive.lower())
        self.assertIn("proactive_suggestions", directive)

    def test_classify_mode_proactive_triggers(self):
        """Verify keyword heuristics classify prompts into PROACTIVE mode."""
        triggers = [
            "Be proactive and audit our project files",
            "What should I do next with this repository?",
            "Suggest next steps for optimizing our backend",
            "Anticipate potential bottlenecks in our build pipeline",
            "Butler mode: take initiative and inspect server health",
            "Recommend improvements for our tests",
            "What's next after finishing the deployment?"
        ]
        for prompt in triggers:
            mode = classify_mode(prompt)
            self.assertEqual(mode, "PROACTIVE", f"Failed to classify '{prompt}' as PROACTIVE")

    def test_proactive_mode_toggle_and_elevation(self):
        """Verify setting proactive mode globally elevates AUTO prompts to PROACTIVE."""
        neutral_prompt = "Hello, can you help me?"
        self.assertEqual(classify_mode(neutral_prompt), "AUTO")

        # Enable proactive mode
        set_proactive_mode(True)
        self.assertTrue(get_proactive_mode())
        self.assertEqual(classify_mode(neutral_prompt), "PROACTIVE")

        # Explicit other modes (like ENGINEER) should still be respected
        engineer_prompt = "Write a python function to calculate fibonacci"
        self.assertEqual(classify_mode(engineer_prompt), "ENGINEER")

        # Disable proactive mode
        set_proactive_mode(False)
        self.assertFalse(get_proactive_mode())
        self.assertEqual(classify_mode(neutral_prompt), "AUTO")

    def test_build_system_prompt_contains_proactive_schema(self):
        """Verify build_system_prompt injects proactive suggestion schema and directives."""
        prompt = "Suggest what to do next for our test coverage"
        sys_prompt = build_system_prompt(prompt, "llama-test", "http://localhost:11434", "dummy_tools_doc")
        
        self.assertIn("COGNITIVE MODE DIRECTIVE: PROACTIVE", sys_prompt)
        self.assertIn("proactive_suggestions", sys_prompt)

    async def test_process_final_response_preserves_proactive_suggestions(self):
        """Verify process_final_response parses and preserves proactive_suggestions block."""
        sample_response = json.dumps({
            "chat": "All tests passed successfully.",
            "speech": "All tests passed successfully.",
            "lang": "en",
            "proactive_suggestions": [
                {
                    "title": "Run Integration Suite",
                    "action": "pytest meridian_backend/tests/test_browser_use.py",
                    "type": "command"
                },
                {
                    "title": "Clean Temp Artifacts",
                    "action": "Clean up temporary test artifacts",
                    "type": "suggestion"
                }
            ]
        })

        mock_client = MagicMock()
        processed = await process_final_response(sample_response, "en", mock_client)
        data = json.loads(processed)

        self.assertIn("proactive_suggestions", data)
        self.assertEqual(len(data["proactive_suggestions"]), 2)
        self.assertEqual(data["proactive_suggestions"][0]["title"], "Run Integration Suite")
        self.assertEqual(data["proactive_suggestions"][0]["type"], "command")


if __name__ == "__main__":
    unittest.main()
