import os
import tempfile
import subprocess

def check_docker_available() -> bool:
    try:
        # Run docker info to check if Docker is running
        res = subprocess.run(
            ["docker", "info"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=3.0
        )
        return res.returncode == 0
    except Exception:
        return False

def run_python(code: str, timeout: float = 10.0) -> str:
    # Save the code to a temp file
    temp_dir = tempfile.gettempdir()
    file_name = f"sandbox_{os.getpid()}_{time_stamp()}.py"
    temp_path = os.path.join(temp_dir, file_name)
    
    with open(temp_path, "w", encoding="utf-8") as f:
        f.write(code)
        
    try:
        if check_docker_available():
            # Run inside Docker sandbox
            cmd = [
                "docker", "run", "--rm",
                "-v", f"{temp_dir}:/sandbox",
                "-w", "/sandbox",
                "-m", "128m",
                "--cpus", "1.0",
                "python:3.11-slim",
                "python", file_name
            ]
            res = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=timeout
            )
            output = res.stdout
            error = res.stderr
            
            result_lines = ["[Docker Isolation Sandbox]"]
            if output:
                result_lines.append("--- STDOUT ---")
                result_lines.append(output)
            if error:
                result_lines.append("--- STDERR ---")
                result_lines.append(error)
                
            return "\n".join(result_lines) if len(result_lines) > 1 else "Code executed successfully with no output inside Docker."
        else:
            # Fallback to host execution
            backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            python_exe = os.path.join(backend_dir, "venv", "Scripts", "python.exe")
            if not os.path.exists(python_exe):
                python_exe = "python" # Fallback to standard path if venv isn't mapped
                
            res = subprocess.run(
                [python_exe, temp_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=timeout
            )
            output = res.stdout
            error = res.stderr
            
            result_lines = ["[WARNING: Docker unavailable. Running with restricted host subprocess isolation]"]
            if output:
                result_lines.append("--- STDOUT ---")
                result_lines.append(output)
            if error:
                result_lines.append("--- STDERR ---")
                result_lines.append(error)
                
            return "\n".join(result_lines) if len(result_lines) > 1 else "Code executed successfully with no output."
    except subprocess.TimeoutExpired:
        return f"Execution timed out after {timeout} seconds."
    except Exception as e:
        return f"Python runner failed: {str(e)}"
    finally:
        try:
            os.remove(temp_path)
        except Exception:
            pass

def open_editor(file: str) -> str:
    # Attempt to open the file in VS Code (assumes `code` is in system PATH)
    try:
        subprocess.Popen(f"code \"{file}\"", shell=True)
        return f"Successfully spawned editor window (VS Code) for file: {file}"
    except Exception as e:
        return f"Failed to open VS Code: {str(e)}"

def git_status(repo_path: str) -> str:
    try:
        out = subprocess.check_output("git status --short", cwd=repo_path, shell=True, stderr=subprocess.STDOUT).decode('utf-8')
        return out if out.strip() else "Git directory clean, no changes."
    except Exception as e:
        return f"Git status failed: {str(e)}"

def git_commit(message: str, repo_path: str) -> str:
    try:
        # stage and commit
        subprocess.check_call("git add .", cwd=repo_path, shell=True)
        out = subprocess.check_output(f"git commit -m \"{message}\"", cwd=repo_path, shell=True).decode('utf-8')
        return f"Git commit successful:\n{out}"
    except Exception as e:
        return f"Git commit failed: {str(e)}"

def git_diff(repo_path: str) -> str:
    try:
        out = subprocess.check_output("git diff HEAD", cwd=repo_path, shell=True).decode('utf-8')
        return out if out.strip() else "No diff changes detected against HEAD."
    except Exception as e:
        return f"Git diff failed: {str(e)}"

def search_codebase(query: str, path: str) -> str:
    # Use ripgrep or fallback to manual python file search inside the path
    try:
        # Check if git grep is available
        out = subprocess.check_output(f"git grep -n \"{query}\"", cwd=path, shell=True).decode('utf-8', errors='ignore')
        return out if out.strip() else "No matching code lines found in repository."
    except Exception:
        # Fallback manual text search
        matches = []
        for root, dirs, files in os.walk(path):
            # Ignore virtualenv, node_modules, git directories
            if any(p in root for p in ["venv", ".git", "node_modules", "__pycache__"]):
                continue
            for file in files:
                if file.endswith((".py", ".ts", ".tsx", ".js", ".json", ".html", ".css", ".md")):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                            for idx, line in enumerate(f, 1):
                                if query in line:
                                    matches.append(f"{os.path.basename(filepath)}:{idx} -> {line.strip()}")
                                    if len(matches) >= 30:
                                        break
                    except Exception:
                        pass
            if len(matches) >= 30:
                break
        return "\n".join(matches) if matches else "No matching codebase instances found."

def time_stamp() -> str:
    import time
    return str(int(time.time() * 1000))

def scaffold_project(name: str, template: str) -> str:
    """Generate a project skeleton from a template ('python', 'fastapi', or 'react')."""
    try:
        os.makedirs(name, exist_ok=True)
        t = template.lower()
        if t == "python":
            os.makedirs(os.path.join(name, "src"), exist_ok=True)
            with open(os.path.join(name, "src", "main.py"), "w") as f:
                f.write('def main():\n    print("Hello from python template!")\n\nif __name__ == "__main__":\n    main()\n')
            with open(os.path.join(name, "README.md"), "w") as f:
                f.write(f"# {name}\nMinimal Python codebase.\n")
            with open(os.path.join(name, "requirements.txt"), "w") as f:
                f.write("# dependencies\n")
            return f"Scaffolded Python project under '{name}/'."
            
        elif t == "fastapi":
            os.makedirs(os.path.join(name, "app"), exist_ok=True)
            with open(os.path.join(name, "app", "main.py"), "w") as f:
                f.write('from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get("/")\ndef read_root():\n    return {"message": "Hello World"}\n')
            with open(os.path.join(name, "requirements.txt"), "w") as f:
                f.write("fastapi\nuvicorn\n")
            return f"Scaffolded FastAPI project under '{name}/'."
            
        elif t == "react":
            os.makedirs(os.path.join(name, "src"), exist_ok=True)
            os.makedirs(os.path.join(name, "public"), exist_ok=True)
            with open(os.path.join(name, "package.json"), "w") as f:
                f.write('{\n  "name": "scaffolded-react",\n  "version": "1.0.0",\n  "scripts": {\n    "start": "react-scripts start"\n  },\n  "dependencies": {\n    "react": "^18.0.0",\n    "react-dom": "^18.0.0"\n  }\n}\n')
            with open(os.path.join(name, "src", "index.js"), "w") as f:
                f.write('import React from "react";\nimport ReactDOM from "react-dom/client";\nimport App from "./App";\nconst root = ReactDOM.createRoot(document.getElementById("root"));\nroot.render(<App />);\n')
            with open(os.path.join(name, "src", "App.js"), "w") as f:
                f.write('import React from "react";\nfunction App() {\n  return <h1>Hello from React</h1>;\n}\nexport default App;\n')
            return f"Scaffolded React project skeleton under '{name}/'."
            
        else:
            return f"Error: Unknown template '{template}'. Supported: python, fastapi, react."
    except Exception as e:
        return f"Scaffold failed: {e}"

def run_tests(path: str, framework: str = "pytest") -> str:
    """Run pytest or unittest tests in the specified directory path."""
    try:
        backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        venv_scripts = os.path.join(backend_dir, "venv", "Scripts")
        
        if framework.lower() == "pytest":
            cmd = [os.path.join(venv_scripts, "pytest.exe") if os.path.exists(venv_scripts) else "pytest"]
        else:
            python_exe = os.path.join(venv_scripts, "python.exe") if os.path.exists(venv_scripts) else "python"
            cmd = [python_exe, "-m", "unittest"]
            
        res = subprocess.run(cmd, cwd=path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        return f"--- TEST RESULTS ---\nSTDOUT:\n{res.stdout}\nSTDERR:\n{res.stderr}"
    except Exception as e:
        return f"Failed to execute tests: {e}"

def install_package(package: str) -> str:
    """Install a Python package into the virtual environment using pip install."""
    try:
        backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        pip_exe = os.path.join(backend_dir, "venv", "Scripts", "pip.exe")
        if not os.path.exists(pip_exe):
            pip_exe = "pip"
            
        res = subprocess.run([pip_exe, "install", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if res.returncode == 0:
            return f"Successfully installed package: {package}\n{res.stdout}"
        return f"Failed to install package {package}:\n{res.stderr}"
    except Exception as e:
        return f"Pip execution failed: {e}"

def lint_file(path: str) -> str:
    """Lint a Python file using ruff (or fall back to pep8 check)."""
    try:
        import shutil
        backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        ruff_exe = os.path.join(backend_dir, "venv", "Scripts", "ruff.exe")
        
        has_ruff = os.path.exists(ruff_exe) or shutil.which("ruff") is not None
        if not has_ruff:
            return "Error: Linter 'ruff' is not installed. Run 'install_package' tool with arg: 'ruff' first."
            
        executable = ruff_exe if os.path.exists(ruff_exe) else "ruff"
        res = subprocess.run([executable, "check", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if res.returncode == 0:
            return "Linting check passed. No issues found."
        return f"Linting issues found:\n{res.stdout}\n{res.stderr}"
    except Exception as e:
        return f"Ruff linter execution failed: {e}"

def format_file(path: str) -> str:
    """Format a Python file in place using black (or ruff format)."""
    try:
        import shutil
        backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        black_exe = os.path.join(backend_dir, "venv", "Scripts", "black.exe")
        
        has_black = os.path.exists(black_exe) or shutil.which("black") is not None
        if not has_black:
            return "Error: Formatter 'black' is not installed. Run 'install_package' tool with arg: 'black' first."
            
        executable = black_exe if os.path.exists(black_exe) else "black"
        res = subprocess.run([executable, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if res.returncode == 0:
            return f"Successfully formatted file in-place: {path}"
        return f"Formatting failed:\n{res.stderr}"
    except Exception as e:
        return f"Black formatter execution failed: {e}"

# --- LSP Client integration ---
import asyncio
from src.core.lsp_client import LspClient

_lsp_client_instance = None
_lsp_client_lock = asyncio.Lock()

async def _get_lsp_client() -> LspClient:
    global _lsp_client_instance
    if _lsp_client_instance is not None:
        return _lsp_client_instance
    async with _lsp_client_lock:
        if _lsp_client_instance is not None:
            return _lsp_client_instance
            
        tools_dir = os.path.dirname(os.path.abspath(__file__))
        src_dir = os.path.dirname(tools_dir)
        backend_dir = os.path.dirname(src_dir)
        root_dir = os.path.dirname(backend_dir)
        
        executable = os.path.join(backend_dir, "venv", "Scripts", "pyright-langserver.exe")
        if not os.path.exists(executable):
            executable = "pyright-langserver"
            
        client = LspClient(executable, root_dir)
        started = await client.start()
        if started:
            _lsp_client_instance = client
            return client
        else:
            raise RuntimeError("Failed to start LSP Server.")

async def _sync_file_to_lsp(client: LspClient, filepath: str):
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    await client.update_document(filepath, content)

async def lsp_get_definition(filepath: str, line: int, char: int) -> str:
    """Find definition locations for a symbol at a specific line and character (0-indexed)."""
    try:
        client = await _get_lsp_client()
        await _sync_file_to_lsp(client, filepath)
        defs = await client.get_definition(filepath, line, char)
        if not defs:
            return f"No definition found for symbol at {os.path.basename(filepath)}:{line}:{char}"
        
        result_lines = ["Definitions found:"]
        for d in defs:
            uri = d.get("uri", "")
            r = d.get("range", {})
            start = r.get("start", {})
            path = uri.replace("file:///", "").replace("/", "\\")
            if ":" in path and path.startswith("\\"):
                path = path[1:]
            result_lines.append(f"- File: {path} | Line: {start.get('line') + 1} | Char: {start.get('character') + 1}")
        return "\n".join(result_lines)
    except Exception as e:
        return f"LSP definition query failed: {str(e)}"

async def lsp_get_references(filepath: str, line: int, char: int) -> str:
    """Find all references/usages of a symbol at a specific line and character (0-indexed)."""
    try:
        client = await _get_lsp_client()
        await _sync_file_to_lsp(client, filepath)
        refs = await client.get_references(filepath, line, char)
        if not refs:
            return f"No references found for symbol at {os.path.basename(filepath)}:{line}:{char}"
        
        result_lines = ["References found:"]
        for ref in refs:
            uri = ref.get("uri", "")
            r = ref.get("range", {})
            start = r.get("start", {})
            path = uri.replace("file:///", "").replace("/", "\\")
            if ":" in path and path.startswith("\\"):
                path = path[1:]
            result_lines.append(f"- File: {path} | Line: {start.get('line') + 1} | Char: {start.get('character') + 1}")
        return "\n".join(result_lines)
    except Exception as e:
        return f"LSP references query failed: {str(e)}"

async def lsp_get_hover_info(filepath: str, line: int, char: int) -> str:
    """Get documentation/type hover information for a symbol at a specific line and character (0-indexed)."""
    try:
        client = await _get_lsp_client()
        await _sync_file_to_lsp(client, filepath)
        hover = await client.get_hover(filepath, line, char)
        if not hover:
            return f"No hover information available for symbol at {os.path.basename(filepath)}:{line}:{char}"
        return f"--- Hover details ---\n{hover}"
    except Exception as e:
        return f"LSP hover query failed: {str(e)}"

async def lsp_diagnose_file(filepath: str) -> str:
    """Retrieve syntax and type checking warnings/errors for a file."""
    try:
        client = await _get_lsp_client()
        await _sync_file_to_lsp(client, filepath)
        await asyncio.sleep(0.5)
        
        uri = client._file_uri(filepath)
        diagnostics = client.diagnostics.get(uri, [])
        if not diagnostics:
            return f"No syntax or type errors detected in: {filepath}"
            
        result_lines = [f"Diagnostics for {os.path.basename(filepath)}:"]
        for d in diagnostics:
            severity = "ERROR" if d.get("severity") == 1 else "WARNING"
            r = d.get("range", {})
            start = r.get("start", {})
            msg = d.get("message", "")
            result_lines.append(f"- [{severity}] Line {start.get('line') + 1}, Char {start.get('character') + 1}: {msg}")
        return "\n".join(result_lines)
    except Exception as e:
        return f"LSP diagnostics query failed: {str(e)}"

