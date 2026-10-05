import os
import json
import urllib.request
from typing import Optional, List
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from database import get_user_profile, save_user_profile, get_ollama_client_host
from src.core.local_model_manager import local_model_manager, LocalModelConfig, QUANTIZATION_PRESETS
from src.core.agent_status_stream import agent_status_stream_manager

router = APIRouter(tags=["models"])

class OllamaModelRequest(BaseModel):
    name: str

class PullModelPayload(BaseModel):
    model_name: str
    quantization: Optional[str] = None

class EstimateResourcePayload(BaseModel):
    param_count_billion: float = 8.0
    quantization: str = "Q4_K_M"

class CustomLLMConfigRequest(BaseModel):
    base_url: str
    api_key: Optional[str] = ""
    model: Optional[str] = "custom-model"

@router.get("/api/ollama-models")
def get_ollama_models(host: Optional[str] = None):
    models = []
    if host:
        if host == "0.0.0.0":
            ollama_host = "http://127.0.0.1:11434"
        elif host.startswith("0.0.0.0:"):
            ollama_host = f"http://127.0.0.1:{host.split(':')[1]}"
        elif "0.0.0.0" in host:
            ollama_host = host.replace("0.0.0.0", "127.0.0.1")
        elif not host.startswith("http://") and not host.startswith("https://"):
            ollama_host = f"http://{host}"
        else:
            ollama_host = host
    else:
        ollama_host = get_ollama_client_host()

    try:
        import ollama
        client = ollama.Client(host=ollama_host)
        res = client.list()
        if hasattr(res, 'models'):
            for m in res.models:
                models.append(m.model)
        elif isinstance(res, dict):
            for m in res.get("models", []):
                models.append(m.get("name", m.get("model")))
        else:
            try:
                for m in res:
                    if hasattr(m, 'model'):
                        models.append(m.model)
                    elif isinstance(m, dict):
                        models.append(m.get("model"))
            except Exception:
                pass
        if models:
            return {"models": list(set(models))}
    except Exception:
        pass

    try:
        url = f"{ollama_host.rstrip('/')}/api/tags"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=2.0) as response:
            data = json.loads(response.read().decode('utf-8'))
            for m in data.get("models", []):
                models.append(m.get("name", m.get("model")))
            if models:
                return {"models": list(set(models))}
    except Exception:
        pass

    return {"models": []}

@router.get("/api/provider-models")
async def get_provider_models(provider: str, host: Optional[str] = None, api_key: Optional[str] = None):
    provider = provider.lower()
    
    if provider == "ollama":
        res = get_ollama_models(host=host)
        return res
        
    if provider == "openai":
        try:
            import httpx
            key = api_key or os.environ.get("OPENAI_API_KEY")
            if not key:
                return {"models": []}
            async with httpx.AsyncClient(timeout=4.0) as client:
                resp = await client.get("https://api.openai.com/v1/models", headers={"Authorization": f"Bearer {key}"})
                if resp.status_code == 200:
                    data = resp.json()
                    models = [m["id"] for m in data.get("data", []) if "gpt" in m["id"].lower()]
                    return {"models": sorted(models)}
        except Exception:
            pass
        return {"models": ["gpt-4o", "gpt-4o-mini", "o1", "o3-mini"]}

    if provider == "anthropic":
        return {"models": ["claude-3-7-sonnet-20250219", "claude-3-5-sonnet-20241022", "claude-3-5-haiku-20241022", "claude-3-opus-20240229"]}

    if provider == "gemini":
        try:
            import httpx
            key = api_key or os.environ.get("GEMINI_API_KEY")
            if not key:
                return {"models": []}
            async with httpx.AsyncClient(timeout=4.0) as client:
                resp = await client.get(f"https://generativelanguage.googleapis.com/v1beta/models?key={key}")
                if resp.status_code == 200:
                    data = resp.json()
                    models = [m["name"].replace("models/", "") for m in data.get("models", []) if "generateContent" in m.get("supportedGenerationMethods", [])]
                    return {"models": sorted(models)}
        except Exception:
            pass
        return {"models": ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-2.0-flash", "gemini-1.5-pro"]}

    if provider == "deepseek":
        return {"models": ["deepseek-chat", "deepseek-reasoner"]}

    if provider == "groq":
        try:
            import httpx
            key = api_key or os.environ.get("GROQ_API_KEY")
            if not key:
                return {"models": []}
            async with httpx.AsyncClient(timeout=4.0) as client:
                resp = await client.get("https://api.groq.com/openai/v1/models", headers={"Authorization": f"Bearer {key}"})
                if resp.status_code == 200:
                    data = resp.json()
                    models = [m["id"] for m in data.get("data", [])]
                    return {"models": sorted(models)}
        except Exception:
            pass
        return {"models": ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "deepseek-r1-distill-llama-70b"]}

    if provider == "openrouter":
        try:
            import httpx
            async with httpx.AsyncClient(timeout=4.0) as client:
                resp = await client.get("https://openrouter.ai/api/v1/models")
                if resp.status_code == 200:
                    data = resp.json()
                    models = [m["id"] for m in data.get("data", [])]
                    return {"models": sorted(models[:50])}
        except Exception:
            pass

    return {"models": []}

