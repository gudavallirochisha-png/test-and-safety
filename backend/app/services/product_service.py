import uuid
from typing import List, Optional
from backend.app.models.product import Product
from backend.app.schemas.product import ProductCreate, ProductUpdate
from backend.app.services.audit_service import AuditService
from backend.app.core.exceptions import EntityNotFoundException


class ProductService:
    @staticmethod
    async def create_product(data: ProductCreate) -> Product:
        product_id = f"PROD-{uuid.uuid4().hex[:4].upper()}"
        product = Product(
            product_id=product_id,
            **data.model_dump()
        )
        await product.insert()
        await AuditService.log_action(
            collection="products",
            operation="CREATE",
            entity_id=product.product_id,
            details=f"Created product listing '{product.product_name}' under seller '{product.seller_name}'",
            status="passed" if product.risk_level == "low" else "flagged"
        )
        return product

    @staticmethod
    async def list_products() -> List[Product]:
        return await Product.find_all().to_list()

    @staticmethod
    async def get_product(product_id: str) -> Product:
        product = await Product.find_one(Product.product_id == product_id)
        if not product:
            raise EntityNotFoundException("Product", product_id)
        return product

    @staticmethod
    async def update_product(product_id: str, data: ProductUpdate) -> Product:
        product = await ProductService.get_product(product_id)
        update_data = {k: v for k, v in data.model_dump().items() if v is not None}
        await product.set(update_data)
        await AuditService.log_action(
            collection="products",
            operation="UPDATE",
            entity_id=product.product_id,
            details=f"Updated product fields: {list(update_data.keys())}",
            status="passed"
        )
        return product

    @staticmethod
    async def delete_product(product_id: str) -> bool:
        product = await ProductService.get_product(product_id)
        await product.delete()
        await AuditService.log_action(
            collection="products",
            operation="DELETE",
            entity_id=product_id,
            details=f"Purged product listing '{product.product_name}' from repository",
            status="quarantined"
        )
        return True
