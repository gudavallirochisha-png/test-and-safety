from pydantic import BaseModel, Field
from typing import Dict, Any, Optional


class AIPredictionRequest(BaseModel):
    payload: Dict[str, Any] = Field(default_factory=dict, description="Input features or content for evaluation")


class AIPredictionResponse(BaseModel):
    prediction: str = Field(..., example="High Risk")
    confidence: float = Field(..., example=0.94)
    reason: str = Field(..., example="Placeholder until AI integration")
    agent_type: Optional[str] = None
