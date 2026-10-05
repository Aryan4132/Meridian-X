import os
import json
import asyncio
from typing import Optional, List
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from src.api.deps import (
    ChatRequest,
    ModelSettings,
    check_shortcut_command,
    sync_model_settings
)
from database import (
    get_user_profile,
    get_ollama_client_host,
    add_to_task_log,
    get_conversation_history,
    clear_conversations
)
from src.core.loop import (
    run_react_agent_loop,
    approve_confirmation
)

router = APIRouter(tags=["chat"])

class ConfirmRequest(BaseModel):
    id: str
    approved: bool

class RollbackRequest(BaseModel):
    checkpoint_id: str

class ExportRequest(BaseModel):
    path: str
    format: Optional[str] = "md"

class UndoReq(BaseModel):
    action_id: Optional[str] = None

@router.post("/api/chat")
async def chat(request: ChatRequest):
    try:
        # Check voice/hotkey shortcuts first
        shortcut = check_shortcut_command(request.prompt)
        if shortcut:
            try:
                from src.voice.wakeword import resume_wakeword
                resume_wakeword()
            except Exception:
                pass
            return shortcut

        try:
            from src.voice.wakeword import pause_wakeword
            pause_wakeword()
        except Exception:
            pass

        # Resolve modelSettings if missing
        modelSettings = request.modelSettings
        if not modelSettings:
            provider = get_user_profile("meridian_provider") or os.environ.get("MERIDIAN_PROVIDER") or "ollama"
            selected_model = get_user_profile("meridian_model") or os.environ.get("MERIDIAN_MODEL") or ""
            model_source = get_user_profile("meridian_model_source") or os.environ.get("MERIDIAN_MODEL_SOURCE") or ("local" if provider == "ollama" else "cloud")
            modelSettings = ModelSettings(
                modelSource=model_source,
                apiProvider=provider,
                selectedModel=selected_model,
                brainModel=selected_model,
                ocrModel=selected_model
            )
        else:
            sync_model_settings(modelSettings)

        model_source = modelSettings.modelSource
        api_provider = modelSettings.apiProvider or get_user_profile("meridian_provider") or "ollama"
        brain_model = (modelSettings.brainModel if model_source == "local" else modelSettings.selectedModel) or modelSettings.brainModel or modelSettings.selectedModel or get_user_profile("meridian_model") or os.environ.get("MERIDIAN_MODEL") or ""
        ollama_host = get_ollama_client_host()

        accumulated_text = ""
        thoughts = []
        async for event_str in run_react_agent_loop(
            request.prompt,
            brain_model,
            ollama_host,
            model_source=model_source,
            api_provider=api_provider
        ):
            for line in event_str.splitlines():
                if line.startswith("data: "):
                    raw_data = line[6:]
                    try:
                        parsed = json.loads(raw_data)
                        if isinstance(parsed, dict):
                            if "text" in parsed and "type" in parsed:
                                thoughts.append(parsed)
                            elif "chat" in parsed:
                                accumulated_text = parsed["chat"]
                    except Exception:
                        if not raw_data.startswith("{"):
                            accumulated_text += raw_data

        try:
            from src.voice.wakeword import resume_wakeword
            resume_wakeword()
        except Exception:
            pass

        return {"text": accumulated_text, "thoughts": thoughts}
    except Exception as e:
        add_to_task_log("ollama_api", 2, "failed", str(e))
        try:
            from src.voice.wakeword import resume_wakeword
            resume_wakeword()
        except Exception:
            pass
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/chat/stream")
def chat_stream(request: ChatRequest):
    shortcut = check_shortcut_command(request.prompt)
    if shortcut:
        async def shortcut_generator():
            import json
            yield f"event: thought\ndata: {json.dumps(shortcut['thoughts'][0])}\n\n"
            text_lines = shortcut['text'].split('\n')
            data_block = '\n'.join(f"data: {line}" for line in text_lines)
            yield f"event: text\n{data_block}\n\n"
            try:
                from src.voice.wakeword import resume_wakeword
                resume_wakeword()
            except Exception:
                pass
        return StreamingResponse(shortcut_generator(), media_type="text/event-stream")

    modelSettings = request.modelSettings
    if not modelSettings:
        provider = get_user_profile("meridian_provider") or os.environ.get("MERIDIAN_PROVIDER") or "ollama"
        selected_model = get_user_profile("meridian_model") or os.environ.get("MERIDIAN_MODEL") or ""
        model_source = get_user_profile("meridian_model_source") or os.environ.get("MERIDIAN_MODEL_SOURCE") or ("local" if provider == "ollama" else "cloud")
        modelSettings = ModelSettings(
            modelSource=model_source,
            apiProvider=provider,
            selectedModel=selected_model,
            brainModel=selected_model,
            ocrModel=selected_model
        )
    else:
        sync_model_settings(modelSettings)

    model_source = modelSettings.modelSource
    api_provider = modelSettings.apiProvider or get_user_profile("meridian_provider") or "ollama"
    brain_model = (modelSettings.brainModel if model_source == "local" else modelSettings.selectedModel) or modelSettings.brainModel or modelSettings.selectedModel or get_user_profile("meridian_model") or os.environ.get("MERIDIAN_MODEL") or ""
    ollama_host = get_ollama_client_host()
    
    if (api_provider or "").lower() == "ollama":
        try:
            from database import get_ollama_client
            from src.core.loop_parser import resolve_local_model_name
            client = get_ollama_client()
            brain_model = resolve_local_model_name(brain_model, client)
        except Exception:
            pass

    try:
        from src.core.proactive import record_user_activity
        record_user_activity()
    except Exception:
        pass

    try:
        from src.voice.wakeword import pause_wakeword
        pause_wakeword()
    except Exception:
        pass

    async def run_react_agent_loop_wrapped(*args, **kwargs):
        from src.core.loop_stream import reset_cancel_flag
        reset_cancel_flag()
        try:
            generator = run_react_agent_loop(*args, **kwargs).__aiter__()
            while True:
                try:
                    event = await asyncio.wait_for(generator.__anext__(), timeout=120.0)
                    yield event
                except StopAsyncIteration:
                    break
                except asyncio.TimeoutError:
                    err_msg = json.dumps({"chat": "\n[Stream Error: LLM response timed out after 120s of inactivity.]\n", "speech": "", "lang": "en"})
                    yield f"event: text\ndata: {err_msg}\n\n"
                    break
        except (Exception, asyncio.CancelledError, GeneratorExit) as e:
            try:
                from src.core.loop import interrupt_agent_loop
                interrupt_agent_loop()
            except Exception:
                pass
            if not isinstance(e, (asyncio.CancelledError, GeneratorExit)):
                err_msg = json.dumps({"chat": f"\n[Stream Error: {str(e)}]\n", "speech": "", "lang": "en"})
                yield f"event: text\ndata: {err_msg}\n\n"
        finally:
            reset_cancel_flag()
            try:
                from src.voice.wakeword import resume_wakeword
                resume_wakeword()
            except Exception:
                pass

    return StreamingResponse(
        run_react_agent_loop_wrapped(
            request.prompt,
            brain_model,
            ollama_host,
            model_source=model_source,
            api_provider=api_provider
        ),
        media_type="text/event-stream"
    )

