from collections.abc import Generator
from functools import lru_cache

from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import get_settings


class Base(DeclarativeBase):
    pass


@lru_cache
def get_engine():
    database_url = get_settings().database_url
    options = {"connect_args": {"check_same_thread": False}} if database_url.startswith("sqlite") else {"pool_pre_ping": True}
    return create_engine(database_url, **options)


def get_session() -> Generator[Session, None, None]:
    with sessionmaker(bind=get_engine())() as session:
        yield session


def init_database() -> None:
    from app.models.followup import FollowUpRecord  # noqa: F401

    Base.metadata.create_all(get_engine())


def check_database() -> bool:
    try:
        with get_engine().connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except Exception:
        return False

