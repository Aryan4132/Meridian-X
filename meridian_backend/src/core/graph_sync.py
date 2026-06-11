import os
import json
import time
from typing import List, Dict, Any
from src.tools.knowledge import kg_add_entity, kg_add_relation, kg_add_fact

def scan_workspaces(parent_dir: str = r"C:\Users\aryan\OneDrive\Dokumen\Mini_Project") -> str:
    """Scans parent folder for sub-projects and maps their tech stacks into the MongoDB knowledge graph."""
    if not os.path.exists(parent_dir):
        return f"Error: Parent directory '{parent_dir}' does not exist."
        
    try:
        subdirs = [os.path.join(parent_dir, d) for d in os.listdir(parent_dir) 
                   if os.path.isdir(os.path.join(parent_dir, d)) and not d.startswith(".")]
    except Exception as e:
        return f"Error listing parent directory: {e}"
        
    discovered_projects = []
    
    for path in subdirs:
        project_name = os.path.basename(path)
        
        # Check if it looks like a code project
        is_project = False
        markers = [".git", "package.json", "Cargo.toml", "requirements.txt", "venv", "setup.py", "main.py", "index.html"]
        for marker in markers:
            if os.path.exists(os.path.join(path, marker)):
                is_project = True
                break
                
        if not is_project:
            continue
            
        discovered_projects.append(project_name)
        
        # Extract features
        languages = []
        frameworks = []
        databases = []
        
        # 1. Check Python requirements
        req_path = os.path.join(path, "requirements.txt")
        if os.path.exists(req_path):
            languages.append("Python")
            try:
                with open(req_path, "r", encoding="utf-8", errors="ignore") as f:
                    req_content = f.read().lower()
                if "fastapi" in req_content:
                    frameworks.append("FastAPI")
                if "django" in req_content:
                    frameworks.append("Django")
                if "flask" in req_content:
                    frameworks.append("Flask")
                if "lancedb" in req_content:
                    databases.append("LanceDB")
                if "pymongo" in req_content or "mongodb" in req_content:
                    databases.append("MongoDB")
                if "sqlite" in req_content:
                    databases.append("SQLite")
                if "psycopg2" in req_content:
                    databases.append("PostgreSQL")
            except Exception:
                pass
                
        # 2. Check Node/Javascript package.json
        pkg_path = os.path.join(path, "package.json")
        if os.path.exists(pkg_path):
            languages.append("JavaScript")
            try:
                with open(pkg_path, "r", encoding="utf-8", errors="ignore") as f:
                    pkg_data = json.load(f)
                deps = pkg_data.get("dependencies", {})
                dev_deps = pkg_data.get("devDependencies", {})
                all_deps = {**deps, **dev_deps}
                
                if "react" in all_deps:
                    frameworks.append("React")
                if "vue" in all_deps:
                    frameworks.append("Vue")
                if "typescript" in all_deps:
                    languages.append("TypeScript")
                if "tauri" in all_deps or "@tauri-apps/api" in all_deps:
                    frameworks.append("Tauri")
                if "next" in all_deps:
                    frameworks.append("Next.js")
                if "vite" in all_deps:
                    frameworks.append("Vite")
                if "express" in all_deps:
                    frameworks.append("Express")
                if "mongodb" in all_deps:
                    databases.append("MongoDB")
            except Exception:
                pass
                
        # 3. Check Rust Cargo.toml
        cargo_path = os.path.join(path, "Cargo.toml")
        if os.path.exists(cargo_path):
            languages.append("Rust")
            try:
                with open(cargo_path, "r", encoding="utf-8", errors="ignore") as f:
                    cargo_content = f.read().lower()
                if "tauri" in cargo_content:
                    frameworks.append("Tauri")
                if "tokio" in cargo_content:
                    frameworks.append("Tokio")
                if "axum" in cargo_content:
                    frameworks.append("Axum")
                if "rusqlite" in cargo_content or "sqlx" in cargo_content:
                    databases.append("SQLite")
            except Exception:
                pass
                
        # Deduplicate languages/frameworks
        languages = list(set(languages))
        frameworks = list(set(frameworks))
        databases = list(set(databases))
        
        # If no languages mapped, default based on file extensions in folder
        if not languages:
            has_py = False
            has_js = False
            has_rs = False
            try:
                for root, _, files in os.walk(path):
                    if "node_modules" in root or "venv" in root or ".git" in root:
                        continue
                    for file in files:
                        if file.endswith(".py"):
                            has_py = True
                        elif file.endswith((".js", ".jsx", ".ts", ".tsx")):
                            has_js = True
                        elif file.endswith(".rs"):
                            has_rs = True
                    # Cap recursive walk to avoid performance overhead
                    if len(files) > 50 or (has_py and has_js and has_rs):
                        break
            except Exception:
                pass
            if has_py:
                languages.append("Python")
            if has_js:
                languages.append("JavaScript")
            if has_rs:
                languages.append("Rust")
                
        # Upsert entities and relations to KG
        kg_add_entity(project_name, "project", {
            "path": path,
            "last_scanned": time.time()
        })
        kg_add_fact(project_name, "is_a", "project")
        
        for lang in languages:
            kg_add_entity(lang, "language")
            kg_add_relation(project_name, lang, "uses_language")
            kg_add_fact(project_name, "uses_language", lang)
            
        for fw in frameworks:
            kg_add_entity(fw, "framework")
            kg_add_relation(project_name, fw, "uses_framework")
            kg_add_fact(project_name, "uses_framework", fw)
            
        for db in databases:
            kg_add_entity(db, "database")
            kg_add_relation(project_name, db, "uses_database")
            kg_add_fact(project_name, "uses_database", db)

    return f"Scan complete. Mapped {len(discovered_projects)} projects to Knowledge Graph: {', '.join(discovered_projects)}"
