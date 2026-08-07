from fastapi import APIRouter, status
from typing import List
from backend.app.schemas.transaction import TransactionCreate, TransactionUpdate, TransactionResponse
from backend.app.services.order_service import OrderService

router = APIRouter(prefix="/orders", tags=["Orders & Transactions"])


@router.post("/", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
async def create_transaction(payload: TransactionCreate):
    """Create a new transaction order."""
    txn = await OrderService.create_transaction(payload)
    return txn.model_dump(by_alias=True)


@router.get("/", response_model=List[TransactionResponse])
async def list_transactions():
    """List all transactions from MongoDB."""
    txns = await OrderService.list_transactions()
    return [t.model_dump(by_alias=True) for t in txns]


@router.get("/{txn_id}", response_model=TransactionResponse)
async def get_transaction(txn_id: str):
    """Get transaction by ID."""
    txn = await OrderService.get_transaction(txn_id)
    return txn.model_dump(by_alias=True)


@router.put("/{txn_id}", response_model=TransactionResponse)
async def update_transaction(txn_id: str, payload: TransactionUpdate):
    """Update transaction status or risk score."""
    txn = await OrderService.update_transaction(txn_id, payload)
    return txn.model_dump(by_alias=True)
