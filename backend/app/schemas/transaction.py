from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class TransactionCreate(BaseModel):
    order_id: str = Field(..., example="ORD-99014")
    customer_id: str = Field(..., example="CUST-4190")
    customer_name: str = Field(..., example="Alex Mercer")
    seller_id: str = Field(..., example="SELL-8812")
    seller_name: str = Field(..., example="VogueBoutique Outlet")
    amount: float = Field(..., example=4999.00)
    payment_method: str = Field(..., example="Credit Card (Prepaid)")
    ip_address: str = Field(..., example="185.220.101.4")
    device_fingerprint: str = Field(..., example="dev-fp-9910-proxy")
    location: str = Field(..., example="Bucharest, Romania")
    xgboost_risk_score: Optional[float] = 0.0
    risk_level: Optional[str] = "low"
    fraud_factors: Optional[List[str]] = []
    recommendation: Optional[str] = "APPROVE"
    status: Optional[str] = "APPROVED"


class TransactionUpdate(BaseModel):
    status: Optional[str] = None
    risk_level: Optional[str] = None
    xgboost_risk_score: Optional[float] = None
    recommendation: Optional[str] = None
    fraud_factors: Optional[List[str]] = None


class TransactionResponse(BaseModel):
    id: str = Field(..., alias="_id")
    txn_id: str
    order_id: str
    customer_id: str
    customer_name: str
    seller_id: str
    seller_name: str
    amount: float
    payment_method: str
    ip_address: str
    device_fingerprint: str
    location: str
    xgboost_risk_score: float
    risk_level: str
    fraud_factors: List[str]
    recommendation: str
    status: str
    created_at: datetime

    class Config:
        populate_by_name = True
