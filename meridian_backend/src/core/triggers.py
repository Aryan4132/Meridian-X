"""
triggers.py — Event-Action Workflow Automation Engine (BK-18)
Monitors condition rules (CPU, disk, active window, time) and executes automated actions.
"""

import time
from typing import Dict, Any, List, Callable, Optional


class WorkflowTriggerEngine:
    """Manages user-defined background condition triggers and action rules."""

    def __init__(self):
        self.rules: List[Dict[str, Any]] = []

    def register_rule(self, name: str, condition_type: str, threshold: Any, action_command: str) -> Dict[str, Any]:
        """Registers an event-action automation rule."""
        rule = {
            "id": f"rule_{len(self.rules) + 1}",
            "name": name,
            "condition_type": condition_type,
            "threshold": threshold,
            "action_command": action_command,
            "created_at": time.time()
        }
        self.rules.append(rule)
        print(f"[Trigger Engine] Registered workflow rule '{name}' ({condition_type} > {threshold})")
        return rule

    def evaluate_rules(self, current_metrics: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Evaluates registered rules against current system metrics and triggers matching actions."""
        triggered = []
        for rule in self.rules:
            c_type = rule["condition_type"]
            val = current_metrics.get(c_type)
            if val is not None and val > rule["threshold"]:
                triggered.append({
                    "rule": rule["name"],
                    "action": rule["action_command"],
                    "metric_value": val,
                    "triggered_at": time.time()
                })
                print(f"[Trigger Engine] Fired rule '{rule['name']}'! Action: {rule['action_command']}")
        return triggered
