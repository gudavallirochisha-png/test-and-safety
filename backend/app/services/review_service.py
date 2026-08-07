import uuid
from typing import List
from backend.app.models.review import Review
from backend.app.schemas.review import ReviewCreate, ReviewUpdate
from backend.app.services.audit_service import AuditService
from backend.app.core.exceptions import EntityNotFoundException


class ReviewService:
    @staticmethod
    async def create_review(data: ReviewCreate) -> Review:
        review_id = f"REV-{uuid.uuid4().hex[:4].upper()}"
        review = Review(
            review_id=review_id,
            **data.model_dump()
        )
        await review.insert()
        await AuditService.log_action(
            collection="reviews",
            operation="CREATE",
            entity_id=review.review_id,
            details=f"Moderated review for '{review.product_title}' by user '{review.reviewer_name}'",
            status="passed" if review.status == "PUBLISHED" else "flagged"
        )
        return review

    @staticmethod
    async def list_reviews() -> List[Review]:
        return await Review.find_all().to_list()

    @staticmethod
    async def get_review(review_id: str) -> Review:
        review = await Review.find_one(Review.review_id == review_id)
        if not review:
            raise EntityNotFoundException("Review", review_id)
        return review

    @staticmethod
    async def update_review(review_id: str, data: ReviewUpdate) -> Review:
        review = await ReviewService.get_review(review_id)
        update_data = {k: v for k, v in data.model_dump().items() if v is not None}
        await review.set(update_data)
        await AuditService.log_action(
            collection="reviews",
            operation="UPDATE",
            entity_id=review.review_id,
            details=f"Updated review status to '{review.status}'",
            status="passed"
        )
        return review

    @staticmethod
    async def delete_review(review_id: str) -> bool:
        review = await ReviewService.get_review(review_id)
        await review.delete()
        await AuditService.log_action(
            collection="reviews",
            operation="DELETE",
            entity_id=review_id,
            details=f"Purged toxic review from product '{review.product_title}'",
            status="quarantined"
        )
        return True
