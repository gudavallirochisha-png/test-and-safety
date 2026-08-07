from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime


class ProductCreate(BaseModel):
    product_name: str = Field(..., example="Luxury Designer Leather Handbag")
    seller_id: str = Field(..., example="SELL-8812")
    seller_name: str = Field(..., example="VogueBoutique Outlet")
    category: str = Field(..., example="Fashion & Accessories")
    price: float = Field(..., example=1499.99)
    image_url: str = Field(..., example="https://images.unsplash.com/photo-1584917865442-de89df76afd3")
    authenticity_score: Optional[float] = 100.0
    risk_level: Optional[str] = "low"
    status: Optional[str] = "VERIFIED"
    yolo_detections: Optional[List[Dict[str, Any]]] = []
    flagged_reasons: Optional[List[str]] = []


class ProductUpdate(BaseModel):
    product_name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    image_url: Optional[str] = None
    authenticity_score: Optional[float] = None
    risk_level: Optional[str] = None
    status: Optional[str] = None
    yolo_detections: Optional[List[Dict[str, Any]]] = None
    flagged_reasons: Optional[List[str]] = None


class ProductResponse(BaseModel):
    id: str = Field(..., alias="_id", description="MongoDB ID string")
    product_id: str
    product_name: str
    seller_id: str
    seller_name: str
    category: str
    price: float
    image_url: str
    authenticity_score: float
    risk_level: str
    status: str
    yolo_detections: List[Dict[str, Any]]
    flagged_reasons: List[str]
    created_at: datetime

    class Config:
        populate_by_name = True
