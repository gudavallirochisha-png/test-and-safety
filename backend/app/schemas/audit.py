from pydantic import BaseModel, Field
from datetime import datetime


class AuditLogResponse(BaseModel):
    id: str = Field(..., alias="_id")
    audit_id: str
    agent_name: str
    action: str
    collection: str
    entity_id: str
    status: str
    confidence_score: float
    details: str
    timestamp: datetime

    class Config:
        populate_by_name = True
