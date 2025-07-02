from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Mock seed data already includes John Doe and Jane Smith

def test_search_no_filters():
    response = client.get("/api/employee/search")
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert isinstance(data["results"], list)
    assert len(data["results"]) <= 10  # default limit

def test_search_with_status():
    response = client.get("/api/employee/search?status=Active")
    assert response.status_code == 200
    data = response.json()
    for emp in data["results"]:
        assert emp["status"].lower() == "active"

def test_search_with_multiple_status():
    response = client.get("/api/employee/search?status=Active&status=Terminated")
    assert response.status_code == 200
    statuses = [emp["status"].lower() for emp in response.json()["results"]]
    assert "active" in statuses or "terminated" in statuses

def test_search_with_org_column_config():
    response = client.get("/api/employee/search?org_id=org2&status=Active")
    assert response.status_code == 200
    result = response.json()
    assert result["visible_columns"] == ["first_name", "department", "location", "position"]
    for row in result["results"]:
        assert set(row.keys()) == set(result["visible_columns"])

def test_rate_limit_exceeded():
    for i in range(11):
        response = client.get("/api/employee/search")
        assert response.status_code == 200

    response = client.get("/api/employee/search")
    assert response.status_code == 429
    assert response.json()["detail"].startswith("Too Many Requests")
