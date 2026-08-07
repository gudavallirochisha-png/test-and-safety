from fastapi import APIRouter, status
from typing import List
from backend.app.schemas.review import ReviewCreate, ReviewUpdate, ReviewResponse
from backend.app.services.review_service import ReviewService

router = APIRouter(prefix="/reviews", tags=["Reviews"])


@router.post("/", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
async def create_review(payload: ReviewCreate):
    """Create a new product review."""
    review = await ReviewService.create_review(payload)
    return review.model_dump(by_alias=True)


@router.get("/", response_model=List[ReviewResponse])
async def list_reviews():
    """List all moderated reviews from MongoDB."""
    reviews = await ReviewService.list_reviews()
    return [r.model_dump(by_alias=True) for r in reviews]


@router.put("/{review_id}", response_model=ReviewResponse)
async def update_review(review_id: str, payload: ReviewUpdate):
    """Update review status or toxicity score."""
    review = await ReviewService.update_review(review_id, payload)
    return review.model_dump(by_alias=True)


@router.delete("/{review_id}", status_code=status.HTTP_200_OK)
async def delete_review(review_id: str):
    """Delete a review."""
    await ReviewService.delete_review(review_id)
    return {"message": f"Review '{review_id}' deleted successfully"}
