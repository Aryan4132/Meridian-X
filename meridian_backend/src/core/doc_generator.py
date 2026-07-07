import os
import re

def parse_imports_in_file(file_path: str) -> list:
    """Parses imports in a python or typescript/javascript file."""
    imports = []
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".py":
        # Heuristics for Python imports
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("import ") or line.startswith("from "):
                        # Extract module names
                        parts = line.split()
                        if len(parts) >= 2:
                            module = parts[1].split(".")[0]
                            if module and module not in imports:
                                imports.append(module)
        except Exception:
            pass
    elif ext in [".js", ".jsx", ".ts", ".tsx"]:
        # Heuristics for JS/TS imports
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    line = line.strip()
                    # e.g., import x from './y' or import './y'
                    match = re.search(r'import\s+.*\s+from\s+[\'"]([^\'"]+)[\'"]', line)
                    if not match:
                        match = re.search(r'import\s+[\'"]([^\'"]+)[\'"]', line)
                    if match:
                        imported_path = match.group(1)
                        # Extract basename or module name
                        module = imported_path.split("/")[-1].replace(".ts", "").replace(".tsx", "").replace(".js", "")
                        if module and module not in imports:
                            imports.append(module)
        except Exception:
            pass
            
    return imports

def generate_mermaid_docs(workspace_dir: str = None) -> str:
    """Scans the workspace, builds dependency map, writes Mermaid architectural docs."""
    from src.core.history_manager import find_workspace_root
    if workspace_dir is None:
        workspace_dir = find_workspace_root()
        
    exclude_dirs = {
        "venv", ".venv", "env", "node_modules", ".git", "dist", "build", 
        "meridian_memory", "__pycache__", ".antigravitycli", ".codegraph",
        "dist-ssr", "target"
    }
    
    dependency_graph = {}
    
    for root, dirs, files in os.walk(workspace_dir):
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in [".py", ".ts", ".tsx", ".js", ".jsx"]:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, workspace_dir).replace("\\", "/")
                
                # Extract imports
                imports = parse_imports_in_file(full_path)
                if imports:
                    dependency_graph[rel_path] = imports
                    
    # Generate Mermaid Chart content
    lines = [
        "# Workspace Architecture & Component Map",
        "Generated automatically by Meridian-X.",
        "",
        "## Component Dependency Graph",
        "```mermaid",
        "graph TD"
    ]
    
    # We will map files to node IDs to prevent Mermaid syntax errors
    node_ids = {}
    node_counter = 1
    
    # First, declare nodes with readable labels
    for file_path in dependency_graph.keys():
        if file_path not in node_ids:
            node_ids[file_path] = f"N{node_counter}"
            node_counter += 1
            
    for file_path, imports in dependency_graph.items():
        nid = node_ids[file_path]
        label = file_path.split("/")[-1]
        dir_label = os.path.dirname(file_path).replace("(", "").replace(")", "")
        lines.append(f'    {nid}["{label} [{dir_label}]"]')
        
    lines.append("")
    
    # Render edges
    for file_path, imports in dependency_graph.items():
        nid = node_ids[file_path]
        for imp in imports:
            # Check if this import matches any of our workspace files (fuzzy match)
            for other_path, other_nid in node_ids.items():
                other_name = other_path.split("/")[-1].split(".")[0]
                if imp == other_name and other_path != file_path:
                    lines.append(f"    {nid} --> {other_nid}")
                    
    lines.append("```")
    lines.append("")
    lines.append("## Detailed File Index")
    for file_path in sorted(dependency_graph.keys()):
        lines.append(f"- **{file_path}**")
        for imp in sorted(dependency_graph[file_path]):
            lines.append(f"  - Imports: `{imp}`")
            
    doc_content = "\n".join(lines)
    
    # Write to .meridian/docs/architecture.md
    docs_dir = os.path.join(workspace_dir, ".meridian", "docs")
    os.makedirs(docs_dir, exist_ok=True)
    doc_path = os.path.join(docs_dir, "architecture.md")
    
    with open(doc_path, "w", encoding="utf-8") as f:
        f.write(doc_content)
        
    print(f"[Doc Generator] Successfully generated architecture doc at: {doc_path}")
    return doc_path
