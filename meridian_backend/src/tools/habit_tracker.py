"""
habit_tracker.py — Habit Streaks & Goal Tracker (BUTLER-18)

Tracks daily executive habit consistency, computes streaks, and surfaces
Sunday weekly review scores.
"""

import time
import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)

class HabitTrackerSentinel:
    """Monitors daily habit streaks, targets, and executive consistency."""

    def __init__(self):
        self._habits: Dict[str, Dict[str, Any]] = {
            "morning_workout": {
                "name": "Morning Workout",
                "streak": 14,
                "longest_streak": 28,
                "weekly_target": 5,
                "completions_this_week": 4,
                "last_completed": time.time()
            },
            "deep_work_session": {
                "name": "90m Deep Focus Block",
                "streak": 22,
                "longest_streak": 30,
                "weekly_target": 5,
                "completions_this_week": 5,
                "last_completed": time.time()
            }
        }

    def log_habit_completion(self, habit_id: str) -> Dict[str, Any]:
        habit = self._habits.get(habit_id)
        if not habit:
            habit = {
                "name": habit_id.replace("_", " ").title(),
                "streak": 0,
                "longest_streak": 0,
                "weekly_target": 5,
                "completions_this_week": 0,
                "last_completed": 0
            }
            self._habits[habit_id] = habit

        habit["streak"] += 1
        habit["completions_this_week"] += 1
        habit["longest_streak"] = max(habit["longest_streak"], habit["streak"])
        habit["last_completed"] = time.time()
        logger.info(f"[HabitTracker] Completed habit '{habit['name']}' (streak: {habit['streak']})")

        return {
            "status": "logged",
            "habit": habit["name"],
            "current_streak": habit["streak"],
            "longest_streak": habit["longest_streak"],
            "weekly_progress": f"{habit['completions_this_week']}/{habit['weekly_target']}"
        }

    def get_habit_summary(self) -> Dict[str, Any]:
        total_streak = sum(h["streak"] for h in self._habits.values())
        return {
            "active_habits_count": len(self._habits),
            "combined_streak_days": total_streak,
            "habits": list(self._habits.values())
        }

habit_tracker_sentinel = HabitTrackerSentinel()

def habit_log(habit_id: str) -> Dict[str, Any]:
    return habit_tracker_sentinel.log_habit_completion(habit_id=habit_id)

def habit_get_summary() -> Dict[str, Any]:
    return habit_tracker_sentinel.get_habit_summary()

