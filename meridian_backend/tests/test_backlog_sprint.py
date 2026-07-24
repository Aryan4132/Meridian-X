import pytest
import os
import sys

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.voice.duplex import DuplexVoiceEngine
from src.tools.browser_agent import AutonomousWebBrowser
from src.core.graph_rag import CodebaseASTGraph
from src.core.governor import HardwareGovernor
from src.core.p2p_crypto import NoiseP2PCrypto
from src.tools.mcp_marketplace import MCPMarketplaceManager
from src.core.triggers import WorkflowTriggerEngine


def test_duplex_voice_engine():
    engine = DuplexVoiceEngine()
    assert engine.start_duplex_session() == "Duplex voice session initialized."
    engine.set_speaking_state(True)
    assert engine.check_barge_in(300.0) is True
    assert engine.state == "interrupted"
    assert engine.stop_duplex_session() == "Duplex voice session stopped."


def test_browser_agent():
    browser = AutonomousWebBrowser()
    nav_res = browser.navigate("https://example.com")
    assert nav_res["status"] == "success"
    click_res = browser.click_element("#submit-button")
    assert click_res["status"] == "success"


def test_codebase_ast_graph():
    graph = CodebaseASTGraph()
    # Index self (duplex.py or this file)
    curr_file = os.path.abspath(__file__)
    indexed = graph.index_python_file(curr_file)
    assert indexed is True
    syms = graph.query_symbol("test")
    assert len(syms) > 0


def test_hardware_governor():
    governor = HardwareGovernor()
    bench = governor.probe_model_benchmark()
    assert bench["status"] == "healthy"
    gov = governor.check_system_governance()
    assert "cpu_percent" in gov


def test_noise_p2p_crypto():
    crypto = NoiseP2PCrypto()
    priv1, pub1 = crypto.generate_ephemeral_keypair()
    priv2, pub2 = crypto.generate_ephemeral_keypair()
    key1 = crypto.derive_shared_session_key(priv1, pub2)
    assert len(key1) > 0
    bio = crypto.verify_biometric_vault_access()
    assert bio["authenticated"] is True


def test_mcp_marketplace():
    manager = MCPMarketplaceManager()
    catalog = manager.list_available_servers()
    assert len(catalog) >= 4
    install_res = manager.install_mcp_server("github-mcp")
    assert install_res["status"] == "success"


def test_workflow_triggers():
    triggers = WorkflowTriggerEngine()
    triggers.register_rule("High CPU Alert", "cpu", 80.0, "notify_user")
    fired = triggers.evaluate_rules({"cpu": 85.0})
    assert len(fired) == 1
    assert fired[0]["rule"] == "High CPU Alert"
