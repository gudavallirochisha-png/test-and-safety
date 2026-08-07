from backend.app.models.product import Product
from backend.app.models.transaction import Transaction
from backend.app.models.review import Review
from backend.app.models.alert import Alert
from backend.app.models.audit_log import AuditLog
from backend.app.core.logging import logger


async def seed_initial_data_if_empty():
    """Seeds initial dataset into MongoDB if collections are empty."""
    if await Product.count() == 0:
        logger.info("Seeding initial products into MongoDB...")
        await Product.insert_all([
            Product(
                product_id="PROD-9021",
                product_name="Luxury Designer Leather Handbag",
                seller_id="SELL-8812",
                seller_name="VogueBoutique Outlet",
                category="Fashion & Accessories",
                price=1499.99,
                image_url="https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=500&auto=format&fit=crop&q=60",
                authenticity_score=14.0,
                risk_level="critical",
                status="COUNTERFEIT_FLAGGED",
                yolo_detections=[{"label": "Counterfeit Logo Misalignment", "confidence": 0.96}],
                flagged_reasons=["Logo proportions violate trademark policy", "Listing price 85% below market baseline"],
            ),
            Product(
                product_id="PROD-9022",
                product_name="Wireless Noise Cancelling Headphones v2",
                seller_id="SELL-4109",
                seller_name="TechHaven Official",
                category="Electronics",
                price=299.00,
                image_url="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&auto=format&fit=crop&q=60",
                authenticity_score=98.0,
                risk_level="low",
                status="VERIFIED",
                yolo_detections=[{"label": "Authentic Brand Seal", "confidence": 0.99}],
                flagged_reasons=[],
            ),
            Product(
                product_id="PROD-9023",
                product_name="Ultra Edition Smartwatch Stainless Steel",
                seller_id="SELL-9910",
                seller_name="GadgetDeals Corp",
                category="Wearables",
                price=89.99,
                image_url="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&auto=format&fit=crop&q=60",
                authenticity_score=42.0,
                risk_level="high",
                status="MANUAL_REVIEW",
                yolo_detections=[{"label": "Cloned Shell Geometry", "confidence": 0.88}],
                flagged_reasons=["Serial number checksum mismatch"],
            ),
        ])

    if await Transaction.count() == 0:
        logger.info("Seeding initial transactions into MongoDB...")
        await Transaction.insert_all([
            Transaction(
                txn_id="TXN-88001",
                order_id="ORD-99014",
                customer_id="CUST-4190",
                customer_name="Alex Mercer",
                seller_id="SELL-8812",
                seller_name="VogueBoutique Outlet",
                amount=4999.00,
                payment_method="Credit Card (Prepaid)",
                ip_address="185.220.101.4",
                device_fingerprint="dev-fp-9910-proxy",
                location="Bucharest, Romania",
                xgboost_risk_score=94.0,
                risk_level="critical",
                fraud_factors=["Known Tor Exit Node IP Address", "Velocity: 12 checkout attempts in 3 minutes"],
                recommendation="REJECT",
                status="BLOCKED",
            ),
            Transaction(
                txn_id="TXN-88002",
                order_id="ORD-99015",
                customer_id="CUST-8102",
                customer_name="Sarah Jenkins",
                seller_id="SELL-4109",
                seller_name="TechHaven Official",
                amount=299.00,
                payment_method="Apple Pay",
                ip_address="73.189.24.110",
                device_fingerprint="dev-fp-4412-ios",
                location="San Francisco, CA, USA",
                xgboost_risk_score=4.0,
                risk_level="low",
                fraud_factors=[],
                recommendation="APPROVE",
                status="APPROVED",
            ),
        ])

    if await Review.count() == 0:
        logger.info("Seeding initial reviews into MongoDB...")
        await Review.insert_all([
            Review(
                review_id="REV-1001",
                product_id="PROD-9021",
                product_title="Luxury Designer Leather Handbag",
                reviewer_id="USER-9941",
                reviewer_name="FastPromoterBot",
                review_text="THIS IS TERRIBLE DO NOT BUY THIS ITEM GO TO HTTP://SPAM-SCAM-DEALS.SITE FOR DISCOUNT NOW!!!",
                rating=1,
                distilbert_toxicity_score=96.0,
                distilbert_sentiment_score=-0.92,
                is_fake_review_prob=98.0,
                risk_level="critical",
                flagged_categories=["SPAM_URL", "TOXICITY"],
                status="REJECTED",
                reviewer_history_stats={"totalReviews": 84, "flaggedRatio": 0.95, "accountAgeDays": 1},
            ),
            Review(
                review_id="REV-1002",
                product_id="PROD-9022",
                product_title="Wireless Noise Cancelling Headphones v2",
                reviewer_id="USER-3310",
                reviewer_name="Michael Scott",
                review_text="Outstanding active noise cancellation! Audio clarity is crisp.",
                rating=5,
                distilbert_toxicity_score=1.0,
                distilbert_sentiment_score=0.94,
                is_fake_review_prob=2.0,
                risk_level="low",
                flagged_categories=[],
                status="PUBLISHED",
                reviewer_history_stats={"totalReviews": 18, "flaggedRatio": 0.0, "accountAgeDays": 420},
            ),
        ])

    if await Alert.count() == 0:
        logger.info("Seeding initial alerts into MongoDB...")
        await Alert.insert_all([
            Alert(
                alert_id="ALT-901",
                alert_code="SEC-TOR-VELOCITY",
                title="High Velocity Tor Checkout Ring Detected",
                description="Risk Agent identified 14 rapid checkout attempts originating from Tor Exit Node.",
                severity="critical",
                agent_source="Risk Agent",
                target_type="Seller",
                target_id="SELL-8812",
                is_resolved=False,
            ),
            Alert(
                alert_id="ALT-902",
                alert_code="CV-LOGO-TM",
                title="Counterfeit Trademark Infringement Detected",
                description="Authenticity Agent flagged product listing PROD-9021 with 96% confidence.",
                severity="high",
                agent_source="Authenticity Agent",
                target_type="Product",
                target_id="PROD-9021",
                is_resolved=False,
            ),
        ])

    if await AuditLog.count() == 0:
        logger.info("Seeding initial audit logs into MongoDB...")
        await AuditLog.insert_all([
            AuditLog(
                audit_id="AUD-501",
                agent_name="Risk Agent (XGBoost v2.4.1)",
                action="REJECT",
                collection="transactions",
                entity_id="TXN-88001",
                status="quarantined",
                confidence_score=94.2,
                details="Automated order rejection triggered by Tor Exit Node detection.",
            ),
            AuditLog(
                audit_id="AUD-502",
                agent_name="Review Agent (DistilBERT v1.9.2)",
                action="REJECT",
                collection="reviews",
                entity_id="REV-1001",
                status="flagged",
                confidence_score=98.0,
                details="Spam URL promotion detected and review content auto-purged.",
            ),
        ])

    logger.info("Database seeding completed.")
