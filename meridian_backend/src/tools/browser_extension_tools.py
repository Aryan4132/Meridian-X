"""
Meridian-X Browser Extension Agent Tools
Empowers the AI to read, inspect, navigate, and click inside the user's live,
logged-in daily Google Chrome browser without profile locks or session recreation.
"""

import asyncio
import concurrent.futures
from typing import Any, Optional
from src.core.browser_extension_hub import extension_manager


def _run_rpc(action: str, params: Optional[dict[str, Any]] = None, timeout: float = 12.0) -> dict[str, Any]:
    """
    Thread-safe bridge to dispatch an async RPC to the Chrome extension.

    When called from inside FastAPI's async event loop (the normal case), we cannot
    call asyncio.run() — that raises RuntimeError: 'This event loop is already running'.
    The correct pattern is to spin a NEW event loop on a background thread and await
    the coroutine there, which keeps it completely isolated from the running loop.
    """
    def _in_thread() -> dict[str, Any]:
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(extension_manager.send_rpc(action, params or {}, timeout))
        finally:
            loop.close()

    try:
        # Check if we're currently inside a running event loop (FastAPI context)
        asyncio.get_running_loop()
        # Yes — offload to a dedicated thread with its own fresh event loop
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            future = pool.submit(_in_thread)
            return future.result(timeout=timeout + 2)
    except RuntimeError:
        # No running loop — safe to call asyncio.run() directly
        return asyncio.run(extension_manager.send_rpc(action, params or {}, timeout))


def is_chrome_extension_available() -> bool:
    """Returns True if the user's Chrome browser has the Meridian extension connected."""
    return extension_manager.is_connected


def chrome_get_active_tab() -> str:
    """
    Retrieves the title and URL of the active tab in the user's personal Chrome browser.
    Useful for contextual awareness of what the user is currently looking at.
    """
    if not extension_manager.is_connected:
        return "Chrome Extension is not connected. (Load the extension from meridian_extension/ in chrome://extensions to use your logged-in browser)."

    try:
        res = _run_rpc("get_tab_info", timeout=6.0)
        if not res.get("success"):
            return f"Failed to retrieve active tab: {res.get('error')}"
        data = res.get("data", {})
        return f"Active Chrome Tab:\n- Title: {data.get('title')}\n- URL: {data.get('url')}"
    except Exception as e:
        return f"Error querying Chrome extension: {e}"


def chrome_read_page(max_length: int = 6000) -> str:
    """
    Extracts the visible textual content and metadata from the user's currently active Chrome tab.
    Works seamlessly on personal Google Docs, Gmail, GitHub, Jira, and authenticated portals.
    """
    if not extension_manager.is_connected:
        return "Chrome Extension is not connected. Please enable it in chrome://extensions."

    try:
        res = _run_rpc("extract_text", {"maxLength": max_length}, timeout=10.0)
        if not res.get("success"):
            return f"Failed to extract page text: {res.get('error')}"
        data = res.get("data", {})
        return (
            f"Page Title: {data.get('title')}\n"
            f"URL: {data.get('url')}\n"
            f"Description: {data.get('metaDescription')}\n\n"
            f"Content Snippet:\n{data.get('text')}"
        )
    except Exception as e:
        return f"Error extracting page text via extension: {e}"


def chrome_click_element(selector: Optional[str] = None, text: Optional[str] = None) -> str:
    """
    Clicks an interactive element, link, or button in the user's active Chrome tab.
    Specify either a CSS selector (e.g. '#submit-btn') or visible button text (e.g. 'Sign in').
    """
    if not extension_manager.is_connected:
        return "Chrome Extension is not connected. Enable extension to automate personal browser."

    try:
        params: dict[str, Any] = {}
        if selector:
            params["selector"] = selector
        if text:
            params["text"] = text
        res = _run_rpc("click", params, timeout=8.0)
        if not res.get("success"):
            return f"Click failed: {res.get('error')}"
        return str(res.get("message", "Clicked successfully."))
    except Exception as e:
        return f"Error executing click via Chrome extension: {e}"


def chrome_fill_input(selector: str, value: str, submit: bool = False) -> str:
    """
    Fills a text input field, textarea, or search box in the active Chrome tab.
    Dispatches reactive events so modern frameworks (React, Vue, Angular) register the change.
    """
    if not extension_manager.is_connected:
        return "Chrome Extension is not connected. Enable extension in chrome://extensions."

    try:
        res = _run_rpc("fill", {"selector": selector, "value": value, "submit": submit}, timeout=8.0)
        if not res.get("success"):
            return f"Fill input failed: {res.get('error')}"
        return str(res.get("message", "Field populated successfully."))
    except Exception as e:
        return f"Error filling input via Chrome extension: {e}"


