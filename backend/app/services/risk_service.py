import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from backend.app.schemas.transaction import RiskAnalysisRequestSchema
from backend.app.models.transaction import TransactionModel
from backend.app.models.agent_decision import AgentDecisionModel
from backend.app.repositories.transaction_repository import TransactionRepository
from backend.app.repositories.agent_decision_repository import AgentDecisionRepository
from backend.app.services.alert_service import AlertService
from backend.app.services.audit_service import AuditService
from backend.app.core.exceptions import EntityNotFoundException


class RiskService:
    def __init__(
        self,
        transaction_repo: Optional[TransactionRepository] = None,
        decision_repo: Optional[AgentDecisionRepository] = None,
        alert_service: Optional[AlertService] = None,
        audit_service: Optional[AuditService] = None,
    ):
        self.txn_repo = transaction_repo or TransactionRepository()
        self.decision_repo = decision_repo or AgentDecisionRepository()
        self.alert_service = alert_service or AlertService()
        self.audit_service = audit_service or AuditService()

    async def analyze_transaction(self, request: RiskAnalysisRequestSchema) -> Dict[str, Any]:
        """Orchestrates transaction risk assessment, decision persistence, alert triggering, and audit logging."""
        txn_id = request.transaction_id or f"TXN-{uuid.uuid4().hex[:5].upper()}"

        # Synthetic Mock Risk Agent Evaluation Logic
        risk_score = 0.12
        risk_factors: List[str] = []
        if request.amount > 3000:
            risk_score += 0.45
            risk_factors.append("High monetary value purchase")
        if request.account_age_days < 3:
            risk_score += 0.35
            risk_factors.append("Account age under 72 hours")
        if "Tor" in request.location or "proxy" in request.device_id.lower():
            risk_score += 0.40
            risk_factors.append("Tor Exit Node / Anonymizing proxy detected")

        risk_score = min(0.98, risk_score)

        # Categorize risk level & decision
        if risk_score >= 0.85:
            risk_level = "CRITICAL"
            decision = "BLOCKED"
        elif risk_score >= 0.60:
            risk_level = "HIGH"
            decision = "MANUAL_REVIEW"
        elif risk_score >= 0.35:
            risk_level = "MEDIUM"
            decision = "MANUAL_REVIEW"
        else:
            risk_level = "LOW"
            decision = "APPROVED"

        now = datetime.now(timezone.utc)

        # 1. Store Transaction
        txn_doc = TransactionModel(
            transaction_id=txn_id,
            customer_id=request.customer_id,
            product_id=request.product_id,
            seller_id=request.seller_id,
            amount=request.amount,
            currency=request.currency,
            payment_method=request.payment_method,
            account_age_days=request.account_age_days,
            device_id=request.device_id,
            ip_address=request.ip_address,
            location=request.location,
            order_history_count=request.order_history_count,
            return_history_count=request.return_history_count,
            risk_score=risk_score,
            risk_level=risk_level,
            decision=decision,
            risk_factors=risk_factors,
            created_at=now,
            updated_at=now,
        ).to_dict()

        saved_txn = await self.txn_repo.create(txn_doc)

        # 2. Store Agent Decision
        decision_id = f"DEC-{uuid.uuid4().hex[:5].upper()}"
        decision_doc = AgentDecisionModel(
            decision_id=decision_id,
            agent="Risk Agent",
            agent_type="RISK",
            entity_type="Transaction",
            entity_id=txn_id,
            model_version="v2.4-XGBoost",
            score=risk_score,
            confidence=0.94,
            decision=decision,
            risk_factors=risk_factors,
            metadata={"ip_address": request.ip_address, "amount": request.amount},
            created_at=now,
        ).to_dict()
        saved_decision = await self.decision_repo.create(decision_doc)

        # 3. Create Alert if High or Critical Risk
        alert_created = False
        if risk_level in ["HIGH", "CRITICAL"]:
            await self.alert_service.create_alert(
                alert_type="SEC-RISK-HIGH",
                severity=risk_level,
                agent="Risk Agent",
                entity_type="Transaction",
                entity_id=txn_id,
                title=f"High Risk Transaction ({risk_level}) Detected",
                description=f"Transaction {txn_id} assigned risk score {risk_score:.2f} due to: {', '.join(risk_factors)}",
                confidence=0.94,
            )
            alert_created = True

        # 4. Store Audit Log
        audit_entry = await self.audit_service.log_action(
            action="TRANSACTION_ANALYZED",
            entity_type="Transaction",
            entity_id=txn_id,
            status="FLAGGED" if decision != "APPROVED" else "PASSED",
            decision=decision,
            confidence=0.94,
            agent="Risk Agent",
            metadata={"risk_score": risk_score, "risk_level": risk_level},
        )

        return {
            "transaction": saved_txn,
            "decision": saved_decision,
            "alert_created": alert_created,
            "audit_log_id": audit_entry.get("audit_id", ""),
        }

    async def list_transactions(self, page: int = 1, limit: int = 50, risk_level: Optional[str] = None) -> List[Dict[str, Any]]:
        return await self.txn_repo.list(page=page, limit=limit, risk_level=risk_level)

    async def get_by_id(self, transaction_id: str) -> Dict[str, Any]:
        txn = await self.txn_repo.get_by_id(transaction_id)
        if not txn:
            raise EntityNotFoundException("Transaction", transaction_id)
        return txn
