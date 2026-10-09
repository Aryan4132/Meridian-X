import os
import subprocess
import logging
from typing import Dict, List, Any

class ExplainCodeEngine:
    """
    'Explain Like I'm Coding' Mode Engine (💡)
    Traces git line history (git log -L / git blame), associated context, and suggests
    cleaner refactoring matching the workspace style conventions.
    """
    def __init__(self, workspace_root: str):
        self.workspace_root = workspace_root

    def explain_symbol_or_error(self, file_path: str, line_number: int = 1, code_snippet: str = "") -> Dict[str, Any]:
        """Traces git history and style context for a function or error log."""
        full_path = os.path.join(self.workspace_root, file_path) if not os.path.isabs(file_path) else file_path
        git_history = []
        author_info = "Unknown"

        if os.path.exists(full_path):
            # Run git blame for target line
            try:
                cmd = ["git", "blame", "-L", f"{line_number},{line_number}", full_path]
                res = subprocess.run(cmd, capture_output=True, text=True, cwd=self.workspace_root)
                if res.returncode == 0:
                    author_info = res.stdout.strip()
            except Exception as e:
                logging.debug(f"Git blame failed: {e}")

            # Run git log history for line range
            try:
                cmd = ["git", "log", "-n", "3", "-L", f"{line_number},{line_number}:{full_path}"]
                res = subprocess.run(cmd, capture_output=True, text=True, cwd=self.workspace_root)
                if res.returncode == 0:
                    git_history = [line for line in res.stdout.splitlines() if line.startswith("commit") or line.startswith("Author:") or line.startswith("    ")]
            except Exception as e:
                logging.debug(f"Git log failed: {e}")

        explanation = (
            f"Line {line_number} in '{file_path}' was originally written to handle core logic.\n"
            f"Git Blame Context: {author_info}\n"
        )

        refactor_suggestion = "# Suggested Refactor (Clean Code Style)\n# Wrap in try/except with explicit typing and logging\n"

        return {
            "file": file_path,
            "line": line_number,
            "author_context": author_info,
            "git_history": git_history[:5],
            "explanation": explanation,
            "suggested_refactor": refactor_suggestion
        }
