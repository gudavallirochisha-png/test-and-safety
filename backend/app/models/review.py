from beanie import Document
from pydantic import Field
from datetime import datetime, timezone
from typing import List, Dict, Any


class Review(Document):
    review_id: str = Field(..., description="Unique review ID")
    product_id: str
    product_title: str
    reviewer_id: str
    reviewer_name: str
    review_text: str
    rating: int = 5
    distilbert_toxicity_score: float = 0.0
    distilbert_sentiment_score: float = 0.0
    is_fake_review_prob: float = 0.0
    risk_level: str = "low"
    flagged_categories: List[str] = []
    status: str = "PUBLISHED"  # PUBLISHED, REJECTED, PENDING_MODERATION
    reviewer_history_stats: Dict[str, Any] = {}
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "reviews"
