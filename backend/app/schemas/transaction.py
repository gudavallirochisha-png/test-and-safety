from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class RiskAnalysisRequestSchema(BaseModel):
    transaction_id: Optional[str] = None
    customer_id: str = Field(..., example="CUST-4190")
    product_id: str = Field("PROD-1001", example="PROD-1001")
    seller_id: str = Field("SELL-8812", example="SELL-8812")
    amount: float = Field(..., example=4999.00)
    currency: str = Field("USD", example="USD")
    payment_method: str = Field("Credit Card", example="Credit Card (Prepaid)")
    account_age_days: int = Field(1, example=1)
    device_id: str = Field("dev-fp-9910-proxy", example="dev-fp-9910-proxy")
    ip_address: str = Field("185.220.101.4", example="185.220.101.4")
    location: str = Field("Bucharest, Romania", example="Bucharest, Romania")
    order_history_count: int = Field(0, example=0)
    return_history_count: int = Field(0, example=0)


class TransactionResponseSchema(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    transaction_id: str
    customer_id: str
    product_id: str
    seller_id: str
    amount: float
    currency: str
    payment_method: str
    account_age_days: int
    device_id: str
    ip_address: str
    location: str
    order_history_count: int
    return_history_count: int
    risk_score: float
    risk_level: str
    decision: str
    risk_factors: List[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        populate_by_name = True


class RiskAnalysisResponseSchema(BaseModel):
    transaction: TransactionResponseSchema
    decision: dict
    alert_created: bool = False
    audit_log_id: str
