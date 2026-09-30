import os
import sys
import asyncio
import logging
import shutil
import subprocess
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

class FormatCodeRequest(BaseModel):
    file_path: Optional[str] = None
    formatter: str = "auto" # auto, black, ruff, prettier

class RunTestsRequest(BaseModel):
    test_target: str = "all"
    grep_filter: Optional[str] = None
    coverage: bool = False

class BuildProjectRequest(BaseModel):
    target: str = "all" # backend, frontend, all
    production: bool = False

class DevAutomationEngine:
    """Provides safe async desktop automation runners for common developer tasks."""

    def __init__(self, workspace_root: Optional[str] = None):
        self.workspace_root = workspace_root or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

    async def _run_command(self, cmd: List[str], cwd: Optional[str] = None, timeout: float = 60.0) -> Dict[str, Any]:
        """Utility runner for shell commands with timeout."""
        target_dir = cwd or self.workspace_root
        start_time = asyncio.get_event_loop().time()
        try:
            proc = await asyncio.create_subprocess_exec(
                *cmd,
                cwd=target_dir,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
            duration = round(asyncio.get_event_loop().time() - start_time, 2)
            return {
                "success": proc.returncode == 0,
                "exit_code": proc.returncode,
                "stdout": stdout.decode("utf-8", errors="replace"),
                "stderr": stderr.decode("utf-8", errors="replace"),
                "duration_seconds": duration,
                "command": " ".join(cmd)
            }
        except asyncio.TimeoutError:
            return {
                "success": False,
                "exit_code": -1,
                "stdout": "",
                "stderr": f"Command timed out after {timeout} seconds",
                "duration_seconds": timeout,
                "command": " ".join(cmd)
            }
        except Exception as e:
            return {
                "success": False,
                "exit_code": -1,
                "stdout": "",
                "stderr": str(e),
                "duration_seconds": 0.0,
                "command": " ".join(cmd)
            }

    async def get_git_status(self) -> Dict[str, Any]:
        """Fetch current git status, active branch, and modified files."""
        branch_res = await self._run_command(["git", "rev-parse", "--abbrev-ref", "HEAD"])
        status_res = await self._run_command(["git", "status", "--porcelain"])

        branch = branch_res["stdout"].strip() if branch_res["success"] else "unknown"
        modified_files = []
        untracked_files = []

        if status_res["success"]:
            for line in status_res["stdout"].splitlines():
                if not line.strip():
                    continue
                code = line[:2]
                filename = line[3:].strip()
                if code.strip() == "??":
                    untracked_files.append(filename)
                else:
                    modified_files.append({"status": code.strip(), "file": filename})

        return {
            "is_git_repo": branch_res["success"],
            "branch": branch,
            "modified_count": len(modified_files),
            "untracked_count": len(untracked_files),
            "modified_files": modified_files,
            "untracked_files": untracked_files
        }

    async def format_code(self, req: FormatCodeRequest) -> Dict[str, Any]:
        """Run code formatting tools on file or workspace."""
        file_target = req.file_path or "."
        is_python = file_target.endswith(".py") or req.formatter in ["black", "ruff"]

        if is_python:
            cmd = [sys.executable, "-m", "black", file_target]
            res = await self._run_command(cmd)
            if not res["success"] and "No module named black" in res["stderr"]:
                # Fallback to ruff
                cmd = [sys.executable, "-m", "ruff", "format", file_target]
                res = await self._run_command(cmd)
            return res
        else:
            # Frontend JS/TS formatting
            cmd = ["npx", "prettier", "--write", file_target]
            return await self._run_command(cmd, cwd=os.path.join(self.workspace_root, "meridian_frontend"))

    async def run_tests(self, req: RunTestsRequest) -> Dict[str, Any]:
        """Run pytest test suite with options."""
        cmd = [sys.executable, "-m", "pytest"]
        if req.grep_filter:
            cmd.extend(["-k", req.grep_filter])
        if req.coverage:
            cmd.extend(["--cov=src"])

        backend_dir = os.path.join(self.workspace_root, "meridian_backend")
        res = await self._run_command(cmd, cwd=backend_dir, timeout=120.0)
        return res

    async def build_project(self, req: BuildProjectRequest) -> Dict[str, Any]:
        """Build backend or frontend project targets."""
        results = {}
        if req.target in ["frontend", "all"]:
            frontend_dir = os.path.join(self.workspace_root, "meridian_frontend")
            res = await self._run_command(["npm", "run", "build"], cwd=frontend_dir, timeout=180.0)
            results["frontend"] = res

        if req.target in ["backend", "all"]:
            backend_dir = os.path.join(self.workspace_root, "meridian_backend")
            res = await self._run_command([sys.executable, "-m", "py_compile", "api.py"], cwd=backend_dir)
            results["backend"] = res

        return {
            "success": all(r.get("success", False) for r in results.values()),
            "details": results
        }

dev_automation_engine = DevAutomationEngine()
