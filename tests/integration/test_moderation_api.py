from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_moderate_api_healthcheck():
    resp = client.post("/api/v1/moderate", json={"content": "hello world"})
    assert resp.status_code == 200
    assert "is_flagged" in resp.json()
