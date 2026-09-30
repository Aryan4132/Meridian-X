import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# Ensure meridian_backend is in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.tools.browser_agent import AutonomousWebBrowser, browser_navigate_tool, browser_interact_tool
from src.tools.web_browser import browser_find_and_click, browser_type_in


class TestBrowserAgent(unittest.TestCase):

    def setUp(self):
        self.agent = AutonomousWebBrowser(headless=True)

    @patch("src.tools.browser_agent.sync_playwright")
    def test_navigate_success(self, mock_playwright):
        # Mock Playwright context & page
        mock_p = MagicMock()
        mock_playwright.return_value.start.return_value = mock_p
        mock_browser = MagicMock()
        mock_p.chromium.launch.return_value = mock_browser
        mock_page = MagicMock()
        mock_browser.new_page.return_value = mock_page
        mock_page.url = "https://example.com"
        mock_page.evaluate.return_value = "Sample Page Text Content"
        mock_page.title.return_value = "Sample Page"

        res = self.agent.navigate("https://example.com")
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["url"], "https://example.com")
        self.assertIn("Sample Page Text Content", res["text_content"])

    @patch("src.tools.browser_agent.sync_playwright")
    def test_click_element_css_and_text_selector(self, mock_playwright):
        mock_p = MagicMock()
        mock_playwright.return_value.start.return_value = mock_p
        mock_browser = MagicMock()
        mock_p.chromium.launch.return_value = mock_browser
        mock_page = MagicMock()
        mock_browser.new_page.return_value = mock_page
        mock_page.url = "https://example.com"
        mock_page.is_visible.return_value = True
        mock_page.evaluate.return_value = "Content"

        # First navigate
        self.agent.navigate("https://example.com")

        # Test click by selector
        res_click = self.agent.click_element("button#submit")
        self.assertEqual(res_click["status"], "success")
        self.assertEqual(res_click["selector"], "button#submit")

    @patch("src.tools.browser_agent.sync_playwright")
    def test_type_text(self, mock_playwright):
        mock_p = MagicMock()
        mock_playwright.return_value.start.return_value = mock_p
        mock_browser = MagicMock()
        mock_p.chromium.launch.return_value = mock_browser
        mock_page = MagicMock()
        mock_browser.new_page.return_value = mock_page
        mock_page.url = "https://example.com"
        mock_page.is_visible.return_value = True

        self.agent.navigate("https://example.com")
        res_type = self.agent.type_text("input[name='q']", "meridian ai")
        self.assertEqual(res_type["status"], "success")
        self.assertEqual(res_type["text"], "meridian ai")

    @patch("src.tools.web_browser._locate_element_by_vision", return_value=None)
    @patch("src.tools.web_browser._page")
    def test_web_browser_dom_fallback_click(self, mock_page, mock_vision):
        # When vision returns None, browser_find_and_click should fall back to DOM selector / text matching
        mock_page.click.return_value = None

        res = browser_find_and_click("Login Button")
        self.assertIn("Visually or via DOM clicked", res)


if __name__ == "__main__":
    unittest.main()
