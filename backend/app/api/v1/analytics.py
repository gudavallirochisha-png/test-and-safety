from fastapi import APIRouter
from backend.app.services.analytics_service import AnalyticsService

router = APIRouter(prefix="/analytics", tags=["Analytics"])
analytics_service = AnalyticsService()


@router.get("/")
async def get_analytics():
    """Calculate analytics trends and distributions using MongoDB aggregation pipelines."""
    data = await analytics_service.get_analytics()
    return data
