from unittest.mock import AsyncMock
"""
Sprint 47 Unit Tests: Native Chrome Extension Bridge & Agent Tools
Synchronous mock unit testing without hanging event loop calls.
"""

import asyncio
from unittest.mock import MagicMock, AsyncMock, patch
from src.api.browser_extension import extension_manager, ExtensionConnectionManager
from src.tools.browser_extension_tools import (
    chrome_get_active_tab,
    chrome_read_page,
    chrome_click_element,
    chrome_fill_input,
    chrome_scroll,
    chrome_open_tab,
    chrome_edit_element,
    chrome_navigate,
    chrome_get_interactive_elements,
    is_chrome_extension_available
)

def test_extension_manager_status_when_disconnected():
    mgr = ExtensionConnectionManager()
    assert not mgr.is_connected
    assert len(mgr.active_sockets) == 0

def test_extension_manager_connect_disconnect_sync():
    mgr = ExtensionConnectionManager()
    mock_ws = AsyncMock()
    asyncio.run(mgr.connect(mock_ws))
    assert mgr.is_connected
    assert len(mgr.active_sockets) == 1

    mgr.disconnect(mock_ws)
    assert not mgr.is_connected
    assert len(mgr.active_sockets) == 0

def test_extension_send_rpc_when_disconnected():
    mgr = ExtensionConnectionManager()
    res = asyncio.run(mgr.send_rpc("extract_text"))
    assert res["success"] is False
    assert "not currently connected" in res["error"]

def test_extension_send_rpc_success():
    mgr = ExtensionConnectionManager()
    mock_ws = AsyncMock()
    asyncio.run(mgr.connect(mock_ws))

    async def run_test():
        task = asyncio.create_task(mgr.send_rpc("get_tab_info", timeout=2.0))
        await asyncio.sleep(0.01)
        req_id = list(mgr._pending_requests.keys())[0]
        mgr.handle_incoming_rpc_response(req_id, {
            "success": True,
            "data": {"title": "Google Inbox", "url": "https://mail.google.com"}
        })
        return await task

    res = asyncio.run(run_test())
    assert res["success"] is True
    assert res["data"]["title"] == "Google Inbox"

def test_chrome_get_active_tab_disconnected():
    extension_manager.active_sockets.clear()
    out = chrome_get_active_tab()
    assert "Chrome Extension is not connected" in out
    assert "chrome://extensions" in out

def test_chrome_read_page_disconnected():
    extension_manager.active_sockets.clear()
    out = chrome_read_page()
    assert "Chrome Extension is not connected" in out

def test_chrome_click_disconnected():
    extension_manager.active_sockets.clear()
    out = chrome_click_element(text="Log In")
    assert "Chrome Extension is not connected" in out

def test_chrome_fill_input_disconnected():
    extension_manager.active_sockets.clear()
    out = chrome_fill_input("#search", "Meridian-X", submit=True)
    assert "Chrome Extension is not connected" in out

def test_chrome_scroll_disconnected():
    extension_manager.active_sockets.clear()
    out = chrome_scroll(direction="down", amount=300)
    assert "Chrome Extension is not connected" in out

@patch("src.tools.browser_extension_tools.extension_manager")
def test_chrome_tools_connected_mock(mock_mgr):
    mock_mgr.is_connected = True

    async def mock_rpc(action, params=None, timeout=None):
        if action == "get_tab_info":
            return {"success": True, "data": {"title": "GitHub Dashboard", "url": "https://github.com"}}
        elif action == "extract_text":
            return {"success": True, "data": {"title": "GitHub", "url": "https://github.com", "text": "Welcome to your repos."}}
        elif action == "click":
            return {"success": True, "message": "Clicked button."}
        elif action == "fill":
            return {"success": True, "message": "Field populated."}
        elif action == "scroll":
            return {"success": True, "message": "Scrolled."}
        elif action == "open_tab":
            return {"success": True, "message": f"Opened tab at {params.get('url')}"}
        elif action == "navigate":
            return {"success": True, "message": f"Navigated to {params.get('url')}"}
        elif action == "edit_element":
            return {"success": True, "message": f"Element updated: {params.get('selector')}"}
        elif action == "get_interactive_elements":
            return {"success": True, "data": [{"id": 1, "tag": "button", "text": "Submit", "selector": "#btn"}]}
        return {"success": False}

    mock_mgr.send_rpc = mock_rpc

    tab_info = chrome_get_active_tab()
    assert "GitHub Dashboard" in tab_info
    assert "https://github.com" in tab_info

    content = chrome_read_page()
    assert "Welcome to your repos" in content

    click_res = chrome_click_element(text="Pull Requests")
    assert "Clicked button" in click_res

    fill_res = chrome_fill_input("#q", "python")
    assert "Field populated" in fill_res

    scroll_res = chrome_scroll("down", 400)
    assert "Scrolled" in scroll_res

    open_res = chrome_open_tab("https://github.com/new")
    assert "Opened tab" in open_res

    nav_res = chrome_navigate("https://github.com/explore")
    assert "Navigated to" in nav_res

    edit_res = chrome_edit_element("#title", text="Updated Title")
    assert "Element updated" in edit_res

    elem_res = chrome_get_interactive_elements()
    assert "[1] <button> 'Submit'" in elem_res
