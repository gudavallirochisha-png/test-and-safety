import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from backend.app.schemas.review import ReviewAnalysisRequestSchema
from backend.app.models.review import ReviewModel
from backend.app.models.agent_decision import AgentDecisionModel
from backend.app.repositories.review_repository import ReviewRepository
from backend.app.repositories.agent_decision_repository import AgentDecisionRepository
from backend.app.services.alert_service import AlertService
from backend.app.services.audit_service import AuditService
from backend.app.core.exceptions import EntityNotFoundException


class ReviewService:
    def __init__(
        self,
        review_repo: Optional[ReviewRepository] = None,
        decision_repo: Optional[AgentDecisionRepository] = None,
        alert_service: Optional[AlertService] = None,
        audit_service: Optional[AuditService] = None,
    ):
        self.review_repo = review_repo or ReviewRepository()
        self.decision_repo = decision_repo or AgentDecisionRepository()
        self.alert_service = alert_service or AlertService()
        self.audit_service = audit_service or AuditService()

    async def analyze_review(self, request: ReviewAnalysisRequestSchema) -> Dict[str, Any]:
        """Orchestrates NLP review analysis, decision persistence, alert creation, and audit logging."""
        review_id = request.review_id or f"REV-{uuid.uuid4().hex[:4].upper()}"

        # Synthetic Mock Review Agent Evaluation Logic
        fake_probability = 0.05
        authenticity_score = 95.0
        risk_factors: List[str] = []

        if "http://" in request.review_text.lower() or "https://" in request.review_text.lower():
            fake_probability = 0.96
            authenticity_score = 10.0
            risk_factors.append("Spam promotion link detected in review body")

        if not request.verified_purchase and request.rating == 1:
            fake_probability += 0.30
            risk_factors.append("Unverified purchase with extreme negative rating")

        fake_probability = min(0.99, fake_probability)

        if fake_probability > 0.85:
            decision = "REJECTED"
        elif fake_probability > 0.50:
            decision = "FLAGGED"
        else:
            decision = "APPROVED"

        now = datetime.now(timezone.utc)

        # 1. Store Review
        review_doc = ReviewModel(
            review_id=review_id,
            product_id=request.product_id,
            customer_id=request.customer_id,
            rating=request.rating,
            review_text=request.review_text,
            verified_purchase=request.verified_purchase,
            fake_probability=fake_probability,
            authenticity_score=authenticity_score,
            decision=decision,
            risk_factors=risk_factors,
            created_at=now,
            updated_at=now,
        ).to_dict()

        saved_review = await self.review_repo.create(review_doc)

        # 2. Store Agent Decision
        decision_id = f"DEC-{uuid.uuid4().hex[:5].upper()}"
        decision_doc = AgentDecisionModel(
            decision_id=decision_id,
            agent="Review Agent",
            agent_type="REVIEW",
            entity_type="Review",
            entity_id=review_id,
            model_version="v1.9-DistilBERT",
            score=fake_probability,
            confidence=0.95,
            decision=decision,
            risk_factors=risk_factors,
            metadata={"product_id": request.product_id, "rating": request.rating},
            created_at=now,
        ).to_dict()
        saved_decision = await self.decision_repo.create(decision_doc)

        # 3. Create Alert if Flagged or Rejected
        alert_created = False
        if decision in ["FLAGGED", "REJECTED"]:
            await self.alert_service.create_alert(
                alert_type="NLP-BOT-SPAM",
                severity="HIGH" if decision == "FLAGGED" else "CRITICAL",
                agent="Review Agent",
                entity_type="Review",
                entity_id=review_id,
                title=f"Review Moderation Violation ({decision})",
                description=f"Review {review_id} flagged with fake probability {fake_probability*100:.1f}%",
                confidence=0.95,
            )
            alert_created = True

        # 4. Store Audit Log
        audit_entry = await self.audit_service.log_action(
            action="REVIEW_ANALYZED",
            entity_type="Review",
            entity_id=review_id,
            status="FLAGGED" if decision != "APPROVED" else "PASSED",
            decision=decision,
            confidence=0.95,
            agent="Review Agent",
            metadata={"fake_probability": fake_probability},
        )

        return {
            "review": saved_review,
            "decision": saved_decision,
            "alert_created": alert_created,
            "audit_log_id": audit_entry.get("audit_id", ""),
        }

    async def list_reviews(self, page: int = 1, limit: int = 50, decision: Optional[str] = None) -> List[Dict[str, Any]]:
        return await self.review_repo.list(page=page, limit=limit, decision=decision)

    async def get_by_id(self, review_id: str) -> Dict[str, Any]:
        review = await self.review_repo.get_by_id(review_id)
        if not review:
            raise EntityNotFoundException("Review", review_id)
        return review

    async def update(self, review_id: str, update_data: Dict[str, Any]) -> Dict[str, Any]:
        await self.get_by_id(review_id)
        update_data["updated_at"] = datetime.now(timezone.utc)
        updated = await self.review_repo.update(review_id, update_data)
        
        await self.audit_service.log_action(
            action="MANUAL_DECISION_MADE",
            entity_type="Review",
            entity_id=review_id,
            status="PASSED",
            decision=updated.get("decision", "UPDATED"),
            confidence=1.0,
            agent="Analyst Workstation",
            actor_type="ANALYST",
            metadata={"fields_updated": list(update_data.keys())},
        )
        return updated

    async def delete(self, review_id: str) -> bool:
        await self.get_by_id(review_id)
        res = await self.review_repo.delete(review_id)
        await self.audit_service.log_action(
            action="REVIEW_DELETED",
            entity_type="Review",
            entity_id=review_id,
            status="QUARANTINED",
            decision="DELETED",
            confidence=1.0,
            agent="Analyst Workstation",
            actor_type="ANALYST",
            metadata={},
        )
        return res
