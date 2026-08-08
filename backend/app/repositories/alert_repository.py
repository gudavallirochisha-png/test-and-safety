from typing import Any, Dict, List, Optional, Tuple
import math
from datetime import datetime, timezone
from backend.app.repositories.base_repository import BaseRepository


class AlertRepository(BaseRepository):
    def __init__(self, db=None):
        super().__init__("alerts", db=db)

    async def create(self, alert_data: Dict[str, Any]) -> Dict[str, Any]:
        return await self.insert(alert_data)

    async def get_by_id(self, alert_id: str) -> Optional[Dict[str, Any]]:
        return await self.find_one({"alert_id": alert_id})

    async def list_paginated(
        self,
        severity: Optional[str] = None,
        status: Optional[str] = None,
        agent: Optional[str] = None,
        page: int = 1,
        limit: int = 10,
    ) -> Tuple[List[Dict[str, Any]], int, int]:
        query = {}
        if severity:
            query["severity"] = severity.upper()
        if status:
            query["status"] = status.upper()
        if agent:
            query["agent"] = agent

        total = await self.count(query)
        total_pages = max(1, math.ceil(total / limit))
        items = await self.find_all(query=query, sort_by="created_at", ascending=False, page=page, limit=limit)
        return items, total, total_pages

    async def update_status(
        self,
        alert_id: str,
        status: str,
        resolution_notes: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        update_data = {
            "status": status.upper(),
            "updated_at": datetime.now(timezone.utc),
        }
        if status.upper() in ["RESOLVED", "DISMISSED"]:
            update_data["resolved_at"] = datetime.now(timezone.utc)
        if resolution_notes:
            update_data["resolution_notes"] = resolution_notes

        return await self.update_one({"alert_id": alert_id}, update_data)
