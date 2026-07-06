import os
import glob
import subprocess
import ollama
from typing import List, Dict, Any
from database import get_ollama_client_host

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
    return os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")

def review_file(path: str) -> str:
    """Perform a structured 5-pillar code review of a single file."""
    if not os.path.exists(path):
        return f"Error: File '{path}' not found."
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read()
            
        client = ollama.Client(host=get_ollama_client_host())
        prompt = f"Please review this file located at '{path}':\n\n```\n{code}\n```"
        
        res = client.chat(
            model=_get_active_model(),
            messages=[
                {"role": "system", "content": REVIEW_SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )
        if hasattr(res, "message") and hasattr(res.message, "content"):
            return res.message.content
        return res.get("message", {}).get("content", "Failed to generate code review.")
    except Exception as e:
        return f"Error reviewing file: {e}"

def review_diff(repo_path: str) -> str:
    """Review git diff HEAD of the specified repository path."""
    try:
        diff_out = subprocess.check_output("git diff HEAD", cwd=repo_path, shell=True, stderr=subprocess.STDOUT).decode('utf-8')
        if not diff_out.strip():
            return "No git diff changes detected against HEAD to review."
            
        client = ollama.Client(host=get_ollama_client_host())
        prompt = f"Please review this git diff in repository '{repo_path}':\n\n```diff\n{diff_out}\n```"
        
        res = client.chat(
            model=_get_active_model(),
            messages=[
                {"role": "system", "content": REVIEW_SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )
        if hasattr(res, "message") and hasattr(res.message, "content"):
            return res.message.content
        return res.get("message", {}).get("content", "Failed to generate diff review.")
    except Exception as e:
        return f"Error reviewing git diff: {e}"

def review_directory(path: str, glob_pattern: str = "**/*.py") -> str:
    """Review all files matching a glob pattern in the directory and compile an aggregated review report."""
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
        report = review_file(code_path) if os.path.isfile(code_path) else review_directory(code_path)
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)
        return f"Successfully exported code review report to '{output_path}'."
    except Exception as e:
        return f"Failed to export review: {e}"
