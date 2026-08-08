from fastapi import APIRouter, status, Query
from typing import List, Optional
from backend.app.schemas.review import (
    ReviewAnalysisRequestSchema,
    ReviewAnalysisResponseSchema,
    ReviewResponseSchema,
)
from backend.app.services.review_service import ReviewService

router = APIRouter(prefix="/reviews", tags=["Reviews"])
review_service = ReviewService()


@router.post("/analyze", response_model=ReviewAnalysisResponseSchema, status_code=status.HTTP_201_CREATED)
async def analyze_review(payload: ReviewAnalysisRequestSchema):
    """Analyzes a review, persists review record, agent decision, audit log, and creates alert if toxic/fake."""
    result = await review_service.analyze_review(payload)
    return result


@router.post("/", response_model=ReviewResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_review(payload: ReviewAnalysisRequestSchema):
    result = await review_service.analyze_review(payload)
    return result["review"]


@router.get("/", response_model=List[ReviewResponseSchema])
async def list_reviews(
    page: int = Query(1, ge=1),
    limit: int = Query(50, ge=1, le=100),
    decision: Optional[str] = None,
):
    """List reviews stored in MongoDB."""
    reviews = await review_service.list_reviews(page=page, limit=limit, decision=decision)
    return reviews


@router.get("/{review_id}", response_model=ReviewResponseSchema)
async def get_review_by_id(review_id: str):
    """Get a review by ID."""
    review = await review_service.get_by_id(review_id)
    return review


@router.put("/{review_id}", response_model=ReviewResponseSchema)
async def update_review(review_id: str, update_data: dict):
    """Update review status or decision."""
    review = await review_service.update(review_id, update_data)
    return review


@router.delete("/{review_id}", status_code=status.HTTP_200_OK)
async def delete_review(review_id: str):
    """Delete a review."""
    await review_service.delete(review_id)
    return {"message": f"Review '{review_id}' deleted successfully"}
