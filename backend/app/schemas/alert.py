from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class AlertCreateSchema(BaseModel):
    alert_id: Optional[str] = None
    type: str = Field("SECURITY_VELOCITY", example="SECURITY_VELOCITY")
    severity: str = Field("HIGH", example="HIGH")
    agent: str = Field("Risk Agent", example="Risk Agent")
    entity_type: str = Field("Transaction", example="Transaction")
    entity_id: str = Field(..., example="TXN-88001")
    title: str = Field(..., example="High Velocity Tor Checkout Ring")
    description: str = Field(..., example="Risk Agent identified 14 rapid checkout attempts.")
    confidence: float = Field(0.95, example=0.95)
    status: str = Field("OPEN", example="OPEN")


class AlertStatusUpdateSchema(BaseModel):
    status: str = Field(..., example="RESOLVED")  # OPEN, INVESTIGATING, RESOLVED, DISMISSED
    resolution_notes: Optional[str] = Field(None, example="Verified customer identity and cleared hold.")


class AlertResponseSchema(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    alert_id: str
    type: str
    severity: str
    agent: str
    entity_type: str
    entity_id: str
    title: str
    description: str
    confidence: float
    status: str
    created_at: datetime
    resolved_at: Optional[datetime] = None
    resolution_notes: Optional[str] = None

    class Config:
        populate_by_name = True


class PaginatedAlertsResponseSchema(BaseModel):
    items: List[AlertResponseSchema]
    page: int
    limit: int
    total: int
    total_pages: int
