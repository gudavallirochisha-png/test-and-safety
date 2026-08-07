from beanie import Document
from pydantic import Field
from datetime import datetime, timezone
from typing import Optional


class Alert(Document):
    alert_id: str = Field(..., description="Unique alert ID")
    alert_code: str
    title: str
    description: str
    severity: str = "medium"  # low, medium, high, critical
    agent_source: str = "Risk Agent"  # Risk Agent, Review Agent, Authenticity Agent
    target_type: str = "Product"  # Seller, Product, Transaction, User
    target_id: str
    is_resolved: bool = False
    assigned_to: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "alerts"
