import pytest
from src.tools.web_browser import browser_capture_b64, get_latest_browser_frame

def test_browser_capture_b64_when_closed():
    # When browser is not open, should safely return None without throwing exceptions
    frame = browser_capture_b64()
    assert frame is None or isinstance(frame, str)

def test_get_latest_browser_frame_and_mock(monkeypatch):
    import src.tools.web_browser as wb
    monkeypatch.setattr(wb, "_latest_frame_b64", "data:image/jpeg;base64,mockframe123")
    frame = get_latest_browser_frame()
    assert frame == "data:image/jpeg;base64,mockframe123"

def test_browser_use_agent_records_frame(monkeypatch):
    from src.tools.browser_use_agent import BrowserUseAgent
    import src.tools.browser_use_agent as bua
    import src.tools.web_browser as wb

    monkeypatch.setattr(wb, "_page_alive", lambda: True)
    monkeypatch.setattr(bua, "browser_open", lambda *a, **k: "Opened")
    monkeypatch.setattr(bua, "browser_wait", lambda *a, **k: None)
    monkeypatch.setattr(bua, "browser_highlight_elements", lambda *a, **k: None)
    monkeypatch.setattr(bua, "browser_get_interactive_elements", lambda: [])
    monkeypatch.setattr(bua, "browser_get_text", lambda: "Page body text")
    monkeypatch.setattr(bua, "browser_capture_b64", lambda: "data:image/jpeg;base64,mockscreenshot")
    monkeypatch.setattr(BrowserUseAgent, "_plan_with_llm", lambda *a, **k: {"action": "finish", "result": "Done"})

    agent = BrowserUseAgent(max_steps=1)
    res = agent.run("Search for AI", start_url="https://google.com", visible=False)
    assert res["status"] in ("success", "finished", "completed")
    assert len(res["history"]) >= 1
    assert "frame" in res["history"][0]
