import os
import signal
import platform
import shutil
import psutil
from typing import Optional, Dict, Any, List
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from src.api.deps import limiter
from src.core.response_models import HealthResponse, DiagnosticsResponse
from src.core.hardware_detector import detect_hardware_specs
from src.core.ollama_manager import detect_ollama, stream_pull_model
from database import get_ollama_client_host

router = APIRouter(tags=["system"])

CURRENT_VERSION = "0.1.5"
_auto_download_in_progress = False
_auto_download_ready = False

class DebugLog(BaseModel):
    message: str = Field(..., max_length=5000)
    level: str = Field("error", max_length=20)

class PullModelRequest(BaseModel):
    model_name: str
    base_url: Optional[str] = None

class PowerSaveRequest(BaseModel):
    active: bool

class StartupRequest(BaseModel):
    enabled: bool

class KillProcessPayload(BaseModel):
    pid: int

class AutoHealPayload(BaseModel):
    kill_rogue_processes: bool = False

def _parse_version(v_str: str) -> tuple:
    try:
        clean = v_str.lstrip("v").strip()
        parts = [int(p) for p in clean.split(".") if p.isdigit()]
        while len(parts) < 3:
            parts.append(0)
        return tuple(parts[:3])
    except Exception:
        return (0, 0, 0)

def _determine_update_type(current_str: str, remote_str: str) -> str:
    c_maj, c_min, c_pat = _parse_version(current_str)
    r_maj, r_min, r_pat = _parse_version(remote_str)
    if (r_maj, r_min, r_pat) <= (c_maj, c_min, c_pat):
        return "none"
    if r_maj > c_maj:
        return "major"
    if r_min > c_min:
        return "minor"
    return "patch"

