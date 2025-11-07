from fastapi.testclient import TestClient
from urllib.parse import quote

from src.app import app


def test_signup_and_unregister_flow():
    client = TestClient(app)

    activity = "Chess Club"
    encoded = quote(activity, safe="")
    email = "testuser@example.com"

    # Ensure not signed up initially
    resp = client.get("/activities")
    assert resp.status_code == 200
    activities = resp.json()
    assert email not in activities[activity]["participants"]

    # Sign up
    resp = client.post(f"/activities/{encoded}/signup", params={"email": email})
    assert resp.status_code == 200
    data = resp.json()
    assert "Signed up" in data["message"]

    # Verify present
    resp = client.get("/activities")
    activities = resp.json()
    assert email in activities[activity]["participants"]

    # Unregister
    resp = client.post(f"/activities/{encoded}/unregister", params={"email": email})
    assert resp.status_code == 200
    data = resp.json()
    assert "Unregistered" in data["message"]

    # Verify removed
    resp = client.get("/activities")
    activities = resp.json()
    assert email not in activities[activity]["participants"]
