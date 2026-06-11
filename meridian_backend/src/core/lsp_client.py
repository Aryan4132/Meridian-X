import os
import sys
import json
import asyncio
from typing import Dict, Any, List, Optional, Callable

class LspClient:
    def __init__(self, executable_path: str, root_dir: str):
        self.executable_path = os.path.abspath(executable_path)
        self.root_dir = os.path.abspath(root_dir)
        self.process: Optional[asyncio.subprocess.Process] = None
        self._read_task: Optional[asyncio.Task] = None
        self._next_id = 1
        self._pending_requests: Dict[int, asyncio.Future] = {}
        self._notification_callbacks: Dict[str, List[Callable[[Dict[str, Any]], None]]] = {}
        self._open_documents: Dict[str, int] = {} # filepath -> version
        self.diagnostics: Dict[str, List[Dict[str, Any]]] = {}
        self.register_callback("textDocument/publishDiagnostics", self._handle_diagnostics)

    def _handle_diagnostics(self, params: Dict[str, Any]):
        uri = params.get("uri")
        diagnostics = params.get("diagnostics", [])
        if uri:
            self.diagnostics[uri] = diagnostics

    def register_callback(self, method: str, callback: Callable[[Dict[str, Any]], None]):
        """Register a callback for server notifications (e.g., publishDiagnostics)."""
        if method not in self._notification_callbacks:
            self._notification_callbacks[method] = []
        self._notification_callbacks[method].append(callback)

    async def start(self) -> bool:
        """Starts the language server process and initialises communication."""
        try:
            print(f"[LSP Client] Starting LSP process: '{self.executable_path}' in CWD '{self.root_dir}'")
            
            # Start the language server in stdio mode
            self.process = await asyncio.create_subprocess_exec(
                self.executable_path, "--stdio",
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.DEVNULL,
                cwd=self.root_dir
            )
            
            # Start background reading loop
            self._read_task = asyncio.create_task(self._read_loop())
            
            # Initialize handshake
            await self._initialize()
            return True
        except Exception as e:
            print(f"[LSP Client] Failed to start LSP server: {e}")
            await self.stop()
            return False

    async def _initialize(self):
        # Convert path to standard URI
        root_uri = f"file:///{self.root_dir.replace('\\', '/')}"
        
        capabilities = {
            "textDocument": {
                "synchronization": {
                    "dynamicRegistration": True,
                    "willSave": False,
                    "willSaveWaitUntil": False,
                    "didSave": True
                },
                "definition": { "dynamicRegistration": True },
                "references": { "dynamicRegistration": True },
                "hover": { "dynamicRegistration": True }
            }
        }
        
        params = {
            "processId": os.getpid(),
            "clientInfo": {
                "name": "Meridian-X-LSP",
                "version": "1.0.0"
            },
            "rootPath": self.root_dir,
            "rootUri": root_uri,
            "capabilities": capabilities,
            "initializationOptions": {}
        }
        
        print("[LSP Client] Sending 'initialize' request...")
        init_res = await self.send_request("initialize", params, timeout=10.0)
        print("[LSP Client] 'initialize' completed. Sending 'initialized' notification.")
        await self.send_notification("initialized", {})
        print("[LSP Client] Handshake complete.")

    async def send_request(self, method: str, params: Dict[str, Any], timeout: float = 5.0) -> Any:
        if not self.process or self.process.stdin is None:
            raise RuntimeError("LSP Server is not running.")
            
        req_id = self._next_id
        self._next_id += 1
        
        future = asyncio.get_running_loop().create_future()
        self._pending_requests[req_id] = future
        
        msg = {
            "jsonrpc": "2.0",
            "id": req_id,
            "method": method,
            "params": params
        }
        
        payload = json.dumps(msg).encode('utf-8')
        headers = f"Content-Length: {len(payload)}\r\n\r\n".encode('utf-8')
        
        self.process.stdin.write(headers + payload)
        await self.process.stdin.drain()
        
        try:
            response = await asyncio.wait_for(future, timeout=timeout)
            if "error" in response:
                raise Exception(f"LSP Error: {response['error']}")
            return response.get("result")
        except asyncio.TimeoutError:
            self._pending_requests.pop(req_id, None)
            raise TimeoutError(f"LSP Request '{method}' (id={req_id}) timed out.")

    async def send_notification(self, method: str, params: Dict[str, Any]):
        if not self.process or self.process.stdin is None:
            raise RuntimeError("LSP Server is not running.")
            
        msg = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params
        }
        
        payload = json.dumps(msg).encode('utf-8')
        headers = f"Content-Length: {len(payload)}\r\n\r\n".encode('utf-8')
        
        self.process.stdin.write(headers + payload)
        await self.process.stdin.drain()

    async def _read_loop(self):
        try:
            while self.process and self.process.stdout and not self.process.stdout.at_eof():
                # Read headers
                content_length = None
                while True:
                    line_bytes = await self.process.stdout.readline()
                    if not line_bytes:
                        break
                    line = line_bytes.decode('utf-8', errors='ignore').strip()
                    if not line:
                        break # Finished headers
                    if line.lower().startswith("content-length:"):
                        content_length = int(line.split(":")[1].strip())
                
                if content_length is None:
                    if self.process.stdout.at_eof():
                        break
                    continue
                
                # Read body content
                body_bytes = await self.process.stdout.readexactly(content_length)
                body = body_bytes.decode('utf-8', errors='ignore')
                msg = json.loads(body)
                self._handle_message(msg)
        except asyncio.CancelledError:
            pass
        except Exception as e:
            print(f"[LSP Client] Read loop exception: {e}")

    def _handle_message(self, msg: Dict[str, Any]):
        if "id" in msg:
            msg_id = msg["id"]
            future = self._pending_requests.pop(msg_id, None)
            if future and not future.done():
                future.set_result(msg)
        elif "method" in msg:
            method = msg["method"]
            params = msg.get("params", {})
            callbacks = self._notification_callbacks.get(method, [])
            for cb in callbacks:
                try:
                    cb(params)
                except Exception as e:
                    print(f"[LSP Client] Callback error for {method}: {e}")

    # --- Document Synchronisation Helpers ---

    def _file_uri(self, filepath: str) -> str:
        abs_path = os.path.abspath(filepath).replace('\\', '/')
        # Windows absolute paths need file:/// prefix
        if not abs_path.startswith('/'):
            return f"file:///{abs_path}"
        return f"file://{abs_path}"

    async def open_document(self, filepath: str, text: str):
        """Notifies the LSP server that a document has been opened."""
        uri = self._file_uri(filepath)
        self._open_documents[filepath] = 1
        
        params = {
            "textDocument": {
                "uri": uri,
                "languageId": "python",
                "version": 1,
                "text": text
            }
        }
        await self.send_notification("textDocument/didOpen", params)

    async def update_document(self, filepath: str, text: str):
        """Sends the full updated content of a document to the LSP server."""
        if filepath not in self._open_documents:
            await self.open_document(filepath, text)
            return
            
        uri = self._file_uri(filepath)
        version = self._open_documents[filepath] + 1
        self._open_documents[filepath] = version
        
        params = {
            "textDocument": {
                "uri": uri,
                "version": version
            },
            "contentChanges": [
                {
                    "text": text
                }
            ]
        }
        await self.send_notification("textDocument/didChange", params)

    # --- Feature Navigation APIs ---

    async def get_definition(self, filepath: str, line: int, char: int) -> List[Dict[str, Any]]:
        """Query definition coordinates for a symbol at a specific line and character (0-indexed)."""
        uri = self._file_uri(filepath)
        params = {
            "textDocument": { "uri": uri },
            "position": { "line": line, "character": char }
        }
        res = await self.send_request("textDocument/definition", params)
        if not res:
            return []
        if isinstance(res, list):
            return res
        return [res] # Singular location object returned sometimes

    async def get_references(self, filepath: str, line: int, char: int, include_declaration: bool = True) -> List[Dict[str, Any]]:
        """Query all references to a symbol at a specific line and character (0-indexed)."""
        uri = self._file_uri(filepath)
        params = {
            "textDocument": { "uri": uri },
            "position": { "line": line, "character": char },
            "context": { "includeDeclaration": include_declaration }
        }
        res = await self.send_request("textDocument/references", params)
        return res or []

    async def get_hover(self, filepath: str, line: int, char: int) -> Optional[str]:
        """Query hover tooltip documentation for a symbol at a specific line and character (0-indexed)."""
        uri = self._file_uri(filepath)
        params = {
            "textDocument": { "uri": uri },
            "position": { "line": line, "character": char }
        }
        res = await self.send_request("textDocument/hover", params)
        if not res or "contents" not in res:
            return None
            
        contents = res["contents"]
        if isinstance(contents, dict) and "value" in contents:
            return contents["value"]
        elif isinstance(contents, list):
            vals = []
            for item in contents:
                if isinstance(item, dict) and "value" in item:
                    vals.append(item["value"])
                elif isinstance(item, str):
                    vals.append(item)
            return "\n".join(vals)
        elif isinstance(contents, str):
            return contents
        return None

    async def stop(self):
        """Gracefully shuts down the LSP client and processes."""
        if self.process:
            try:
                # Try graceful LSP handshake first while the read task is still running
                if self.process.stdin:
                    await self.send_request("shutdown", {}, timeout=1.0)
                    await self.send_notification("exit", {})
            except Exception as e:
                print(f"[LSP Client] Error during handshake shutdown: {e}")
                
        # Cancel read task
        if self._read_task:
            self._read_task.cancel()
            try:
                await self._read_task
            except asyncio.CancelledError:
                pass
            self._read_task = None
            
        # Cancel any pending requests
        for f in self._pending_requests.values():
            if not f.done():
                f.cancel()
        self._pending_requests.clear()
        
        # Terminate process
        if self.process:
            try:
                self.process.kill()
                await asyncio.wait_for(self.process.wait(), timeout=1.0)
            except Exception:
                try:
                    self.process.terminate()
                except Exception:
                    pass
            self.process = None
        print("[LSP Client] Server stopped.")
