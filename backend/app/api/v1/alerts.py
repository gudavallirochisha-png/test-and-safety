from fastapi import APIRouter, status, Query
from typing import Optional
from backend.app.schemas.alert import (
    AlertCreateSchema,
    AlertStatusUpdateSchema,
    AlertResponseSchema,
    PaginatedAlertsResponseSchema,
)
from backend.app.services.alert_service import AlertService

router = APIRouter(prefix="/alerts", tags=["Fraud Alerts"])
alert_service = AlertService()


@router.post("/", response_model=AlertResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_alert(payload: AlertCreateSchema):
    """Trigger a new security alert."""
    alert = await alert_service.create_alert(
        alert_type=payload.type,
        severity=payload.severity,
        agent=payload.agent,
        entity_type=payload.entity_type,
        entity_id=payload.entity_id,
        title=payload.title,
        description=payload.description,
        confidence=payload.confidence,
    )
    return alert


@router.get("/", response_model=PaginatedAlertsResponseSchema)
async def list_alerts(
    severity: Optional[str] = None,
    status: Optional[str] = None,
    agent: Optional[str] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
):
    """Get paginated fraud alerts from MongoDB."""
    res = await alert_service.list_alerts(
        severity=severity, status=status, agent=agent, page=page, limit=limit
    )
    return res


@router.get("/{alert_id}", response_model=AlertResponseSchema)
async def get_alert_by_id(alert_id: str):
    """Get an alert by ID."""
    alert = await alert_service.get_by_id(alert_id)
    return alert


@router.patch("/{alert_id}/status", response_model=AlertResponseSchema)
async def update_alert_status(alert_id: str, payload: AlertStatusUpdateSchema):
    """Update alert status (e.g. RESOLVED), set resolved_at timestamp, store resolution notes, and create audit log."""
    updated = await alert_service.update_status(
        alert_id=alert_id,
        new_status=payload.status,
        resolution_notes=payload.resolution_notes,
    )
    return updated


@router.put("/{alert_id}/resolve", response_model=AlertResponseSchema)
async def resolve_alert_alias(alert_id: str):
    """Legacy alias endpoint for resolving alerts."""
    updated = await alert_service.update_status(
        alert_id=alert_id,
        new_status="RESOLVED",
        resolution_notes="Resolved via analyst action.",
    )
    return updated
