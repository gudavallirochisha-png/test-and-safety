from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import List, Optional


class TransactionModel(BaseModel):
    transaction_id: str
    customer_id: str
    product_id: str = "PROD-1001"
    seller_id: str = "SELL-8812"
    amount: float
    currency: str = "USD"
    payment_method: str = "Credit Card"
    account_age_days: int = 30
    device_id: str = "dev-fp-default"
    ip_address: str = "127.0.0.1"
    location: str = "San Francisco, CA"
    order_history_count: int = 5
    return_history_count: int = 0
    risk_score: float = 0.15
    risk_level: str = "LOW"  # LOW, MEDIUM, HIGH, CRITICAL
    decision: str = "APPROVED"  # APPROVED, MANUAL_REVIEW, BLOCKED
    risk_factors: List[str] = []
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict:
        return self.model_dump()
