from datetime import date
from enum import StrEnum

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.models.followup import FollowUpRecord


router = APIRouter(prefix="/follow-ups", tags=["follow-ups"])


class FollowUpStatus(StrEnum):
    NEEDS_FOLLOW_UP = "needs_follow_up"
    WAITING = "waiting"
    REPLIED = "replied"
    CLOSED = "closed"


class FollowUpCreate(BaseModel):
    contact_name: str = Field(min_length=1, max_length=120)
    subject: str = Field(min_length=1, max_length=200)
    last_message_summary: str = Field(min_length=1)
    reason: str = Field(min_length=1)
    due_date: date | None = None
    missing_materials: list[str] = Field(default_factory=list)


class FollowUpUpdate(BaseModel):
    status: FollowUpStatus


class FollowUp(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    contact_name: str
    subject: str
    last_message_summary: str
    reason: str
    due_date: date | None
    missing_materials: list[str]
    status: FollowUpStatus
    is_demo: bool


def seed_demo_data() -> None:
    from app.core.database import get_engine

    with Session(get_engine()) as session:
        if session.scalar(select(FollowUpRecord.id).limit(1)) is not None:
            return
        session.add_all(
            [
                FollowUpRecord(
                    contact_name="Anonymous speaker lead",
                    subject="Workshop speaker invitation",
                    last_message_summary="Invitation sent four days ago; no reply yet.",
                    reason="Confirm availability before planning the workshop.",
                    due_date=date(2026, 10, 2),
                    missing_materials=[],
                    status=FollowUpStatus.NEEDS_FOLLOW_UP,
                    is_demo=True,
                ),
                FollowUpRecord(
                    contact_name="Anonymous partner contact",
                    subject="Project collaboration proposal",
                    last_message_summary="Proposal sent after a meeting; response pending.",
                    reason="Agree on a next step while the meeting is recent.",
                    due_date=date(2026, 10, 3),
                    missing_materials=["project brief"],
                    status=FollowUpStatus.WAITING,
                    is_demo=True,
                ),
                FollowUpRecord(
                    contact_name="Anonymous member",
                    subject="Onboarding question",
                    last_message_summary="A logistics question has not received an answer.",
                    reason="The requester is waiting for an owner to respond.",
                    due_date=date(2026, 10, 1),
                    missing_materials=[],
                    status=FollowUpStatus.NEEDS_FOLLOW_UP,
                    is_demo=True,
                ),
            ]
        )
        session.commit()


@router.get("", response_model=list[FollowUp])
def list_follow_ups(session: Session = Depends(get_session)) -> list[FollowUpRecord]:
    return list(session.scalars(select(FollowUpRecord).order_by(FollowUpRecord.due_date)).all())


@router.post("", response_model=FollowUp, status_code=201)
def create_follow_up(
    payload: FollowUpCreate, session: Session = Depends(get_session)
) -> FollowUpRecord:
    record = FollowUpRecord(**payload.model_dump(), status=FollowUpStatus.NEEDS_FOLLOW_UP)
    session.add(record)
    session.commit()
    session.refresh(record)
    return record


@router.patch("/{follow_up_id}", response_model=FollowUp)
def update_follow_up(
    follow_up_id: str, payload: FollowUpUpdate, session: Session = Depends(get_session)
) -> FollowUpRecord:
    record = session.get(FollowUpRecord, follow_up_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Follow-up not found")
    record.status = payload.status
    session.commit()
    session.refresh(record)
    return record
