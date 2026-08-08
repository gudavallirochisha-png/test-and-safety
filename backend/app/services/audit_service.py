import uuid
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from backend.app.repositories.audit_log_repository import AuditLogRepository
from backend.app.models.audit_log import AuditLogModel
from backend.app.core.logging import logger


class AuditService:
    def __init__(self, audit_repo: Optional[AuditLogRepository] = None):
        self.audit_repo = audit_repo or AuditLogRepository()

    async def log_action(
        self,
        action: str,
        entity_type: str,
        entity_id: str,
        status: str = "PASSED",
        decision: str = "APPROVED",
        confidence: float = 1.0,
        agent: str = "Risk Agent",
        actor_type: str = "AGENT",
        actor_id: str = "SYSTEM",
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        audit_id = f"AUD-{uuid.uuid4().hex[:6].upper()}"
        audit_doc = AuditLogModel(
            audit_id=audit_id,
            timestamp=datetime.now(timezone.utc),
            actor_type=actor_type,
            actor_id=actor_id,
            agent=agent,
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            status=status,
            decision=decision,
            confidence=confidence,
            metadata=metadata or {},
        ).to_dict()

        saved_doc = await self.audit_repo.create(audit_doc)
        logger.info(f"[AUDIT LOG PERSISTED] {action} on {entity_type}:{entity_id} - ID: {audit_id}")
        return saved_doc

    async def list_logs(
        self,
        agent: Optional[str] = None,
        action: Optional[str] = None,
        status: Optional[str] = None,
        entity_type: Optional[str] = None,
        page: int = 1,
        limit: int = 20,
    ) -> Dict[str, Any]:
        items, total, total_pages = await self.audit_repo.list_paginated(
            agent=agent, action=action, status=status, entity_type=entity_type, page=page, limit=limit
        )
        return {
            "items": items,
            "page": page,
            "limit": limit,
            "total": total,
            "total_pages": total_pages,
        }
