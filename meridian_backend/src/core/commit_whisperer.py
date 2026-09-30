import os
import subprocess
import logging
from typing import Dict, List, Any

class CommitWhisperer:
    """
    The Commit Whisperer (📜)
    Triggers before git commit, inspects staged changes against semantic versioning rules,
    checks CHANGELOG.md & package.json synchronization, and prompts version bump suggestions.
    """
    def __init__(self, workspace_root: str):
        self.workspace_root = workspace_root

    def inspect_staged_commit(self) -> Dict[str, Any]:
        """Inspects git status & staged changes prior to commit."""
        staged_files = []
        has_public_api_change = False
        changelog_updated = False
        package_json_updated = False

        try:
            cmd = ["git", "diff", "--cached", "--name-only"]
            res = subprocess.run(cmd, capture_output=True, text=True, cwd=self.workspace_root)
            if res.returncode == 0:
                staged_files = [line.strip() for line in res.stdout.splitlines() if line.strip()]
        except Exception as e:
            logging.debug(f"Git diff cached failed: {e}")

        for f in staged_files:
            if "CHANGELOG.md" in f or "TIMELINE.md" in f:
                changelog_updated = True
            if "package.json" in f or "setup.py" in f or "Cargo.toml" in f:
                package_json_updated = True
            if any(core_kw in f for core_kw in ["src/core/", "api.py", "types.ts", "engine"]):
                has_public_api_change = True

        suggested_bump = "patch"
        if has_public_api_change:
            suggested_bump = "minor"

        notification = ""
        if has_public_api_change and not changelog_updated:
            notification = f"You changed public API in staged files ({len(staged_files)} files)—suggest {suggested_bump} bump? Also, add entry to CHANGELOG.md? [Y]es / [N]o / [E]dit"

        has_staged = len(staged_files) > 0
        if has_staged:
            primary_file = os.path.basename(staged_files[0])
            mod_prefix = "feat" if has_public_api_change else "fix"
            suggested_message = f"{mod_prefix}: update {primary_file} and related modules"
        else:
            suggested_message = ""

        return {
            "has_staged": has_staged,
            "staged_files": staged_files,
            "has_public_api_change": has_public_api_change,
            "changelog_updated": changelog_updated,
            "package_json_updated": package_json_updated,
            "suggested_version_bump": suggested_bump,
            "suggested_message": suggested_message,
            "notification": notification
        }
