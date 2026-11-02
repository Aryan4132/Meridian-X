import os
import sys
import json
import pytest
import yaml

# Ensure project root & meridian_backend are in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import doctor
from src.api.system import get_mobile_pairing_info, get_pairing_qr_svg


def test_doctor_python_runtime():
    res = doctor.check_python_runtime()
    assert res["status"] in ("PASS", "WARN")
    assert "3." in res["version"]
    assert "message" in res


def test_doctor_dependencies():
    res = doctor.check_dependencies()
    assert "modules" in res
    assert "fastapi" in res["modules"]
    assert res["modules"]["fastapi"]["installed"] is True
    assert "uvicorn" in res["modules"]
    assert res["modules"]["uvicorn"]["installed"] is True


def test_doctor_database_check():
    res = doctor.check_database()
    assert "name" in res
    assert res["status"] in ("PASS", "WARN")
    assert "path" in res


def test_doctor_ollama_check():
    res = doctor.check_ollama()
    assert "reachable" in res
    assert "models" in res
    assert isinstance(res["models"], list)


def test_doctor_ports_check():
    res = doctor.check_ports()
    assert "ports" in res
    assert len(res["ports"]) >= 3
    port_nums = [p["port"] for p in res["ports"]]
    assert 4132 in port_nums
    assert 4133 in port_nums
    assert 11434 in port_nums


def test_doctor_frontend_check():
    res = doctor.check_frontend()
    assert res["dist_exists"] is True
    assert res["status"] == "PASS"


def test_doctor_self_healing_safe_execution():
    actions = doctor.perform_self_healing()
    assert isinstance(actions, list)


def test_doctor_full_run():
    report = doctor.run_doctor(auto_fix=False)
    assert report["status"] in ("PASS", "WARN")
    assert "platform" in report
    assert len(report["checks"]) >= 5


def test_caddyfile_configuration():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    caddy_path = os.path.join(repo_root, "Caddyfile")
    assert os.path.exists(caddy_path)
    with open(caddy_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "reverse_proxy meridian-backend:4132" in content
    assert "try_files {path} /index.html" in content
    assert "file_server" in content


def test_docker_compose_prod_configuration():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    compose_path = os.path.join(repo_root, "docker-compose.prod.yml")
    assert os.path.exists(compose_path)
    with open(compose_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    services = data.get("services", {})
    assert "meridian-backend" in services
    assert "ollama" in services
    assert "caddy" in services
    # Check volume mounts
    caddy_vols = services["caddy"].get("volumes", [])
    assert any("dist:/srv" in v for v in caddy_vols)


def test_mobile_pairing_info_api():
    info = get_mobile_pairing_info()
    assert "lan_ip" in info
    assert info["port"] == 4132
    assert "ws://" in info["ws_url"]
    assert "auth_token" in info
    assert info["pairing_uri"].startswith("meridian://pair")
    
    # Verify qr_payload JSON structure
    payload = json.loads(info["qr_payload"])
    assert payload["lan_ip"] == info["lan_ip"]
    assert payload["port"] == 4132
    assert payload["url"] == info["ws_url"]


def test_mobile_pairing_qr_svg_generation():
    resp = get_pairing_qr_svg()
    assert resp.media_type == "image/svg+xml"
    body_str = resp.body.decode("utf-8")
    assert "<svg" in body_str
    assert "</svg>" in body_str

