import os
import json
import uuid
import hashlib
import hmac as hmac_mod
from typing import Optional, List, Dict, Any
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel

router = APIRouter(tags=["scheduler"])

class CreateSchedulerJob(BaseModel):
    goal: str
    interval_seconds: int

class WinSchedulerRequest(BaseModel):
    name: str
    goal: str
    schedule: str  # "daily" or "once"
    time: str      # "HH:MM"
    date: str = "" # "YYYY-MM-DD" for once

class WinSchedulerDeleteRequest(BaseModel):
    name: str

class WatchLogRequest(BaseModel):
    path: str
    patterns: List[str]
    on_match_goal: str

class UnwatchLogRequest(BaseModel):
    path: str

class ProposeHealRequest(BaseModel):
    file_path: str
    error_message: str

class ApplyHealRequest(BaseModel):
    file_path: str
    proposed_code: str
    secret_to_env: Optional[str] = None
    checkpoint_id: Optional[str] = None

class WorkflowCreateRequest(BaseModel):
    name: str
    nodes: List[Dict[str, Any]]
    edges: List[Dict[str, Any]]
    active: Optional[bool] = True

class AIWorkflowRequest(BaseModel):
    goal: str

@router.get("/api/scheduler/runs")
def scheduler_runs(limit: Optional[int] = 20):
    try:
        from database import get_background_runs
        runs = get_background_runs(limit=limit or 20)
        return {"runs": runs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/scheduler/create")
def api_scheduler_create(request: CreateSchedulerJob):
    try:
        from src.core.scheduler import scheduler, execute_scheduled_goal
        job_id = f"user_job_{uuid.uuid4().hex[:8]}"
        scheduler.add_job(
            execute_scheduled_goal,
            trigger='interval',
            seconds=request.interval_seconds,
            args=[request.goal],
            id=job_id,
            name=request.goal[:50],
            replace_existing=True
        )
        return {"status": "success", "message": f"Successfully scheduled background job '{job_id}' every {request.interval_seconds}s."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/scheduler/win/list")
def api_scheduler_win_list():
    try:
        from src.tools.task_scheduler import win_list_tasks_raw
        tasks = win_list_tasks_raw()
        return {"status": "success", "tasks": tasks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/scheduler/win/create")
def api_scheduler_win_create(request: WinSchedulerRequest):
    try:
        from src.tools.task_scheduler import win_schedule_daily, win_schedule_once
        if request.schedule.lower() == "daily":
            res = win_schedule_daily(request.name, request.goal, request.time)
        elif request.schedule.lower() == "once":
            res = win_schedule_once(request.name, request.goal, request.date, request.time)
        else:
            raise HTTPException(status_code=400, detail="Invalid schedule type. Choose 'daily' or 'once'.")
        
        if "error" in res.lower():
            raise HTTPException(status_code=500, detail=res)
        return {"status": "success", "message": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/scheduler/win/delete")
def api_scheduler_win_delete(request: WinSchedulerDeleteRequest):
    try:
        from src.tools.task_scheduler import win_delete_task
        res = win_delete_task(request.name)
        if "error" in res.lower():
            raise HTTPException(status_code=500, detail=res)
        return {"status": "success", "message": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/watcher/start")
def watcher_start(request: WatchLogRequest):
    try:
        from src.core.watcher import start_watching_log
        msg = start_watching_log(request.path, request.patterns, request.on_match_goal)
        return {"status": "success", "message": msg}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/watcher/stop")
def watcher_stop(request: UnwatchLogRequest):
    try:
        from src.core.watcher import stop_watching_log
        msg = stop_watching_log(request.path)
        return {"status": "success", "message": msg}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/watcher/list")
def watcher_list():
    try:
        from src.core.watcher import list_log_watchers
        watchers = list_log_watchers()
        return {"watchers": watchers}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/watcher/propose-heal")
def propose_heal(request: ProposeHealRequest):
    try:
        abs_path = os.path.abspath(request.file_path)
        if not os.path.exists(abs_path):
            raise HTTPException(status_code=404, detail=f"File not found: {request.file_path}")
        
        with open(abs_path, "r", encoding="utf-8", errors="ignore") as f:
            original_code = f.read()

        import ollama
        from database import get_ollama_client_host, get_brain_model
        ollama_host = get_ollama_client_host()
        client = ollama.Client(host=ollama_host)
        model = get_brain_model()

        is_secret = request.error_message == "secret_leak"
        
        if is_secret:
            prompt = (
                f"You are a security self-healing assistant. The following file has a hardcoded API key or credential:\n"
                f"File: {abs_path}\n\n"
                f"Original Code:\n"
                f"```\n{original_code}\n```\n\n"
                f"Rewrite this file so it loads the credential securely from environment variables (using 'os.environ.get' for Python, 'process.env' for Node/JS/TS, etc.).\n"
                f"Output ONLY the raw corrected file contents. Do NOT include markdown code blocks, explanation, or notes. Just the raw, compile-ready code."
            )
        else:
            prompt = (
                f"You are a compiler self-healing assistant. The following file has a syntax or compile error:\n"
                f"File: {abs_path}\n"
                f"Error: {request.error_message}\n\n"
                f"Original Code:\n"
                f"```\n{original_code}\n```\n\n"
                f"Rewrite this file to fix the compilation/syntax error.\n"
                f"Output ONLY the raw corrected file contents. Do NOT include markdown code blocks, explanation, or notes. Just the raw, compile-ready code."
            )

        res = client.generate(model=model, prompt=prompt)
        response_text = (res.response if hasattr(res, "response") else res.get("response", "")).strip()

        if response_text.startswith("```"):
            lines = response_text.splitlines()
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].startswith("```"):
                lines = lines[:-1]
            response_text = "\n".join(lines).strip()

        return {
            "original": original_code,
            "proposed": response_text,
            "file_path": abs_path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/watcher/apply-heal")
def apply_heal(request: ApplyHealRequest):
    try:
        if request.checkpoint_id:
            try:
                from src.core.history_manager import create_checkpoint
                create_checkpoint(request.checkpoint_id)
            except Exception as che:
                print(f"[History Manager] Failed to create checkpoint: {che}")

        abs_path = os.path.abspath(request.file_path)
        
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(request.proposed_code)
            
        if request.secret_to_env:
            from src.core.config import ENV_FILE as env_file
            if "=" in request.secret_to_env:
                k, v = request.secret_to_env.split("=", 1)
                os.environ[k.strip()] = v.strip().strip("\"'")
                
            with open(env_file, "a", encoding="utf-8") as f:
                f.write(f"\n{request.secret_to_env.strip()}\n")

        from database import add_to_task_log
        add_to_task_log("heal_file", 1, "success", f"Healed file: {request.file_path}")

        return {"status": "success", "message": f"Successfully applied changes to {request.file_path}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/workflows/list")
async def list_workflows_api():
    """WKF-01: Lists all configured Meridian-X automation workflows."""
    from src.core.workflow_engine import list_workflows
    return {"status": "success", "workflows": list_workflows()}

@router.post("/api/workflows/ai-create")
async def create_ai_workflow_api(payload: AIWorkflowRequest):
    """WKF-01: Generates a Meridian-X workflow DAG automatically from natural language prompt."""
    from src.core.workflow_engine import create_ai_workflow
    wf = create_ai_workflow(payload.goal)
    return {"status": "success", "workflow": wf}

@router.post("/api/workflows/create")
async def create_workflow_api(payload: WorkflowCreateRequest):
    """WKF-01: Creates a new Meridian-X node workflow definition."""
    from src.core.workflow_engine import create_workflow
    wf = create_workflow(payload.name, payload.nodes, payload.edges, payload.active if payload.active is not None else True)
    return {"status": "success", "workflow": wf}

@router.post("/api/workflows/{workflow_id}/execute")
async def execute_workflow_api(workflow_id: str, trigger_payload: Optional[Dict[str, Any]] = None):
    """WKF-01: Triggers manual execution of a workflow DAG graph."""
    from src.core.workflow_engine import execute_workflow
    res = execute_workflow(workflow_id, trigger_payload or {})
    return {"status": "success", "data": res}

@router.post("/api/workflows/webhook/{workflow_id}")
async def handle_workflow_webhook_ingress_api(workflow_id: str, request: Request):
    """WKF-02: External Webhook Ingress Gateway for triggering workflows."""
    from src.core.auth import bootstrap_webhook_secret

    raw_body = await request.body()
    provided = (request.headers.get("X-Webhook-Signature") or "").strip().lower()
    secret = bootstrap_webhook_secret()
    expected = hmac_mod.new(secret.encode("utf-8"), raw_body, hashlib.sha256).hexdigest()
    if not (provided and hmac_mod.compare_digest(provided, expected)):
        try:
            from src.core.audit_logger import log_sensitive_action
            log_sensitive_action("SECURITY_AUDIT", "webhook_signature_rejected", {"workflow_id": workflow_id}, "FAILED")
        except Exception:
            pass
        raise HTTPException(status_code=401, detail="Unauthorized: missing or invalid X-Webhook-Signature.")
    try:
        payload = json.loads(raw_body.decode("utf-8")) if raw_body else {}
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON payload.")
    from src.core.workflow_engine import execute_workflow
    res = execute_workflow(workflow_id, payload)
    return {"status": "success", "ingress": "processed", "data": res}

@router.delete("/api/workflows/{workflow_id}")
async def delete_workflow_api(workflow_id: str):
    """WKF-01: Deletes a workflow by ID."""
    from src.core.workflow_engine import delete_workflow
    deleted = delete_workflow(workflow_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return {"status": "success", "message": f"Workflow '{workflow_id}' deleted."}
