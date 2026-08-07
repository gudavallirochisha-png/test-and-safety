from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any

router = APIRouter(prefix="/settings", tags=["Settings"])


class SystemSettingsSchema(BaseModel):
    environment: str = "development"
    theme: str = "dark"
    emailAlerts: bool = True
    slackAlerts: bool = True
    autoQuarantine: bool = True
    thresholds: Dict[str, float] = {
        "xgboost_risk": 0.85,
        "distilbert_toxicity": 0.75,
        "yolo_authenticity": 0.90,
    }


# In-memory settings state for settings endpoint
current_settings = SystemSettingsSchema()


@router.get("/", response_model=SystemSettingsSchema)
async def get_settings():
    """Retrieve system configuration settings."""
    return current_settings


@router.put("/", response_model=SystemSettingsSchema)
async def update_settings(payload: SystemSettingsSchema):
    """Update system configuration settings."""
    global current_settings
    current_settings = payload
    return current_settings
