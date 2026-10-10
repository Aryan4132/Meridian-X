import json
import unittest
from unittest.mock import MagicMock
from src.core.loop_parser import process_final_response
from src.core.mode import build_system_prompt, SYSTEM_PROMPT_TEMPLATE


class TestResponseResilience(unittest.IsolatedAsyncioTestCase):

    def test_system_prompt_anti_hallucination_directives(self):
        """Verify SYSTEM_PROMPT_TEMPLATE explicitly enforces physical file creation tools."""
        sys_prompt = build_system_prompt("create a chrome extension project", "test_brain", "http://localhost:11434", "")
        self.assertIn("write_file", sys_prompt)
        self.assertIn("cannot create physical folders", sys_prompt.lower())
        self.assertIn("anti-hallucination", sys_prompt.lower())

    async def test_process_final_response_repairs_unescaped_action_quotes(self):
        """Verify unescaped inner quotes in proactive action do not crash parser or leak raw syntax."""
        raw_malformed = (
            '{"title": "Install Backend Dependencies", '
            '"action": "shell("pip install -r C:\\Users\\aryan\\requirements.txt")", '
            '"type": "command"}]}'
        )
        client = MagicMock()
        result_str = await process_final_response(raw_malformed, "en", client)
        
        # Must be valid parseable JSON
        parsed = json.loads(result_str)
        self.assertIsInstance(parsed, dict)
        self.assertIn("chat", parsed)
        self.assertFalse(parsed["chat"].startswith('{"title":'))
        self.assertIn("proactive_suggestions", parsed)
        self.assertEqual(len(parsed["proactive_suggestions"]), 1)
        self.assertEqual(parsed["proactive_suggestions"][0]["title"], "Install Backend Dependencies")

    async def test_process_final_response_sanitizes_raw_json_leak(self):
        """Verify raw suggestion JSON with no chat key produces clean chat rather than raw JSON leak."""
        raw_suggestions_only = (
            '{"proactive_suggestions": ['
            '{"title": "Run Dev Server", "action": "npm run dev", "type": "command"}'
            ']}'
        )
        client = MagicMock()
        result_str = await process_final_response(raw_suggestions_only, "en", client)
        
        parsed = json.loads(result_str)
        self.assertIsInstance(parsed, dict)
        self.assertIn("chat", parsed)
        self.assertNotIn('{"proactive_suggestions"', parsed["chat"])
        self.assertTrue(len(parsed["chat"]) > 0)

    async def test_process_final_response_normalizes_clean_payload(self):
        """Verify clean payload passes through preserved with speech and chat."""
        clean_payload = json.dumps({
            "chat": "Project files created successfully.",
            "speech": "Project files created successfully.",
            "lang": "en",
            "proactive_suggestions": [
                {"title": "Build Project", "action": "npm run build", "type": "command"}
            ]
        })
        client = MagicMock()
        result_str = await process_final_response(clean_payload, "en", client)
        parsed = json.loads(result_str)
        self.assertEqual(parsed["chat"], "Project files created successfully.")
        self.assertEqual(len(parsed["proactive_suggestions"]), 1)


if __name__ == "__main__":
    unittest.main()
