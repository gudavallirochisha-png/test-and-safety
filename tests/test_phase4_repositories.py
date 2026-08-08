import pytest
import asyncio
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_health_check_api():
    """Verify backend and database connection health status."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "database_status" in data


def test_dashboard_summary_api():
    """Verify dashboard summary metrics calculation API."""
    response = client.get("/api/v1/dashboard/summary")
    assert response.status_code == 200
    data = response.json()
    assert "total_products" in data
    assert "total_transactions" in data
    assert "total_reviews" in data
    assert "open_alerts" in data
    assert "agent_status" in data


def test_risk_analysis_persistence_flow():
    """Verify transaction risk analysis, decision persistence, and audit logging flow."""
    payload = {
        "customer_id": "CUST-9901",
        "product_id": "PROD-1001",
        "seller_id": "SELL-8812",
        "amount": 4999.0,
        "currency": "USD",
        "payment_method": "Prepaid Card",
        "account_age_days": 1,
        "device_id": "dev-fp-tor-proxy",
        "ip_address": "185.220.101.4",
        "location": "Bucharest, Romania",
        "order_history_count": 0,
        "return_history_count": 0,
    }
    response = client.post("/api/v1/risk/analyze", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "transaction" in data
    assert "decision" in data
    assert "audit_log_id" in data
    assert data["transaction"]["risk_level"] in ["HIGH", "CRITICAL"]


def test_product_verification_persistence_flow():
    """Verify product verification, agent decision persistence, and alert generation."""
    payload = {
        "seller_id": "SELL-8812",
        "name": "Luxury Leather Handbag Outlet",
        "brand": "VogueBoutique",
        "category": "Fashion",
        "description": "Discount handbag",
        "price": 25.0,  # Unusually low price triggering counterfeit flag
        "currency": "USD",
        "image_urls": ["https://example.com/handbag.jpg"],
    }
    response = client.post("/api/v1/products/verify", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "product" in data
    assert "decision" in data
    assert data["product"]["verification_status"] in ["FLAGGED", "REJECTED"]


def test_review_analysis_persistence_flow():
    """Verify review toxicity moderation and decision persistence."""
    payload = {
        "product_id": "PROD-1001",
        "customer_id": "USER-9941",
        "rating": 1,
        "review_text": "THIS IS TERRIBLE DO NOT BUY THIS ITEM GO TO HTTP://SPAM-SCAM-DEALS.SITE FOR DISCOUNT NOW!!!",
        "verified_purchase": False,
    }
    response = client.post("/api/v1/reviews/analyze", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "review" in data
    assert data["review"]["decision"] in ["FLAGGED", "REJECTED"]


def test_alerts_pagination_and_status_patch():
    """Verify alert listing pagination and status resolution patch."""
    list_res = client.get("/api/v1/alerts?page=1&limit=5")
    assert list_res.status_code == 200
    paginated = list_res.json()
    assert "items" in paginated
    assert "total" in paginated
    assert "total_pages" in paginated

    if len(paginated["items"]) > 0:
        alert_id = paginated["items"][0]["alert_id"]
        patch_res = client.patch(
            f"/api/v1/alerts/{alert_id}/status",
            json={"status": "RESOLVED", "resolution_notes": "Cleared by analyst verification."},
        )
        assert patch_res.status_code == 200
        assert patch_res.json()["status"] == "RESOLVED"


def test_audit_logs_pagination():
    """Verify audit logs listing pagination and ordering (newest first)."""
    res = client.get("/api/v1/audit-logs?page=1&limit=10")
    assert res.status_code == 200
    data = res.json()
    assert "items" in data
    assert "total" in data


def test_validation_error_handling():
    """Verify validation error response formatting."""
    res = client.post("/api/v1/products/verify", json={"price": "invalid_number"})
    assert res.status_code == 422
