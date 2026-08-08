from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import List, Optional


class ProductModel(BaseModel):
    product_id: str
    seller_id: str
    name: str
    brand: str = "Generic"
    category: str = "General"
    description: str = ""
    price: float
    currency: str = "USD"
    image_urls: List[str] = []
    status: str = "VERIFIED"
    authenticity_score: float = 95.0
    counterfeit_probability: float = 0.05
    verification_status: str = "VERIFIED"  # PENDING, VERIFIED, FLAGGED, REJECTED, MANUAL_REVIEW
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict:
        data = self.model_dump()
        return data
