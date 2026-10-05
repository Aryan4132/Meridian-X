"""
browser_agent.py — Autonomous Playwright Web Browser Agent (BK-12)
Provides real web page interaction, form navigation, element clicking, and DOM extraction via Playwright.
"""

import os
import json
import time
import logging
from typing import Dict, Any, Optional, List

logger = logging.getLogger("meridian.browser")

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sync_playwright = None


class AutonomousWebBrowser:
    """Autonomous Playwright web browser interaction engine."""

    def __init__(self, headless: bool = True):
        self.headless = headless
        self.active_url: Optional[str] = None
        self.history: List[str] = []
        self._playwright = None
        self._browser = None
        self._page = None

    def _ensure_browser(self):
        """Initializes Playwright browser session if not running."""
        if not sync_playwright:
            raise RuntimeError("'playwright' library is not installed. Run 'pip install playwright && playwright install chromium'.")

        if not self._playwright:
            self._playwright = sync_playwright().start()

        if not self._browser:
            self._browser = self._playwright.chromium.launch(
                headless=self.headless,
                args=["--no-sandbox", "--disable-setuid-sandbox"]
            )

        if not self._page or self._page.is_closed() is True:
            self._page = self._browser.new_page(viewport={"width": 1280, "height": 800})

    def navigate(self, url: str) -> Dict[str, Any]:
        """Navigates browser to target URL and extracts page title & text summary."""
        if not url.startswith("http://") and not url.startswith("https://"):
            url = f"https://{url}"

        try:
            self._ensure_browser()
            if not self._page:
                return {"status": "failed", "error": "Failed to initialize page context", "timestamp": time.time()}
            self._page.goto(url, wait_until="domcontentloaded", timeout=20000)
            self.active_url = self._page.url
            self.history.append(self.active_url)

            title = self._page.title() or f"Page - {self.active_url}"
            text_content = self._page.evaluate("document.body.innerText") or ""
            text_snippet = text_content[:2000] if text_content else "No readable text content."

            return {
                "status": "success",
                "url": self.active_url,
                "title": title,
                "text_content": text_snippet,
                "timestamp": time.time()
            }
        except Exception as e:
            return {
                "status": "failed",
                "url": url,
                "error": f"Navigation error: {str(e)}",
                "timestamp": time.time()
            }

    def click_element(self, selector: str) -> Dict[str, Any]:
        """Clicks an element by CSS selector, text content, or button text."""
        if not self._page or self._page.is_closed() is True:
            return {"status": "failed", "error": "No active browser page. Call navigate first."}

        # Candidate Playwright selector strategies
        strategies = [
            selector,  # Exact selector passed by agent
            f"text={selector}",
            f"button:has-text('{selector}')",
            f"a:has-text('{selector}')",
            f"[aria-label='{selector}']",
            f"[title='{selector}']",
            f"[placeholder='{selector}']"
        ]

        clicked = False
        last_err = ""
        for strat in strategies:
            try:
                if self._page.is_visible(strat):
                    self._page.click(strat, timeout=2000)
                    clicked = True
                    break
            except Exception as exc:
                last_err = str(exc)

        if clicked:
            time.sleep(0.5)
            new_title = self._page.title()
            return {
                "status": "success",
                "action": "click",
                "selector": selector,
                "url": self._page.url,
                "page_title": new_title
            }
        else:
            return {
                "status": "failed",
                "action": "click",
                "selector": selector,
                "error": f"Could not find or click element matching '{selector}'. Last error: {last_err}"
            }

    def type_text(self, selector: str, text: str) -> Dict[str, Any]:
        """Fills input field identified by selector, placeholder, or name with text."""
        if not self._page or self._page.is_closed() is True:
            return {"status": "failed", "error": "No active browser page. Call navigate first."}

        strategies = [
            selector,
            f"input[name='{selector}']",
            f"input[placeholder*='{selector}']",
            f"textarea[name='{selector}']",
            f"[aria-label='{selector}']",
            f"text={selector}"
        ]

        typed = False
        last_err = ""
        for strat in strategies:
            try:
                if self._page.is_visible(strat):
                    self._page.fill(strat, text, timeout=2000)
                    typed = True
                    break
            except Exception as exc:
                last_err = str(exc)

        if typed:
            return {
                "status": "success",
                "action": "type",
                "selector": selector,
                "text": text,
                "url": self._page.url
            }
        else:
            return {
                "status": "failed",
                "action": "type",
                "selector": selector,
                "error": f"Could not locate input field matching '{selector}'. Last error: {last_err}"
            }

    def close(self):
        """Safely tears down browser session."""
        try:
            if self._page and not self._page.is_closed():
                self._page.close()
            if self._browser:
                self._browser.close()
            if self._playwright:
                self._playwright.stop()
        except Exception:
            pass
        finally:
            self._page = None
            self._browser = None
            self._playwright = None


# Global singleton instance
browser_instance = AutonomousWebBrowser()


def browser_navigate_tool(url: str) -> str:
    """Tool wrapper for browser page navigation routed primarily to browser_use_task."""
    try:
        from src.tools.browser_use_agent import browser_use_task
        task_output = browser_use_task(task=f"Navigate to {url} and extract page summary", start_url=url)
        return json.dumps({"status": "success", "url": url, "result": task_output}, indent=2)
    except Exception as e:
        logger.warning(f"browser_use_task navigation failed for {url}, attempting web_browser fallback: {e}")

    try:
        from src.tools import web_browser
        if web_browser._page_alive():
            nav_res = web_browser.browser_open(url, visible=True)
            return json.dumps({"status": "success", "url": url, "result": nav_res}, indent=2)
    except Exception as e:
        logger.warning(f"web_browser navigation fallback failed for {url}, falling back to AutonomousWebBrowser: {e}")

    res = browser_instance.navigate(url)
    return json.dumps(res, indent=2)


def browser_interact_tool(action: str, selector: str, text: str = "") -> str:
    """Tool wrapper for browser element interaction routed primarily to browser_use_task."""
    try:
        from src.tools.browser_use_agent import browser_use_task
        task = f"Click element '{selector}'" if action == "click" else f"Type '{text}' into '{selector}'"
        task_output = browser_use_task(task=task)
        return json.dumps({"status": "success", "action": action, "selector": selector, "result": task_output}, indent=2)
    except Exception as e:
        logger.warning(f"browser_use_task interaction failed for '{action}' on '{selector}', attempting web_browser fallback: {e}")

    try:
        from src.tools import web_browser
        if web_browser._page_alive():
            if action == "click":
                click_res = web_browser.browser_click_element(selector)
                return json.dumps({"status": "success", "action": "click", "selector": selector, "result": click_res}, indent=2)
            elif action == "type":
                type_res = web_browser.browser_type_element(selector, text, press_enter=True)
                return json.dumps({"status": "success", "action": "type", "selector": selector, "text": text, "result": type_res}, indent=2)
    except Exception as e:
        logger.warning(f"web_browser interaction fallback failed for '{action}' on '{selector}', falling back to AutonomousWebBrowser: {e}")

    if action == "click":
        res = browser_instance.click_element(selector)
    elif action == "type":
        res = browser_instance.type_text(selector, text)
    else:
        res = {"status": "failed", "error": f"Unknown action '{action}'"}
    return json.dumps(res, indent=2)
