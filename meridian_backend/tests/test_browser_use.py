import os
import sys
import unittest
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.tools.web_browser import (
    browser_press_key,
    browser_scroll,
    browser_wait,
    browser_get_interactive_elements,
    browser_click_element,
    browser_type_element,
)


class TestBrowserUseCore(unittest.TestCase):

    @patch("src.tools.web_browser._page_alive", return_value=True)
    @patch("src.tools.web_browser._page")
    def test_browser_press_key(self, mock_page, mock_alive):
        res = browser_press_key("Enter")
        mock_page.keyboard.press.assert_called_with("Enter")
        self.assertIn("Pressed key 'Enter'", res)

    @patch("src.tools.web_browser._page_alive", return_value=True)
    @patch("src.tools.web_browser._page")
    def test_browser_scroll_down(self, mock_page, mock_alive):
        res = browser_scroll("down", 400)
        mock_page.evaluate.assert_called_with("window.scrollBy(0, 400);")
        self.assertIn("Scrolled down by 400px", res)

    @patch("src.tools.web_browser._page_alive", return_value=True)
    @patch("src.tools.web_browser._page")
    def test_browser_wait(self, mock_page, mock_alive):
        res = browser_wait(0.1)
        mock_page.wait_for_timeout.assert_called_with(100.0)
        self.assertIn("Waited 0.1s", res)

    @patch("src.tools.web_browser._page_alive", return_value=True)
    @patch("src.tools.web_browser._page")
    def test_browser_get_interactive_elements(self, mock_page, mock_alive):
        mock_page.evaluate.return_value = [
            {"index": 1, "tag": "button", "text": "Submit", "selector": "#btn-1", "type": "submit"},
            {"index": 2, "tag": "input", "text": "", "selector": "input[name='q']", "placeholder": "Search"},
        ]
        elements = browser_get_interactive_elements()
        self.assertEqual(len(elements), 2)
        self.assertEqual(elements[0]["index"], 1)
        self.assertEqual(elements[0]["tag"], "button")

    @patch("src.tools.web_browser._page_alive", return_value=True)
    @patch("src.tools.web_browser._page")
    def test_browser_click_element_by_index(self, mock_page, mock_alive):
        with patch("src.tools.web_browser.browser_get_interactive_elements") as mock_get_elements:
            mock_get_elements.return_value = [
                {"index": 1, "tag": "button", "text": "Submit", "selector": "#btn-1"},
            ]
            mock_page.is_visible.return_value = True
            res = browser_click_element("1")
            mock_page.click.assert_called_with("#btn-1", timeout=3000)
            self.assertIn("Clicked element [1]", res)

    @patch("src.tools.web_browser._page_alive", return_value=True)
    @patch("src.tools.web_browser._page")
    def test_browser_type_element_by_index_with_enter(self, mock_page, mock_alive):
        with patch("src.tools.web_browser.browser_get_interactive_elements") as mock_get_elements:
            mock_get_elements.return_value = [
                {"index": 2, "tag": "input", "text": "", "selector": "input[name='q']"},
            ]
            mock_page.is_visible.return_value = True
            res = browser_type_element("2", "meridian ai", press_enter=True)
            mock_page.fill.assert_called_with("input[name='q']", "meridian ai", timeout=3000)
            mock_page.keyboard.press.assert_called_with("Enter")
            self.assertIn("Typed into element [2]", res)


    @patch("src.tools.browser_use_agent.browser_wait")
    @patch("src.tools.browser_use_agent.browser_highlight_elements")
    @patch("src.tools.browser_use_agent.browser_open", return_value="Opened")
    @patch("src.tools.browser_use_agent.browser_get_interactive_elements")
    @patch("src.tools.browser_use_agent.browser_get_text", return_value="AI research papers list")
    @patch("src.tools.browser_use_agent._get_page_url", return_value="https://www.google.com/search?q=ai")
    @patch("src.tools.browser_use_agent._get_page_title", return_value="Google Search")
    def test_browser_use_task_heuristic(self, mock_title, mock_url, mock_text, mock_elements, mock_open, mock_highlight, mock_wait):
        from src.tools.browser_use_agent import BrowserUseAgent, browser_use_task
        mock_elements.return_value = [
            {"index": 1, "tag": "input", "text": "", "selector": "textarea[name='q']"},
            {"index": 2, "tag": "button", "text": "Search", "selector": "input[type='submit']"},
        ]
        with patch("src.tools.browser_use_agent.browser_type_element", return_value="Typed"):
            agent = BrowserUseAgent(max_steps=2)
            res = agent.run("search for ai papers on google", visible=False)
            self.assertEqual(res["status"], "success")
            self.assertGreater(res["steps_taken"], 0)
            self.assertIn("steps_log", res)


if __name__ == "__main__":
    unittest.main()

