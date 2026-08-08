from typing import Any, Dict, List, Optional
from backend.app.repositories.base_repository import BaseRepository


class TransactionRepository(BaseRepository):
    def __init__(self, db=None):
        super().__init__("transactions", db=db)

    async def create(self, txn_data: Dict[str, Any]) -> Dict[str, Any]:
        return await self.insert(txn_data)

    async def get_by_id(self, transaction_id: str) -> Optional[Dict[str, Any]]:
        doc = await self.find_one({"transaction_id": transaction_id})
        if not doc:
            doc = await self.find_one({"order_id": transaction_id})
        return doc

    async def list(self, page: int = 1, limit: int = 50, risk_level: Optional[str] = None) -> List[Dict[str, Any]]:
        query = {}
        if risk_level:
            query["risk_level"] = risk_level.upper()
        return await self.find_all(query=query, page=page, limit=limit)

    async def update(self, transaction_id: str, update_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        return await self.update_one({"transaction_id": transaction_id}, update_data)
