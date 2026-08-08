from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime


class AuditLogResponseSchema(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    audit_id: str
    timestamp: datetime
    actor_type: str
    actor_id: str
    agent: str
    action: str
    entity_type: str
    entity_id: str
    status: str
    decision: str
    confidence: float
    metadata: Dict[str, Any]

    class Config:
        populate_by_name = True


class PaginatedAuditLogsResponseSchema(BaseModel):
    items: List[AuditLogResponseSchema]
    page: int
    limit: int
    total: int
    total_pages: int
