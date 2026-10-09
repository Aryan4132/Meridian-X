import os
import re
import json
import socket
import logging
import asyncio
from typing import Optional, List
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

logger = logging.getLogger("meridian.swarm")

router = APIRouter(tags=["swarm"])

class VerifyPairingRequest(BaseModel):
    secret: str

class LobbyDebateRequest(BaseModel):
    prompt: str

class SwarmAutoFixRequest(BaseModel):
    target_path: Optional[str] = None

class ProactiveNotifyRequest(BaseModel):
    title: str
    message: str
    priority: Optional[str] = "medium"
    category: Optional[str] = "general"
    action_hint: Optional[str] = None
    mascot_state: Optional[str] = "default"

@router.get("/api/swarm/stream")
async def swarm_stream():
    async def event_generator():
        from src.core.bus import event_bus
        queue = event_bus.subscribe("agent_thoughts")
        try:
            while True:
                message = await queue.get()
                yield f"event: message\ndata: {json.dumps(message)}\n\n"
        except (asyncio.CancelledError, GeneratorExit):
            pass
        except Exception as e:
            logger.debug(f"[Swarm Stream] Event generator closed: {e}")
        finally:
            event_bus.unsubscribe("agent_thoughts", queue)
    return StreamingResponse(event_generator(), media_type="text/event-stream")

@router.get("/api/proactive/stream")
async def proactive_stream():
    """SSE endpoint that pushes proactive nudges from background triggers to the frontend."""
    async def event_generator():
        from src.core.bus import event_bus
        queue = event_bus.subscribe("proactive_nudge")
        try:
            while True:
                nudge = await queue.get()
                yield f"event: nudge\ndata: {json.dumps(nudge)}\n\n"
        except (asyncio.CancelledError, GeneratorExit):
            pass
        except Exception as e:
            logger.debug(f"[Proactive Stream] Event generator closed: {e}")
        finally:
            event_bus.unsubscribe("proactive_nudge", queue)
    return StreamingResponse(event_generator(), media_type="text/event-stream")

@router.get("/api/p2p/status")
def get_p2p_status():
    from src.core.p2p import p2p_node, _server_running
    return {
        "active": _server_running,
        "host": p2p_node.host,
        "port": p2p_node.port,
        "peers_count": len(p2p_node.peers),
        "peers": [f"{ip}:{port}" for ip, port in p2p_node.peers],
        "secret_token_configured": bool(os.environ.get("P2P_SECRET_TOKEN"))
    }

@router.post("/api/p2p/sync")
def post_p2p_sync():
    from src.core.p2p import p2p_node, _server_running
    if not _server_running:
        raise HTTPException(status_code=400, detail="P2P Sync server is not active.")
    try:
        log = p2p_node.sync_now()
        return {"status": "success", "log": log}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/p2p/toggle")
def post_p2p_toggle():
    from src.core.p2p import p2p_node, _server_running
    try:
        if _server_running:
            msg = p2p_node.stop()
            active = False
        else:
            msg = p2p_node.start()
            active = True
        return {"status": "success", "message": msg, "active": active}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/p2p/pairing-info")
def get_p2p_pairing_info():
    host_ip = "127.0.0.1"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        host_ip = s.getsockname()[0]
        s.close()
    except Exception:
        pass
    try:
        from src.core.p2p import P2P_PORT
        port = P2P_PORT
    except Exception:
        port = 4133
    return {"status": "success", "host": host_ip, "port": port}

@router.post("/api/p2p/verify-pairing")
def post_verify_pairing(req: VerifyPairingRequest):
    from src.core.p2p import verify_mobile_pairing_secret
    paired = verify_mobile_pairing_secret(req.secret)
    if paired:
        return {"status": "success", "authenticated": True, "message": "Mobile client successfully paired."}
    else:
        raise HTTPException(status_code=401, detail="Invalid pairing secret token.")

