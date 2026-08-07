from pydantic import BaseModel
from typing import Dict, List, Any


class AnalyticsDashboardResponse(BaseModel):
    totalProducts: int
    totalTransactions: int
    totalReviews: int
    totalFraudAlerts: int
    riskDistribution: Dict[str, int]
    monthlyFraudTrend: List[Dict[str, Any]]
    agents: List[Dict[str, Any]]
    systemHealth: Dict[str, Any]
