from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime


class ReviewCreate(BaseModel):
    product_id: str = Field(..., example="PROD-9021")
    product_title: str = Field(..., example="Luxury Designer Leather Handbag")
    reviewer_id: str = Field(..., example="USER-9941")
    reviewer_name: str = Field(..., example="FastPromoterBot")
    review_text: str = Field(..., example="THIS IS TERRIBLE DO NOT BUY THIS ITEM GO TO HTTP://SPAM-SCAM-DEALS.SITE FOR DISCOUNT")
    rating: int = Field(..., example=1)
    distilbert_toxicity_score: Optional[float] = 0.0
    distilbert_sentiment_score: Optional[float] = 0.0
    is_fake_review_prob: Optional[float] = 0.0
    risk_level: Optional[str] = "low"
    flagged_categories: Optional[List[str]] = []
    status: Optional[str] = "PUBLISHED"
    reviewer_history_stats: Optional[Dict[str, Any]] = {}


class ReviewUpdate(BaseModel):
    status: Optional[str] = None
    risk_level: Optional[str] = None
    distilbert_toxicity_score: Optional[float] = None
    flagged_categories: Optional[List[str]] = None


class ReviewResponse(BaseModel):
    id: str = Field(..., alias="_id")
    review_id: str
    product_id: str
    product_title: str
    reviewer_id: str
    reviewer_name: str
    review_text: str
    rating: int
    distilbert_toxicity_score: float
    distilbert_sentiment_score: float
    is_fake_review_prob: float
    risk_level: str
    flagged_categories: List[str]
    status: str
    reviewer_history_stats: Dict[str, Any]
    created_at: datetime

    class Config:
        populate_by_name = True
