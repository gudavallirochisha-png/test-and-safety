import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_health_endpoint_function():
    """Test /api/v1/health endpoint functionality."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "database_status" in data


def test_ai_risk_placeholder_function():
    """Test AI Risk agent evaluation function."""
    payload = {"seller_id": "SELL-8812", "transaction_value": 4999.0}
    response = client.post("/api/v1/ai/risk", json={"payload": payload})
    assert response.status_code == 200
    data = response.json()
    assert data["prediction"] == "High Risk"
    assert data["confidence"] == 0.94


def test_ai_review_placeholder_function():
    """Test AI Review agent evaluation function."""
    payload = {"review_text": "Spam URL promotion http://scam.site"}
    response = client.post("/api/v1/ai/review", json={"payload": payload})
    assert response.status_code == 200
    data = response.json()
    assert "Toxic Review" in data["prediction"]


def test_ai_product_placeholder_function():
    """Test AI Product authenticity evaluation function."""
    payload = {"image_url": "https://example.com/item.jpg"}
    response = client.post("/api/v1/ai/product", json={"payload": payload})
    assert response.status_code == 200
    data = response.json()
    assert "Authentic" in data["prediction"]


def test_settings_get_and_update_function():
    """Test system settings GET and PUT functionality."""
    get_res = client.get("/api/v1/settings")
    assert get_res.status_code == 200

    update_payload = {
        "environment": "development",
        "theme": "dark",
        "emailAlerts": True,
        "slackAlerts": False,
        "autoQuarantine": True,
        "thresholds": {"xgboost_risk": 0.85},
    }
    put_res = client.put("/api/v1/settings", json=update_payload)
    assert put_res.status_code == 200
    assert put_res.json()["slackAlerts"] is False
