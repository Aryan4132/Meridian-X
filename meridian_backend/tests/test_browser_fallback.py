import os
import sys
import unittest
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.tools.web_browser import _launch_engine, browser_open
from src.tools.shell import nl_run
from src.core.llm_provider import call_llm_sync


class TestBrowserFallback(unittest.TestCase):

    def test_launch_engine_fallback_to_chrome_on_missing_executable(self):
        mock_pw = MagicMock()
        # Simulate chromium.launch raising Executable doesn't exist on first call, then succeeding on channel="chrome"
        first_call = True

        def mock_launch(*args, **kwargs):
            nonlocal first_call
            if kwargs.get("channel") == "chrome":
                return MagicMock(name="ChromeBrowser")
            if first_call:
                first_call = False
                raise Exception("Executable doesn't exist at C:\\path\\to\\.local-browsers\\chromium-1223\\chrome.exe. Run playwright install.")
            return MagicMock(name="DefaultChromium")

        mock_pw.chromium.launch.side_effect = mock_launch
        browser = _launch_engine(mock_pw, "chromium", headless=True)
        self.assertIsNotNone(browser)
        # Verify it called launch with channel='chrome'
        mock_pw.chromium.launch.assert_called_with(headless=True, slow_mo=0, channel="chrome")

    def test_launch_engine_fallback_to_edge_when_chrome_fails(self):
        mock_pw = MagicMock()

        def mock_launch(*args, **kwargs):
            if kwargs.get("channel") == "chrome":
                raise Exception("Google Chrome channel not found")
            if kwargs.get("channel") == "msedge":
                return MagicMock(name="EdgeBrowser")
            raise Exception("Executable doesn't exist at C:\\path\\to\\.local-browsers\\chromium-1223\\chrome.exe.")

        mock_pw.chromium.launch.side_effect = mock_launch
        browser = _launch_engine(mock_pw, "chromium", headless=True)
        self.assertIsNotNone(browser)
        mock_pw.chromium.launch.assert_called_with(headless=True, slow_mo=0, channel="msedge")

    @patch("playwright.sync_api.sync_playwright")
    def test_browser_open_persistent_context_fallback(self, mock_sync_pw):
        mock_pw_inst = MagicMock()
        mock_sync_pw.return_value.start.return_value = mock_pw_inst

        def mock_persist(*args, **kwargs):
            if kwargs.get("channel") == "chrome":
                ctx = MagicMock()
                ctx.new_page.return_value = MagicMock()
                return ctx
            raise Exception("Executable doesn't exist at internal path")

        mock_pw_inst.chromium.launch_persistent_context.side_effect = mock_persist

        res = browser_open("https://example.com", visible=True, profile=True)
        self.assertIn("Successfully opened", res)


class TestToolTolerance(unittest.TestCase):

    @patch("src.tools.shell.subprocess.run")
    def test_nl_run_accepts_command_kwarg(self, mock_subproc):
        mock_subproc.return_value = MagicMock(returncode=0, stdout="Playwright installed", stderr="")
        res = nl_run(command="playwright install chromium")
        self.assertIn("Playwright installed", res)

    @patch("src.tools.shell.subprocess.run")
    def test_nl_run_accepts_cmd_kwarg(self, mock_subproc):
        mock_subproc.return_value = MagicMock(returncode=0, stdout="pip installed", stderr="")
        res = nl_run(cmd="pip --version")
        self.assertIn("pip installed", res)


if __name__ == "__main__":
    unittest.main()
