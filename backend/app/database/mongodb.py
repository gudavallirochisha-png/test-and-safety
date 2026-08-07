from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from backend.app.config.settings import settings
from backend.app.core.logging import logger
from backend.app.models.user import User
from backend.app.models.seller import Seller
from backend.app.models.product import Product
from backend.app.models.transaction import Transaction
from backend.app.models.review import Review
from backend.app.models.alert import Alert
from backend.app.models.audit_log import AuditLog
from backend.app.models.ai_prediction import AIPrediction

class DatabaseManager:
    client: AsyncIOMotorClient = None

db = DatabaseManager()

async def connect_and_init_db():
    """Initializes Motor Async Client and registers all Beanie ODM Document models."""
    logger.info(f"Connecting to MongoDB at {settings.MONGODB_URI}...")
    try:
        db.client = AsyncIOMotorClient(
            settings.MONGODB_URI,
            maxPoolSize=settings.MONGODB_MAX_POOL_SIZE
        )
        database = db.client[settings.MONGODB_DATABASE]
        
        await init_beanie(
            database=database,
            document_models=[
                User,
                Seller,
                Product,
                Transaction,
                Review,
                Alert,
                AuditLog,
                AIPrediction,
            ]
        )
        logger.info(f"Beanie ODM successfully initialized for database: '{settings.MONGODB_DATABASE}'")
    except Exception as e:
        logger.error(f"Failed to connect/initialize MongoDB: {str(e)}")
        # Allow fallback gracefully or raise
        raise e

async def close_db_connection():
    if db.client:
        db.client.close()
        logger.info("MongoDB client connection closed.")
