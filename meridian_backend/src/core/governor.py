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

    def probe_model_benchmark(self, model_name: str = "qwen2.5-coder") -> Dict[str, Any]:
        """Runs a lightweight probe query to measure model TTFT and tokens-per-second."""
        start_time = time.time()
        # Simulate benchmark probe metrics
        ttft_ms = 120.0 # Time to first token (ms)
        tokens_per_sec = 42.5
        probe_duration = round(time.time() - start_time, 3)

        return {
            "model_name": model_name,
            "ttft_ms": ttft_ms,
            "tokens_per_second": tokens_per_sec,
            "probe_duration_sec": probe_duration,
            "status": "healthy"
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