async def _async_bg_git_pull():
    global _auto_download_in_progress, _auto_download_ready
    try:
        import asyncio
        import subprocess
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        repo_root = os.path.abspath(os.path.join(root_dir, ".."))
        if not os.path.exists(os.path.join(repo_root, ".git")) and not os.path.exists(os.path.join(root_dir, ".git")):
            _auto_download_in_progress = False
            return
        
        proc = await asyncio.create_subprocess_exec(
            "git", "pull", "origin", "main",
            cwd=repo_root if os.path.exists(os.path.join(repo_root, ".git")) else root_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        await proc.communicate()
        _auto_download_ready = True
    except Exception as e:
        print("[Auto-Update] Background git pull failed:", e)
    finally:
        _auto_download_in_progress = False

def check_startup_enabled():
    appdata = os.environ.get("APPDATA", "")
    if not appdata:
        return False
    startup_dir = os.path.join(appdata, r"Microsoft\Windows\Start Menu\Programs\Startup")
    vbs_path = os.path.join(startup_dir, "MeridianStartup.vbs")
    lnk_path = os.path.join(startup_dir, "Meridian.lnk")
    return os.path.exists(vbs_path) or os.path.exists(lnk_path)

@router.get("/api/version")
async def get_api_version():
    return {
        "version": "1.0.0",
        "status": "stable",
        "release_date": "2026-09-18",
        "description": "Meridian-X Backend API"
    }

@router.post("/api/debug/log")
def post_debug_log(log: DebugLog):
    print(f"[FRONTEND DEBUG {log.level.upper()}] {log.message}")
    return {"status": "logged"}

@router.get("/api/onboarding/hardware-spec")
def get_hardware_spec():
    return detect_hardware_specs()

@router.get("/api/onboarding/ollama-status")
async def get_ollama_status():
    return await detect_ollama()

@router.post("/api/onboarding/models/pull")
async def pull_model_endpoint(req: PullModelRequest):
    async def sse_event_generator():
        async for chunk in stream_pull_model(req.model_name, req.base_url):
            yield f"data: {json.dumps(chunk)}\n\n"
    return StreamingResponse(sse_event_generator(), media_type="text/event-stream")

@router.post("/api/system/shutdown")
@limiter.limit("5/minute")
def post_system_shutdown(request: Request):
    try:
        from src.core.audit_logger import log_sensitive_action
        log_sensitive_action("SHUTDOWN", "post_system_shutdown", {"ip": request.client.host if request.client else "unknown"}, "SUCCESS")
    except Exception:
        pass
    os.kill(os.getpid(), signal.SIGTERM)
    return {"status": "success", "message": "Graceful shutdown initiated."}

@router.get("/api/health", response_model=HealthResponse)
@limiter.limit("10/minute")
def api_health(request: Request):
    health_status = {
        "status": "healthy",
        "sqlite": "online",
        "mongodb": "online",
        "ollama": "online",
        "details": {}
    }
    
    conn = None
    try:
        from database import get_sqlite_conn
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
    except Exception as e:
        health_status["sqlite"] = f"offline: {e}"
        health_status["status"] = "degraded"
    finally:
        if conn:
            conn.close()
        
    try:
        from database import get_mongo_db
        db_conn = get_mongo_db()
        if db_conn is None:
            health_status["mongodb"] = "offline"
        else:
            health_status["mongodb"] = "online"
    except Exception as e:
        health_status["mongodb"] = f"offline: {e}"
        health_status["status"] = "degraded"
        
    try:
        import httpx
        host = get_ollama_client_host()
        res = httpx.get(f"{host}/api/tags", timeout=2.0)
        if res.status_code == 200:
            models = [m["name"] for m in res.json().get("models", [])]
            health_status["ollama"] = "online"
            health_status["details"]["ollama_models"] = models
        else:
            health_status["ollama"] = f"degraded (HTTP {res.status_code})"
            health_status["status"] = "degraded"
    except Exception as e:
        health_status["ollama"] = f"offline: {e}"
        health_status["status"] = "degraded"
        
    try:
        cpu_percent = psutil.cpu_percent(interval=0.1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        health_status["details"]["system"] = {
            "cpu_percent": cpu_percent,
            "memory_percent": memory.percent,
            "disk_percent": (disk.used / disk.total) * 100
        }
        if cpu_percent > 95 or memory.percent > 95 or (disk.used / disk.total) > 0.95:
            health_status["status"] = "degraded"
    except Exception as e:
        health_status["details"]["system"] = {"error": str(e)}
        
    try:
        from src.core.mcp_client import mcp_manager
        health_status["details"]["mcp"] = {
            "initialized": hasattr(mcp_manager, 'sessions') and len(getattr(mcp_manager, 'sessions', {})) > 0
        }
    except Exception as e:
        health_status["details"]["mcp"] = {"error": str(e)}
        
    return health_status

@router.get("/api/diagnostics", response_model=DiagnosticsResponse)
@limiter.limit("5/minute")
def api_diagnostics(request: Request):
    try:
        cpu = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory().percent
        total_disk, used_disk, free_disk = shutil.disk_usage(os.getcwd())
        
        from database import SQLITE_DB_PATH
        sqlite_size = os.path.getsize(SQLITE_DB_PATH) if os.path.exists(SQLITE_DB_PATH) else 0
        
        log_lines = []
        from src.core.audit_logger import get_audit_log_path
        audit_path = get_audit_log_path()
        log_path = os.path.join(os.path.dirname(audit_path), "meridian.log")
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
                log_lines = f.readlines()[-50:]
                
        audit_lines = []
        if os.path.exists(audit_path):
            with open(audit_path, "r", encoding="utf-8", errors="ignore") as f:
                audit_lines = f.readlines()[-10:]
                
        parsed_audits = []
        for line in audit_lines:
            try:
                parsed_audits.append(json.loads(line))
            except Exception:
                parsed_audits.append({"raw": line})
                
        env_keys = ["MONGODB_URI", "OLLAMA_HOST", "OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GEMINI_API_KEY", "DEEPSEEK_API_KEY"]
        env_summary = {}
        for k in env_keys:
            val = os.environ.get(k)
            if val:
                env_summary[k] = f"configured (length={len(val)})" if "KEY" in k else val
            else:
                env_summary[k] = "not set"

        return {
            "status": "success",
            "system": {
                "os": platform.system(),
                "os_release": platform.release(),
                "cpu_percent": cpu,
                "ram_percent": ram,
                "disk_free_gb": round(free_disk / (1024**3), 2),
                "disk_total_gb": round(total_disk / (1024**3), 2)
            },
            "databases": {
                "sqlite_size_kb": round(sqlite_size / 1024, 2),
                "sqlite_path": SQLITE_DB_PATH
            },
            "environment": env_summary,
            "recent_logs": [line.strip() for line in log_lines],
            "recent_audit_logs": parsed_audits
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch diagnostics: {e}")

@router.get("/api/system-usage")
def get_system_usage():
    try:
        cpu = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory().percent
        return {"cpu": cpu, "ram": ram}
    except Exception:
        import random
        return {
            "cpu": round(random.uniform(10, 80), 1),
            "ram": round(random.uniform(40, 70), 1)
        }

@router.post("/api/system/power-save")
def toggle_power_save(request: PowerSaveRequest):
    try:
        if request.active:
            from database import get_auditor_model
            auditor_model = get_auditor_model()
            os.environ["MERIDIAN_MODEL"] = auditor_model
            os.environ["MERIDIAN_AUDITOR_MODEL"] = auditor_model
            return {"status": "success", "message": "Power-Saving Mode activated. Using lightweight fallback model."}
        else:
            from database import get_user_profile
            default_model = get_user_profile("meridian_model") or os.environ.get("MERIDIAN_MODEL", "")
            os.environ["MERIDIAN_MODEL"] = default_model
            auditor_model = get_user_profile("meridian_auditor_model") or os.environ.get("MERIDIAN_AUDITOR_MODEL", "")
            os.environ["MERIDIAN_AUDITOR_MODEL"] = auditor_model
            return {"status": "success", "message": f"Power-Saving Mode deactivated. Restored model {default_model}."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/system/startup")
def get_startup_status():
    try:
        return {"enabled": check_startup_enabled()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/system/startup")
def toggle_startup_status(request: StartupRequest):
    try:
        import sys
        import subprocess
        project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        script_path = os.path.join(project_dir, "setup_startup.py")
        python_exe = sys.executable or "python"
        args = [python_exe, script_path]
        if not request.enabled:
            args.append("--disable")
            
        res = subprocess.run(args, capture_output=True, text=True)
        if res.returncode != 0:
            raise Exception(res.stderr or res.stdout)
            
        return {"status": "success", "enabled": check_startup_enabled(), "output": res.stdout}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/system/check-update")
async def api_check_update():
    global _auto_download_in_progress, _auto_download_ready
    try:
        import httpx
        url = "https://api.github.com/repos/Aryan4132/Meridian-X/releases/latest"
        headers = {"User-Agent": "Meridian-X-Agent"}
        async with httpx.AsyncClient(timeout=6.0) as client:
            resp = await client.get(url, headers=headers)
            
        if resp.status_code == 200:
            data = resp.json()
            remote_tag = data.get("tag_name", CURRENT_VERSION)
            version_on_github = remote_tag.lstrip("v")
            update_type = _determine_update_type(CURRENT_VERSION, version_on_github)
            update_available = update_type != "none"
            release_url = data.get("html_url", "https://github.com/Aryan4132/Meridian-X/releases")
            release_notes = data.get("body", "")
            published_at = data.get("published_at", "")

            if update_type in ["patch", "minor"] and not _auto_download_ready and not _auto_download_in_progress:
                import asyncio
                _auto_download_in_progress = True
                asyncio.create_task(_async_bg_git_pull())

            return {
                "status": "success",
                "current_version": CURRENT_VERSION,
                "version_on_github": version_on_github,
                "update_available": update_available,
                "update_type": update_type,
                "auto_downloaded": _auto_download_ready,
                "auto_downloading": _auto_download_in_progress,
                "release_url": release_url,
                "release_notes": release_notes,
                "published_at": published_at
            }
        else:
            return {
                "status": "offline",
                "current_version": CURRENT_VERSION,
                "version_on_github": CURRENT_VERSION,
                "update_available": False,
                "update_type": "none",
                "message": f"Offline mode / Standalone package (GitHub API returned HTTP {resp.status_code})"
            }
    except Exception:
        return {
            "status": "offline",
            "current_version": CURRENT_VERSION,
            "version_on_github": CURRENT_VERSION,
            "update_available": False,
            "update_type": "none",
            "message": f"Offline mode / Standalone package — running local release v{CURRENT_VERSION}"
        }

@router.post("/api/system/trigger-update")
def api_trigger_update():
    try:
        import subprocess
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        repo_root = os.path.abspath(os.path.join(root_dir, ".."))
        target_dir = repo_root if os.path.exists(os.path.join(repo_root, ".git")) else root_dir
        
        if not os.path.exists(os.path.join(target_dir, ".git")):
            return {"status": "error", "message": "Git repository not found for in-place update."}
        res = subprocess.run(["git", "pull", "origin", "main"], cwd=target_dir, capture_output=True, text=True)
        return {"status": "success", "output": res.stdout, "errors": res.stderr}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/update/check")
def check_update_api():
    """OPS-01: Check GitHub releases API for newer Meridian-X version."""
    from src.core.updater import SystemUpdater
    updater = SystemUpdater()
    return updater.check_for_updates()

@router.get("/api/guard/resources")
async def get_system_guard_resources():
    from src.core.proactive_system_guard import system_guard
    return system_guard.check_system_resources()

@router.post("/api/guard/kill-process")
async def kill_system_process(payload: KillProcessPayload):
    from src.core.proactive_system_guard import system_guard
    return system_guard.kill_process(payload.pid)

@router.post("/api/guard/auto-heal")
async def auto_heal_system_resources(payload: AutoHealPayload):
    from src.core.proactive_system_guard import system_guard
    return system_guard.auto_heal_anomalies(kill_rogue_processes=payload.kill_rogue_processes)

@router.get("/api/cache/stats")
def get_cache_stats():
    try:
        from database import get_cache_statistics
        stats = get_cache_statistics()
        return {
            "status": "success",
            "cache_statistics": stats
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
