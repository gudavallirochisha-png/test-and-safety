from typing import Any, Dict, List, Optional
from backend.app.repositories.base_repository import BaseRepository


class ProductRepository(BaseRepository):
    def __init__(self, db=None):
        super().__init__("products", db=db)

    async def create(self, product_data: Dict[str, Any]) -> Dict[str, Any]:
        return await self.insert(product_data)

    async def get_by_id(self, product_id: str) -> Optional[Dict[str, Any]]:
        return await self.find_one({"product_id": product_id})

    async def update(self, product_id: str, update_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        return await self.update_one({"product_id": product_id}, update_data)

    async def list(self, page: int = 1, limit: int = 50, verification_status: Optional[str] = None) -> List[Dict[str, Any]]:
        query = {}
        if verification_status:
            query["verification_status"] = verification_status
        return await self.find_all(query=query, page=page, limit=limit)

    async def delete(self, product_id: str) -> bool:
        return await self.delete_one({"product_id": product_id})