@router.post("/api/chat/abort")
@router.post("/api/chat/stop")
def chat_abort():
    try:
        from src.core.loop import interrupt_agent_loop
        from src.core.loop_stream import request_stream_cancellation
        request_stream_cancellation("default")
        interrupt_agent_loop()
        return {"status": "success", "message": "Chat execution aborted."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/chat/clear")
def chat_clear():
    from src.core.loop import interrupt_agent_loop
    from src.core.loop_stream import reset_cancel_flag
    interrupt_agent_loop()
    reset_cancel_flag()
    clear_conversations()
    return {"status": "success", "message": "Conversation history cleared."}

@router.get("/api/chat/history")
def chat_history(limit: Optional[int] = 50):
    try:
        history = get_conversation_history(limit=limit or 50)
        formatted_history = []
        for msg in history:
            formatted_history.append({
                "id": msg["id"],
                "sender": msg["role"],
                "text": msg["content"],
                "timestamp": msg["timestamp"]
            })
        return {"history": formatted_history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/chat/confirm")
async def chat_confirm(request: ConfirmRequest):
    if await approve_confirmation(request.id, request.approved):
        return {"status": "success", "message": "Confirmation processed."}
    raise HTTPException(status_code=404, detail="Confirmation ID not found or already processed.")

@router.post("/api/history/rollback")
def rollback_workspace(request: RollbackRequest):
    try:
        from src.core.history_manager import rollback_to_checkpoint
        success = rollback_to_checkpoint(request.checkpoint_id)
        if success:
            return {"status": "success", "message": f"Successfully rolled back to checkpoint '{request.checkpoint_id}'"}
        else:
            raise HTTPException(status_code=400, detail=f"Checkpoint '{request.checkpoint_id}' not found or rollback failed.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/session/export")
def session_export(request: ExportRequest):
    try:
        from src.core.exporter import export_session_runbook
        msg = export_session_runbook(request.path, request.format or "md")
        return {"status": "success", "message": msg}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/action/journal")
def get_action_journal_api(limit: Optional[int] = 20):
    """BUTLER-14: List recent reversible actions in action journal."""
    from src.core.action_journal import global_action_journal
    actions = global_action_journal.get_recent_actions(limit=limit or 20)
    return {"status": "success", "count": len(actions), "actions": actions}

@router.post("/api/action/undo")
def undo_action_api(req: UndoReq):
    """BUTLER-14: Execute inverse handler for last recorded or target action."""
    from src.core.action_journal import global_action_journal
    res = global_action_journal.undo_action(action_id=req.action_id)
    return res
