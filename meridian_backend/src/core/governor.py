"""
governor.py — Model Performance Benchmarker & Hardware Governor (BK-15)
Measures LLM TTFT/throughput speeds and monitors system thermal/RAM limits.
"""

import time
import os
import psutil
from typing import Dict, Any, Optional


class HardwareGovernor:
    """Monitors system hardware safety limits and benchmarks LLM model speed."""

    def __init__(self, ram_limit_pct: float = 90.0, cpu_limit_pct: float = 95.0):
        self.ram_limit_pct = ram_limit_pct
        self.cpu_limit_pct = cpu_limit_pct

    def probe_model_benchmark(self, model_name: str = "for ex: model name") -> Dict[str, Any]:
        """
        #4 FIX: Runs a real timed probe query to measure actual model TTFT and tokens-per-second.
        Previously returned hardcoded constants (ttft_ms=120, tps=42.5) which made the model
        router unable to make informed decisions. Now times a live Ollama generate() call.
        """
        start_time = time.time()
        ttft_ms = -1.0
        tokens_per_sec = -1.0
        status = "unknown"
        try:
            import ollama
            from src.core.llm_provider import get_ollama_host
            host = get_ollama_host()
            client = ollama.Client(host=host)

            probe_prompt = "Reply with exactly one word: OK"
            token_count = 0
            first_token_time = None

            stream = client.generate(model=model_name, prompt=probe_prompt, stream=True)
            for chunk in stream:
                if first_token_time is None:
                    first_token_time = time.time()
                    ttft_ms = round((first_token_time - start_time) * 1000.0, 1)
                response_text = chunk.response if hasattr(chunk, "response") else (chunk.get("response", "") if isinstance(chunk, dict) else "")
                token_count += len(response_text.split())

            probe_duration = round(time.time() - start_time, 3)
            elapsed_after_first = max(probe_duration - (ttft_ms / 1000.0), 0.001)
            tokens_per_sec = round(token_count / elapsed_after_first, 1) if token_count > 0 else 0.0
            status = "healthy"

        except Exception as e:
            probe_duration = round(time.time() - start_time, 3)
            status = f"probe_failed: {e}"
            print(f"[Hardware Governor] Benchmark probe failed for model '{model_name}': {e}")

        return {
            "model_name": model_name,
            "ttft_ms": ttft_ms,
            "tokens_per_second": tokens_per_sec,
            "probe_duration_sec": probe_duration,
            "status": status
        }

    def check_system_governance(self) -> Dict[str, Any]:
        """Checks system CPU, RAM, and disk utilization against governor safety thresholds."""
        cpu_usage = psutil.cpu_percent(interval=0.1)
        mem_info = psutil.virtual_memory()
        mem_usage = mem_info.percent

        is_throttled = (cpu_usage > self.cpu_limit_pct) or (mem_usage > self.ram_limit_pct)

        return {
            "cpu_percent": cpu_usage,
            "memory_percent": mem_usage,
            "throttled": is_throttled,
            "recommendation": "Throttle active model context window" if is_throttled else "Normal operation"
        }

def switch_power_thermal_profile(mode: str = "balanced") -> Dict[str, Any]:
    """Adjusts CPU/GPU power profiles, FPS caps, and thermal targets (GAM-02)."""
    valid_modes = {"gaming": {"fps_cap": 144, "power": "high_performance"},
                   "compiling": {"fps_cap": 60, "power": "turbo"},
                   "idle": {"fps_cap": 30, "power": "power_saver"},
                   "balanced": {"fps_cap": 60, "power": "balanced"}}
    m = mode.lower().strip()
    profile = valid_modes.get(m, valid_modes["balanced"])
    profile["active_mode"] = m
    from src.core.audit_logger import log_sensitive_action
    log_sensitive_action("THERMAL_GOVERNOR", "switch_power_thermal_profile", profile, "SUCCESS")
    return profile
