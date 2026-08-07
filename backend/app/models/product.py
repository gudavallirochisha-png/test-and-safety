from beanie import Document
from pydantic import Field
from datetime import datetime, timezone
from typing import List, Dict, Any


class Product(Document):
    product_id: str = Field(..., description="Unique product identifier")
    product_name: str
    seller_id: str
    seller_name: str
    category: str
    price: float
    image_url: str
    authenticity_score: float = 100.0
    risk_level: str = "low"
    status: str = "VERIFIED"  # VERIFIED, COUNTERFEIT_FLAGGED, MANUAL_REVIEW
    yolo_detections: List[Dict[str, Any]] = []
    flagged_reasons: List[str] = []
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "products"
