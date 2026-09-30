import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.loop import interrupt_agent_loop, _interrupt_event
from src.core.loop_stream import is_cancellation_requested, request_stream_cancellation, reset_cancel_flag
from fastapi.testclient import TestClient
from api import app

class TestChatAbort(unittest.TestCase):
    def setUp(self):
        _interrupt_event.clear()
        reset_cancel_flag("default")

    def test_interrupt_agent_loop_sets_event(self):
        self.assertFalse(_interrupt_event.is_set())
        interrupt_agent_loop()
        self.assertTrue(_interrupt_event.is_set())

    def test_stream_cancellation_flag(self):
        self.assertFalse(is_cancellation_requested("default"))
        request_stream_cancellation("default")
        self.assertTrue(is_cancellation_requested("default"))
        reset_cancel_flag("default")
        self.assertFalse(is_cancellation_requested("default"))

    def test_chat_abort_endpoint(self):
        client = TestClient(app)
        res = client.post("/api/chat/abort")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["status"], "success")
        self.assertTrue(_interrupt_event.is_set())

    def test_chat_stop_endpoint(self):
        _interrupt_event.clear()
        client = TestClient(app)
        res = client.post("/api/chat/stop")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["status"], "success")
        self.assertTrue(_interrupt_event.is_set())

    def test_voice_interrupt_stops_active_tts(self):
        from src.voice.tts import _tts_stop_event, stop_active_tts
        _tts_stop_event.clear()
        self.assertFalse(_tts_stop_event.is_set())
        
        # Calling stop_active_tts directly
        stop_active_tts()
        self.assertTrue(_tts_stop_event.is_set())

        # Calling /api/voice/interrupt endpoint
        _tts_stop_event.clear()
        _interrupt_event.clear()
        client = TestClient(app)
        res = client.post("/api/voice/interrupt")
        self.assertEqual(res.status_code, 200)
        self.assertTrue(_tts_stop_event.is_set())
        self.assertTrue(_interrupt_event.is_set())

