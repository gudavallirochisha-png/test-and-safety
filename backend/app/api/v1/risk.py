from fastapi import APIRouter, status, Query
from typing import List, Optional
from backend.app.schemas.transaction import (
    RiskAnalysisRequestSchema,
    RiskAnalysisResponseSchema,
    TransactionResponseSchema,
)
from backend.app.services.risk_service import RiskService

router = APIRouter(prefix="/risk", tags=["Risk Analysis & Orders"])
risk_service = RiskService()


@router.post("/analyze", response_model=RiskAnalysisResponseSchema, status_code=status.HTTP_201_CREATED)
async def analyze_transaction_risk(payload: RiskAnalysisRequestSchema):
    """Evaluates transaction risk, persists transaction, agent decision, audit log, and creates alert if high/critical risk."""
    result = await risk_service.analyze_transaction(payload)
    return result


@router.get("/transactions", response_model=List[TransactionResponseSchema])
async def list_transactions(
    page: int = Query(1, ge=1),
    limit: int = Query(50, ge=1, le=100),
    risk_level: Optional[str] = None,
):
    """List transactions stored in MongoDB."""
    transactions = await risk_service.list_transactions(page=page, limit=limit, risk_level=risk_level)
    return transactions


@router.get("/transactions/{transaction_id}", response_model=TransactionResponseSchema)
async def get_transaction_by_id(transaction_id: str):
    """Get a transaction by ID."""
    txn = await risk_service.get_by_id(transaction_id)
    return txn
