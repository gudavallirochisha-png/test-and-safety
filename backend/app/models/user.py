from beanie import Document
from pydantic import Field, EmailStr
from datetime import datetime, timezone
from typing import Optional


class User(Document):
    user_id: str = Field(..., description="Unique user identifier")
    name: str
    email: str
    role: str = "CUSTOMER"
    account_age_days: int = 1
    total_reviews_written: int = 0
    flagged_review_ratio: float = 0.0
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "users"
