"""
Standalone Database Seeder Script for Phase 4 MongoDB Persistence.
Inserts synthetic demo data across all 6 collections:
1. products
2. transactions
3. reviews
4. alerts
5. agent_decisions
6. audit_logs
"""

import asyncio
from datetime import datetime, timezone
from motor.motor_asyncio import AsyncIOMotorClient
from backend.app.config.settings import settings
from backend.app.core.logging import logger


async def seed_database():
    logger.info(f"Connecting to MongoDB at {settings.MONGODB_URI} for database seeding...")
    client = AsyncIOMotorClient(settings.MONGODB_URI)
    db = client[settings.MONGODB_DATABASE]

    now = datetime.now(timezone.utc)

    # 1. Seed products
    products = [
        {
            "product_id": "PROD-1001",
            "seller_id": "SELL-8812",
            "name": "Luxury Designer Leather Handbag",
            "brand": "VogueBoutique",
            "category": "Fashion & Accessories",
            "description": "High quality leather handbag outlet sale",
            "price": 1499.99,
            "currency": "USD",
            "image_urls": ["https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=500"],
            "status": "COUNTERFEIT_FLAGGED",
            "authenticity_score": 14.0,
            "counterfeit_probability": 0.86,
            "verification_status": "REJECTED",
            "created_at": now,
            "updated_at": now,
        },
        {
            "product_id": "PROD-1002",
            "seller_id": "SELL-4109",
            "name": "Wireless Noise Cancelling Headphones v2",
            "brand": "TechHaven",
            "category": "Electronics",
            "description": "Active noise cancellation audio headphones",
            "price": 299.00,
            "currency": "USD",
            "image_urls": ["https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"],
            "status": "VERIFIED",
            "authenticity_score": 98.0,
            "counterfeit_probability": 0.02,
            "verification_status": "VERIFIED",
            "created_at": now,
            "updated_at": now,
        },
        {
            "product_id": "PROD-1003",
            "seller_id": "SELL-9910",
            "name": "Ultra Edition Smartwatch Stainless Steel",
            "brand": "GadgetCorp",
            "category": "Wearables",
            "description": "Smartwatch with biometric sensors",
            "price": 89.99,
            "currency": "USD",
            "image_urls": ["https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500"],
            "status": "MANUAL_REVIEW",
            "authenticity_score": 42.0,
            "counterfeit_probability": 0.58,
            "verification_status": "MANUAL_REVIEW",
            "created_at": now,
            "updated_at": now,
        },
        {
            "product_id": "PROD-1004",
            "seller_id": "SELL-1102",
            "name": "Ergonomic Mesh Office Chair",
            "brand": "FurnishDirect",
            "category": "Home & Office",
            "description": "Lumbar support office mesh chair",
            "price": 249.50,
            "currency": "USD",
            "image_urls": ["https://images.unsplash.com/photo-1580481072645-022f9a6d129b?w=500"],
            "status": "VERIFIED",
            "authenticity_score": 96.0,
            "counterfeit_probability": 0.04,
            "verification_status": "VERIFIED",
            "created_at": now,
            "updated_at": now,
        },
    ]

    await db.products.delete_many({})
    await db.products.insert_many(products)
    logger.info(f"Seeded {len(products)} products.")

    # 2. Seed transactions
    transactions = [
        {
            "transaction_id": "TXN-8001",
            "customer_id": "CUST-4190",
            "product_id": "PROD-1001",
            "seller_id": "SELL-8812",
            "amount": 4999.00,
            "currency": "USD",
            "payment_method": "Credit Card (Prepaid)",
            "account_age_days": 1,
            "device_id": "dev-fp-9910-proxy",
            "ip_address": "185.220.101.4",
            "location": "Bucharest, Romania",
            "order_history_count": 0,
            "return_history_count": 0,
            "risk_score": 0.94,
            "risk_level": "CRITICAL",
            "decision": "BLOCKED",
            "risk_factors": ["Known Tor Exit Node IP", "Velocity spike: 12 checkouts in 3 mins"],
            "created_at": now,
            "updated_at": now,
        },
        {
            "transaction_id": "TXN-8002",
            "customer_id": "CUST-8102",
            "product_id": "PROD-1002",
            "seller_id": "SELL-4109",
            "amount": 299.00,
            "currency": "USD",
            "payment_method": "Apple Pay",
            "account_age_days": 420,
            "device_id": "dev-fp-4412-ios",
            "ip_address": "73.189.24.110",
            "location": "San Francisco, CA",
            "order_history_count": 18,
            "return_history_count": 1,
            "risk_score": 0.04,
            "risk_level": "LOW",
            "decision": "APPROVED",
            "risk_factors": [],
            "created_at": now,
            "updated_at": now,
        },
        {
            "transaction_id": "TXN-8003",
            "customer_id": "CUST-1092",
            "product_id": "PROD-1003",
            "seller_id": "SELL-9910",
            "amount": 1250.00,
            "currency": "USD",
            "payment_method": "Crypto Gateway",
            "account_age_days": 4,
            "device_id": "dev-fp-7718-headless",
            "ip_address": "194.26.29.11",
            "location": "Limassol, Cyprus",
            "order_history_count": 1,
            "return_history_count": 0,
            "risk_score": 0.81,
            "risk_level": "HIGH",
            "decision": "MANUAL_REVIEW",
            "risk_factors": ["Headless browser fingerprint", "Device linked to chargebacks"],
            "created_at": now,
            "updated_at": now,
        },
    ]

    await db.transactions.delete_many({})
    await db.transactions.insert_many(transactions)
    logger.info(f"Seeded {len(transactions)} transactions.")

    # 3. Seed reviews
    reviews = [
        {
            "review_id": "REV-3001",
            "product_id": "PROD-1001",
            "customer_id": "USER-9941",
            "rating": 1,
            "review_text": "THIS IS TERRIBLE DO NOT BUY THIS ITEM GO TO HTTP://SPAM-SCAM-DEALS.SITE FOR DISCOUNT NOW!!!",
            "verified_purchase": False,
            "fake_probability": 0.98,
            "authenticity_score": 5.0,
            "decision": "REJECTED",
            "risk_factors": ["SPAM_PROMOTION_URL", "BOT_PATTERN"],
            "created_at": now,
            "updated_at": now,
        },
        {
            "review_id": "REV-3002",
            "product_id": "PROD-1002",
            "customer_id": "USER-3310",
            "rating": 5,
            "review_text": "Outstanding active noise cancellation! Audio clarity is crisp and battery life easily lasts two full working days.",
            "verified_purchase": True,
            "fake_probability": 0.02,
            "authenticity_score": 98.0,
            "decision": "APPROVED",
            "risk_factors": [],
            "created_at": now,
            "updated_at": now,
        },
    ]

    await db.reviews.delete_many({})
    await db.reviews.insert_many(reviews)
    logger.info(f"Seeded {len(reviews)} reviews.")

    # 4. Seed alerts
    alerts = [
        {
            "alert_id": "ALT-5001",
            "type": "SEC-TOR-VELOCITY",
            "severity": "CRITICAL",
            "agent": "Risk Agent",
            "entity_type": "Transaction",
            "entity_id": "TXN-8001",
            "title": "High Velocity Tor Checkout Ring Detected",
            "description": "Risk Agent identified 14 rapid checkout attempts originating from Tor Exit Node.",
            "confidence": 0.95,
            "status": "OPEN",
            "created_at": now,
            "resolved_at": None,
            "resolution_notes": None,
        },
        {
            "alert_id": "ALT-5002",
            "type": "CV-LOGO-TM",
            "severity": "HIGH",
            "agent": "Authenticity Agent",
            "entity_type": "Product",
            "entity_id": "PROD-1001",
            "title": "Counterfeit Trademark Infringement Detected",
            "description": "Authenticity Agent flagged product PROD-1001 with 86% counterfeit probability.",
            "confidence": 0.96,
            "status": "INVESTIGATING",
            "created_at": now,
            "resolved_at": None,
            "resolution_notes": None,
        },
    ]

    await db.alerts.delete_many({})
    await db.alerts.insert_many(alerts)
    logger.info(f"Seeded {len(alerts)} alerts.")

    # 5. Seed agent decisions
    decisions = [
        {
            "decision_id": "DEC-9001",
            "agent": "Risk Agent",
            "agent_type": "RISK",
            "entity_type": "Transaction",
            "entity_id": "TXN-8001",
            "model_version": "v2.4-XGBoost",
            "score": 0.94,
            "confidence": 0.94,
            "decision": "BLOCKED",
            "risk_factors": ["Known Tor Exit Node IP", "High checkout velocity"],
            "metadata": {"amount": 4999.00},
            "created_at": now,
        },
        {
            "decision_id": "DEC-9002",
            "agent": "Authenticity Agent",
            "agent_type": "AUTHENTICITY",
            "entity_type": "Product",
            "entity_id": "PROD-1001",
            "model_version": "v3.1-YOLOv8",
            "score": 14.0,
            "confidence": 0.96,
            "decision": "REJECTED",
            "risk_factors": ["Logo geometry deformation"],
            "metadata": {"brand": "VogueBoutique"},
            "created_at": now,
        },
    ]

    await db.agent_decisions.delete_many({})
    await db.agent_decisions.insert_many(decisions)
    logger.info(f"Seeded {len(decisions)} agent decisions.")

    # 6. Seed audit logs
    audit_logs = [
        {
            "audit_id": "AUD-7001",
            "timestamp": now,
            "actor_type": "AGENT",
            "actor_id": "SYSTEM",
            "agent": "Risk Agent",
            "action": "TRANSACTION_ANALYZED",
            "entity_type": "Transaction",
            "entity_id": "TXN-8001",
            "status": "FLAGGED",
            "decision": "BLOCKED",
            "confidence": 0.94,
            "metadata": {"risk_score": 0.94},
        },
        {
            "audit_id": "AUD-7002",
            "timestamp": now,
            "actor_type": "AGENT",
            "actor_id": "SYSTEM",
            "agent": "Authenticity Agent",
            "action": "PRODUCT_VERIFIED",
            "entity_type": "Product",
            "entity_id": "PROD-1001",
            "status": "FLAGGED",
            "decision": "REJECTED",
            "confidence": 0.96,
            "metadata": {"authenticity_score": 14.0},
        },
    ]

    await db.audit_logs.delete_many({})
    await db.audit_logs.insert_many(audit_logs)
    logger.info(f"Seeded {len(audit_logs)} audit logs.")

    client.close()
    logger.info("✅ Database Seeding Successfully Completed across all 6 collections!")


if __name__ == "__main__":
    asyncio.run(seed_database())
