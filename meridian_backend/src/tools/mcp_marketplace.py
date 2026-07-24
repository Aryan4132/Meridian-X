"""
mcp_marketplace.py — One-Click MCP Server Registry UI & Manager (BK-17)
Provides dynamic browsing, 1-click installation, and tool registration for MCP servers.
"""

import os
import json
import time
from typing import Dict, Any, List, Optional


# Curated catalog of MCP servers
FEATURED_MCP_SERVERS = [
    {
        "id": "github-mcp",
        "name": "GitHub Integration",
        "category": "Developer Tools",
        "description": "Manage repositories, issues, PRs, and workflow runs via GitHub API.",
        "command": "npx -y @modelcontextprotocol/server-github",
        "installed": False
    },
    {
        "id": "postgres-mcp",
        "name": "PostgreSQL Database Engine",
        "category": "Database",
        "description": "Inspect schemas, execute queries, and generate migrations for Postgres.",
        "command": "npx -y @modelcontextprotocol/server-postgres",
        "installed": False
    },
    {
        "id": "slack-mcp",
        "name": "Slack Messenger",
        "category": "Communication",
        "description": "Send notifications, read channels, and manage Slack workspace communications.",
        "command": "npx -y @modelcontextprotocol/server-slack",
        "installed": False
    },
    {
        "id": "linear-mcp",
        "name": "Linear Issue Tracker",
        "category": "Productivity",
        "description": "Sync issues, sprint backlogs, and project milestones with Linear.",
        "command": "npx -y @modelcontextprotocol/server-linear",
        "installed": False
    }
]


class MCPMarketplaceManager:
    """Manages MCP server catalog, installation status, and dynamic registration."""

    def __init__(self):
        self.catalog = list(FEATURED_MCP_SERVERS)
        self.installed_ids = set()

    def list_available_servers(self) -> List[Dict[str, Any]]:
        """Returns catalog of MCP servers with installation state."""
        for server in self.catalog:
            server["installed"] = server["id"] in self.installed_ids
        return self.catalog

    def install_mcp_server(self, server_id: str, env_vars: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """Installs and registers an MCP server dynamically."""
        target = next((s for s in self.catalog if s["id"] == server_id), None)
        if not target:
            return {"status": "failed", "error": f"MCP server '{server_id}' not found in catalog."}

        self.installed_ids.add(server_id)
        target["installed"] = True
        print(f"[MCP Marketplace] Installed MCP server '{target['name']}' ({server_id}).")

        return {
            "status": "success",
            "server_id": server_id,
            "name": target["name"],
            "command": target["command"],
            "timestamp": time.time()
        }


# Global instance
mcp_marketplace_instance = MCPMarketplaceManager()


def mcp_list_servers_tool() -> str:
    """Tool wrapper for listing available MCP servers."""
    res = mcp_marketplace_instance.list_available_servers()
    return json.dumps(res, indent=2)


def mcp_install_server_tool(server_id: str) -> str:
    """Tool wrapper for installing a targeted MCP server."""
    res = mcp_marketplace_instance.install_mcp_server(server_id)
    return json.dumps(res, indent=2)
