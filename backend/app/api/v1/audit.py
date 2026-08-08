from fastapi import APIRouter, Query
from typing import Optional
from backend.app.schemas.audit_log import PaginatedAuditLogsResponseSchema
from backend.app.services.audit_service import AuditService

router = APIRouter(tags=["Audit Logs"])
audit_service = AuditService()


@router.get("/audit-logs", response_model=PaginatedAuditLogsResponseSchema)
async def list_audit_logs(
    agent: Optional[str] = None,
    action: Optional[str] = None,
    status: Optional[str] = None,
    entity_type: Optional[str] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
):
    """Read paginated audit logs from MongoDB sorted newest first."""
    res = await audit_service.list_logs(
        agent=agent, action=action, status=status, entity_type=entity_type, page=page, limit=limit
    )
    return res


@router.get("/audit", response_model=PaginatedAuditLogsResponseSchema)
async def list_audit_logs_alias(
    agent: Optional[str] = None,
    action: Optional[str] = None,
    status: Optional[str] = None,
    entity_type: Optional[str] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
):
    """Alias endpoint for /api/v1/audit."""
    return await list_audit_logs(
        agent=agent, action=action, status=status, entity_type=entity_type, page=page, limit=limit
    )
