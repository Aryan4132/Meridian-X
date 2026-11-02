"""
error_diagnostics.py — Root Cause Error Diagnostic Engine
Converts raw exceptions, tool failures, and stack traces into human-readable,
actionable diagnostics identifying the main issue, root cause, and suggested fix.
"""

import re
from typing import Dict, Any, Optional

ERROR_PATTERNS = [
    {
        "type": "FILE_NOT_FOUND",
        "regex": r"(?:FileNotFoundError|No such file or directory|cannot find the file specified|File not found:)",
        "main_issue": "Target File or Directory Not Found",
        "why": "The specified file path does not exist in the active workspace.",
        "suggested_fix": "Verify the filepath, check if the file was moved or renamed, or run `search_files` to locate it."
    },
    {
        "type": "MODEL_UNAVAILABLE",
        "regex": r"(?:model '.*' not found|try pulling it first|connection refused.*11434|Ollama is offline|Model not found)",
        "main_issue": "AI Model Not Available Locally",
        "why": "The selected model has not been downloaded in Ollama, or the local Ollama service is stopped.",
        "suggested_fix": "Start the Ollama application or pull the model in Settings -> AI Models tab."
    },
    {
        "type": "CONNECTION_REFUSED",
        "regex": r"(?:ConnectionRefusedError|WinError 10061|Failed to establish a new connection|actively refused it)",
        "main_issue": "Local Service Connection Refused",
        "why": "The target port or server daemon (e.g. FastAPI on 4132 or Ollama on 11434) is not running.",
        "suggested_fix": "Verify that the background service or dev server is started and listening on the expected port."
    },
    {
        "type": "PERMISSION_DENIED",
        "regex": r"(?:PermissionError|Access is denied|WinError 32|WinError 5|EACCES|being used by another process)",
        "main_issue": "Permission Denied / File Locked",
        "why": "The operating system denied access, or the file is locked by another running process.",
        "suggested_fix": "Close any editors or terminals currently holding the file, or run the app with appropriate user privileges."
    },
    {
        "type": "SYNTAX_ERROR",
        "regex": r"(?:SyntaxError|IndentationError|JSONDecodeError|TypeError|AttributeError)",
        "main_issue": "Code Syntax or Data Parsing Error",
        "why": "The program or response encountered invalid formatting, unclosed brackets, or unexpected types.",
        "suggested_fix": "Inspect the line number referenced in the details or use `lint_file` / `format_file` to fix syntax."
    },
    {
        "type": "TIMEOUT",
        "regex": r"(?:TimeoutError|asyncio\.TimeoutError|timed out|Execution timed out)",
        "main_issue": "Execution Timed Out",
        "why": "The tool or operation took longer than the safety timeout limit (60s).",
        "suggested_fix": "Break the task into smaller sub-steps, or check network connection if downloading assets."
    },
    {
        "type": "COMMAND_FAILED",
        "regex": r"(?:Command exited with code|non-zero exit status|command not found|is not recognized as an internal or external command)",
        "main_issue": "Terminal Command Execution Failed",
        "why": "The shell command returned a non-zero exit code or the requested executable is not installed in system PATH.",
        "suggested_fix": "Review command flags, verify dependencies are installed, or ask the assistant to auto-debug the command."
    }
]


def diagnose_error_root_cause(raw_error: str) -> Dict[str, str]:
    """Inspects raw error text and returns structured root cause diagnosis."""
    if not raw_error or not raw_error.strip():
        return {
            "type": "UNKNOWN",
            "main_issue": "Unspecified Execution Failure",
            "why": "An empty or unknown error occurred.",
            "suggested_fix": "Retry the action or check background service logs.",
            "raw_details": ""
        }

    cleaned = raw_error.strip()

    for pattern in ERROR_PATTERNS:
        if re.search(pattern["regex"], cleaned, re.IGNORECASE):
            return {
                "type": pattern["type"],
                "main_issue": pattern["main_issue"],
                "why": pattern["why"],
                "suggested_fix": pattern["suggested_fix"],
                "raw_details": cleaned
            }

    # Extract first non-empty line as clean fallback summary
    first_line = cleaned.splitlines()[0] if cleaned.splitlines() else cleaned
    if len(first_line) > 120:
        first_line = first_line[:117] + "..."

    return {
        "type": "GENERAL_ERROR",
        "main_issue": f"Execution Issue: {first_line}",
        "why": "The tool or operation encountered an unexpected exception during execution.",
        "suggested_fix": "Review the technical details below or ask the assistant to propose an alternative approach.",
        "raw_details": cleaned
    }


def format_explainable_error_markdown(raw_error: str, tool_name: Optional[str] = None) -> str:
    """Formats raw error text into an actionable, user-friendly markdown diagnostic block."""
    diag = diagnose_error_root_cause(raw_error)

    tool_line = f"**Tool**: `{tool_name}`\n" if tool_name else ""
    raw_preview = diag["raw_details"]
    if len(raw_preview) > 1500:
        raw_preview = raw_preview[:1500] + "\n...[truncated]"

    return (
        f"> [!WARNING]\n"
        f"> ### ⚠️ Main Issue: {diag['main_issue']}\n"
        f"> {tool_line}"
        f"> **What Happened / Why**: {diag['why']}\n"
        f"> **Suggested Fix**: {diag['suggested_fix']}\n"
        f">\n"
        f"> <details>\n"
        f"> <summary>Technical Details</summary>\n"
        f">\n"
        f"> ```text\n"
        f"> {raw_preview}\n"
        f"> ```\n"
        f"> </details>"
    )

