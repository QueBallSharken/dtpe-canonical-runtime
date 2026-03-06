from pydantic import BaseModel
from typing import Any, Dict, Optional


class ExecuteRequest(BaseModel):
    identity_id: str
    owner_id: str
    intent: str
    action: str
    params: Optional[Dict[str, Any]] = None


class ExecuteResponse(BaseModel):
    allow: bool
    execution_state: str
    reasons: list[str]
