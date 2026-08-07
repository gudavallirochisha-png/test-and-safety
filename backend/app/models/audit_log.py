from beanie import Document
from pydantic import Field
from datetime import datetime, timezone


class AuditLog(Document):
    audit_id: str = Field(..., description="Unique audit log ID")
    agent_name: str = "System Automated Engine"
    action: str  # CREATE, UPDATE, DELETE, APPROVE, REJECT, QUARANTINE, FLAG
    collection: str  # products, transactions, reviews, alerts
    entity_id: str
    status: str = "passed"  # passed, flagged, quarantined, escalated
    confidence_score: float = 100.0
    details: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "audit_logs"
