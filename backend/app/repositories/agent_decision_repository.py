from typing import Any, Dict, List, Optional
from backend.app.repositories.base_repository import BaseRepository


class AgentDecisionRepository(BaseRepository):
    def __init__(self, db=None):
        super().__init__("agent_decisions", db=db)

    async def create(self, decision_data: Dict[str, Any]) -> Dict[str, Any]:
        return await self.insert(decision_data)

    async def get_by_id(self, decision_id: str) -> Optional[Dict[str, Any]]:
        return await self.find_one({"decision_id": decision_id})

    async def list(
        self,
        agent: Optional[str] = None,
        entity_id: Optional[str] = None,
        page: int = 1,
        limit: int = 50,
    ) -> List[Dict[str, Any]]:
        query = {}
        if agent:
            query["agent"] = agent
        if entity_id:
            query["entity_id"] = entity_id
        return await self.find_all(query=query, sort_by="created_at", ascending=False, page=page, limit=limit)
