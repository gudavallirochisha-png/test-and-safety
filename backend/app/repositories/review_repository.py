from typing import Any, Dict, List, Optional
from backend.app.repositories.base_repository import BaseRepository


class ReviewRepository(BaseRepository):
    def __init__(self, db=None):
        super().__init__("reviews", db=db)

    async def create(self, review_data: Dict[str, Any]) -> Dict[str, Any]:
        return await self.insert(review_data)

    async def get_by_id(self, review_id: str) -> Optional[Dict[str, Any]]:
        return await self.find_one({"review_id": review_id})

    async def list(self, page: int = 1, limit: int = 50, decision: Optional[str] = None) -> List[Dict[str, Any]]:
        query = {}
        if decision:
            query["decision"] = decision.upper()
        return await self.find_all(query=query, page=page, limit=limit)

    async def update(self, review_id: str, update_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        return await self.update_one({"review_id": review_id}, update_data)

    async def delete(self, review_id: str) -> bool:
        return await self.delete_one({"review_id": review_id})
