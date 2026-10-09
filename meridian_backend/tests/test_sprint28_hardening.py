import os
import inspect
import pytest
from database import get_ollama_client_host
from src.api.deps import update_local_env_file


def test_docs_architecture_exists():
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    arch_path = os.path.join(root, "docs", "architecture.md")
    assert os.path.exists(arch_path), "docs/architecture.md does not exist"
    with open(arch_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "Five-Layer Architecture Overview" in content
    assert "Layer 1: Perception & System Guard" in content
    assert "Layer 2: Memory, Storage & Knowledge" in content
    assert "Layer 3: Tool Execution & Dynamic Capability" in content
    assert "Layer 4: Cognitive & Reasoning Loop" in content
    assert "Layer 5: Presentation & Client Interfaces" in content


def test_contributing_guide_exists():
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    contrib_path = os.path.join(root, "CONTRIBUTING.md")
    assert os.path.exists(contrib_path), "CONTRIBUTING.md does not exist"
    with open(contrib_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "ruff check" in content
    assert "pytest" in content
    assert "npm" in content


def test_legacy_scripts_purged():
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    assert not os.path.exists(os.path.join(root, "cleanup.py")), "cleanup.py should be purged"
    assert not os.path.exists(os.path.join(root, "create_shortcut.py")), "create_shortcut.py should be purged"


def test_chat_stream_cooperative_yield():
    import src.api.chat as chat_module
    src_code = inspect.getsource(chat_module.chat_stream)
    assert "await asyncio.sleep(0)" in src_code, "chat_stream generator missing cooperative back-pressure yield"


def test_database_and_deps_type_signatures():
    sig_host = inspect.signature(get_ollama_client_host)
    assert sig_host.return_annotation is str

    sig_env = inspect.signature(update_local_env_file)
    assert sig_env.return_annotation is None
