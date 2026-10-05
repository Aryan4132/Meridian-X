import os
import ast
import json
import subprocess
from typing import Optional, List, Dict, Any
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from database import (
    get_sqlite_conn,
    get_user_profile,
    get_ollama_client_host,
    add_to_task_log
)
from src.core.dev_automation import dev_automation_engine, FormatCodeRequest, RunTestsRequest, BuildProjectRequest
from src.core.agent_status_stream import agent_status_stream_manager
from src.core.deep_project_context import DeepProjectContextEngine
from src.core.workspace_orchestrator import WorkspaceOrchestrator
from src.core.self_evolving_tooling import SelfEvolvingToolingManager
from src.core.explain_code_engine import ExplainCodeEngine
from src.core.experiment_runner import ExperimentRunner
from src.core.silent_workflow_guardian import SilentWorkflowGuardian
from src.core.what_broke_detective import WhatBrokeDetective
from src.core.boilerplate_genie import BoilerplateGenie
from src.core.commit_whisperer import CommitWhisperer

router = APIRouter(tags=["automation"])

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
deep_context_engine = DeepProjectContextEngine(WORKSPACE_ROOT)
workspace_orchestrator = WorkspaceOrchestrator(WORKSPACE_ROOT)
self_evolving_manager = SelfEvolvingToolingManager(os.path.join(WORKSPACE_ROOT, "meridian_backend", "src", "tools"))
explain_engine = ExplainCodeEngine(WORKSPACE_ROOT)
experiment_runner = ExperimentRunner()
silent_guardian = SilentWorkflowGuardian(WORKSPACE_ROOT)
what_broke_detective = WhatBrokeDetective(WORKSPACE_ROOT)
boilerplate_genie = BoilerplateGenie(WORKSPACE_ROOT)
commit_whisperer = CommitWhisperer(WORKSPACE_ROOT)

class SandboxRequest(BaseModel):
    code: str
    timeout: Optional[float] = 10.0

class PaperCoderRequest(BaseModel):
    paper_input: str

class LaunchPresetPayload(BaseModel):
    preset: str = "coding"

class PrepareToolPayload(BaseModel):
    tool_name: str
    code: str
    description: str

class ExecuteSandboxPayload(BaseModel):
    sandbox_id: str
    approved_by_user: bool = False

class RegisterToolPayload(BaseModel):
    sandbox_id: str

class ExplainSymbolPayload(BaseModel):
    file_path: str
    line_number: int = 1
    code_snippet: str = ""

class ExperimentPayload(BaseModel):
    endpoint: str
    method: str = "GET"
    headers: Optional[Dict[str, str]] = None
    payload: Optional[Dict[str, Any]] = None
    expected_status: int = 200
    expected_schema_keys: Optional[List[str]] = None

class GuardianInspectPayload(BaseModel):
    file_path: str
    content: str

class DetectiveDiagnosePayload(BaseModel):
    updated_package: str = ""

class BoilerplateGeniePayload(BaseModel):
    component_name: str
    target_dir: str = "meridian_frontend/src/components"

class EmitActivityPayload(BaseModel):
    status: str = "idle"
    message: str
    tool: Optional[str] = None
    subagent: Optional[str] = None
    task: Optional[str] = None
    details: Dict[str, Any] = {}
    progress: Optional[float] = None

