from beanie import Document
from pydantic import Field
from datetime import datetime, timezone


class Seller(Document):
    seller_id: str = Field(..., description="Unique seller identifier")
    name: str
    risk_score: float = 0.0
    risk_level: str = "low"
    total_sales_count: int = 0
    is_verified: bool = True
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "sellers"
