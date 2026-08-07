from fastapi import APIRouter
from backend.app.api.v1.health import router as health_router
from backend.app.api.v1.products import router as products_router
from backend.app.api.v1.orders import router as orders_router
from backend.app.api.v1.reviews import router as reviews_router
from backend.app.api.v1.alerts import router as alerts_router
from backend.app.api.v1.analytics import router as analytics_router
from backend.app.api.v1.audit import router as audit_router
from backend.app.api.v1.settings import router as settings_router
from backend.app.api.v1.ai_placeholder import router as ai_router

api_v1_router = APIRouter(prefix="/api/v1")

api_v1_router.include_router(health_router)
api_v1_router.include_router(products_router)
api_v1_router.include_router(orders_router)
api_v1_router.include_router(reviews_router)
api_v1_router.include_router(alerts_router)
api_v1_router.include_router(analytics_router)
api_v1_router.include_router(audit_router)
api_v1_router.include_router(settings_router)
api_v1_router.include_router(ai_router)
