from beanie import Document
from pydantic import Field
from datetime import datetime, timezone
from typing import List


class Transaction(Document):
    txn_id: str = Field(..., description="Unique transaction ID")
    order_id: str
    customer_id: str
    customer_name: str
    seller_id: str
    seller_name: str
    amount: float
    payment_method: str
    ip_address: str
    device_fingerprint: str
    location: str
    xgboost_risk_score: float = 0.0
    risk_level: str = "low"
    fraud_factors: List[str] = []
    recommendation: str = "APPROVE"
    status: str = "APPROVED"  # APPROVED, BLOCKED, FLAGGED_FOR_REVIEW
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "transactions"
