"""
test_tool_regression.py — Tool-Use Regression Suite Runner (TRUST-02)
Runs scripted NL scenarios asserting correct tool selection and argument validation in CI pre-release checks.
"""

import os
import pytest
from src.tools.registry import registry
from src.core.tool_regression_sentinel import ToolRegressionSentinel

sentinel = ToolRegressionSentinel()


def test_tool_scenarios_schema():
    """Validates that all expected tools in scenarios exist in ToolRegistry or VIRTUAL_TOOLS."""
    scenarios = sentinel.load_scenarios()
    assert len(scenarios) > 0, "No scenarios loaded from tool_scenarios.yaml"

    registered_tools = registry.list_tools()
    registered_names = {t["name"] for t in registered_tools}

    for scenario in scenarios:
        expected = scenario["expected_tool"]
        assert expected in registered_names or expected in sentinel.VIRTUAL_TOOLS, (
            f"Scenario {scenario['id']} expected tool '{expected}' is missing from registry!"
        )


@pytest.mark.parametrize("scenario", sentinel.load_scenarios())
def test_scenario_rule_matching(scenario):
    """Asserts prompt heuristic tool matching for each scripted scenario using sentinel."""
    matched_tool = sentinel.match_prompt_to_tool(scenario["prompt"])
    expected = scenario["expected_tool"]
    assert matched_tool == expected, f"Scenario {scenario['id']} expected '{expected}', matched '{matched_tool}'"


@pytest.mark.parametrize("scenario", sentinel.load_scenarios())
def test_scenario_required_args_validation(scenario):
    """Validates that required_args specified in scenario schema pass argument validation."""
    assert sentinel.validate_scenario_args(scenario), (
        f"Scenario {scenario['id']} required_args validation failed for prompt: '{scenario['prompt']}'"
    )


def test_sentinel_overall_health():
    """Asserts that the comprehensive sentinel check returns healthy with zero failures."""
    report = sentinel.check_regressions()
    assert report["status"] == "healthy", f"Regression detected: {report.get('failures')}"
    assert report["failed"] == 0
    assert report["passed"] > 0


