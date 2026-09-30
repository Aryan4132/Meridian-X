from pydantic import BaseModel, Field
from typing import Any, Dict, List, Literal, Optional

class HealthResponse(BaseModel):
    status: Literal["healthy", "degraded"]
    sqlite: str
    mongodb: str
    ollama: str
    details: Dict[str, Any] = Field(default_factory=dict)

class DiagnosticsResponse(BaseModel):
    status: Literal["success", "error"]
    system: Dict[str, Any]
    databases: Dict[str, Any]
    environment: Dict[str, Any]
    recent_logs: List[str]
    recent_audit_logs: List[Dict[str, Any]]

class RotateKeyResponse(BaseModel):
    status: Literal["success", "failed"]
    message: str
    new_key_prefix: str
