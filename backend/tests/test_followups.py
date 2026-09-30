from fastapi.testclient import TestClient

from app.main import app


def test_list_follow_ups_includes_demo_data() -> None:
    with TestClient(app) as client:
        response = client.get("/api/follow-ups")

    assert response.status_code == 200
    assert len(response.json()) >= 3


def test_create_follow_up() -> None:
    with TestClient(app) as client:
        response = client.post(
            "/api/follow-ups",
            json={
                "contact_name": "Anonymous tester",
                "subject": "Pilot feedback",
                "last_message_summary": "Tester has not replied after the first demo.",
                "reason": "Follow up while the demo is still fresh.",
                "due_date": "2026-10-05",
            },
        )

    assert response.status_code == 201
    body = response.json()
    assert body["id"]
    assert body["status"] == "needs_follow_up"
    assert body["subject"] == "Pilot feedback"


def test_update_follow_up_status() -> None:
    with TestClient(app) as client:
        created = client.post(
            "/api/follow-ups",
            json={
                "contact_name": "Anonymous reviewer",
                "subject": "Research interview",
                "last_message_summary": "Reviewer agreed to talk but has not picked a time.",
                "reason": "Scheduling is waiting on a gentle reminder.",
            },
        ).json()

        response = client.patch(f"/api/follow-ups/{created['id']}", json={"status": "waiting"})

    assert response.status_code == 200
    assert response.json()["status"] == "waiting"
