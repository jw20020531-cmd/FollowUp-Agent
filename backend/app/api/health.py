from fastapi import APIRouter

from app.core.database import check_database

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/health/db")
def database_health() -> dict[str, str]:
    if check_database():
        return {"status": "ok"}
    return {"status": "unavailable"}

