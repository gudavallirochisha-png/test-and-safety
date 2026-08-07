import uuid
from typing import List
from backend.app.models.alert import Alert
from backend.app.schemas.alert import AlertCreate
from backend.app.services.audit_service import AuditService
from backend.app.core.exceptions import EntityNotFoundException


class AlertService:
    @staticmethod
    async def create_alert(data: AlertCreate) -> Alert:
        alert_id = f"ALT-{uuid.uuid4().hex[:3].upper()}"
        alert = Alert(
            alert_id=alert_id,
            **data.model_dump()
        )
        await alert.insert()
        await AuditService.log_action(
            collection="alerts",
            operation="CREATE",
            entity_id=alert.alert_id,
            details=f"Triggered alert '{alert.title}' [Severity: {alert.severity.upper()}]",
            status="flagged" if alert.severity in ["high", "critical"] else "passed"
        )
        return alert

    @staticmethod
    async def list_alerts() -> List[Alert]:
        return await Alert.find_all().to_list()

    @staticmethod
    async def resolve_alert(alert_id: str) -> Alert:
        alert = await Alert.find_one(Alert.alert_id == alert_id)
        if not alert:
            raise EntityNotFoundException("Alert", alert_id)
        alert.is_resolved = True
        await alert.save()
        await AuditService.log_action(
            collection="alerts",
            operation="RESOLVE",
            entity_id=alert_id,
            details=f"Security analyst resolved incident alert '{alert.alert_code}'",
            status="passed"
        )
        return alert
