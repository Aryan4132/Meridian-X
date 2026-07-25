import os
import sys
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api import app
from src.voice.wakeword import _listen_loop

client = TestClient(app)

def test_get_onnx_models_endpoint():
    response = client.get("/api/voice/onnx-models")
    assert response.status_code == 200
    data = response.json()
    assert data.get("status") == "success"
    assert "models" in data
    assert isinstance(data["models"], list)

def test_wakeword_path_resolution(tmp_path):
    fake_onnx = tmp_path / "custom_test_wakeword.onnx"
    fake_onnx.write_text("fake_onnx_content")
    
    abs_path = str(fake_onnx)
    assert os.path.isabs(abs_path)
    assert os.path.exists(abs_path)
