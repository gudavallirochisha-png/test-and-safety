from fastapi import APIRouter, status, Query
from typing import List, Optional
from backend.app.schemas.transaction import (
    RiskAnalysisRequestSchema,
    TransactionResponseSchema,
)
from backend.app.services.risk_service import RiskService

router = APIRouter(prefix="/orders", tags=["Orders & Transactions Alias"])
risk_service = RiskService()


@router.post("/", response_model=TransactionResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_order(payload: RiskAnalysisRequestSchema):
    result = await risk_service.analyze_transaction(payload)
    return result["transaction"]


@router.get("/", response_model=List[TransactionResponseSchema])
async def list_orders(
    page: int = Query(1, ge=1),
    limit: int = Query(50, ge=1, le=100),
    risk_level: Optional[str] = None,
):
    return await risk_service.list_transactions(page=page, limit=limit, risk_level=risk_level)


@router.get("/{order_id}", response_model=TransactionResponseSchema)
async def get_order_by_id(order_id: str):
    return await risk_service.get_by_id(order_id)
