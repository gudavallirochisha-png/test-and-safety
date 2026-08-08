from fastapi import APIRouter, status, Query
from typing import List, Optional
from backend.app.schemas.product import (
    ProductVerificationRequestSchema,
    ProductVerificationResponseSchema,
    ProductResponseSchema,
    ProductCreateSchema,
)
from backend.app.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["Products"])
product_service = ProductService()


@router.post("/verify", response_model=ProductVerificationResponseSchema, status_code=status.HTTP_201_CREATED)
async def verify_product(payload: ProductVerificationRequestSchema):
    """Verifies a product, persists product listing, agent decision, audit log, and creates alert if counterfeit/flagged."""
    result = await product_service.verify_product(payload)
    return result


@router.post("/", response_model=ProductResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_product(payload: ProductCreateSchema):
    """Create a new product listing."""
    req = ProductVerificationRequestSchema(**payload.model_dump())
    res = await product_service.verify_product(req)
    return res["product"]


@router.get("/", response_model=List[ProductResponseSchema])
async def list_products(
    page: int = Query(1, ge=1),
    limit: int = Query(50, ge=1, le=100),
    verification_status: Optional[str] = None,
):
    """List products stored in MongoDB."""
    products = await product_service.list_products(page=page, limit=limit, verification_status=verification_status)
    return products


@router.get("/{product_id}", response_model=ProductResponseSchema)
async def get_product_by_id(product_id: str):
    """Get a product listing by ID."""
    product = await product_service.get_by_id(product_id)
    return product


@router.put("/{product_id}", response_model=ProductResponseSchema)
async def update_product(product_id: str, update_data: dict):
    """Update a product listing."""
    product = await product_service.update(product_id, update_data)
    return product


@router.delete("/{product_id}", status_code=status.HTTP_200_OK)
async def delete_product(product_id: str):
    """Delete a product listing."""
    await product_service.delete(product_id)
    return {"message": f"Product '{product_id}' deleted successfully"}
