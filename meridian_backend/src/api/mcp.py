import os
import json
import shutil
import tempfile
import subprocess
from typing import Optional, List, Dict, Any
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from src.core.mcp_client import mcp_manager

router = APIRouter(tags=["mcp"])

CORE_SKILLS = set()
SKILLS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".opencode")

def initialize_core_skills():
    global CORE_SKILLS
    if os.path.exists(SKILLS_DIR):
        for item in os.listdir(SKILLS_DIR):
            item_path = os.path.join(SKILLS_DIR, item)
            if os.path.isdir(item_path):
                if os.path.exists(os.path.join(item_path, "SKILL.md")):
                    CORE_SKILLS.add(item)

initialize_core_skills()

class MCPToolRegisterRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Unique identifier for the tool")
    description: str = Field(..., max_length=500, description="Human-readable description of what the tool does")
    tier: int = Field(1, ge=1, le=3, description="Security tier: 0=read-only, 1=safe mutations, 2=high-risk")
    input_schema: Dict[str, Any] = Field(default_factory=dict, description="JSON Schema for tool input parameters")
    output_schema: Dict[str, Any] = Field(default_factory=dict, description="JSON Schema for tool output")
    supports_streaming: bool = Field(False, description="Whether the tool supports streaming responses")
    handler_module: str = Field(..., description="Python module path containing the tool implementation")
    handler_function: str = Field(..., description="Function name within the module to execute")

class SaveMcpConfig(BaseModel):
    mcpServers: Dict[str, Any]

class MCPInstallRequest(BaseModel):
    server_id: str

class AddMCPServerRequest(BaseModel):
    name: str
    command: str
    args: Optional[List[str]] = []
    env: Optional[Dict[str, str]] = {}

class SkillInstallRequest(BaseModel):
    github_url: str = Field(..., description="GitHub repository URL to install the skill from (must contain a SKILL.md file)")

class SkillUninstallRequest(BaseModel):
    skill_name: str = Field(..., min_length=1, description="Name of the skill to uninstall")

class SkillInfo(BaseModel):
    name: str
    description: str
    path: str
    is_core: bool

class ToolGenerateRequest(BaseModel):
    prompt: str

@router.get("/api/mcp/v1/tools")
def get_mcp_reverse_tools():
    """Exposes Meridian's registered tools as an MCP Server for external IDEs (DEV-02)."""
    from src.tools.registry import TOOL_REGISTRY
    mcp_tools = []
    for name, tool in TOOL_REGISTRY.items():
        mcp_tools.append({
            "name": name,
            "description": tool.get("description", ""),
            "tier": tool.get("tier", 1),
            "inputSchema": {"type": "object", "properties": {}},
            "outputSchema": {"type": "object", "properties": {}},
            "supportsStreaming": tool.get("supportsStreaming", False)
        })
    return {"status": "success", "tools": mcp_tools}

@router.post("/api/mcp/v1/tools/register")
def register_mcp_tool(request: MCPToolRegisterRequest):
    """Dynamically register a new MCP tool at runtime."""
    try:
        from src.tools.registry import register_tool
        
        metadata = {
            "name": request.name,
            "description": request.description,
            "tier": request.tier,
            "inputSchema": request.input_schema,
            "outputSchema": request.output_schema,
            "supportsStreaming": request.supports_streaming,
            "handlerModule": request.handler_module,
            "handlerFunction": request.handler_function
        }
        
        success = register_tool(request.name, metadata)
        if success:
            return {
                "status": "success",
                "message": f"MCP tool '{request.name}' registered successfully",
                "tool": {
                    "name": request.name,
                    "description": request.description,
                    "tier": request.tier,
                    "supportsStreaming": request.supports_streaming
                }
            }
        else:
            raise HTTPException(status_code=400, detail=f"Failed to register MCP tool '{request.name}'")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/api/mcp/v1/tools/{tool_name}")
def unregister_mcp_tool(tool_name: str):
    """Unregister an MCP tool at runtime."""
    try:
        from src.tools.registry import unregister_tool
        success = unregister_tool(tool_name)
        if success:
            return {"status": "success", "message": f"MCP tool '{tool_name}' unregistered successfully"}
        else:
            raise HTTPException(status_code=404, detail=f"MCP tool '{tool_name}' not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/mcp/config")
def get_mcp_config_route():
    config_path = "mcp_config.json"
    if not os.path.exists(config_path):
        return {"mcpServers": {}}
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return {"mcpServers": {}}
            return json.loads(content)
    except Exception:
        return {"mcpServers": {}}

