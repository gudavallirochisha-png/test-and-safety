from fastapi import APIRouter
from backend.app.schemas.analytics import AnalyticsDashboardResponse
from backend.app.services.analytics_service import AnalyticsService

router = APIRouter(prefix="/analytics", tags=["Analytics & KPIs"])


@router.get("/", response_model=AnalyticsDashboardResponse)
async def get_analytics_overview():
    """Return real-time dashboard KPIs aggregated directly from MongoDB collections."""
    metrics = await AnalyticsService.get_dashboard_metrics()
    return metrics
