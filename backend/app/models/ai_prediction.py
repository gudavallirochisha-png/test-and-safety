from beanie import Document
from pydantic import Field
from datetime import datetime, timezone
from typing import Dict, Any, Optional


class AIPrediction(Document):
    prediction_id: str = Field(..., description="Unique prediction log ID")
    agent_type: str  # risk, review, authenticity
    model_version: str = "v1.0-placeholder"
    input_payload: Dict[str, Any] = {}
    prediction: str = "Low Risk"
    confidence: float = 0.95
    reason: str = "Placeholder until AI model integration"
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "ai_predictions"
