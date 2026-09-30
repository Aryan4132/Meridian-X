import os
import ast
import logging
from typing import Dict, List, Any, Set

class DeepProjectContextEngine:
    """
    Deep Project Context Engine (🧠)
    Scans project workspace AST graph, tracks imports, functions, classes, and exported symbols.
    Provides live connection map and suggests potential bugs/optimizations pre-execution.
    """
    def __init__(self, workspace_root: str):
        self.workspace_root = workspace_root
        self.file_map: Dict[str, Dict[str, Any]] = {}
        self.symbol_graph: Dict[str, Set[str]] = {}

    def scan_workspace(self) -> Dict[str, Any]:
        """Scans workspace python files and generates symbol connection graph."""
        file_count = 0
        total_symbols = 0
        optimizations: List[Dict[str, Any]] = []

        ignore_dirs = {'.git', '__pycache__', 'node_modules', '.venv', 'venv', 'env', '.env', 'dist', 'build', '.codegraph', 'target'}
        for root, dirs, files in os.walk(self.workspace_root):
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.workspace_root)
                    file_data = self._analyze_file(file_path, rel_path)
                    self.file_map[rel_path] = file_data
                    file_count += 1
                    total_symbols += len(file_data.get("functions", [])) + len(file_data.get("classes", []))

                    # Analyze optimizations / potential bugs
                    if file_data.get("unused_imports"):
                        optimizations.append({
                            "file": rel_path,
                            "type": "unused_import",
                            "message": f"Unused imports detected: {', '.join(file_data['unused_imports'])}",
                            "severity": "info"
                        })
                    if file_data.get("bare_excepts"):
                        optimizations.append({
                            "file": rel_path,
                            "type": "bare_except",
                            "message": "Bare 'except:' block found. Consider catching specific exceptions.",
                            "severity": "warning"
                        })

        return {
            "status": "indexed",
            "files_scanned": file_count,
            "total_symbols": total_symbols,
            "suggestions": optimizations
        }

    def _analyze_file(self, full_path: str, rel_path: str) -> Dict[str, Any]:
        functions = []
        classes = []
        imports = []
        bare_excepts = 0

        try:
            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            tree = ast.parse(content, filename=rel_path)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
                    functions.append(node.name)
                elif isinstance(node, ast.ClassDef):
                    classes.append(node.name)
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.append(node.module)
                elif isinstance(node, ast.ExceptHandler):
                    if node.type is None:
                        bare_excepts += 1
        except Exception as e:
            logging.debug(f"Failed to parse AST for {rel_path}: {e}")

        return {
            "path": rel_path,
            "functions": functions,
            "classes": classes,
            "imports": imports,
            "bare_excepts": bare_excepts,
            "unused_imports": []
        }

    def get_file_connections(self, target_file: str) -> Dict[str, Any]:
        """Returns connection graph for a target file."""
        data = self.file_map.get(target_file, {})
        imported_by = [
            f for f, info in self.file_map.items()
            if any(target_file.replace('/', '.').replace('.py', '') in imp for imp in info.get("imports", []))
        ]
        return {
            "file": target_file,
            "imports": data.get("imports", []),
            "imported_by": imported_by,
            "symbols": data.get("functions", []) + data.get("classes", [])
        }
