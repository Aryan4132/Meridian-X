"""
prompt_templates.py — Reusable System Prompt & Tool Definition Library (BK-23)
Provides template management, role-based system prompts, and standardized tool JSON schemas.
"""

import json
from typing import Dict, Any, List, Optional


class PromptTemplateEngine:
    """Manages role system prompt templates and tool schema definitions."""

    DEFAULT_TEMPLATES: Dict[str, str] = {
        "coding_agent": (
            "You are Meridian-X Coding Agent, an expert AI developer.\n"
            "Task Context: {context}\n"
            "System Rules: Output strict, modular, high-performance code. Maintain comments and type hints."
        ),
        "rag_agent": (
            "You are Meridian-X Memory & Retrieval Agent.\n"
            "Relevant Knowledge: {context}\n"
            "Task: Synthesize retrieved context to answer user query: '{query}'. Reduce noise and cite facts."
        ),
        "tool_agent": (
            "You are Meridian-X Active Tool Execution Agent.\n"
            "Available Tools: {tools}\n"
            "Goal: Select optimal tool, validate parameter JSON schema, and execute active task."
        ),
        "auditor_agent": (
            "You are Meridian-X Code Quality & Security Auditor.\n"
            "Code Under Review:\n{code}\n"
            "Checklist: Check for memory leaks, unhandled exceptions, token efficiency, and security flaws.\n"
            "Temporal Rules: Do not flag real-time dates on or before current system date as temporal hallucinations."
        )
    }

    def __init__(self, custom_templates: Optional[Dict[str, str]] = None):
        self.templates = dict(self.DEFAULT_TEMPLATES)
        if custom_templates:
            self.templates.update(custom_templates)
        self.tool_schemas: Dict[str, Dict[str, Any]] = {}

    def register_template(self, name: str, template: str):
        """Registers or overrides a prompt template."""
        self.templates[name] = template

    def render_prompt(self, template_name: str, **kwargs) -> str:
        """Renders a system prompt using template key and format arguments."""
        if template_name not in self.templates:
            raise KeyError(f"Prompt template '{template_name}' not found.")
        
        template_str = self.templates[template_name]
        try:
            return template_str.format(**kwargs)
        except KeyError as e:
            # Return template with missing placeholder noted
            return f"{template_str} [Missing param: {e}]"

    def register_tool_schema(self, tool_name: str, description: str, parameters: Dict[str, Any]):
        """Registers a reusable tool definition schema in OpenAI function format."""
        schema = {
            "type": "function",
            "function": {
                "name": tool_name,
                "description": description,
                "parameters": parameters
            }
        }
        self.tool_schemas[tool_name] = schema

    def get_tool_schemas(self, tool_names: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Retrieves list of registered tool schema definitions."""
        if tool_names is None:
            return list(self.tool_schemas.values())
        return [self.tool_schemas[name] for name in tool_names if name in self.tool_schemas]
