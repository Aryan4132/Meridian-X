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


CONFIG_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "mcp_config.json")


def load_mcp_config() -> Dict[str, Any]:
    """Loads custom MCP server configuration from mcp_config.json."""
    if not os.path.exists(CONFIG_FILE_PATH):
        return {"mcpServers": {}}
    try:
        with open(CONFIG_FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            if "mcpServers" not in data:
                data["mcpServers"] = {}
            return data
    except Exception as e:
        print(f"[MCP] Failed to load mcp_config.json: {e}")
        return {"mcpServers": {}}


def save_mcp_config(config_data: Dict[str, Any]) -> bool:
    """Saves custom MCP server configuration to mcp_config.json."""
    try:
        with open(CONFIG_FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(config_data, f, indent=2)
        return True
    except Exception as e:
        print(f"[MCP] Failed to save mcp_config.json: {e}")
        return False


class MCPMarketplaceManager:
    """Manages MCP server catalog, installation status, and dynamic registration."""

    def __init__(self):
        self.catalog = list(FEATURED_MCP_SERVERS)
        self.installed_ids = set()

    def list_available_servers(self) -> List[Dict[str, Any]]:
        """Returns catalog of MCP servers with installation state."""
        config_data = load_mcp_config()
        custom_servers = config_data.get("mcpServers", {})

        for server in self.catalog:
            server["installed"] = (server["id"] in self.installed_ids) or (server["id"] in custom_servers)
        return self.catalog

    def list_custom_servers(self) -> Dict[str, Any]:
        """Returns registered custom MCP servers."""
        config_data = load_mcp_config()
        return config_data.get("mcpServers", {})

    def add_custom_server(self, name: str, command: str, args: List[str] = None, env: Dict[str, str] = None) -> Dict[str, Any]:
        """Adds a custom MCP server to configuration."""
        name_clean = name.strip()
        if not name_clean or not command.strip():
            return {"status": "failed", "error": "Server name and command are required."}
        
        config_data = load_mcp_config()
        config_data["mcpServers"][name_clean] = {
            "command": command.strip(),
            "args": args or [],
            "env": env or {},
            "added_at": time.time()
        }
        save_mcp_config(config_data)
        self.installed_ids.add(name_clean)

        return {
            "status": "success",
            "name": name_clean,
            "command": command.strip(),
            "config": config_data["mcpServers"][name_clean]
        }

    def delete_custom_server(self, name: str) -> bool:
        """Deletes a custom MCP server from configuration."""
        config_data = load_mcp_config()
        if name in config_data["mcpServers"]:
            del config_data["mcpServers"][name]
            save_mcp_config(config_data)
            self.installed_ids.discard(name)
            return True
        return False

    def install_mcp_server(self, server_id: str, env_vars: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """Installs and registers a catalog MCP server dynamically."""
        target = next((s for s in self.catalog if s["id"] == server_id), None)
        if not target:
            return {"status": "failed", "error": f"MCP server '{server_id}' not found in catalog."}

        parts = target["command"].split()
        cmd = parts[0] if parts else target["command"]
        args = parts[1:] if len(parts) > 1 else []

        self.add_custom_server(target["id"], cmd, args, env_vars or {})
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
