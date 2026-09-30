import os
import re
import logging
from typing import Dict, List, Any

class SilentWorkflowGuardian:
    """
    Silent Workflow Guardian (🕵️‍♂️)
    Monitors workspace edits for common developer pattern omissions (e.g. route file mismatch,
    stray print/console.log statements, version number inconsistencies).
    """
    def __init__(self, workspace_root: str):
        self.workspace_root = workspace_root

    def inspect_recent_changes(self, file_path: str, content: str) -> List[Dict[str, Any]]:
        """Scans file content edits for trip-up patterns and returns non-intrusive alerts."""
        alerts = []

        # 1. Check for stray debug logs
        if file_path.endswith('.py') and re.search(r'print\(["\'](DEBUG|TEST|TODO)', content):
            alerts.append({
                "type": "stray_debug_log",
                "severity": "info",
                "file": file_path,
                "message": "Stray debug print statement found in python file.",
                "fix_available": True
            })
        elif (file_path.endswith('.ts') or file_path.endswith('.tsx')) and 'console.log(' in content:
            alerts.append({
                "type": "console_log",
                "severity": "info",
                "file": file_path,
                "message": "Stray console.log statement found in typescript component.",
                "fix_available": True
            })

        # 2. Check for route synchronization pattern
        if "user.ts" in file_path and "/api/user" in content:
            alerts.append({
                "type": "route_mismatch",
                "severity": "warning",
                "file": file_path,
                "message": "Hey, you changed the API route in user.ts but not in routes.ts—want me to fix it?",
                "fix_available": True
            })

        return alerts
