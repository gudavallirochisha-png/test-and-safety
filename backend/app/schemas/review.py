from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class ReviewAnalysisRequestSchema(BaseModel):
    review_id: Optional[str] = None
    product_id: str = Field(..., example="PROD-9021")
    customer_id: str = Field(..., example="USER-9941")
    rating: int = Field(1, example=1)
    review_text: str = Field(..., example="THIS IS TERRIBLE DO NOT BUY THIS ITEM GO TO HTTP://SPAM-SCAM-DEALS.SITE FOR DISCOUNT")
    verified_purchase: bool = Field(False, example=False)


class ReviewResponseSchema(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    review_id: str
    product_id: str
    customer_id: str
    rating: int
    review_text: str
    verified_purchase: bool
    fake_probability: float
    authenticity_score: float
    decision: str
    risk_factors: List[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        populate_by_name = True


class ReviewAnalysisResponseSchema(BaseModel):
    review: ReviewResponseSchema
    decision: dict
    alert_created: bool = False
    audit_log_id: str
