from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.config.settings import settings
from backend.app.core.logging import logger
from backend.app.database.connection import connect_db, close_db, db_manager
from backend.app.database.indexes import create_indexes
from backend.app.api.v1.router import api_v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI Lifespan Context Manager: Handles startup Motor DB connection, index creation, & shutdown cleanup."""
    logger.info("Initializing Enterprise AI Trust & Safety Backend (Phase 4 Motor Async Database)...")
    try:
        db = await connect_db()
        if db is not None:
            await create_indexes(db)
    except Exception as e:
        logger.warning(f"Database connection skipped or unavailable during startup: {e}")
    yield
    await close_db()
    logger.info("Shutdown completed cleanly.")


app = FastAPI(
    title="Enterprise AI Trust & Safety Platform API",
    description="Scalable, production-ready async REST API gateway backed by persistent MongoDB storage.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# Configure CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount master v1 router
app.include_router(api_v1_router)


@app.get("/", tags=["Health"])
async def root():
    return {
        "service": "AI Trust & Safety Platform Gateway",
        "status": "online",
        "docs": "/docs",
        "version": "1.0.0",
    }
