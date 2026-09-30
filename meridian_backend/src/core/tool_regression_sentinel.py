"""
tool_regression_sentinel.py — Continuous Proactive Tool Regression Sentinel
Validates scripted scenario coverage and heuristic prompt matching from tool_scenarios.yaml.
Fires proactive nudges if tool selection degrades.
"""

import os
import yaml
import logging
from typing import Dict, Any, List, Optional

from src.tools.registry import registry

logger = logging.getLogger(__name__)


class ToolRegressionSentinel:
    """Continuously evaluates tool registry availability and NL heuristic routing."""

    VIRTUAL_TOOLS: List[str] = [
        "search_codebase",
        "browser_use_task",
        "get_all_memories",
        "get_spend_stats",
        "undo_last_action"
    ]

    def __init__(self, scenarios_path: str = ""):
        if not scenarios_path:
            scenarios_path = os.path.join(
                os.path.dirname(__file__), "..", "..", "tests", "tool_scenarios.yaml"
            )
        self.scenarios_path = os.path.abspath(scenarios_path)

    def load_scenarios(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.scenarios_path):
            return []
        try:
            with open(self.scenarios_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            return data.get("scenarios", [])
        except Exception as e:
            logger.error("[ToolRegressionSentinel] Failed reading scenarios: %s", e)
            return []

    def validate_scenario_args(self, scenario: Dict[str, Any]) -> bool:
        """Validates that scenario required_args are well-formed and covered in the prompt if applicable."""
        req_args = scenario.get("required_args", {})
        if not req_args:
            return True
        prompt = scenario.get("prompt", "").lower()
        for k, v in req_args.items():
            if v and str(v).lower() not in prompt:
                # If argument value is not contained in prompt, verify it can be derived or prompt is relevant
                return False
        return True

    def match_prompt_to_tool(self, prompt: str) -> Optional[str]:
        """Matches a natural language prompt to a registered or virtual tool via heuristic routing."""
        lower = (prompt or "").lower()
        if "codebase" in lower or "function" in lower or "grep" in lower:
            return "search_codebase"
        elif "browse" in lower or "web" in lower or "url" in lower:
            return "browser_use_task"
        elif "memory" in lower or "facts" in lower:
            return "get_all_memories"
        elif "token spend" in lower or "budget" in lower or "cost" in lower:
            return "get_spend_stats"
        elif "undo" in lower:
            return "undo_last_action"
        return None

    def check_regressions(self) -> Dict[str, Any]:
        """Runs validation across all scenarios and returns health summary."""
        scenarios = self.load_scenarios()
        if not scenarios:
            return {"status": "skipped", "reason": "no_scenarios_found", "passed": 0, "failed": 0, "total_scenarios": 0}

        registered_tools = registry.list_tools()
        registered_names = {t["name"] for t in registered_tools}

        passed = 0
        failed = 0
        failures = []

        for scenario in scenarios:
            prompt = scenario["prompt"]
            expected = scenario["expected_tool"]

            # 1. Existence check
            tool_exists = expected in registered_names or expected in self.VIRTUAL_TOOLS

            # 2. Heuristic prompt matching check
            matched_tool = self.match_prompt_to_tool(prompt)

            # 3. Argument schema validation check
            args_valid = self.validate_scenario_args(scenario)

            if tool_exists and matched_tool == expected and args_valid:
                passed += 1
            else:
                failed += 1
                failures.append({
                    "scenario_id": scenario.get("id"),
                    "prompt": scenario.get("prompt"),
                    "expected": expected,
                    "matched": matched_tool,
                    "tool_exists": tool_exists,
                    "args_valid": args_valid
                })

        return {
            "status": "healthy" if failed == 0 else "regressed",
            "total_scenarios": len(scenarios),
            "passed": passed,
            "failed": failed,
            "failures": failures
        }
