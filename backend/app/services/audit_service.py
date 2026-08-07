import uuid
from datetime import datetime, timezone
from backend.app.models.audit_log import AuditLog
from backend.app.core.logging import logger


class AuditService:
    @staticmethod
    async def log_action(
        collection: str,
        operation: str,
        entity_id: str,
        details: str,
        status: str = "passed",
        agent_name: str = "System Automated Engine",
        confidence_score: float = 100.0,
    ) -> AuditLog:
        """Automatically creates and persists an audit log entry in MongoDB."""
        audit_entry = AuditLog(
            audit_id=f"AUD-{uuid.uuid4().hex[:6].upper()}",
            agent_name=agent_name,
            action=operation.upper(),
            collection=collection,
            entity_id=entity_id,
            status=status,
            confidence_score=confidence_score,
            details=details,
            timestamp=datetime.now(timezone.utc),
        )
        await audit_entry.insert()
        logger.info(f"[AUDIT LOG] {operation.upper()} on '{collection}' (ID: {entity_id}): {details}")
        return audit_entry
