import uuid
from typing import List
from backend.app.models.transaction import Transaction
from backend.app.schemas.transaction import TransactionCreate, TransactionUpdate
from backend.app.services.audit_service import AuditService
from backend.app.core.exceptions import EntityNotFoundException


class OrderService:
    @staticmethod
    async def create_transaction(data: TransactionCreate) -> Transaction:
        txn_id = f"TXN-{uuid.uuid4().hex[:5].upper()}"
        txn = Transaction(
            txn_id=txn_id,
            **data.model_dump()
        )
        await txn.insert()
        await AuditService.log_action(
            collection="transactions",
            operation="CREATE",
            entity_id=txn.txn_id,
            details=f"Evaluated transaction order '{txn.order_id}' value ${txn.amount:.2f}",
            status="passed" if txn.status == "APPROVED" else "flagged"
        )
        return txn

    @staticmethod
    async def list_transactions() -> List[Transaction]:
        return await Transaction.find_all().to_list()

    @staticmethod
    async def get_transaction(txn_id: str) -> Transaction:
        txn = await Transaction.find_one(Transaction.txn_id == txn_id)
        if not txn:
            # Fallback to search by order_id if txn_id not found directly
            txn = await Transaction.find_one(Transaction.order_id == txn_id)
        if not txn:
            raise EntityNotFoundException("Transaction", txn_id)
        return txn

    @staticmethod
    async def update_transaction(txn_id: str, data: TransactionUpdate) -> Transaction:
        txn = await OrderService.get_transaction(txn_id)
        update_data = {k: v for k, v in data.model_dump().items() if v is not None}
        await txn.set(update_data)
        await AuditService.log_action(
            collection="transactions",
            operation="UPDATE",
            entity_id=txn.txn_id,
            details=f"Updated transaction status to '{txn.status}'",
            status="passed"
        )
        return txn
