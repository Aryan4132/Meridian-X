import os
import json
import asyncio
import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger("meridian_mcp")

class McpClient:
  """
  An asynchronous stdio client for Model Context Protocol (MCP) servers.
  Launches the server as a subprocess and interacts using JSON-RPC.
  """
  def __init__(self, name: str, command: str, args: List[str] = None, env: Dict[str, str] = None):
    self.name = name
    self.command = command
    self.args = args or []
    self.env = env or {}
    self.process: Optional[asyncio.subprocess.Process] = None
    self.read_task: Optional[asyncio.Task] = None
    self.pending_requests: Dict[int, asyncio.Future] = {}
    self.next_id = 1
    self._lock = asyncio.Lock()

  async def start(self) -> bool:
    """Launches the MCP server subprocess."""
    try:
      # Inject current environment variables
      full_env = os.environ.copy()
      full_env.update(self.env)
      
      # Spawn subprocess
      self.process = await asyncio.create_subprocess_exec(
        self.command,
        *self.args,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        env=full_env
      )
      
      # Start background stdout read listener
      self.read_task = asyncio.create_task(self._read_loop())
      logger.info(f"MCP server '{self.name}' started successfully.")
      return True
    except Exception as e:
      logger.error(f"Failed to start MCP server '{self.name}': {e}")
      return False

  async def stop(self):
    """Gracefully terminates the MCP server subprocess."""
    if self.read_task:
      self.read_task.cancel()
    if self.process:
      try:
        self.process.terminate()
        await self.process.wait()
      except Exception:
        pass
    logger.info(f"MCP server '{self.name}' stopped.")

  async def _read_loop(self):
    """Listens to stdout and resolves pending JSON-RPC futures."""
    while self.process and self.process.stdout:
      try:
        line = await self.process.stdout.readline()
        if not line:
          break
        
        # Parse JSON-RPC line
        response = json.loads(line.decode("utf-8").strip())
        resp_id = response.get("id")
        
        if resp_id is not None and resp_id in self.pending_requests:
          future = self.pending_requests.pop(resp_id)
          if not future.cancelled():
            future.set_result(response)
      except asyncio.CancelledError:
        break
      except Exception as e:
        logger.error(f"Error in MCP client read loop for '{self.name}': {e}")

  async def _send_request(self, method: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """Sends JSON-RPC request and awaits response."""
    if not self.process or not self.process.stdin:
      raise RuntimeError(f"MCP server '{self.name}' is not running.")

    async with self._lock:
      req_id = self.next_id
      self.next_id += 1
      
    future = asyncio.get_running_loop().create_future()
    self.pending_requests[req_id] = future
    
    payload = {
      "jsonrpc": "2.0",
      "id": req_id,
      "method": method,
      "params": params
    }
    
    # Write message to stdin
    msg = json.dumps(payload) + "\n"
    self.process.stdin.write(msg.encode("utf-8"))
    await self.process.stdin.drain()
    
    # Await response with a timeout (e.g. 15 seconds)
    try:
      response = await asyncio.wait_for(future, timeout=15.0)
      if "error" in response:
        raise RuntimeError(f"MCP error: {response['error']}")
      return response.get("result", {})
    except asyncio.TimeoutError:
      if req_id in self.pending_requests:
        self.pending_requests.pop(req_id)
      raise TimeoutError(f"MCP request '{method}' to '{self.name}' timed out.")

  async def list_tools(self) -> List[Dict[str, Any]]:
    """Lists tools supported by this MCP server."""
    try:
      result = await self._send_request("tools/list", {})
      return result.get("tools", [])
    except Exception as e:
      logger.error(f"Failed to list tools from MCP server '{self.name}': {e}")
      return []

  async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> str:
    """Calls a specific tool on this MCP server."""
    try:
      params = {"name": tool_name, "arguments": arguments}
      result = await self._send_request("tools/call", params)
      # Extract text from result content block
      content = result.get("content", [])
      text_parts = []
      for block in content:
        if block.get("type") == "text":
          text_parts.append(block.get("text", ""))
      return "\n".join(text_parts)
    except Exception as e:
      logger.error(f"Failed to call tool '{tool_name}' on '{self.name}': {e}")
      raise


class McpManager:
  """
  Manages multiple stdio-based MCP servers configured via mcp_config.json.
  """
  def __init__(self, config_path: str = "mcp_config.json"):
    self.config_path = config_path
    self.clients: Dict[str, McpClient] = {}

  async def initialize(self):
    """Loads config and starts all MCP servers."""
    if not os.path.exists(self.config_path):
      # Write a default empty or sample config
      default_config = {
        "mcpServers": {
          # Example configuration
          # "sqlite": {
          #   "command": "npx",
          #   "args": ["-y", "@modelcontextprotocol/server-sqlite", "--db", "meridian_memory/metadata.db"]
          # }
        }
      }
      try:
        with open(self.config_path, "w") as f:
          json.dump(default_config, f, indent=2)
      except Exception:
        pass
      return

    try:
      with open(self.config_path, "r") as f:
        config = json.load(f)
        
      servers = config.get("mcpServers", {})
      for name, srv_conf in servers.items():
        command = srv_conf.get("command")
        args = srv_conf.get("args", [])
        env = srv_conf.get("env", {})
        if command:
          client = McpClient(name, command, args, env)
          success = await client.start()
          if success:
            self.clients[name] = client
    except Exception as e:
      logger.error(f"Error initializing MCP Manager: {e}")

  async def shutdown(self):
    """Stops all running MCP servers."""
    for client in self.clients.values():
      await client.stop()
    self.clients.clear()

  async def get_all_mcp_tools(self) -> List[Dict[str, Any]]:
    """Aggregates all tools from active MCP servers."""
    all_tools = []
    for client in self.clients.values():
      tools = await client.list_tools()
      for tool in tools:
        # Tag tool to identify its source server
        tool["mcp_server"] = client.name
        all_tools.append(tool)
    return all_tools

  async def execute_mcp_tool(self, server_name: str, tool_name: str, arguments: Dict[str, Any]) -> str:
    """Executes a tool on a specific MCP server."""
    client = self.clients.get(server_name)
    if not client:
      raise ValueError(f"MCP server '{server_name}' is not running.")
    return await client.call_tool(tool_name, arguments)

# Global MCP Manager instance
mcp_manager = McpManager()
