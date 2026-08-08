from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime


class AgentDecisionResponseSchema(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    decision_id: str
    agent: str
    agent_type: str
    entity_type: str
    entity_id: str
    model_version: str
    score: float
    confidence: float
    decision: str
    risk_factors: List[str]
    metadata: Dict[str, Any]
    created_at: datetime

    class Config:
        populate_by_name = True
