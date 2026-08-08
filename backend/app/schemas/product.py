from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class ProductCreateSchema(BaseModel):
    product_id: Optional[str] = None
    seller_id: str = Field(..., example="SELL-8812")
    name: str = Field(..., example="Luxury Designer Leather Handbag")
    brand: str = Field("Generic", example="VogueBoutique")
    category: str = Field("General", example="Fashion & Accessories")
    description: str = Field("", example="High quality leather handbag")
    price: float = Field(..., example=1499.99)
    currency: str = Field("USD", example="USD")
    image_urls: List[str] = Field(default_factory=list)


class ProductVerificationRequestSchema(BaseModel):
    product_id: Optional[str] = None
    seller_id: str = Field(..., example="SELL-8812")
    name: str = Field(..., example="Luxury Leather Handbag")
    brand: str = Field("VogueBoutique", example="VogueBoutique")
    category: str = Field("Fashion & Accessories", example="Fashion & Accessories")
    description: str = Field("", example="Handbag sample")
    price: float = Field(1499.99, example=1499.99)
    currency: str = Field("USD", example="USD")
    image_urls: List[str] = Field(default_factory=list)


class ProductResponseSchema(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    product_id: str
    seller_id: str
    name: str
    brand: str
    category: str
    description: str
    price: float
    currency: str
    image_urls: List[str]
    status: str
    authenticity_score: float
    counterfeit_probability: float
    verification_status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        populate_by_name = True


class ProductVerificationResponseSchema(BaseModel):
    product: ProductResponseSchema
    decision: dict
    alert_created: bool = False
    audit_log_id: str
