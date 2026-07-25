"""
mcp_executor.py — Active MCP Tool Execution Engine (BK-22)
Handles active Model Context Protocol (MCP) server tool discovery, invocation, 
execution state tracking, and JSON-RPC response formatting.
"""

import asyncio
import logging
from typing import Dict, Any, List, Optional
from meridian_backend.src.core.mcp_client import McpClient

logger = logging.getLogger("meridian_mcp_executor")


class McpToolExecutor:
    """Manages active tool execution across registered MCP clients."""

    def __init__(self):
        self.clients: Dict[str, McpClient] = {}
        self.execution_history: List[Dict[str, Any]] = []

    def register_client(self, name: str, client: McpClient):
        """Registers an active MCP client instance."""
        self.clients[name] = client
        logger.info(f"Registered MCP client: {name}")

    def unregister_client(self, name: str):
        """Unregisters an MCP client."""
        if name in self.clients:
            del self.clients[name]
            logger.info(f"Unregistered MCP client: {name}")

    async def discover_tools(self, server_name: Optional[str] = None) -> Dict[str, List[Dict[str, Any]]]:
        """Discovers available tools across registered MCP servers."""
        tools_by_server: Dict[str, List[Dict[str, Any]]] = {}
        target_clients = (
            {server_name: self.clients[server_name]}
            if server_name and server_name in self.clients
            else self.clients
        )

        for name, client in target_clients.items():
            try:
                # Standard MCP tools/list request
                req_id = client.next_id
                client.next_id += 1
                fut = asyncio.Future()
                client.pending_requests[req_id] = fut

                payload = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "method": "tools/list",
                    "params": {}
                }

                if client.process and client.process.stdin:
                    client.process.stdin.write((json.dumps(payload) + "\n").encode("utf-8"))
                    await client.process.stdin.drain()
                    res = await asyncio.wait_for(fut, timeout=5.0)
                    tools = res.get("result", {}).get("tools", [])
                    tools_by_server[name] = tools
                else:
                    tools_by_server[name] = []
            except Exception as e:
                logger.warning(f"Could not discover tools for server {name}: {e}")
                tools_by_server[name] = []

        return tools_by_server

    async def execute_tool(self, server_name: str, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Executes a tool on a specified MCP server."""
        if server_name not in self.clients:
            return {"status": "error", "error": f"MCP server '{server_name}' not registered."}

        client = self.clients[server_name]
        try:
            req_id = client.next_id
            client.next_id += 1
            fut = asyncio.Future()
            client.pending_requests[req_id] = fut

            payload = {
                "jsonrpc": "2.0",
                "id": req_id,
                "method": "tools/call",
                "params": {
                    "name": tool_name,
                    "arguments": arguments
                }
            }

            if not (client.process and client.process.stdin):
                return {"status": "error", "error": f"MCP server '{server_name}' stdin process not active."}

            import json
            client.process.stdin.write((json.dumps(payload) + "\n").encode("utf-8"))
            await client.process.stdin.drain()

            response = await asyncio.wait_for(fut, timeout=30.0)
            result = response.get("result", {})
            record = {
                "server": server_name,
                "tool": tool_name,
                "arguments": arguments,
                "result": result,
                "status": "success"
            }
            self.execution_history.append(record)
            return record
        except Exception as e:
            err_record = {
                "server": server_name,
                "tool": tool_name,
                "arguments": arguments,
                "error": str(e),
                "status": "error"
            }
            self.execution_history.append(err_record)
            return err_record
