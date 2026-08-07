from fastapi import APIRouter, status
from typing import List
from backend.app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from backend.app.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(payload: ProductCreate):
    """Create a new product listing."""
    product = await ProductService.create_product(payload)
    return product.model_dump(by_alias=True)


@router.get("/", response_model=List[ProductResponse])
async def list_products():
    """List all product listings from MongoDB."""
    products = await ProductService.list_products()
    return [p.model_dump(by_alias=True) for p in products]


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str):
    """Get product details by product_id."""
    product = await ProductService.get_product(product_id)
    return product.model_dump(by_alias=True)


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(product_id: str, payload: ProductUpdate):
    """Update a product listing."""
    product = await ProductService.update_product(product_id, payload)
    return product.model_dump(by_alias=True)


@router.delete("/{product_id}", status_code=status.HTTP_200_OK)
async def delete_product(product_id: str):
    """Delete a product listing."""
    await ProductService.delete_product(product_id)
    return {"message": f"Product '{product_id}' deleted successfully"}
