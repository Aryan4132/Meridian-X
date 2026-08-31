"""
presence_briefing.py — Executive Room Arrival Briefing Stub (JARVIS-06)
"""
from typing import Dict, Any, Optional

def generate_presence_briefing(user_name: Optional[str] = "User") -> Dict[str, Any]:
    name = user_name or "User"
    return {"briefing": f"Welcome back to your workspace, {name}."}
