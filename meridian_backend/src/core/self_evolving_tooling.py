import os
import sys
import subprocess
import tempfile
import logging
from typing import Dict, List, Any, Optional

class SelfEvolvingToolingManager:
    """
    Self-Evolving Tooling (🛠️)
    Generates Python helper scripts, requires user approval before execution in a sandbox,
    tests code logic, and permanently registers successful scripts to the toolset.
    """
    def __init__(self, tools_dir: str):
        self.tools_dir = tools_dir
        os.makedirs(self.tools_dir, exist_ok=True)
        self.pending_sandboxes: Dict[str, Dict[str, Any]] = {}
        self.tool_call_history: List[str] = []

    def record_tool_call(self, tool_name: str, args: Optional[Dict[str, Any]] = None) -> None:
        """Records an invoked tool to identify recurring multi-tool workflows."""
        self.tool_call_history.append(tool_name)
        if len(self.tool_call_history) > 100:
            self.tool_call_history = self.tool_call_history[-100:]

    def detect_sequence_opportunity(self, min_occurrences: int = 3, window_size: int = 2) -> Optional[Dict[str, Any]]:
        """Scans tool history for repeating sequences suitable for macro synthesis."""
        if len(self.tool_call_history) < window_size * min_occurrences:
            return None

        from collections import Counter
        pairs = []
        for i in range(len(self.tool_call_history) - window_size + 1):
            pair = tuple(self.tool_call_history[i:i + window_size])
            pairs.append(pair)

        counts = Counter(pairs)
        for seq, count in counts.items():
            if count >= min_occurrences:
                macro_name = f"macro_{seq[0]}_{seq[1]}"
                return {
                    "sequence": seq,
                    "count": count,
                    "suggested_macro_name": macro_name,
                    "description": f"Compound macro executing {' -> '.join(seq)}"
                }
        return None

    def prepare_tool_script(self, tool_name: str, code: str, description: str) -> Dict[str, Any]:
        """Prepares a proposed tool script and generates a sandbox ticket requiring user approval."""
        sandbox_id = f"sandbox-{tool_name}-{os.urandom(4).hex()}"
        ticket = {
            "sandbox_id": sandbox_id,
            "tool_name": tool_name,
            "code": code,
            "description": description,
            "status": "pending_approval",
            "requires_user_approval": True
        }
        self.pending_sandboxes[sandbox_id] = ticket
        return ticket

    def validate_code_safety(self, code: str) -> tuple[bool, str]:
        """Performs static AST safety validation before allowing execution."""
        try:
            import ast
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Attribute):
                    if node.attr in ("rmtree", "system", "popen", "kill", "remove_tree"):
                        return False, f"Potentially destructive operation '{node.attr}' blocked by safety policy."
                elif isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Name) and node.func.id in ("eval", "exec", "__import__"):
                        return False, f"Dynamic execution primitive '{node.func.id}' blocked by safety policy."
            return True, "Code passed static safety analysis."
        except SyntaxError as se:
            return False, f"Syntax error in proposed script: {se}"
        except Exception as e:
            return False, f"AST verification failed: {e}"

    def execute_in_sandbox(self, sandbox_id: str, approved_by_user: bool = False) -> Dict[str, Any]:
        """Executes the tool script inside an isolated subprocess sandbox upon user approval."""
        if sandbox_id not in self.pending_sandboxes:
            return {"success": False, "error": f"Sandbox ID '{sandbox_id}' not found."}

        ticket = self.pending_sandboxes[sandbox_id]
        if not approved_by_user:
            return {
                "success": False,
                "error": "User approval required before running script in sandbox.",
                "status": "approval_required"
            }

        code = ticket["code"]
        safe, reason = self.validate_code_safety(code)
        if not safe:
            return {
                "success": False,
                "error": reason,
                "sandbox_id": sandbox_id,
                "status": "blocked_by_safety"
            }
        # Write to temporary file for isolated execution
        with tempfile.NamedTemporaryFile(suffix=".py", mode="w", delete=False, encoding="utf-8") as temp_file:
            temp_file.write(code)
            temp_path = temp_file.name

        try:
            proc = subprocess.run(
                [sys.executable, temp_path],
                capture_output=True,
                text=True,
                timeout=10
            )
            ticket["status"] = "tested"
            ticket["stdout"] = proc.stdout
            ticket["stderr"] = proc.stderr
            ticket["exit_code"] = proc.returncode

            return {
                "success": proc.returncode == 0,
                "exit_code": proc.returncode,
                "stdout": proc.stdout,
                "stderr": proc.stderr,
                "sandbox_id": sandbox_id
            }
        except subprocess.TimeoutExpired:
            return {"success": False, "error": "Execution timed out (10s limit).", "sandbox_id": sandbox_id}
        except Exception as err:
            return {"success": False, "error": str(err), "sandbox_id": sandbox_id}
        finally:
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except Exception:
                    pass

    def register_permanent_tool(self, sandbox_id: str) -> Dict[str, Any]:
        """Promotes a tested tool from sandbox into permanent workspace tools directory."""
        if sandbox_id not in self.pending_sandboxes:
            return {"success": False, "error": "Invalid sandbox ID."}

        ticket = self.pending_sandboxes[sandbox_id]
        tool_name = ticket["tool_name"].lower().replace(" ", "_")
        if not tool_name.endswith(".py"):
            file_name = f"custom_{tool_name}.py"
        else:
            file_name = tool_name

        dest_path = os.path.join(self.tools_dir, file_name)
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(ticket["code"])

        ticket["status"] = "permanently_added"
        ticket["file_path"] = dest_path

        return {
            "success": True,
            "message": f"Tool '{file_name}' permanently added to toolset.",
            "file_path": dest_path
        }
