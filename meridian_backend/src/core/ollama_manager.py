import os
import sys
import logging
import asyncio
import httpx
from typing import Dict, Any, List, AsyncGenerator, Optional

logger = logging.getLogger(__name__)

DEFAULT_PORTS = [11434, 11435, 8080, 5000]

def get_ollama_base_url() -> str:
    env_host = os.getenv("OLLAMA_HOST", "").strip()
    if env_host:
        if not env_host.startswith("http://") and not env_host.startswith("https://"):
            return f"http://{env_host}"
        return env_host
    return "http://127.0.0.1:11434"

async def detect_ollama() -> Dict[str, Any]:
    """Detect if Ollama service is running on default or alternative ports."""
    configured_url = get_ollama_base_url()
    candidate_urls = [configured_url] + [f"http://127.0.0.1:{port}" for port in DEFAULT_PORTS if f"http://127.0.0.1:{port}" != configured_url]

    async with httpx.AsyncClient(timeout=1.5) as client:
        for url in candidate_urls:
            try:
                res = await client.get(f"{url}/api/tags")
                if res.status_code == 200:
                    data = res.json()
                    models = [m.get("name") for m in data.get("models", [])]
                    return {
                        "installed": True,
                        "running": True,
                        "base_url": url,
                        "models": models,
                        "detected_port": url.split(":")[-1]
                    }
            except Exception:
                continue

    # Ollama not responding on HTTP. Check if binary is in PATH
    binary_found = False
    for path_dir in os.environ.get("PATH", "").split(os.pathsep):
        exe_path = os.path.join(path_dir, "ollama.exe" if sys.platform == "win32" else "ollama")
        if os.path.isfile(exe_path) and os.access(exe_path, os.X_OK):
            binary_found = True
            break

    return {
        "installed": binary_found,
        "running": False,
        "base_url": configured_url,
        "models": [],
        "detected_port": None
    }

async def stream_pull_model(model_name: str, base_url: Optional[str] = None) -> AsyncGenerator[Dict[str, Any], None]:
    """Stream model download progress from Ollama service."""
    if not base_url:
        base_url = get_ollama_base_url()

    pull_url = f"{base_url}/api/pull"
    payload = {"name": model_name, "stream": True}

    async with httpx.AsyncClient(timeout=None) as client:
        try:
            async with client.stream("POST", pull_url, json=payload) as response:
                if response.status_code != 200:
                    yield {"status": "error", "message": f"Ollama returned HTTP {response.status_code}"}
                    return

                async for line in response.aiter_lines():
                    if not line:
                        continue
                    try:
                        import json
                        chunk = json.loads(line)
                        completed = chunk.get("completed", 0)
                        total = chunk.get("total", 0)
                        percent = round((completed / total) * 100, 1) if total > 0 else 0
                        status_text = chunk.get("status", "Downloading...")
                        yield {
                            "status": status_text,
                            "completed": completed,
                            "total": total,
                            "percentage": percent,
                            "done": chunk.get("status") == "success"
                        }
                    except Exception:
                        yield {"status": line, "percentage": 0, "done": False}
        except Exception as e:
            logger.error(f"Error streaming model pull: {e}")
            yield {"status": "error", "message": str(e), "percentage": 0, "done": False}
