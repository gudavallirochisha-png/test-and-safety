from pymongo import ASCENDING, DESCENDING
from motor.motor_asyncio import AsyncIOMotorDatabase
from backend.app.core.logging import logger


async def create_indexes(db: AsyncIOMotorDatabase) -> None:
    """Creates database indexes for the 6 core collections asynchronously."""
    if db is None:
        return

    try:
        logger.info("Initializing MongoDB collection indexes...")

        # 1. products collection indexes
        await db.products.create_index("product_id", unique=True)
        await db.products.create_index("seller_id")
        await db.products.create_index("verification_status")
        await db.products.create_index([("created_at", DESCENDING)])

        # 2. transactions collection indexes
        await db.transactions.create_index("transaction_id", unique=True)
        await db.transactions.create_index("customer_id")
        await db.transactions.create_index("risk_level")
        await db.transactions.create_index("decision")
        await db.transactions.create_index([("created_at", DESCENDING)])

        # 3. reviews collection indexes
        await db.reviews.create_index("review_id", unique=True)
        await db.reviews.create_index("product_id")
        await db.reviews.create_index("customer_id")
        await db.reviews.create_index("decision")
        await db.reviews.create_index([("created_at", DESCENDING)])

        # 4. alerts collection indexes
        await db.alerts.create_index("alert_id", unique=True)
        await db.alerts.create_index("severity")
        await db.alerts.create_index("status")
        await db.alerts.create_index("agent")
        await db.alerts.create_index([("created_at", DESCENDING)])

        # 5. agent_decisions collection indexes
        await db.agent_decisions.create_index("decision_id", unique=True)
        await db.agent_decisions.create_index("agent")
        await db.agent_decisions.create_index("entity_id")
        await db.agent_decisions.create_index([("created_at", DESCENDING)])

        # 6. audit_logs collection indexes
        await db.audit_logs.create_index("audit_id", unique=True)
        await db.audit_logs.create_index("entity_id")
        await db.audit_logs.create_index([("timestamp", DESCENDING)])

        logger.info("Successfully configured indexes for all 6 collections.")
    except Exception as e:
        logger.warning(f"Index creation notice: {e}")
