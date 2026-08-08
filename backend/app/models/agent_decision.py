from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import List, Dict, Any


class AgentDecisionModel(BaseModel):
    decision_id: str
    agent: str
    agent_type: str  # RISK, AUTHENTICITY, REVIEW
    entity_type: str
    entity_id: str
    model_version: str = "v1.0-synthetic"
    score: float = 0.95
    confidence: float = 0.95
    decision: str = "APPROVED"
    risk_factors: List[str] = []
    metadata: Dict[str, Any] = {}
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def to_dict(self) -> dict:
        return self.model_dump()
