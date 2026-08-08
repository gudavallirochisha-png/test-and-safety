import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from backend.app.schemas.product import ProductVerificationRequestSchema, ProductCreateSchema
from backend.app.models.product import ProductModel
from backend.app.models.agent_decision import AgentDecisionModel
from backend.app.repositories.product_repository import ProductRepository
from backend.app.repositories.agent_decision_repository import AgentDecisionRepository
from backend.app.services.alert_service import AlertService
from backend.app.services.audit_service import AuditService
from backend.app.core.exceptions import EntityNotFoundException


class ProductService:
    def __init__(
        self,
        product_repo: Optional[ProductRepository] = None,
        decision_repo: Optional[AgentDecisionRepository] = None,
        alert_service: Optional[AlertService] = None,
        audit_service: Optional[AuditService] = None,
    ):
        self.product_repo = product_repo or ProductRepository()
        self.decision_repo = decision_repo or AgentDecisionRepository()
        self.alert_service = alert_service or AlertService()
        self.audit_service = audit_service or AuditService()

    async def verify_product(self, request: ProductVerificationRequestSchema) -> Dict[str, Any]:
        """Orchestrates product authenticity verification, decision persistence, alert generation, and audit logging."""
        product_id = request.product_id or f"PROD-{uuid.uuid4().hex[:4].upper()}"

        # Synthetic Mock Authenticity Agent Evaluation Logic
        authenticity_score = 95.0
        counterfeit_probability = 0.05
        flagged_reasons: List[str] = []

        if request.price < 50 and "luxury" in request.name.lower():
            authenticity_score = 25.0
            counterfeit_probability = 0.85
            flagged_reasons.append("Listing price 85% below market brand baseline")
            flagged_reasons.append("Visual logo geometry deformation detected")

        if authenticity_score < 40:
            verification_status = "REJECTED"
            status = "COUNTERFEIT_FLAGGED"
        elif authenticity_score < 70:
            verification_status = "MANUAL_REVIEW"
            status = "MANUAL_REVIEW"
        else:
            verification_status = "VERIFIED"
            status = "VERIFIED"

        now = datetime.now(timezone.utc)

        # 1. Store Product
        product_doc = ProductModel(
            product_id=product_id,
            seller_id=request.seller_id,
            name=request.name,
            brand=request.brand,
            category=request.category,
            description=request.description,
            price=request.price,
            currency=request.currency,
            image_urls=request.image_urls,
            status=status,
            authenticity_score=authenticity_score,
            counterfeit_probability=counterfeit_probability,
            verification_status=verification_status,
            created_at=now,
            updated_at=now,
        ).to_dict()

        saved_product = await self.product_repo.create(product_doc)

        # 2. Store Agent Decision
        decision_id = f"DEC-{uuid.uuid4().hex[:5].upper()}"
        decision_doc = AgentDecisionModel(
            decision_id=decision_id,
            agent="Authenticity Agent",
            agent_type="AUTHENTICITY",
            entity_type="Product",
            entity_id=product_id,
            model_version="v3.1-YOLOv8",
            score=authenticity_score,
            confidence=0.96,
            decision=verification_status,
            risk_factors=flagged_reasons,
            metadata={"brand": request.brand, "category": request.category},
            created_at=now,
        ).to_dict()
        saved_decision = await self.decision_repo.create(decision_doc)

        # 3. Create Alert if Flagged or Rejected
        alert_created = False
        if verification_status in ["FLAGGED", "REJECTED"]:
            await self.alert_service.create_alert(
                alert_type="CV-LOGO-TM",
                severity="HIGH" if verification_status == "FLAGGED" else "CRITICAL",
                agent="Authenticity Agent",
                entity_type="Product",
                entity_id=product_id,
                title=f"Product Counterfeit Risk ({verification_status})",
                description=f"Product {product_id} flagged with counterfeit probability {counterfeit_probability*100:.1f}%",
                confidence=0.96,
            )
            alert_created = True

        # 4. Store Audit Log
        audit_entry = await self.audit_service.log_action(
            action="PRODUCT_VERIFIED",
            entity_type="Product",
            entity_id=product_id,
            status="FLAGGED" if verification_status != "VERIFIED" else "PASSED",
            decision=verification_status,
            confidence=0.96,
            agent="Authenticity Agent",
            metadata={"authenticity_score": authenticity_score},
        )

        return {
            "product": saved_product,
            "decision": saved_decision,
            "alert_created": alert_created,
            "audit_log_id": audit_entry.get("audit_id", ""),
        }

    async def list_products(self, page: int = 1, limit: int = 50, verification_status: Optional[str] = None) -> List[Dict[str, Any]]:
        return await self.product_repo.list(page=page, limit=limit, verification_status=verification_status)

    async def get_by_id(self, product_id: str) -> Dict[str, Any]:
        product = await self.product_repo.get_by_id(product_id)
        if not product:
            raise EntityNotFoundException("Product", product_id)
        return product

    async def update(self, product_id: str, update_data: Dict[str, Any]) -> Dict[str, Any]:
        existing = await self.get_by_id(product_id)
        update_data["updated_at"] = datetime.now(timezone.utc)
        updated = await self.product_repo.update(product_id, update_data)
        
        await self.audit_service.log_action(
            action="MANUAL_DECISION_MADE",
            entity_type="Product",
            entity_id=product_id,
            status="PASSED",
            decision=updated.get("verification_status", "UPDATED"),
            confidence=1.0,
            agent="Analyst Workstation",
            actor_type="ANALYST",
            metadata={"fields_updated": list(update_data.keys())},
        )
        return updated

    async def delete(self, product_id: str) -> bool:
        await self.get_by_id(product_id)
        res = await self.product_repo.delete(product_id)
        await self.audit_service.log_action(
            action="PRODUCT_DELETED",
            entity_type="Product",
            entity_id=product_id,
            status="QUARANTINED",
            decision="DELETED",
            confidence=1.0,
            agent="Analyst Workstation",
            actor_type="ANALYST",
            metadata={},
        )
        return res
