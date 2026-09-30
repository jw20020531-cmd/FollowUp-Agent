from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.followups import router as followups_router, seed_demo_data
from app.api.health import router as health_router
from app.core.config import get_settings
from app.core.database import init_database


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_database()
    seed_demo_data()
    yield

settings = get_settings()
app = FastAPI(title=settings.app_name, version="0.2.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(health_router, prefix="/api")
app.include_router(followups_router, prefix="/api")

