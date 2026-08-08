from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Dict, Any, Optional


class AuditLogModel(BaseModel):
    audit_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    actor_type: str = "AGENT"  # AGENT, ANALYST, SYSTEM
    actor_id: str = "SYSTEM"
    agent: str = "Risk Agent"
    action: str  # PRODUCT_VERIFIED, TRANSACTION_ANALYZED, REVIEW_ANALYZED, ALERT_CREATED, ALERT_RESOLVED, MANUAL_REVIEW_STARTED, MANUAL_DECISION_MADE
    entity_type: str
    entity_id: str
    status: str = "PASSED"
    decision: str = "APPROVED"
    confidence: float = 0.95
    metadata: Dict[str, Any] = {}

    def to_dict(self) -> dict:
        return self.model_dump()
