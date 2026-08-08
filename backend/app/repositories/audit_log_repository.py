from typing import Any, Dict, List, Optional, Tuple
import math
from backend.app.repositories.base_repository import BaseRepository


class AuditLogRepository(BaseRepository):
    def __init__(self, db=None):
        super().__init__("audit_logs", db=db)

    async def create(self, audit_data: Dict[str, Any]) -> Dict[str, Any]:
        return await self.insert(audit_data)

    async def list_paginated(
        self,
        agent: Optional[str] = None,
        action: Optional[str] = None,
        status: Optional[str] = None,
        entity_type: Optional[str] = None,
        page: int = 1,
        limit: int = 20,
    ) -> Tuple[List[Dict[str, Any]], int, int]:
        query = {}
        if agent:
            query["agent"] = agent
        if action:
            query["action"] = action.upper()
        if status:
            query["status"] = status.upper()
        if entity_type:
            query["entity_type"] = entity_type

        total = await self.count(query)
        total_pages = max(1, math.ceil(total / limit))
        items = await self.find_all(query=query, sort_by="timestamp", ascending=False, page=page, limit=limit)
        return items, total, total_pages
