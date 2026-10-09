"""
llm_clients.py — Cached client instances and GPU resource tracking for local and cloud LLMs.
"""

import os
from typing import Dict, Any, Optional
import ollama

import time

_cached_openai_clients: Dict[str, Any] = {}
_cached_anthropic_clients: Dict[str, Any] = {}
_cached_ollama_clients: Dict[str, Any] = {}

_last_vram_query_time: float = 0.0
_cached_vram_usage: float = 50.0


def get_cached_openai_client(api_key: str, base_url: Optional[str] = None):
    cache_key = f"{api_key}::{base_url or ''}"
    if cache_key not in _cached_openai_clients:
        from openai import OpenAI
        kwargs = {"api_key": api_key}
        if base_url:
            kwargs["base_url"] = base_url
        _cached_openai_clients[cache_key] = OpenAI(**kwargs)
    return _cached_openai_clients[cache_key]


def get_cached_anthropic_client(api_key: str):
    if api_key not in _cached_anthropic_clients:
        from anthropic import Anthropic
        _cached_anthropic_clients[api_key] = Anthropic(api_key=api_key)
    return _cached_anthropic_clients[api_key]


def get_cached_ollama_client(host: str):
    """Returns a cached Ollama client for the given host, creating one on first call."""
    if host not in _cached_ollama_clients:
        _cached_ollama_clients[host] = ollama.Client(host=host)
    return _cached_ollama_clients[host]


def get_ollama_client(host: Optional[str] = None):
    """Convenience accessor for primary Ollama client."""
    from database import get_ollama_client as _db_get_ollama_client
    return _db_get_ollama_client()


def get_gpu_vram_usage() -> float:
    global _last_vram_query_time, _cached_vram_usage
    now = time.time()
    if now - _last_vram_query_time < 5.0:
        return _cached_vram_usage

    _last_vram_query_time = now
    try:
        import subprocess
        output = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=memory.used,memory.total", "--format=csv,nounits,noheader"],
            encoding="utf-8"
        )
        used, total = map(float, output.strip().split(","))
        _cached_vram_usage = (used / total) * 100.0
        return _cached_vram_usage
    except Exception:
        try:
            import psutil
            _cached_vram_usage = float(psutil.virtual_memory().percent)
            return _cached_vram_usage
        except Exception:
            _cached_vram_usage = 50.0
            return _cached_vram_usage
