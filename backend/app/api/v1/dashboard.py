from fastapi import APIRouter
from backend.app.schemas.analytics import DashboardSummaryResponseSchema
from backend.app.services.analytics_service import AnalyticsService

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])
analytics_service = AnalyticsService()


@router.get("/summary", response_model=DashboardSummaryResponseSchema)
async def get_dashboard_summary():
    """Returns dashboard statistics calculated dynamically from MongoDB collections."""
    summary = await analytics_service.get_dashboard_summary()
    return summary
