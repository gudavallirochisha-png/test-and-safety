from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional


class AlertModel(BaseModel):
    alert_id: str
    type: str = "SECURITY_VELOCITY"
    severity: str = "MEDIUM"  # LOW, MEDIUM, HIGH, CRITICAL
    agent: str = "Risk Agent"
    entity_type: str = "Transaction"
    entity_id: str
    title: str
    description: str
    confidence: float = 0.90
    status: str = "OPEN"  # OPEN, INVESTIGATING, RESOLVED, DISMISSED
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    resolved_at: Optional[datetime] = None
    resolution_notes: Optional[str] = None

    def to_dict(self) -> dict:
        return self.model_dump()
