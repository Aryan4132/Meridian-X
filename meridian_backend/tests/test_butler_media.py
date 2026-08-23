import os
import sys
import unittest
from unittest.mock import patch, MagicMock

# Add backend directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database import save_user_preference, get_user_preference
from src.tools.chrome_manager import find_chrome_executable, get_chrome_user_data_dir, get_chrome_profile_status
from src.tools.media_player import control_media_playback, verify_media_playing, play_youtube_music

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

    def test_media_control_playback(self):
        """Verify media playback hotkey control dispatch."""
        with patch("src.tools.media_player.gui_hotkey", return_value="Pressed hotkey playpause"):
            res = control_media_playback("playpause")
            self.assertIn("Executed system media key action 'playpause'", res)

        invalid_res = control_media_playback("invalid_action_xyz")
        self.assertIn("Invalid action", invalid_res)

    @patch("src.tools.media_player.gui_hotkey", return_value="Pressed hotkey")
    @patch("src.tools.media_player.launch_chrome_with_profile", return_value="Opened Chrome persistent context")
    @patch("src.tools.media_player.verify_media_playing")
    def test_play_youtube_music_workflow(self, mock_verify, mock_launch, mock_hotkey):
        """Verify YT Music search URL generation, visual verification retries, and account persistence."""
        mock_verify.return_value = {"playing": True, "verified": True, "matched_keywords": ["kalyani"]}

        with patch("playwright.sync_api.sync_playwright") as mock_pw:
            res = play_youtube_music(song_query="kalyani", account_email="aryanshukla4132@gmail.com")
            self.assertIn("Successfully playing 'kalyani'", res)
            self.assertIn("CONFIRMED", res)

        # Check preference saved
        email = get_user_preference("media_account_email")
        self.assertEqual(email, "aryanshukla4132@gmail.com")


if __name__ == "__main__":
    unittest.main()
