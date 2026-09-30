import os
import sys
import unittest
from unittest.mock import patch, MagicMock

# Add meridian_backend directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.telegram_bridge import _is_rate_limited, _send_telegram_message
from src.core.discord_bridge import _is_rate_limited_discord, send_discord_msg
from src.core.ar_bridge import list_ar_headsets

class TestBridges(unittest.TestCase):
    def test_telegram_rate_limiter(self):
        chat_id = 99999
        # First 5 calls within the window should not be limited
        for i in range(5):
            self.assertFalse(_is_rate_limited(chat_id))
        # 6th call should be rate limited
        self.assertTrue(_is_rate_limited(chat_id))

    def test_telegram_message_chunker(self):
        mock_client = MagicMock()
        text = "Hello World\n\n" * 500  # Creates a long text (> 4096 chars)
        _send_telegram_message(mock_client, "fake_token", 12345, text)
        # Verify client.post was called multiple times due to chunking
        self.assertGreater(mock_client.post.call_count, 1)

    def test_discord_rate_limiter(self):
        user_id = 88888
        # First 5 calls within the window should not be limited
        for i in range(5):
            self.assertFalse(_is_rate_limited_discord(user_id))
        # 6th call should be rate limited
        self.assertTrue(_is_rate_limited_discord(user_id))

    def test_discord_msg_empty(self):
        res = send_discord_msg("", "")
        self.assertIn("Error: Empty message provided", res)

    def test_discord_msg_fallback_inactive(self):
        with patch.dict(os.environ, {"USERNAME": "testuser"}, clear=True):
            res = send_discord_msg("general", "Test message")
            self.assertIn("Error: Discord bot bridge is inactive", res)

    def test_discord_msg_user_id(self):
        with patch.dict(os.environ, {"USERNAME": "testuser"}, clear=True):
            res = send_discord_msg("971779848844509214", "Test message")
            self.assertIn("Error: Discord bot bridge is inactive", res)

    def test_discord_msg_webhook(self):
        mock_resp = MagicMock()
        mock_resp.status_code = 204
        with patch.dict(os.environ, {"DISCORD_WEBHOOK_URL": "https://discord.com/api/webhooks/test"}):
            with patch("httpx.Client.post", return_value=mock_resp):
                res = send_discord_msg("general", "Test webhook message")
                self.assertIn("dispatched via Webhook", res)

    def test_ar_bridge(self):
        headsets = list_ar_headsets()
        self.assertIsInstance(headsets, list)

    def test_communication_discord_tool(self):
        from src.tools.communication import send_discord_message
        with patch.dict(os.environ, {"USERNAME": "testuser"}, clear=True):
            res = send_discord_message(target="general", message="Hello from tool test")
            self.assertIn("Error: Discord bot bridge is inactive", res)

    def test_read_discord_messages_tool(self):
        from src.tools.communication import read_discord_messages
        res = read_discord_messages()
        self.assertTrue(isinstance(res, str))

    def test_add_discord_reaction_tool(self):
        from src.tools.communication import add_discord_reaction
        with patch.dict(os.environ, {"USERNAME": "testuser"}, clear=True):
            res = add_discord_reaction(message_id="123456789", emoji="👍")
            self.assertIn("inactive", res)

    def test_list_discord_channels_tool(self):
        from src.tools.communication import list_discord_channels
        res = list_discord_channels()
        self.assertIn("inactive", res)

if __name__ == "__main__":
    unittest.main()


