import pytest
from src.core.error_diagnostics import (
    diagnose_error_root_cause,
    format_explainable_error_markdown
)


def test_diagnose_file_not_found():
    raw = "FileNotFoundError: [Errno 2] No such file or directory: 'src/missing.py'"
    diag = diagnose_error_root_cause(raw)
    assert diag["type"] == "FILE_NOT_FOUND"
    assert "Target File or Directory Not Found" in diag["main_issue"]
    assert "search_files" in diag["suggested_fix"]


def test_diagnose_model_unavailable():
    raw = "model 'qwen2.5:latest' not found, try pulling it first"
    diag = diagnose_error_root_cause(raw)
    assert diag["type"] == "MODEL_UNAVAILABLE"
    assert "AI Model Not Available Locally" in diag["main_issue"]
    assert "Ollama" in diag["suggested_fix"]


def test_diagnose_connection_refused():
    raw = "ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it"
    diag = diagnose_error_root_cause(raw)
    assert diag["type"] == "CONNECTION_REFUSED"
    assert "Connection Refused" in diag["main_issue"]


def test_diagnose_permission_denied():
    raw = "PermissionError: [WinError 32] The process cannot access the file because it is being used by another process: 'data.db'"
    diag = diagnose_error_root_cause(raw)
    assert diag["type"] == "PERMISSION_DENIED"
    assert "Permission Denied" in diag["main_issue"]


def test_diagnose_syntax_error():
    raw = "SyntaxError: invalid syntax (main.py, line 42)"
    diag = diagnose_error_root_cause(raw)
    assert diag["type"] == "SYNTAX_ERROR"
    assert "Code Syntax" in diag["main_issue"]


def test_diagnose_timeout():
    raw = "asyncio.TimeoutError: Execution timed out after 60.0s"
    diag = diagnose_error_root_cause(raw)
    assert diag["type"] == "TIMEOUT"
    assert "Timed Out" in diag["main_issue"]


def test_diagnose_command_failed():
    raw = "Command exited with code 127: 'pytest: command not found'"
    diag = diagnose_error_root_cause(raw)
    assert diag["type"] == "COMMAND_FAILED"
    assert "Command Execution Failed" in diag["main_issue"]


def test_diagnose_empty_and_general():
    empty_diag = diagnose_error_root_cause("   ")
    assert empty_diag["type"] == "UNKNOWN"

    general_diag = diagnose_error_root_cause("Something completely bizarre happened in custom library")
    assert general_diag["type"] == "GENERAL_ERROR"
    assert "Something completely bizarre" in general_diag["main_issue"]


def test_format_explainable_error_markdown():
    raw = "FileNotFoundError: [Errno 2] No such file or directory: 'app.config'"
    md = format_explainable_error_markdown(raw, tool_name="read_file")

    assert "> [!WARNING]" in md
    assert "Main Issue: Target File or Directory Not Found" in md
    assert "**Tool**: `read_file`" in md
    assert "**What Happened / Why**:" in md
    assert "**Suggested Fix**:" in md
    assert "<details>" in md
    assert "No such file or directory" in md