@router.post("/api/ollama/pull")
def api_ollama_pull(request: OllamaModelRequest):
    try:
        from src.tools.ollama_manager import ollama_pull_model
        res = ollama_pull_model(request.name)
        return {"status": "success", "message": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/ollama/delete")
def api_ollama_delete(request: OllamaModelRequest):
    try:
        from src.tools.ollama_manager import ollama_delete_model
        res = ollama_delete_model(request.name)
        return {"status": "success", "message": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/ollama/pull/status")
def api_ollama_pull_status(name: str):
    try:
        from src.tools.ollama_manager import pull_status
        status = pull_status.get(name, "unknown")
        return {"status": "success", "model": name, "pull_status": status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/models/local")
async def get_local_models():
    """List installed local models, quantization levels, and status."""
    return await local_model_manager.list_models()

@router.get("/api/models/quantization-options")
async def get_quantization_options():
    """Return available quantization profiles and specs."""
    return {
        "presets": list(QUANTIZATION_PRESETS.values())
    }

@router.post("/api/models/local/pull")
async def pull_local_model(payload: PullModelPayload):
    """Stream model download progress with quantization tag."""
    async def event_generator():
        async for progress in local_model_manager.pull_model_stream(payload.model_name, payload.quantization):
            yield json.dumps(progress) + "\n"
    return StreamingResponse(event_generator(), media_type="application/x-ndjson")

@router.delete("/api/models/local/{model_name:path}")
async def delete_local_model(model_name: str):
    """Delete local model."""
    success = await local_model_manager.delete_model(model_name)
    if not success:
        raise HTTPException(status_code=400, detail=f"Failed to delete model {model_name}")
    return {"status": "deleted", "model": model_name}

@router.post("/api/models/local/active")
async def set_active_local_model(config: LocalModelConfig):
    """Set active local model and runtime parameters."""
    updated = local_model_manager.set_active_config(config)
    agent_status_stream_manager.broadcast_event(
        status="idle",
        message=f"Active local model changed to {config.model_name} ({config.quantization})",
        details={"config": config.model_dump()}
    )
    return {"status": "active_updated", "config": updated.model_dump()}

@router.post("/api/models/estimate-resources")
async def estimate_model_resources(payload: EstimateResourcePayload):
    """Estimate RAM and VRAM footprint for parameter count and quantization profile."""
    return local_model_manager.estimate_resource_requirements(payload.param_count_billion, payload.quantization)

@router.get("/api/llm/providers/custom")
async def get_custom_llm_config_api():
    """Returns configured custom AI model endpoint settings."""
    return {
        "status": "success",
        "base_url": get_user_profile("custom_llm_base_url") or os.getenv("CUSTOM_LLM_BASE_URL") or "http://localhost:8000/v1",
        "model": get_user_profile("custom_llm_model") or os.getenv("CUSTOM_LLM_MODEL") or "custom-model",
        "api_key_configured": bool(get_user_profile("custom_llm_api_key") or os.getenv("CUSTOM_LLM_API_KEY"))
    }

@router.post("/api/llm/providers/custom")
async def save_custom_llm_config_api(payload: CustomLLMConfigRequest):
    """Saves user custom AI model endpoint (llama.cpp, LocalAI, vLLM, HuggingFace, LM Studio)."""
    save_user_profile("custom_llm_base_url", payload.base_url)
    if payload.model:
        save_user_profile("custom_llm_model", payload.model)
    if payload.api_key:
        save_user_profile("custom_llm_api_key", payload.api_key)
        
    return {
        "status": "success",
        "message": "Custom AI model provider endpoint saved successfully.",
        "base_url": payload.base_url,
        "model": payload.model
    }
