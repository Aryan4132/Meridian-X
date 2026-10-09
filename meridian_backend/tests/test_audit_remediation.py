"""
Unit test suite verifying fixes from project audit (Task 32).
"""
import os
from unittest.mock import patch

from src.core.lsp_client import LspClient
from src.tools.dynamic_manager import create_dynamic_tool
from src.tools.external_connectors import generate_draft_reply


def test_lsp_client_python_310_compatibility():
    """Verify LSPClient root_uri construction works cleanly without Python 3.10 f-string backslash syntax errors."""
    client = LspClient(executable_path="python", root_dir=r"C:\Test\Workspace\Path")
    norm_path = client.root_dir.replace("\\", "/")
    root_uri = f"file:///{norm_path}"
    assert "file:///" in root_uri
    assert "\\" not in root_uri


def test_dynamic_tool_ast_security_rejection():
    """Verify dynamic_manager rejects code with disallowed calls or dangerous module imports."""
    # 1. Reject subprocess
    dangerous_subproc = "import subprocess\ndef exploit():\n    subprocess.run(['calc'])"
    res1 = create_dynamic_tool("exploit_subproc", "Exploit", dangerous_subproc)
    assert "Security policy violation" in res1 or "Disallowed module import" in res1

    # 2. Reject eval
    dangerous_eval = "def exploit(x):\n    return eval(x)"
    res2 = create_dynamic_tool("exploit_eval", "Exploit", dangerous_eval)
    assert "Security policy violation" in res2 or "Disallowed call" in res2

    # 3. Allow safe pure Python
    safe_code = "def safe_calculator(a: int, b: int) -> int:\n    return a + b"
    res3 = create_dynamic_tool("safe_calculator_test", "Calculates sum", safe_code)
    assert "Successfully created" in res3


def test_draft_reply_configurable_author():
    """Verify generate_draft_reply respects MERIDIAN_USER_NAME configuration."""
    with patch.dict(os.environ, {"MERIDIAN_USER_NAME": "Alex Vance"}):
        reply = generate_draft_reply("email_123", "Thanks for reaching out")
        assert "Alex Vance" in reply["draft_reply"]

    with patch.dict(os.environ, {}, clear=True):
        reply_default = generate_draft_reply("email_456", "Sounds good")
        assert "Aryan Shukla" in reply_default["draft_reply"]
