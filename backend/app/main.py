from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.config.settings import settings
from backend.app.core.logging import logger
from backend.app.database.mongodb import connect_and_init_db, close_db_connection
from backend.app.database.seed import seed_initial_data_if_empty
from backend.app.api.v1.router import api_v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI Lifespan Context Manager: Handles startup DB connection & shutdown cleanup."""
    logger.info("Initializing Enterprise AI Trust & Safety Backend...")
    try:
        await connect_and_init_db()
        await seed_initial_data_if_empty()
    except Exception as e:
        logger.warning(f"Database connection skipped or unavailable during startup: {e}")
    yield
    await close_db_connection()
    logger.info("Shutdown completed cleanly.")


app = FastAPI(
    title="Enterprise AI Trust & Safety Platform API",
    description="Scalable, production-ready async REST API gateway orchestrating XGBoost, DistilBERT, and YOLO micro-agent evaluation pipelines.",
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
