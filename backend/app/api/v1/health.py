from fastapi import APIRouter, status
from backend.app.database.mongodb import db
from backend.app.config.settings import settings

router = APIRouter(tags=["Health Check"])


@router.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    """Returns backend status, MongoDB database connectivity status, and API version."""
    db_status = "connected" if db.client is not None else "disconnected"
    return {
        "status": "healthy",
        "database_status": db_status,
        "database_name": settings.MONGODB_DATABASE,
        "version": "1.0.0",
        "environment": settings.ENVIRONMENT,
    }
