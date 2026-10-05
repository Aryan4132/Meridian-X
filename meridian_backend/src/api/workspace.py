import os
import time
import json
from typing import Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from database import get_sqlite_conn

router = APIRouter(tags=["workspace"])

class SavePromptRequest(BaseModel):
    name: str
    prompt_text: str
    description: str = ""

class PomodoroRequest(BaseModel):
    work_duration: int = 1500
    break_duration: int = 300

class WriteWorkspaceConfigRequest(BaseModel):
    config: dict

class SetBudgetReq(BaseModel):
    budget_cap_usd: Optional[float] = None
    enabled: Optional[bool] = None

class SetAutonomousReq(BaseModel):
    enabled: bool

class SetSecurityGuardReq(BaseModel):
    level: int

class SetAirGapReq(BaseModel):
    enabled: bool

class GameModeRequest(BaseModel):
    enabled: bool

@router.post("/api/prompts/save")
def api_prompts_save(request: SavePromptRequest):
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO prompt_templates (name, prompt_text, description) VALUES (?, ?, ?)",
            (request.name, request.prompt_text, request.description)
        )
        conn.commit()
        conn.close()
        return {"status": "success", "message": f"Successfully saved prompt template '{request.name}'."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/prompts/load")
def api_prompts_load(name: str):
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT prompt_text, description FROM prompt_templates WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        if not row:
            raise HTTPException(status_code=404, detail=f"Prompt template '{name}' not found.")
        return {"status": "success", "name": name, "prompt_text": row["prompt_text"], "description": row["description"]}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/prompts/list")
def api_prompts_list():
    try:
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT name, description FROM prompt_templates")
        rows = cursor.fetchall()
        conn.close()
        templates = [{"name": r["name"], "description": r["description"]} for r in rows]
        return {"status": "success", "templates": templates}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/pomodoro/start")
def api_pomodoro_start(request: PomodoroRequest):
    try:
        import src.core.proactive as proactive
        proactive.pomodoro_active = True
        proactive.pomodoro_work_duration = request.work_duration
        proactive.pomodoro_break_duration = request.break_duration
        proactive.pomodoro_start_time = time.time()
        proactive.pomodoro_state = "work"
        return {"status": "success", "message": "Pomodoro focus block started."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/pomodoro/stop")
def api_pomodoro_stop():
    try:
        import src.core.proactive as proactive
        proactive.pomodoro_active = False
        proactive.pomodoro_state = "idle"
        return {"status": "success", "message": "Pomodoro focus block stopped."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/pomodoro/status")
def api_pomodoro_status():
    try:
        import src.core.proactive as proactive
        elapsed = time.time() - proactive.pomodoro_start_time if proactive.pomodoro_active else 0
        return {
            "status": "success",
            "active": proactive.pomodoro_active,
            "state": proactive.pomodoro_state,
            "elapsed": int(elapsed),
            "work_duration": proactive.pomodoro_work_duration,
            "break_duration": proactive.pomodoro_break_duration
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/workspace/config")
def api_workspace_config_get():
    try:
        from src.core.mode import load_workspace_config
        return {"status": "success", "config": load_workspace_config()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/workspace/config")
def api_workspace_config_post(request: WriteWorkspaceConfigRequest):
    try:
        from src.core.history_manager import find_workspace_root
        try:
            root = find_workspace_root()
            config_path = os.path.join(root, ".meridian.json")
        except Exception:
            config_path = os.path.join(os.getcwd(), ".meridian.json")
            
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(request.config, f, indent=2)
        return {"status": "success", "message": "Workspace configuration saved successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/mode/autonomous")
def get_autonomous_mode_api():
    from database import get_autonomous_mode
    return {"autonomous_mode": get_autonomous_mode()}

@router.post("/api/mode/autonomous")
def set_autonomous_mode_api(req: SetAutonomousReq):
    from database import set_autonomous_mode, get_autonomous_mode
    set_autonomous_mode(req.enabled)
    return {"autonomous_mode": get_autonomous_mode()}

@router.get("/api/mode/security_guard")
def get_security_guard_api():
    from database import get_security_guard_level, get_unrestricted_pc_access
    level = get_security_guard_level()
    return {
        "level": level,
        "unrestricted": get_unrestricted_pc_access(),
        "mode_label": "Unrestricted PC Access Mode" if level == 0 else "Strict Approval Gates (Level 1)"
    }

@router.post("/api/mode/security_guard")
def set_security_guard_api(req: SetSecurityGuardReq):
    from database import set_security_guard_level, get_security_guard_level, get_unrestricted_pc_access
    set_security_guard_level(req.level)
    level = get_security_guard_level()
    return {
        "level": level,
        "unrestricted": get_unrestricted_pc_access(),
        "mode_label": "Unrestricted PC Access Mode" if level == 0 else "Strict Approval Gates (Level 1)"
    }

@router.get("/api/mode/airgap")
def get_airgap_mode_api():
    from src.core.mode import get_airgap_proof_badge
    return get_airgap_proof_badge()

@router.post("/api/mode/airgap")
def set_airgap_mode_api(req: SetAirGapReq):
    from src.core.mode import set_local_only_mode, get_airgap_proof_badge
    set_local_only_mode(req.enabled)
    return get_airgap_proof_badge()

@router.get("/api/spend/stats")
def get_spend_stats_api():
    from database import get_spend_stats
    return get_spend_stats()

@router.post("/api/spend/budget")
def set_spend_budget_api(req: SetBudgetReq):
    from database import set_budget_cap, set_budget_enabled, get_spend_stats
    if req.budget_cap_usd is not None:
        set_budget_cap(req.budget_cap_usd)
    if req.enabled is not None:
        set_budget_enabled(req.enabled)
    return get_spend_stats()

@router.get("/api/game-mode")
def get_game_mode():
    try:
        from src.core import proactive
        return {"game_mode": proactive.game_mode_active, "auto_game_mode": proactive.auto_game_mode_active}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/game-mode")
def set_game_mode(request: GameModeRequest):
    try:
        from src.core import proactive
        proactive.game_mode_active = request.enabled
        proactive.auto_game_mode_active = False
        
        from src.core.proactive import publish_nudge_sync
        publish_nudge_sync(
            nudge_type="game_mode_changed",
            title="Game Mode Update",
            message="enabled" if request.enabled else "disabled",
            icon="🎮",
            action="game_mode_update"
        )
        return {"status": "success", "game_mode": proactive.game_mode_active}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
