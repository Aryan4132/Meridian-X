import pytest
from unittest.mock import patch, MagicMock
from src.tools.desktop import explain_active_screen
from src.tools.developer import workspace_quick_audit
from src.tools.clipboard import smart_clipboard_action
from src.tools.registry import TOOL_REGISTRY
from src.core.loop_stream import generate_tools_doc, TOOL_SIGNATURES


def test_explain_active_screen_with_vision():
    with patch("src.tools.desktop.screenshot") as mock_shot, \
         patch("src.tools.desktop.vision_analyze", return_value="Active application is VS Code with syntax error on line 42.") as mock_vision, \
         patch("src.core.screen_sense.get_active_window_metadata", return_value={"title": "VS Code - main.py", "process": "Code.exe"}):
        res = explain_active_screen()
        assert "**Active Window**: VS Code - main.py" in res
        assert "Active application is VS Code" in res
        mock_shot.assert_called_once()
        mock_vision.assert_called_once()


def test_explain_active_screen_capture_failure():
    with patch("src.tools.desktop.screenshot", side_effect=Exception("No display attached")), \
         patch("src.core.screen_sense.get_active_window_metadata", return_value={"title": "Desktop", "process": "explorer.exe"}):
        res = explain_active_screen()
        assert "Display capture unavailable" in res


def test_explain_active_screen_ocr_fallback():
    with patch("src.tools.desktop.screenshot"), \
         patch("src.tools.desktop.vision_analyze", return_value="Vision analysis failed: model offline"), \
         patch("src.tools.desktop.ocr_screen", return_value="Error: Connection refused on port 8000"), \
         patch("src.core.screen_sense.get_active_window_metadata", return_value={"title": "Terminal", "process": "powershell.exe"}):
        res = explain_active_screen()
        assert "OCR Fallback" in res
        assert "Connection refused" in res


def test_workspace_quick_audit_clean_repo():
    mock_rev_parse = MagicMock(returncode=0, stdout="true\n")
    mock_branch = MagicMock(returncode=0, stdout="main\n")
    mock_status = MagicMock(returncode=0, stdout="")
    mock_diff = MagicMock(returncode=0, stdout="")
    mock_log = MagicMock(returncode=0, stdout="abc1234 feat: initial commit\n")

    def mock_run(cmd, **kwargs):
        if "rev-parse" in cmd:
            return mock_rev_parse
        elif "branch" in cmd:
            return mock_branch
        elif "status" in cmd:
            return mock_status
        elif "diff" in cmd:
            return mock_diff
        elif "log" in cmd:
            return mock_log
        return MagicMock(returncode=0, stdout="")

    with patch("shutil.which", return_value="/usr/bin/git"), \
         patch("subprocess.run", side_effect=mock_run):
        res = workspace_quick_audit()
        assert "Workspace Health Audit" in res
        assert "**Branch**: `main`" in res
        assert "Working Tree Clean" in res


def test_workspace_quick_audit_dirty_repo():
    mock_rev_parse = MagicMock(returncode=0, stdout="true\n")
    mock_branch = MagicMock(returncode=0, stdout="feature/delight\n")
    mock_status = MagicMock(returncode=0, stdout=" M src/app.py\n?? test.py\n")
    mock_diff = MagicMock(returncode=0, stdout="src/app.py | 5 +----\n 1 file changed\n")
    mock_log = MagicMock(returncode=0, stdout="1122334 fix: minor\n")

    def mock_run(cmd, **kwargs):
        if "rev-parse" in cmd:
            return mock_rev_parse
        elif "branch" in cmd:
            return mock_branch
        elif "status" in cmd:
            return mock_status
        elif "diff" in cmd:
            return mock_diff
        elif "log" in cmd:
            return mock_log
        return MagicMock(returncode=0, stdout="")

    with patch("shutil.which", return_value="/usr/bin/git"), \
         patch("subprocess.run", side_effect=mock_run):
        res = workspace_quick_audit()
        assert "feature/delight" in res
        assert "[Unstaged] `src/app.py`" in res
        assert "[Untracked] `test.py`" in res
        assert "Suggested Atomic Action" in res


def test_smart_clipboard_json():
    sample_json = '{"name": "Meridian-X", "status": "active"}'
    with patch("pyperclip.paste", return_value=sample_json), \
         patch("pyperclip.copy") as mock_copy:
        res = smart_clipboard_action()
        assert "Valid JSON" in res
        assert '"name": "Meridian-X"' in res
        mock_copy.assert_called_once()


def test_smart_clipboard_stack_trace():
    trace = """Traceback (most recent call last):
  File "app.py", line 12, in <module>
    import missing_module
ModuleNotFoundError: No module named 'missing_module'"""
    with patch("pyperclip.paste", return_value=trace):
        res = smart_clipboard_action()
        assert "Error Stack Trace Detected" in res
        assert "ModuleNotFoundError" in res


def test_smart_clipboard_empty():
    with patch("pyperclip.paste", return_value="   "):
        res = smart_clipboard_action()
        assert "Clipboard is empty" in res


def test_tool_registry_and_signatures():
    assert "explain_active_screen" in TOOL_REGISTRY
    assert "workspace_quick_audit" in TOOL_REGISTRY
    assert "smart_clipboard_action" in TOOL_REGISTRY

    assert "explain_active_screen" in TOOL_SIGNATURES
    assert "workspace_quick_audit" in TOOL_SIGNATURES
    assert "smart_clipboard_action" in TOOL_SIGNATURES

    doc = generate_tools_doc()
    assert "explain_active_screen" in doc
    assert "workspace_quick_audit" in doc
    assert "smart_clipboard_action" in doc
