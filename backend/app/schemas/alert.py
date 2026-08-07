from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class AlertCreate(BaseModel):
    alert_code: str = Field(..., example="SEC-TOR-VELOCITY")
    title: str = Field(..., example="High Velocity Tor Checkout Ring Detected")
    description: str = Field(..., example="Risk Agent identified 14 rapid checkout attempts originating from Tor Exit Node.")
    severity: str = Field("medium", example="critical")
    agent_source: str = Field("Risk Agent", example="Risk Agent")
    target_type: str = Field("Seller", example="Seller")
    target_id: str = Field(..., example="SELL-8812")
    is_resolved: Optional[bool] = False
    assigned_to: Optional[str] = None


class AlertResponse(BaseModel):
    id: str = Field(..., alias="_id")
    alert_id: str
    alert_code: str
    title: str
    description: str
    severity: str
    agent_source: str
    target_type: str
    target_id: str
    is_resolved: bool
    assigned_to: Optional[str]
    created_at: datetime

    class Config:
        populate_by_name = True
