from pydantic import BaseModel
from typing import Dict, List, Any


class DashboardSummaryResponseSchema(BaseModel):
    total_products: int
    verified_products: int
    flagged_products: int
    total_transactions: int
    high_risk_transactions: int
    blocked_transactions: int
    total_reviews: int
    flagged_reviews: int
    open_alerts: int
    agent_status: List[Dict[str, Any]]
