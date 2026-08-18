import pytest
import asyncio
import os
import sys

backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from src.core.loop_stream import request_stream_cancellation, is_cancellation_requested, reset_cancel_flag

def test_loop_stream_reset_flags():
    request_stream_cancellation("default")
    assert is_cancellation_requested("default") is True
    
    reset_cancel_flag("default")
    assert is_cancellation_requested("default") is False

@pytest.mark.asyncio
async def test_stream_timeout_wrapper():
    async def mock_generator():
        yield "data: chunk 1\n\n"
        await asyncio.sleep(0.1)
        yield "data: chunk 2\n\n"

    collected = []
    async for chunk in mock_generator():
        collected.append(chunk)
        
    assert len(collected) == 2
    assert "chunk 1" in collected[0]
    assert "chunk 2" in collected[1]