def chrome_scroll(direction: str = "down", amount: int = 500) -> str:
    """
    Smoothly scrolls the active Chrome tab up or down.
    direction: 'down' or 'up'
    amount: pixels to scroll
    """
    if not extension_manager.is_connected:
        return "Chrome Extension is not connected."

    try:
        res = _run_rpc("scroll", {"direction": direction, "amount": amount}, timeout=6.0)
        return str(res.get("message", "Scrolled."))
    except Exception as e:
        return f"Error scrolling via Chrome extension: {e}"


def chrome_open_tab(url: str = "about:blank") -> str:
    """
    Opens a new browser tab in the user's personal Chrome session at the specified URL.
    Falls back to opening in the default system Chrome browser if extension is temporarily disconnected.
    """
    if not extension_manager.is_connected:
        try:
            import webbrowser
            webbrowser.open(url)
            return f"Opened {url} in your personal Chrome browser (default profile)."
        except Exception as e:
            return f"Chrome Extension is not connected and system browser fallback failed: {e}"

    try:
        res = _run_rpc("open_tab", {"url": url}, timeout=6.0)
        if not res.get("success"):
            try:
                import webbrowser
                webbrowser.open(url)
                return f"Opened {url} in your personal Chrome browser (fallback)."
            except Exception:
                return f"Open tab failed: {res.get('error')}"
        return str(res.get("message", f"Opened new tab at {url}"))
    except Exception as e:
        try:
            import webbrowser
            webbrowser.open(url)
            return f"Opened {url} in your personal Chrome browser (fallback)."
        except Exception:
            return f"Error opening tab via Chrome extension: {e}"


def chrome_navigate(url: str) -> str:
    """
    Navigates the user's currently active Chrome tab to a new URL.
    """
    if not extension_manager.is_connected:
        return "Chrome Extension is not connected."

    try:
        res = _run_rpc("navigate", {"url": url}, timeout=6.0)
        if not res.get("success"):
            return f"Navigate failed: {res.get('error')}"
        return str(res.get("message", f"Navigated to {url}"))
    except Exception as e:
        return f"Error navigating via Chrome extension: {e}"


def chrome_get_interactive_elements() -> str:
    """
    Lists all visible interactive elements (buttons, links, inputs) on the active Chrome tab.
    Returns a numbered set-of-marks style element list for targeted clicking or filling.
    """
    if not extension_manager.is_connected:
        return "Chrome Extension is not connected."

    try:
        res = _run_rpc("get_interactive_elements", timeout=8.0)
        if not res.get("success"):
            return f"Failed to extract interactive elements: {res.get('error')}"
        elements = res.get("data", [])
        if not elements:
            return "No visible interactive elements found on the current page."
        lines = [f"[{el['id']}] <{el['tag']}> {el['text']!r} selector={el['selector']}" for el in elements]
        return "Interactive Elements:\n" + "\n".join(lines)
    except Exception as e:
        return f"Error fetching interactive elements: {e}"


def chrome_edit_element(selector: str, html: Optional[str] = None, text: Optional[str] = None) -> str:
    """
    Directly edits an element's text or HTML inside the active Chrome tab.
    Works for text inputs, rich text editors (contenteditable), headings, and DOM bodies.
    """
    if not extension_manager.is_connected:
        return "Chrome Extension is not connected."

    try:
        params: dict[str, Any] = {"selector": selector}
        if html is not None:
            params["html"] = html
        if text is not None:
            params["text"] = text
        res = _run_rpc("edit_element", params, timeout=8.0)
        if not res.get("success"):
            return f"Edit element failed: {res.get('error')}"
        return str(res.get("message", f"Element updated: {selector}"))
    except Exception as e:
        return f"Error editing element via Chrome extension: {e}"


def chrome_compose_gmail(to: str, subject: str = "", body: str = "") -> str:
    """
    Opens Gmail in the user's logged-in Chrome browser with recipient, subject,
    and message body pre-filled ready to review and send.
    """
    import urllib.parse
    params = {"fs": "1", "tf": "cm", "to": to}
    if subject:
        params["su"] = subject
    if body:
        params["body"] = body
    query = urllib.parse.urlencode(params)
    gmail_url = f"https://mail.google.com/mail/u/0/?{query}"
    return chrome_open_tab(url=gmail_url)

