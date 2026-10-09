import os
import sys
import pytest
import logging
from src.core.logger import get_logger, log_event
from src.tools.registry import tool, TOOL_REGISTRY


def test_logger_initialization():
    log = get_logger("test_meridian_module")
    assert isinstance(log, logging.Logger)
    assert log.name == "test_meridian_module"
    assert len(log.handlers) >= 1


def test_log_event_helper(capsys):
    log = get_logger("test_event_logger")
    log_event(log, "USER_LOGIN", {"user_id": "u123", "role": "admin"})
    captured = capsys.readouterr()
    assert "EVENT [USER_LOGIN]" in captured.out
    assert "u123" in captured.out


def test_declarative_tool_decorator():
    test_tool_name = "test_decorated_calc_tool"

    @tool(name=test_tool_name, tier=2, description="Calculates square of a number")
    def square_number(n: int) -> int:
        """Inner docstring that will be overridden by decorator description."""
        return n * n

    assert test_tool_name in TOOL_REGISTRY
    entry = TOOL_REGISTRY[test_tool_name]
    assert entry["tier"] == 2
    assert entry["description"] == "Calculates square of a number"
    assert entry["func"](5) == 25


def test_pyproject_toml_exists():
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    pyproject_path = os.path.join(root, "pyproject.toml")
    assert os.path.exists(pyproject_path), "Root pyproject.toml is missing"

    with open(pyproject_path, "r", encoding="utf-8") as f:
        content = f.read()

    assert "[project]" in content
    assert "meridian-x" in content
    assert "[tool.ruff]" in content
    assert "[tool.pytest.ini_options]" in content


def test_github_actions_ci_has_ruff():
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ci_path = os.path.join(root, ".github", "workflows", "verify.yml")
    assert os.path.exists(ci_path), ".github/workflows/verify.yml is missing"

    with open(ci_path, "r", encoding="utf-8") as f:
        ci_content = f.read()

    assert "ruff check" in ci_content
    assert "pytest" in ci_content
