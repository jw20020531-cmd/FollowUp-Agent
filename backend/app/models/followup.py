from datetime import date
from uuid import uuid4

from sqlalchemy import Date, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class FollowUpRecord(Base):
    __tablename__ = "follow_ups"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    contact_name: Mapped[str] = mapped_column(String(120))
    subject: Mapped[str] = mapped_column(String(200))
    last_message_summary: Mapped[str] = mapped_column(Text)
    reason: Mapped[str] = mapped_column(Text)
    due_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    missing_materials: Mapped[list[str]] = mapped_column(JSON, default=list)
    status: Mapped[str] = mapped_column(String(24), default="needs_follow_up")
    is_demo: Mapped[bool] = mapped_column(default=False)
