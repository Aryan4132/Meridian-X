import os
import subprocess
from typing import Optional
from src.core.llm_provider import call_llm_sync, scan_and_redact_secrets

TEST_GEN_SYSTEM_PROMPT = """You are Meridian's Autonomous Unit Test Generator.
Generate comprehensive, production-ready unit tests covering edge cases, success paths, and error scenarios.
Return ONLY valid, runnable code without conversational filler.
"""

REVIEW_SYSTEM_PROMPT = """You are Meridian's Autonomous Pre-Commit PR Reviewer.
Analyze git diff changes against the 5 Review Pillars:
1. Correctness & Logic
2. Security & Vulnerabilities
3. Performance & Bottlenecks
4. Code Quality & Formatting
5. Test Coverage Needs

Return structured markdown feedback with clear indicators (🔴 CRITICAL, 🟡 WARNING, 🟢 OK).
"""

def generate_unit_tests(file_path: str, framework: str = "pytest", target_output: Optional[str] = None) -> str:
    """Generate comprehensive pytest or jest unit tests for a source file and optionally write them to disk."""
    abs_path = os.path.abspath(file_path)
    if not os.path.exists(abs_path) or not os.path.isfile(abs_path):
        return f"Error: File '{file_path}' not found or invalid."

    try:
        with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
            code_content = f.read()

        sanitized_code = scan_and_redact_secrets(code_content)
        basename = os.path.basename(abs_path)
        name_no_ext, ext = os.path.splitext(basename)

        prompt = (
            f"Generate automated {framework} unit tests for file '{basename}':\n\n"
            f"```\n{sanitized_code}\n```\n\n"
            f"Write robust test cases covering standard execution, invalid inputs, edge cases, and exceptions."
        )

        messages = [
            {"role": "system", "content": TEST_GEN_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]

        test_code = call_llm_sync(messages)

        # Auto-write test file if requested or infer sensible path
        if not target_output:
            repo_dir = os.path.dirname(abs_path)
            if framework.lower() == "pytest" or ext in [".py"]:
                target_output = os.path.join(repo_dir, f"test_{name_no_ext}.py")
            else:
                target_output = os.path.join(repo_dir, f"{name_no_ext}.test.ts")

        try:
            target_output = os.path.abspath(target_output)
            os.makedirs(os.path.dirname(target_output), exist_ok=True)
            with open(target_output, "w", encoding="utf-8") as f:
                f.write(test_code)
            return f"Successfully generated {framework} unit tests and saved to '{target_output}':\n\n```\n{test_code[:500]}...\n```"
        except Exception as write_err:
            return f"Generated unit tests successfully:\n\n```\n{test_code}\n```\n\n(Note: Failed to save to disk: {write_err})"

    except Exception as e:
        return f"Error generating unit tests for '{file_path}': {e}"

def review_git_changes(repo_path: str = ".") -> str:
    """Perform pre-commit automated code review on staged and unstaged git diffs in a repository."""
    abs_repo = os.path.abspath(repo_path)
    if not os.path.exists(abs_repo):
        return f"Error: Repository path '{repo_path}' does not exist."

    try:
        # Cross-platform safe list-based git diff checks
        cmd_unstaged = ["git", "diff"]
        cmd_staged = ["git", "diff", "--cached"]

        unstaged_diff = subprocess.check_output(cmd_unstaged, cwd=abs_repo, stderr=subprocess.STDOUT).decode('utf-8', errors='ignore')
        staged_diff = subprocess.check_output(cmd_staged, cwd=abs_repo, stderr=subprocess.STDOUT).decode('utf-8', errors='ignore')

        combined_diff = ""
        if staged_diff.strip():
            combined_diff += f"### Staged Changes:\n```diff\n{staged_diff}\n```\n\n"
        if unstaged_diff.strip():
            combined_diff += f"### Unstaged Changes:\n```diff\n{unstaged_diff}\n```\n\n"

        if not combined_diff.strip():
            return "No staged or unstaged git diff changes detected to review."

        sanitized_diff = scan_and_redact_secrets(combined_diff)
        prompt = f"Please provide an autonomous pre-commit PR review for repository '{abs_repo}':\n\n{sanitized_diff}"

        messages = [
            {"role": "system", "content": REVIEW_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]

        return call_llm_sync(messages)

    except Exception as e:
        return f"Error reviewing git changes in '{repo_path}': {e}"
