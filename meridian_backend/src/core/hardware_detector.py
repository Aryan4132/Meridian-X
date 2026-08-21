import psutil
import os
import sys
import logging
from typing import Dict, Any, TypedDict

logger = logging.getLogger(__name__)

class GpuInfo(TypedDict):
    has_gpu: bool
    vram_gb: float
    name: str

def detect_hardware_specs() -> Dict[str, Any]:
    """Detect CPU, RAM, and GPU capabilities to recommend optimal offline model."""
    cpu_count = psutil.cpu_count(logical=True) or 4
    mem_info = psutil.virtual_memory()
    ram_gb = round(mem_info.total / (1024 ** 3), 1)

    has_gpu = False
    vram_gb: float = 0.0
    gpu_name = "None"

    # Attempt to detect NVIDIA GPU via pynvml, Apple Silicon, or AMD ROCm
    import platform
    sys_os = platform.system()
    try:
        import pynvml  # type: ignore
        pynvml.nvmlInit()
        device_count = pynvml.nvmlDeviceGetCount()
        if device_count > 0:
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            name = pynvml.nvmlDeviceGetName(handle)
            info = pynvml.nvmlDeviceGetMemoryInfo(handle)
            if isinstance(name, bytes):
                gpu_name = name.decode('utf-8')
            else:
                gpu_name = str(name)
            has_gpu = True
            vram_gb = round(info.total / (1024 ** 3), 1)
        pynvml.nvmlShutdown()
    except Exception as e:
        logger.debug(f"NVIDIA GPU detection skipped: {e}")

    # Fallback to Apple Silicon Metal Unified Memory
    if not has_gpu and sys_os == "Darwin":
        try:
            import subprocess
            res = subprocess.check_output(["sysctl", "-n", "machdep.cpu.brand_string"], stderr=subprocess.DEVNULL).decode('utf-8').strip()
            if "Apple" in res or platform.machine() == "arm64":
                has_gpu = True
                gpu_name = f"Apple Silicon Metal ({res or 'M-Series'})"
                # Unified memory available for Metal GPU shaders (~75% of RAM)
                vram_gb = round(ram_gb * 0.75, 1)
        except Exception:
            pass

    # Fallback to AMD ROCm
    if not has_gpu and sys_os == "Linux":
        try:
            import subprocess
            res = subprocess.check_output(["rocm-smi", "--showproductname"], stderr=subprocess.DEVNULL).decode('utf-8')
            if "Card" in res or "GPU" in res:
                has_gpu = True
                gpu_name = "AMD Radeon (ROCm)"
                vram_gb = round(ram_gb * 0.5, 1)
        except Exception:
            pass

    gpu_info: GpuInfo = {
        "has_gpu": has_gpu,
        "vram_gb": vram_gb,
        "name": gpu_name
    }


    # Determine recommended model tier
    tier = "entry"
    recommended_model = "llama3.2:1b"
    recommended_label = "Llama 3.2 1B (Ultra Light)"
    description = "Fast execution, lowest RAM usage (~1.3 GB download)."

    if ram_gb >= 16.0 or vram_gb >= 6.0:
        tier = "high"
        recommended_model = "llama3.1:8b"
        recommended_label = "Llama 3.1 8B (High Intelligence)"
        description = "High accuracy and reasoning capacity (~4.7 GB download)."
    elif ram_gb >= 8.0 or vram_gb >= 2.0:
        tier = "mid"
        recommended_model = "llama3.2:3b"
        recommended_label = "Llama 3.2 3B (Recommended)"
        description = "Optimal balance of response speed and quality (~2.0 GB download)."

    available_options = [
        {
            "id": "llama3.2:1b",
            "name": "Llama 3.2 1B",
            "tier": "Light",
            "size": "1.3 GB",
            "min_ram": "4 GB",
            "description": "Ultra fast, lightweight for basic PCs"
        },
        {
            "id": "llama3.2:3b",
            "name": "Llama 3.2 3B",
            "tier": "Recommended",
            "size": "2.0 GB",
            "min_ram": "8 GB",
            "description": "Best overall balance for standard laptops"
        },
        {
            "id": "qwen2.5:7b",
            "name": "Qwen 2.5 7B",
            "tier": "Smart",
            "size": "4.4 GB",
            "min_ram": "12 GB",
            "description": "Great for coding and logical reasoning"
        },
        {
            "id": "llama3.1:8b",
            "name": "Llama 3.1 8B",
            "tier": "High Intelligence",
            "size": "4.7 GB",
            "min_ram": "16 GB",
            "description": "Maximum capability for powerful hardware"
        }
    ]

    return {
        "cpu_cores": cpu_count,
        "ram_gb": ram_gb,
        "gpu": gpu_info,
        "hardware_tier": tier,
        "recommended_model": recommended_model,
        "recommended_label": recommended_label,
        "description": description,
        "options": available_options
    }
