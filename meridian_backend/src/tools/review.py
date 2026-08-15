import os
import glob
import subprocess
from typing import List, Dict, Any
from src.core.llm_provider import call_llm_sync, scan_and_redact_secrets

REVIEW_SYSTEM_PROMPT = """You are Meridian's code auditor and reviewer. Switched to REVIEWER mode.
Analyze the provided code or diff thoroughly across the 5 Review Pillars:
1. **Correctness** — Logic errors, off-by-one, wrong conditionals, data races.
2. **Security** — Injection risks, hardcoded credentials, unsafe deserialization.
3. **Performance** — N+1 loops, unnecessary I/O, blocking calls in async contexts.
4. **Maintainability** — Function length, naming consistency, documentation, dead code.
5. **Test Coverage** — Missing edge cases, untested error paths.

Return a structured markdown review. Focus only on actionable critiques. Use indicators like:
🔴 CRITICAL / SECURITY
🟡 WARNING / PERFORMANCE
🟢 OK
"""

def _get_active_model() -> str:
    from database import get_brain_model
    return get_brain_model()

def review_file(path: str) -> str:
    """Perform a structured 5-pillar code review of a single file."""
    path = os.path.abspath(path)
    if not os.path.exists(path) or not os.path.isfile(path):
        return f"Error: File '{path}' not found or is not a valid file."
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read()
            
        sanitized_code = scan_and_redact_secrets(code)
        prompt = f"Please review this file located at '{path}':\n\n```\n{sanitized_code}\n```"
        
        messages = [
            {"role": "system", "content": REVIEW_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
        return call_llm_sync(messages)
    except Exception as e:
        return f"Error reviewing file: {e}"

def review_diff(repo_path: str) -> str:
    """Review git diff HEAD of the specified repository path."""
    repo_path = os.path.abspath(repo_path)
    if not os.path.exists(repo_path):
        return f"Error: Repository path '{repo_path}' not found."
    try:
        cmd = ["git", "diff", "HEAD"]
        try:
            diff_out = subprocess.check_output(cmd, cwd=repo_path, stderr=subprocess.STDOUT).decode('utf-8', errors='ignore')
        except subprocess.CalledProcessError:
            diff_out = subprocess.check_output(["git", "diff"], cwd=repo_path, stderr=subprocess.STDOUT).decode('utf-8', errors='ignore')

        if not diff_out.strip():
            return "No git diff changes detected against HEAD to review."

            
        sanitized_diff = scan_and_redact_secrets(diff_out)
        prompt = f"Please review this git diff in repository '{repo_path}':\n\n```diff\n{sanitized_diff}\n```"
        
        messages = [
            {"role": "system", "content": REVIEW_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
        return call_llm_sync(messages)
    except Exception as e:
        return f"Error reviewing git diff: {e}"

def review_directory(path: str, glob_pattern: str = "**/*.py") -> str:
    """Review all files matching a glob pattern in the directory and compile an aggregated review report."""
    path = os.path.abspath(path)
    if not os.path.exists(path):
        return f"Error: Directory '{path}' not found."
    try:
        search_path = os.path.join(path, glob_pattern)
        files = glob.glob(search_path, recursive=True)
        # Filter directories out
        files = [f for f in files if os.path.isfile(f)]
        
        if not files:
            return f"No files matching '{glob_pattern}' found in '{path}'."
            
        reports = []
        # Limit to top 5 files to prevent LLM fatigue/timeouts in single tool call
        for file in files[:5]:
            reports.append(f"### Review of {os.path.basename(file)}:\n" + review_file(file))
            
        summary = f"Aggregated Code Review Report for {len(files[:5])} files in '{path}':\n\n"
        if len(files) > 5:
            summary += f"(Note: Discovered {len(files)} files, reviewing the first 5 to preserve resources)\n\n"
            
        return summary + "\n\n---\n\n".join(reports)
    except Exception as e:
        return f"Error reviewing directory: {e}"

def export_review(output_path: str, code_path: str) -> str:
    """Generate a code review for code_path and export the report to output_path."""
    try:
        output_path = os.path.abspath(output_path)
        code_path = os.path.abspath(code_path)
        report = review_file(code_path) if os.path.isfile(code_path) else review_directory(code_path)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)
        return f"Successfully exported code review report to '{output_path}'."
    except Exception as e:
        return f"Failed to export review: {e}"

