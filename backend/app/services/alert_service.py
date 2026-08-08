import uuid
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from backend.app.repositories.alert_repository import AlertRepository
from backend.app.models.alert import AlertModel
from backend.app.services.audit_service import AuditService
from backend.app.core.exceptions import EntityNotFoundException


class AlertService:
    def __init__(self, alert_repo: Optional[AlertRepository] = None, audit_service: Optional[AuditService] = None):
        self.alert_repo = alert_repo or AlertRepository()
        self.audit_service = audit_service or AuditService()

    async def create_alert(
        self,
        alert_type: str,
        severity: str,
        agent: str,
        entity_type: str,
        entity_id: str,
        title: str,
        description: str,
        confidence: float = 0.90,
    ) -> Dict[str, Any]:
        alert_id = f"ALT-{uuid.uuid4().hex[:5].upper()}"
        alert_doc = AlertModel(
            alert_id=alert_id,
            type=alert_type,
            severity=severity.upper(),
            agent=agent,
            entity_type=entity_type,
            entity_id=entity_id,
            title=title,
            description=description,
            confidence=confidence,
            status="OPEN",
            created_at=datetime.now(timezone.utc),
        ).to_dict()

        saved_alert = await self.alert_repo.create(alert_doc)
        
        # Log audit entry
        await self.audit_service.log_action(
            action="ALERT_CREATED",
            entity_type="Alert",
            entity_id=alert_id,
            status="FLAGGED",
            decision="OPEN",
            confidence=confidence,
            agent=agent,
            metadata={"alert_code": alert_type, "severity": severity},
        )
        return saved_alert

    async def list_alerts(
        self,
        severity: Optional[str] = None,
        status: Optional[str] = None,
        agent: Optional[str] = None,
        page: int = 1,
        limit: int = 10,
    ) -> Dict[str, Any]:
        items, total, total_pages = await self.alert_repo.list_paginated(
            severity=severity, status=status, agent=agent, page=page, limit=limit
        )
        return {
            "items": items,
            "page": page,
            "limit": limit,
            "total": total,
            "total_pages": total_pages,
        }

    async def get_by_id(self, alert_id: str) -> Dict[str, Any]:
        alert = await self.alert_repo.get_by_id(alert_id)
        if not alert:
            raise EntityNotFoundException("Alert", alert_id)
        return alert

    async def update_status(self, alert_id: str, new_status: str, resolution_notes: Optional[str] = None) -> Dict[str, Any]:
        existing = await self.get_by_id(alert_id)
        updated = await self.alert_repo.update_status(alert_id, status=new_status, resolution_notes=resolution_notes)

        # Append to audit log
        await self.audit_service.log_action(
            action="ALERT_RESOLVED" if new_status.upper() in ["RESOLVED", "DISMISSED"] else "ALERT_UPDATED",
            entity_type="Alert",
            entity_id=alert_id,
            status="PASSED" if new_status.upper() == "RESOLVED" else "INVESTIGATING",
            decision=new_status.upper(),
            confidence=existing.get("confidence", 1.0),
            agent=existing.get("agent", "Security Operations"),
            actor_type="ANALYST",
            metadata={"previous_status": existing.get("status"), "resolution_notes": resolution_notes},
        )
        return updated