@router.get("/api/developer/stats")
def get_developer_stats():
    conn = None
    try:
        try:
            conn = get_sqlite_conn()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM task_log")
            total_tasks = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM task_log WHERE outcome = 'success'")
            success_tasks = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM task_log WHERE outcome = 'failed'")
            failed_tasks = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM task_log WHERE tier >= 2")
            security_audits = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM task_log WHERE tool = 'heal_file' AND outcome = 'success'")
            successful_heals = cursor.fetchone()[0]
        finally:
            if conn:
                conn.close()
            
        pomodoros = get_user_profile("pomodoros_completed")
        if pomodoros is None:
            pomodoros = 0
        try:
            pomodoros = int(pomodoros)
        except Exception:
            pomodoros = 0

        try:
            res = subprocess.run(["git", "rev-list", "--count", "HEAD"], capture_output=True, text=True)
            git_commits = int(res.stdout.strip()) if res.returncode == 0 else 0
        except Exception:
            git_commits = 0
            
        return {
            "total_tasks": total_tasks,
            "success_tasks": success_tasks,
            "failed_tasks": failed_tasks,
            "security_audits": security_audits,
            "pomodoros": pomodoros,
            "pomodoros_completed": pomodoros,
            "count": pomodoros,
            "successful_heals": successful_heals,
            "git_commits": git_commits
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/sandbox/run")
def sandbox_run(request: SandboxRequest):
    try:
        ast.parse(request.code)
    except SyntaxError as se:
        add_to_task_log("sandbox_run", 2, "failed", f"Syntax Error: {se.msg} (line {se.lineno})")
        return {
            "status": "syntax_error",
            "message": f"Syntax Error: {se.msg} on line {se.lineno}",
            "lineno": se.lineno,
            "offset": se.offset,
            "text": se.text,
            "file_path": "sandbox_temp.py"
        }
        
    ollama_host = get_ollama_client_host()
    import ollama
    client = ollama.Client(host=ollama_host)
    from database import get_auditor_model
    auditor_model = get_auditor_model()
    
    args_str = json.dumps({"code": request.code})
    audit_prompt = (
        f"You are the Meridian Security Auditor. Assess if the following Python code execution is safe and does not contain vulnerabilities, dangerous file deletions, shell injections, or malicious system commands.\n"
        f"Arguments: {args_str}\n\n"
        f"Respond ONLY in this exact format:\n"
        f"REASONING: <brief analysis of the arguments>\n"
        f"DECISION: <APPROVED or REJECTED>"
    )
    
    decision = None
    reasoning = "Default approved."
    try:
        audit_res = client.generate(model=auditor_model, prompt=audit_prompt)
        audit_text = (audit_res.response if hasattr(audit_res, "response") else audit_res.get("response", "")).strip()
        for line in audit_text.split("\n"):
            if line.upper().startswith("DECISION:"):
                decision = line.split(":", 1)[1].strip().upper()
            elif line.upper().startswith("REASONING:"):
                reasoning = line.split(":", 1)[1].strip()
    except Exception:
        try:
            from database import get_brain_model
            main_model = get_brain_model()
            audit_res = client.generate(model=main_model, prompt=audit_prompt)
            audit_text = (audit_res.response if hasattr(audit_res, "response") else audit_res.get("response", "")).strip()
            for line in audit_text.split("\n"):
                if line.upper().startswith("DECISION:"):
                    decision = line.split(":", 1)[1].strip().upper()
                elif line.upper().startswith("REASONING:"):
                    reasoning = line.split(":", 1)[1].strip()
        except Exception as ex:
            decision = "REJECTED"
            reasoning = f"Security auditor failed to load: {ex}"

    if not decision:
        decision = "REJECTED"
        reasoning = "Security auditor returned no parsable DECISION."
            
    if "REJECTED" in decision:
        add_to_task_log("sandbox_run", 2, "blocked", f"Rejected by Security Auditor: {reasoning}")
        return {
            "status": "blocked",
            "message": f"Execution blocked by Security Auditor:\n{reasoning}"
        }
        
    add_to_task_log("sandbox_run", 2, "started")
    try:
        from src.tools.developer import run_python
        output = run_python(request.code, timeout=request.timeout or 30.0)
        add_to_task_log("sandbox_run", 2, "success")
        return {
            "status": "success",
            "output": output,
            "auditor_reasoning": reasoning
        }
    except Exception as e:
        add_to_task_log("sandbox_run", 2, "failed", str(e))
        return {
            "status": "error",
            "message": f"Execution failed: {str(e)}"
        }

@router.get("/api/codegraph/symbols")
async def get_codegraph_symbols_api(query: str = "", workspace_dir: Optional[str] = None):
    """DEV-05: AST Codebase Symbol Search."""
    from src.core.code_graph import search_codebase_symbols
    results = search_codebase_symbols(query, workspace_dir=workspace_dir)
    return {"status": "success", "count": len(results), "symbols": results}

@router.get("/api/codegraph/trace")
async def get_codegraph_trace_api(symbol_name: str, trace_type: str = "callers", workspace_dir: Optional[str] = None):
    """DEV-05: AST Caller/Callee Tracing."""
    from src.core.code_graph import trace_symbol_callers, trace_symbol_callees
    if trace_type == "callees":
        traces = trace_symbol_callees(symbol_name, workspace_dir=workspace_dir)
    else:
        traces = trace_symbol_callers(symbol_name, workspace_dir=workspace_dir)
    return {"status": "success", "symbol_name": symbol_name, "trace_type": trace_type, "count": len(traces), "traces": traces}

@router.get("/api/codegraph/impact")
async def get_codegraph_impact_api(target: str, workspace_dir: Optional[str] = None):
    """DEV-05: Instant Change Impact Analysis."""
    from src.core.code_graph import analyze_change_impact
    impact = analyze_change_impact(target, workspace_dir=workspace_dir)
    return {"status": "success", "impact": impact}

@router.post("/api/papercoder/generate")
async def generate_papercoder_repo_api(payload: PaperCoderRequest):
    """DEV-04: 3-Stage Paper-to-Code (PaperCoder) Generator."""
    from src.tools.papercoder import PaperCoderEngine
    engine = PaperCoderEngine()
    return await engine.generate_repository(payload.paper_input)

@router.get("/api/automation/git/status")
async def get_automation_git_status():
    """Inspect local git repository status, active branch, and modified files."""
    return await dev_automation_engine.get_git_status()

@router.post("/api/automation/code/format")
async def format_automation_code(payload: FormatCodeRequest):
    """Run code formatting tools on codebase."""
    agent_status_stream_manager.broadcast_event(
        status="executing_tool",
        message=f"Running code formatter ({payload.formatter}) on {payload.file_path or 'workspace'}",
        tool="dev_automation.format_code"
    )
    res = await dev_automation_engine.format_code(payload)
    agent_status_stream_manager.broadcast_event(
        status="idle" if res["success"] else "error",
        message="Code formatting completed successfully" if res["success"] else "Code formatting failed",
        details=res
    )
    return res

@router.post("/api/automation/test/run")
async def run_automation_tests(payload: RunTestsRequest):
    """Run pytest suite on developer workspace."""
    agent_status_stream_manager.broadcast_event(
        status="executing_tool",
        message=f"Running backend tests (filter: {payload.grep_filter or 'all'})",
        tool="dev_automation.run_tests"
    )
    res = await dev_automation_engine.run_tests(payload)
    agent_status_stream_manager.broadcast_event(
        status="completed" if res["success"] else "error",
        message=f"Tests {'passed' if res['success'] else 'failed'} in {res['duration_seconds']}s",
        details={"exit_code": res["exit_code"]}
    )
    return res

@router.post("/api/automation/build/project")
async def build_automation_project(payload: BuildProjectRequest):
    """Trigger project build steps for backend/frontend targets."""
    agent_status_stream_manager.broadcast_event(
        status="executing_tool",
        message=f"Building project target: {payload.target}",
        tool="dev_automation.build_project"
    )
    res = await dev_automation_engine.build_project(payload)
    agent_status_stream_manager.broadcast_event(
        status="completed" if res["success"] else "error",
        message=f"Project build {'succeeded' if res['success'] else 'failed'}",
        details=res
    )
    return res

@router.get("/api/agent/status")
async def get_agent_status_snapshot():
    """Return current snapshot of agent status, subagent state, and recent activity logs."""
    return agent_status_stream_manager.get_snapshot()

@router.post("/api/agent/activity/event")
async def emit_agent_activity_event(payload: EmitActivityPayload):
    """Manually emit agent activity event."""
    event = agent_status_stream_manager.broadcast_event(
        status=payload.status,
        message=payload.message,
        tool=payload.tool,
        subagent=payload.subagent,
        task=payload.task,
        details=payload.details,
        progress=payload.progress
    )
    return {"status": "broadcasted", "event": event.model_dump()}

@router.post("/api/context/scan")
async def scan_workspace_context():
    return deep_context_engine.scan_workspace()

@router.post("/api/orchestrator/launch")
async def launch_workspace_preset(payload: LaunchPresetPayload):
    return workspace_orchestrator.launch_preset(payload.preset)

@router.post("/api/self-evolving/prepare")
async def prepare_self_evolving_tool(payload: PrepareToolPayload):
    return self_evolving_manager.prepare_tool_script(payload.tool_name, payload.code, payload.description)

@router.post("/api/self-evolving/sandbox-execute")
async def execute_tool_sandbox(payload: ExecuteSandboxPayload):
    return self_evolving_manager.execute_in_sandbox(payload.sandbox_id, payload.approved_by_user)

@router.post("/api/self-evolving/register")
async def register_permanent_tool(payload: RegisterToolPayload):
    return self_evolving_manager.register_permanent_tool(payload.sandbox_id)

@router.post("/api/explain/symbol")
async def explain_code_symbol(payload: ExplainSymbolPayload):
    return explain_engine.explain_symbol_or_error(payload.file_path, payload.line_number, payload.code_snippet)

@router.post("/api/experiment/run")
async def run_api_experiment(payload: ExperimentPayload):
    return await experiment_runner.run_experiment(
        endpoint=payload.endpoint,
        method=payload.method,
        headers=payload.headers,
        payload=payload.payload,
        expected_status=payload.expected_status,
        expected_schema_keys=payload.expected_schema_keys
    )

@router.post("/api/guardian/inspect")
async def inspect_guardian_changes(payload: GuardianInspectPayload):
    return {"alerts": silent_guardian.inspect_recent_changes(payload.file_path, payload.content)}

@router.post("/api/detective/diagnose")
async def diagnose_what_broke(payload: DetectiveDiagnosePayload):
    return what_broke_detective.diagnose_failures(payload.updated_package)

@router.post("/api/boilerplate/generate")
async def generate_component_boilerplate(payload: BoilerplateGeniePayload):
    return boilerplate_genie.generate_component_stub(payload.component_name, payload.target_dir)

@router.get("/api/commit-whisperer/inspect")
async def inspect_commit_status():
    return commit_whisperer.inspect_staged_commit()