@router.post("/api/lobby/debate")
async def lobby_debate(request: LobbyDebateRequest):
    try:
        from database import get_brain_model, get_user_profile
        provider = get_user_profile("meridian_provider") or os.environ.get("MERIDIAN_PROVIDER", "ollama")
        model = get_brain_model()

        async def get_completion(prompt_text: str) -> str:
            from src.core.llm_provider import generate_completion_stream
            parts = []
            async for chunk in generate_completion_stream([{"role": "user", "content": prompt_text}], provider, model):
                if chunk.startswith("Error:"):
                    raise Exception(chunk)
                stripped = chunk.strip()
                if stripped.startswith("[System Warning:") or stripped.startswith("[System Error:"):
                    continue
                parts.append(chunk)
            return "".join(parts).strip()
        
        coder_prompt = (
            f"You are the Coder agent in a developer sandbox. Your task is to write a clean, efficient "
            f"implementation for the following user request:\n"
            f"Request: {request.prompt}\n\n"
            f"Output your implementation along with a brief description of your strategy. Do not wrap the final code yet."
        )
        coder_msg = await get_completion(coder_prompt)
        
        qa_prompt = (
            f"You are the QA Tester agent in the developer sandbox. Review the Coder's implementation below "
            f"for the user request: '{request.prompt}'.\n\n"
            f"Coder's response:\n{coder_msg}\n\n"
            f"Point out potential bugs, edge cases, incorrect assumptions, or performance issues in their code. Suggest fixes."
        )
        qa_msg = await get_completion(qa_prompt)
        
        auditor_prompt = (
            f"You are the Security & Performance Auditor agent in the developer sandbox. Review the Coder's "
            f"implementation and QA's critique below.\n\n"
            f"Coder's response:\n{coder_msg}\n\n"
            f"QA's critique:\n{qa_msg}\n\n"
            f"Analyze security vulnerabilities (e.g. SQL injection, path traversal, buffer overflows), resource efficiency, "
            f"and overall readability. Propose optimizations."
        )
        auditor_msg = await get_completion(auditor_prompt)
        
        final_prompt = (
            f"You are the Coder agent. Incorporate all feedback from the QA Tester and Auditor to "
            f"provide a final, production-ready, highly secure, and optimized code implementation for the request: '{request.prompt}'.\n\n"
            f"History:\n"
            f"- Coder Draft: {coder_msg}\n"
            f"- QA Feedback: {qa_msg}\n"
            f"- Auditor Security Review: {auditor_msg}\n\n"
            f"Provide your final explanation of the changes made, followed by the complete code block wrapped in standard markdown code fences (e.g. ```python ... ```)."
        )
        final_msg = await get_completion(final_prompt)
        
        proposed_code = ""
        code_block_match = re.findall(r'```(?:python|javascript|typescript|json|html|css|bash|powershell|sql|rs|cpp|c)?\n(.*?)```', final_msg, re.DOTALL)
        if code_block_match:
            proposed_code = code_block_match[-1].strip()
        else:
            proposed_code = final_msg
            
        debate_logs = [
            f"Coder: {coder_msg}",
            f"QA Tester: {qa_msg}",
            f"Auditor: {auditor_msg}",
            f"Coder (Final): {final_msg}"
        ]
        decision = f"Consensus reached. Proposed code:\n{proposed_code}" if proposed_code else final_msg

        return {
            "status": "success",
            "debate": [
                {"agent": "Coder", "avatar": "👨‍💻", "message": coder_msg},
                {"agent": "QA Tester", "avatar": "🧪", "message": qa_msg},
                {"agent": "Auditor", "avatar": "🔍", "message": auditor_msg},
                {"agent": "Coder (Final)", "avatar": "🚀", "message": final_msg}
            ],
            "debate_logs": debate_logs,
            "decision": decision,
            "proposed_code": proposed_code
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lobby debate failed: {str(e)}")

@router.post("/api/swarm/auto-fix")
async def api_swarm_auto_fix(req: Optional[SwarmAutoFixRequest] = None):
    """DEV-01: Triggers Autonomous Background Bug Fixer & Auto-PR Agent."""
    try:
        from src.core.swarm import AutonomousBugFixer
        fixer = AutonomousBugFixer()
        target = req.target_path if req else None
        res = await fixer.auto_fix_pipeline(target_path=target)
        return {
            "status": "success",
            "data": res
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Swarm auto-fix execution failed: {e}")

@router.post("/api/proactive/notify")
async def api_trigger_proactive_notification(payload: ProactiveNotifyRequest):
    """PL-28: Multi-Channel Proactive Event & Notification Dispatcher endpoint."""
    try:
        from src.core.proactive import dispatch_notification
        res = dispatch_notification(
            title=payload.title,
            message=payload.message,
            priority=payload.priority or "medium",
            category=payload.category or "general",
            action_hint=payload.action_hint,
            mascot_state=payload.mascot_state or "default"
        )
        return {"status": "success", "data": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to dispatch proactive notification: {e}")
