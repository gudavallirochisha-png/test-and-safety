from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from typing import Optional
from backend.app.config.settings import settings
from backend.app.core.logging import logger


class DatabaseManager:
    """Reusable Asynchronous MongoDB Connection Manager using Motor driver."""
    client: Optional[AsyncIOMotorClient] = None
    db: Optional[AsyncIOMotorDatabase] = None


db_manager = DatabaseManager()


async def connect_db() -> AsyncIOMotorDatabase:
    """Connects to MongoDB using Motor client on application startup."""
    logger.info(f"Initializing Motor Async MongoDB Connection: {settings.MONGODB_URI} [DB: '{settings.MONGODB_DATABASE}']...")
    try:
        db_manager.client = AsyncIOMotorClient(
            settings.MONGODB_URI,
            maxPoolSize=settings.MONGODB_MAX_POOL_SIZE,
            serverSelectionTimeoutMS=5000,
        )
        db_manager.db = db_manager.client[settings.MONGODB_DATABASE]
        # Quick ping check
        await db_manager.client.admin.command('ping')
        logger.info(f"Successfully connected to MongoDB database '{settings.MONGODB_DATABASE}'!")
        return db_manager.db
    except Exception as e:
        logger.warning(f"MongoDB Motor Connection Notice: {e}")
        if db_manager.client:
            db_manager.db = db_manager.client[settings.MONGODB_DATABASE]
        return db_manager.db


async def close_db() -> None:
    """Closes MongoDB Motor client connection on application shutdown."""
    if db_manager.client:
        db_manager.client.close()
        logger.info("MongoDB Motor Client connection closed cleanly.")


def get_database() -> AsyncIOMotorDatabase:
    """Dependency injection accessor for the active Motor database instance."""
    if db_manager.db is None:
        raise RuntimeError("Database connection has not been initialized.")
    return db_manager.db
