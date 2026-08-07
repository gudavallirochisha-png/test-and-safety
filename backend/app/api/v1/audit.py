from fastapi import APIRouter
from typing import List
from backend.app.schemas.audit import AuditLogResponse
from backend.app.models.audit_log import AuditLog

router = APIRouter(prefix="/audit", tags=["Audit Trail"])


@router.get("/", response_model=List[AuditLogResponse])
async def list_audit_logs():
    """List all audit log entries recorded automatically by backend operations."""
    logs = await AuditLog.find_all().sort("-timestamp").to_list()
    return [l.model_dump(by_alias=True) for l in logs]
