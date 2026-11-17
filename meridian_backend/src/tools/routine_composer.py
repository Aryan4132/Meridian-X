"""
routine_composer.py — Routine Composer & Voice Macro Recorder (BUTLER-11)

Records chains of agent tool actions and system commands into named,
customizable execution routines invocable via quick voice or UI triggers.
"""

import time
import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)

class RoutineComposerSentinel:
    """Creates and executes composite multi-action agent routines."""

    def __init__(self):
        self._routines: Dict[str, Dict[str, Any]] = {
            "focus_sprint": {
                "name": "focus_sprint",
                "description": "Sets DND, organizes windows, dims lights, and plays lofi soundscape",
                "steps": [
                    {"tool": "hass_set_light", "args": {"entity_id": "light.desk_ambient", "brightness": 120}},
                    {"tool": "arrange_workspace_grid", "args": {}},
                    {"tool": "control_media_playback", "args": {"action": "play"}}
                ],
                "created_at": time.time()
            }
        }

    def compose_routine(self, name: str, description: str, steps: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Saves a new composite routine sequence."""
        routine = {
            "name": name,
            "description": description,
            "steps": steps,
            "created_at": time.time()
        }
        self._routines[name] = routine
        logger.info(f"[RoutineComposer] Created routine '{name}' with {len(steps)} steps")
        return {"status": "created", "name": name, "step_count": len(steps)}

    def execute_routine(self, name: str) -> Dict[str, Any]:
        """Simulates or dispatches the actions in the named routine."""
        routine = self._routines.get(name)
        if not routine:
            return {"status": "error", "message": f"Routine '{name}' not found"}

        executed = []
        for step in routine["steps"]:
            tool = step.get("tool", "")
            args = step.get("args", {})
            executed.append({"tool": tool, "status": "executed", "args": args})

        return {
            "status": "success",
            "routine_name": name,
            "executed_steps_count": len(executed),
            "steps": executed
        }

    def list_routines(self) -> List[Dict[str, Any]]:
        return list(self._routines.values())

routine_composer_sentinel = RoutineComposerSentinel()

def compose_save_routine(name: str, description: str, steps: List[Dict[str, Any]]) -> Dict[str, Any]:
    return routine_composer_sentinel.compose_routine(name=name, description=description, steps=steps)

def compose_run_routine(name: str) -> Dict[str, Any]:
    return routine_composer_sentinel.execute_routine(name=name)

def compose_list_routines() -> List[Dict[str, Any]]:
    return routine_composer_sentinel.list_routines()

