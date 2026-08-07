from fastapi import APIRouter, status
from typing import List
from backend.app.schemas.alert import AlertCreate, AlertResponse
from backend.app.services.alert_service import AlertService

router = APIRouter(prefix="/alerts", tags=["Fraud Alerts"])


@router.post("/", response_model=AlertResponse, status_code=status.HTTP_201_CREATED)
async def create_alert(payload: AlertCreate):
    """Trigger a new security/fraud alert."""
    alert = await AlertService.create_alert(payload)
    return alert.model_dump(by_alias=True)


@router.get("/", response_model=List[AlertResponse])
async def list_alerts():
    """List all fraud alerts from MongoDB."""
    alerts = await AlertService.list_alerts()
    return [a.model_dump(by_alias=True) for a in alerts]


@router.put("/{alert_id}/resolve", response_model=AlertResponse)
async def resolve_alert(alert_id: str):
    """Mark an incident alert as resolved."""
    alert = await AlertService.resolve_alert(alert_id)
    return alert.model_dump(by_alias=True)
