import os
import sys
import logging
import asyncio
import httpx
from typing import Dict, Any, List, AsyncGenerator, Optional
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

QUANTIZATION_PRESETS: Dict[str, Dict[str, Any]] = {
    "Q4_K_M": {
        "name": "Q4_K_M",
        "description": "4-bit quantization with medium precision (Recommended balanced option)",
        "bits_per_weight": 4.5,
        "quality_loss": "Very Low",
        "speed_rating": "Fast",
        "recommended": True
    },
    "Q4_0": {
        "name": "Q4_0",
        "description": "Legacy 4-bit quantization, lightweight memory footprint",
        "bits_per_weight": 4.0,
        "quality_loss": "Low",
        "speed_rating": "Very Fast",
        "recommended": False
    },
    "Q5_K_M": {
        "name": "Q5_K_M",
        "description": "5-bit quantization for higher reasoning accuracy",
        "bits_per_weight": 5.5,
        "quality_loss": "Negligible",
        "speed_rating": "Moderate",
        "recommended": False
    },
    "Q8_0": {
        "name": "Q8_0",
        "description": "8-bit quantization near FP16 accuracy",
        "bits_per_weight": 8.5,
        "quality_loss": "None",
        "speed_rating": "Standard",
        "recommended": False
    },
    "F16": {
        "name": "F16",
        "description": "16-bit Floating Point full precision",
        "bits_per_weight": 16.0,
        "quality_loss": "Zero",
        "speed_rating": "Slow",
        "recommended": False
    }
}

class LocalModelConfig(BaseModel):
    model_name: str
    quantization: str = "Q4_K_M"
    context_window: int = 4096
    num_gpu_layers: int = -1
    temperature: float = 0.7

class LocalModelManager:
    """Manages local model discovery, quantization profiling, VRAM estimation, model pulling, and active settings."""

    def __init__(self, ollama_base_url: Optional[str] = None):
        self.ollama_base_url = ollama_base_url or os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
        if not self.ollama_base_url.startswith("http://") and not self.ollama_base_url.startswith("https://"):
            self.ollama_base_url = f"http://{self.ollama_base_url}"
        from database import get_brain_model
        self.active_config: LocalModelConfig = LocalModelConfig(model_name=get_brain_model())

    def estimate_resource_requirements(self, param_count_b: float, quant_name: str) -> Dict[str, Any]:
        """Estimate VRAM/RAM required for model given parameter count (in Billions) and quantization level."""
        preset = QUANTIZATION_PRESETS.get(quant_name.upper(), QUANTIZATION_PRESETS["Q4_K_M"])
        bpw = preset["bits_per_weight"]
        
        # Base weight memory in GB: (params * bits_per_weight) / 8
        weight_memory_gb = (param_count_b * bpw) / 8.0
        # Add 20% overhead for context activation tensors and KV cache (4K context default)
        kv_cache_overhead_gb = 1.2
        total_vram_required = round(weight_memory_gb + kv_cache_overhead_gb, 2)
        total_ram_required = round(total_vram_required * 1.25, 2)

        return {
            "parameter_count_billion": param_count_b,
            "quantization": quant_name,
            "weight_size_gb": round(weight_memory_gb, 2),
            "estimated_vram_gb": total_vram_required,
            "estimated_ram_gb": total_ram_required,
            "recommended_gpu_layers": -1 if total_vram_required <= 8.0 else 24
        }

    async def list_models(self) -> Dict[str, Any]:
        """Fetch list of local models with quantization & resource metadata."""
        models: List[Dict[str, Any]] = []
        status = "offline"

        try:
            async with httpx.AsyncClient(timeout=2.0) as client:
                res = await client.get(f"{self.ollama_base_url}/api/tags")
                if res.status_code == 200:
                    status = "online"
                    raw_data = res.json()
                    for m in raw_data.get("models", []):
                        name = m.get("name", "unknown")
                        size_bytes = m.get("size", 0)
                        size_gb = round(size_bytes / (1024 ** 3), 2)
                        details = m.get("details", {})
                        quant = details.get("quantization_level", "Q4_K_M")
                        param_size = details.get("parameter_size", "8B")

                        models.append({
                            "name": name,
                            "size_gb": size_gb,
                            "quantization": quant,
                            "parameter_size": param_size,
                            "modified_at": m.get("modified_at", ""),
                            "active": name == self.active_config.model_name
                        })
        except Exception as e:
            logger.warning(f"Could not connect to Ollama at {self.ollama_base_url}: {e}")

        return {
            "status": status,
            "base_url": self.ollama_base_url,
            "active_model": self.active_config.model_name,
            "models": models,
            "quantization_presets": list(QUANTIZATION_PRESETS.values())
        }

    async def pull_model_stream(self, model_name: str, quantization: Optional[str] = None) -> AsyncGenerator[Dict[str, Any], None]:
        """Stream progress while pulling model from local repository."""
        target_name = model_name
        if quantization and not (":" in model_name and quantization.lower() in model_name.lower()):
            if not ":" in target_name:
                target_name = f"{target_name}:{quantization.lower()}"

        pull_url = f"{self.ollama_base_url}/api/pull"
        payload = {"name": target_name, "stream": True}

        timeout_cfg = httpx.Timeout(connect=10.0, read=600.0, write=600.0, pool=10.0)
        try:
            async with httpx.AsyncClient(timeout=timeout_cfg) as client:
                async with client.stream("POST", pull_url, json=payload) as response:
                    if response.status_code != 200:
                        yield {"status": "error", "message": f"HTTP {response.status_code}", "percentage": 0, "done": False}
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
                            is_done = chunk.get("status") == "success" or percent == 100.0
                            yield {
                                "model": target_name,
                                "status": status_text,
                                "completed": completed,
                                "total": total,
                                "percentage": percent,
                                "done": is_done
                            }
                        except Exception:
                            yield {"model": target_name, "status": line, "percentage": 0, "done": False}
        except Exception as e:
            logger.error(f"Error pulling model {target_name}: {e}")
            yield {"model": target_name, "status": "error", "message": str(e), "percentage": 0, "done": False}

    async def delete_model(self, model_name: str) -> bool:
        """Delete local model."""
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                res = await client.request("DELETE", f"{self.ollama_base_url}/api/delete", json={"name": model_name})
                return res.status_code == 200
        except Exception as e:
            logger.error(f"Error deleting model {model_name}: {e}")
            return False

    def set_active_config(self, config: LocalModelConfig) -> LocalModelConfig:
        """Update active local model configuration."""
        self.active_config = config
        return self.active_config

local_model_manager = LocalModelManager()