@router.post("/api/mcp/config")
async def save_mcp_config_route(request: SaveMcpConfig):
    config_path = "mcp_config.json"
    try:
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump({"mcpServers": request.mcpServers}, f, indent=2)
            
        await mcp_manager.shutdown()
        await mcp_manager.initialize()
        return {"status": "success", "message": "MCP configuration updated and servers hot-reloaded."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/mcp/servers")
def api_list_mcp_servers():
    try:
        from src.tools.mcp_marketplace import mcp_marketplace_instance
        return {"status": "success", "servers": mcp_marketplace_instance.list_available_servers()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/mcp/install")
def api_install_mcp_server(req: MCPInstallRequest):
    try:
        from src.tools.mcp_marketplace import mcp_marketplace_instance
        res = mcp_marketplace_instance.install_mcp_server(req.server_id)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/mcp/custom")
def api_list_custom_mcp_servers():
    try:
        from src.tools.mcp_marketplace import mcp_marketplace_instance
        return {"status": "success", "servers": mcp_marketplace_instance.list_custom_servers()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/mcp/custom")
def api_add_custom_mcp_server(req: AddMCPServerRequest):
    try:
        from src.tools.mcp_marketplace import mcp_marketplace_instance
        res = mcp_marketplace_instance.add_custom_server(
            name=req.name,
            command=req.command,
            args=req.args or [],
            env=req.env or {}
        )
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/api/mcp/custom/{server_name}")
def api_delete_custom_mcp_server(server_name: str):
    try:
        from src.tools.mcp_marketplace import mcp_marketplace_instance
        success = mcp_marketplace_instance.delete_custom_server(server_name)
        if success:
            return {"status": "success", "message": f"Deleted custom server '{server_name}'."}
        raise HTTPException(status_code=404, detail="Server not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/skills/list", response_model=List[SkillInfo])
def list_skills():
    """List all available skills in the .opencode directory."""
    skills = []
    if os.path.exists(SKILLS_DIR):
        for item in os.listdir(SKILLS_DIR):
            item_path = os.path.join(SKILLS_DIR, item)
            if os.path.isdir(item_path):
                skill_md_path = os.path.join(item_path, "SKILL.md")
                if os.path.exists(skill_md_path):
                    description = "No description available"
                    try:
                        with open(skill_md_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            lines = content.split('\n')
                            for line in lines:
                                if line.strip() and not line.strip().startswith('#'):
                                    description = line.strip()[:100]
                                    break
                                elif line.strip().startswith('# '):
                                    description = line.strip()[2:].strip()[:100]
                                    break
                    except Exception:
                        pass
                    skills.append(SkillInfo(
                        name=item,
                        description=description,
                        path=item_path,
                        is_core=item in CORE_SKILLS
                    ))
    return skills

@router.post("/api/skills/install")
def install_skill(request: SkillInstallRequest):
    """Install a new skill from a GitHub repository."""
    github_url = request.github_url.strip()
    if not github_url:
        raise HTTPException(status_code=400, detail="GitHub URL is required")
    
    if not (github_url.startswith("https://github.com/") or github_url.startswith("git@github.com:")):
        raise HTTPException(status_code=400, detail="Only GitHub URLs are supported")
    
    temp_dir = None
    try:
        temp_dir = tempfile.mkdtemp(prefix="meridian_skill_")
        result = subprocess.run(
            ["git", "clone", github_url, temp_dir],
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode != 0:
            raise HTTPException(status_code=400, detail=f"Failed to clone repository: {result.stderr}")
        
        skill_dirs = []
        for root, dirs, files in os.walk(temp_dir):
            if "SKILL.md" in files:
                skill_dirs.append(root)
        
        if not skill_dirs:
            raise HTTPException(status_code=400, detail="No SKILL.md file found in the repository")
        
        skill_source_dir = skill_dirs[0]
        skill_name = os.path.basename(skill_source_dir)
        
        skill_target_dir = os.path.join(SKILLS_DIR, skill_name)
        if os.path.exists(skill_target_dir):
            raise HTTPException(status_code=409, detail=f"Skill '{skill_name}' already exists")
        
        if skill_name in CORE_SKILLS:
            raise HTTPException(status_code=409, detail=f"Cannot install over core skill '{skill_name}'")
        
        shutil.copytree(skill_source_dir, skill_target_dir)
        CORE_SKILLS.add(skill_name)
        
        return {
            "status": "success",
            "message": f"Skill '{skill_name}' installed successfully",
            "skill": {
                "name": skill_name,
                "path": skill_target_dir
            }
        }
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=408, detail="Git clone timeout")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)

@router.post("/api/skills/uninstall")
def uninstall_skill(request: SkillUninstallRequest):
    """Uninstall a skill by name."""
    skill_name = request.skill_name.strip()
    if not skill_name:
        raise HTTPException(status_code=400, detail="Skill name is required")
    
    skill_dir = os.path.join(SKILLS_DIR, skill_name)
    if not os.path.exists(skill_dir):
        raise HTTPException(status_code=404, detail=f"Skill '{skill_name}' not found")
    
    if skill_name in CORE_SKILLS:
        raise HTTPException(status_code=409, detail=f"Cannot uninstall core skill '{skill_name}'. Core skills are essential to the system.")
    
    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    if not os.path.exists(skill_md_path):
        raise HTTPException(status_code=400, detail=f"'{skill_name}' is not a valid skill directory")
    
    try:
        shutil.rmtree(skill_dir)
        if skill_name in CORE_SKILLS:
            CORE_SKILLS.remove(skill_name)
        return {"status": "success", "message": f"Skill '{skill_name}' uninstalled successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/tools/generate")
def api_generate_tool(request: ToolGenerateRequest):
    try:
        from src.tools.dynamic_manager import generate_dynamic_tool
        result = generate_dynamic_tool(request.prompt)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
