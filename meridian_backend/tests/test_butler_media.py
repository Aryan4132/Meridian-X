import os
import sys
import unittest
from unittest.mock import patch, MagicMock

# Add backend directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database import save_user_preference, get_user_preference
from src.tools.chrome_manager import find_chrome_executable, get_chrome_user_data_dir, get_chrome_profile_status
from src.tools.system import control_media_playback
from src.tools.registry import registry

class TestButlerMediaAutomation(unittest.TestCase):

    def test_user_preference_save_and_get(self):
        """Verify user preference persistence in profile memory."""
        res_save = save_user_preference("test_media_email", "aryanshukla4132@gmail.com")
        self.assertIn("Successfully saved preference", res_save)

        email = get_user_preference("test_media_email")
        self.assertEqual(email, "aryanshukla4132@gmail.com")

        fallback = get_user_preference("non_existent_key_999", default="default_value")
        self.assertEqual(fallback, "default_value")

    def test_chrome_executable_and_profile_status(self):
        """Verify Chrome path resolution and profile status dict structure."""
        status = get_chrome_profile_status()
        self.assertIn("chrome_installed", status)
        self.assertIn("chrome_path", status)
        self.assertIn("user_data_dir", status)
        self.assertIn("media_account_email", status)

        user_dir = get_chrome_user_data_dir()
        self.assertTrue(len(user_dir) > 0)

    def test_system_media_playback_control(self):
        """Verify OS system media playback hotkey control dispatch via system.py."""
        with patch("pyautogui.press") as mock_press:
            res = control_media_playback("play")
            self.assertIn("PLAY", res)
            mock_press.assert_called_with("playpause")

        invalid_res = control_media_playback("invalid_action_xyz")
        self.assertIn("Unknown media action", invalid_res)

    def test_music_player_tool_removed_from_registry(self):
        """Verify that play_youtube_music and verify_media_playing are removed from registry."""
        tool_names = {t["name"] for t in registry.list_tools()}
        self.assertNotIn("play_youtube_music", tool_names)
        self.assertNotIn("verify_media_playing", tool_names)
        self.assertIsNone(registry.get_tool("play_youtube_music"))
        self.assertIsNone(registry.get_tool("verify_media_playing"))


if __name__ == "__main__":
    unittest.main()
