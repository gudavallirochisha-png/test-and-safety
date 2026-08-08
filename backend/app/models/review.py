from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import List, Optional


class ReviewModel(BaseModel):
    review_id: str
    product_id: str
    customer_id: str
    rating: int = 5
    review_text: str
    verified_purchase: bool = True
    fake_probability: float = 0.05
    authenticity_score: float = 95.0
    decision: str = "APPROVED"  # APPROVED, FLAGGED, REJECTED, MANUAL_REVIEW
    risk_factors: List[str] = []
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict:
        return self.model_dump()
