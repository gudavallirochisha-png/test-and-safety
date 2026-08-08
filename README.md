# Enterprise AI Trust & Safety Platform 🛡️🛒

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com)
[![React 19](https://img.shields.io/badge/React-19.0.0-61DAFB.svg?logo=react)](https://react.dev)
[![MongoDB](https://img.shields.io/badge/MongoDB-Motor_Async-47A248.svg?logo=mongodb)](https://www.mongodb.com)

An enterprise-grade, multi-modal **AI Trust & Safety Platform** designed specifically for high-throughput e-commerce marketplaces. Engineered with **Clean Architecture**, **Motor Async MongoDB Persistence**, **Repository Pattern**, and **Multi-Modal AI Evaluation Pipelines**.

- **GitHub Repository**: [https://github.com/gudavallirochisha-png/test-and-safety.git](https://github.com/gudavallirochisha-png/test-and-safety.git)

---

## 🏗️ End-to-End System Architecture

```mermaid
graph TD
    Client[E-Commerce Marketplace Client] -->|HTTP / REST| WebApp[React 19 Frontend - Vite + Zustand]
    WebApp -->|Axios REST / JSON| Gateway[FastAPI Gateway - Port 8000]
    
    subgraph Backend Core Layer
        Gateway --> Router[API v1 Master Router]
        Router --> Service[Service Layer - Risk, Product, Review, Alert Services]
        Service --> Repo[Repository Layer - Motor Async MongoDB]
    end

    subgraph Intelligent Micro-Agent Subsystems
        Service -->|Tabular Metrics| RiskAgent[Risk Agent - XGBoost v2.4]
        Service -->|NLP Text| ReviewAgent[Review Agent - DistilBERT v1.9]
        Service -->|Visual Imagery| AuthAgent[Authenticity Agent - YOLO v8x]
    end

    subgraph Persistent Storage Layer
        Repo -->|Motor Async Driver| MongoDB[(MongoDB Atlas Cloud / Local DB)]
        MongoDB --> ProductsColl[(products)]
        MongoDB --> TxnColl[(transactions)]
        MongoDB --> ReviewColl[(reviews)]
        MongoDB --> AlertColl[(alerts)]
        MongoDB --> DecisionColl[(agent_decisions)]
        MongoDB --> AuditColl[(audit_logs)]
    end
```

---

## 🔄 Multi-Document Persistence & Decision Flow

```mermaid
sequenceDiagram
    autonumber
    participant UI as React 19 Frontend
    participant API as FastAPI Gateway
    participant Agent as Synthetic AI Agent
    participant Repo as Repository Layer
    participant DB as MongoDB Storage

    UI->>API: POST /api/v1/risk/analyze (Transaction Payload)
    API->>Agent: Evaluate Risk Features (Amount, Velocity, Tor IP)
    Agent-->>API: Return Risk Score (0.94) & Risk Factors
    API->>Repo: 1. Save Transaction Record (`transactions`)
    API->>Repo: 2. Save Agent Decision Record (`agent_decisions`)
    API->>Repo: 3. Append Audit Trail Entry (`audit_logs`)
    alt Risk Level >= HIGH
        API->>Repo: 4. Trigger Incident Alert (`alerts`)
    end
    Repo->>DB: Persist Documents via Motor Driver
    DB-->>UI: Return Analysis Result & Alert Status
```

---

## 🎯 Core Features & Modules

### 1. Command Center Dashboard (`/`)
- Real-time KPI summary (*Total Products, Transactions, Reviews, Fraud Alerts*).
- Live health indicators for **XGBoost Risk Agent**, **YOLO Authenticity Agent**, and **DistilBERT Review Agent**.
- Monthly prevented financial loss trend chart.
- Quick scan trigger button dispatching synchronous evaluation jobs.

### 2. Product Verification & Computer Vision (`/products`)
- Drag & drop product photo upload area.
- Interactive **YOLO v8 Bounding Box Inspection Modal** highlighting logo geometry deformations and trademark anomalies.
- Filter products by risk level (*Critical, High, Medium, Low*).

### 3. Order & Seller Risk Analysis (`/orders`)
- Checkout transaction risk score table.
- Selected order deep-dive panel showing **XGBoost 0-100 Score**, Customer Telemetry (IP, Device Fingerprint, Tor exit node detection), and Order Context.
- Analyst manual decision actions (**Approve** / **Reject Order**).

### 4. Review Moderation & Content Safety (`/reviews`)
- DistilBERT NLP toxicity scoring (-1.0 to +1.0 sentiment, toxicity percentage, spam URL detection).
- Reviewer account age and past flagging history.
- Content moderation actions (**Publish Review** / **Purge & Block**).

### 5. Security Fraud Alerts Queue (`/alerts`)
- Incident cards categorized by severity (*Critical, High, Medium*).
- Filter alerts by status and agent source.
- Resolution action patches (`PATCH /api/v1/alerts/{alert_id}/status`) updating status, `resolved_at`, `resolution_notes`, and audit log entries.

### 6. Audit Logs & Compliance Ledger (`/audit`)
- Immutable append-only audit trail logging every automated agent decision and analyst manual action.
- Displays timestamp, actor type, target entity ID, action type, status, and confidence percentage.

### 7. Telemetry Analytics (`/analytics`)
- Category risk volume breakdown.
- Hourly threat velocity line chart tracking attack spikes.
- Geographic fraud origin heatmap.
- Agent accuracy vs. latency matrix.

### 8. System Settings (`/settings`)
- Dark theme configuration.
- Real-time incident email & Slack webhook toggles.
- AI Agent model threshold sliders (*XGBoost threshold, DistilBERT toxicity threshold*).
- Environment telemetry system info.

---

## 🗄️ Database Collections Schema

| Collection | Document Key | Primary Attributes | Role |
| :--- | :--- | :--- | :--- |
| **`products`** | `product_id` | `seller_id`, `name`, `price`, `authenticity_score`, `verification_status` | Product item listings & visual verification state (`VERIFIED`, `FLAGGED`, `REJECTED`, `MANUAL_REVIEW`) |
| **`transactions`** | `transaction_id` | `customer_id`, `amount`, `risk_score`, `risk_level`, `decision` | Checkout order risk metrics (`LOW`, `MEDIUM`, `HIGH`, `CRITICAL` risk; `APPROVED`, `MANUAL_REVIEW`, `BLOCKED`) |
| **`reviews`** | `review_id` | `product_id`, `rating`, `review_text`, `fake_probability`, `decision` | Moderated feedback text & toxicity classification (`APPROVED`, `FLAGGED`, `REJECTED`, `MANUAL_REVIEW`) |
| **`alerts`** | `alert_id` | `severity`, `agent`, `entity_type`, `entity_id`, `status` | Incident queue & analyst resolution lifecycle (`OPEN`, `INVESTIGATING`, `RESOLVED`, `DISMISSED`) |
| **`agent_decisions`** | `decision_id` | `agent`, `agent_type`, `model_version`, `score`, `confidence` | Generic prediction ledger for AI model evaluation records (`RISK`, `AUTHENTICITY`, `REVIEW`) |
| **`audit_logs`** | `audit_id` | `timestamp`, `actor_type`, `agent`, `action`, `status` | Immutable append-only audit trail for all system CRUD actions and manual decisions |

---

## ⚡ Local Development Setup

### Prerequisites
- **Python**: v3.12+
- **Node.js**: v18+
- **MongoDB**: Local MongoDB instance or MongoDB Atlas URI

### 1. Environment Setup
Copy `.env.example` to `.env` in the project root directory:
```bash
cp .env.example .env
```
Ensure your `.env` contains your connection credentials:
```env
MONGODB_URI=mongodb+srv://rochishagudavalli_db_user:HxFa1iSkGWC61iSV@cluster0.lc4dnd3.mongodb.net/
MONGODB_DATABASE=trust_safety
```

### 2. Install Dependencies
```bash
# Install Python backend dependencies
pip install -r requirements.txt

# Install Node frontend dependencies
cd frontend && npm install --legacy-peer-deps
```

### 3. Seed MongoDB Database
Populate all 6 MongoDB collections with synthetic demo data:
```bash
python3 scripts/seed_database.py
```

### 4. Start FastAPI Backend (Terminal 1)
```bash
uvicorn backend.app.main:app --reload --port 8000
```
- **Interactive OpenAPI Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Health Check**: [http://localhost:8000/api/v1/health](http://localhost:8000/api/v1/health)

### 5. Start React Frontend (Terminal 2)
```bash
cd frontend && npm run dev
```
- **Web App Interface**: [http://localhost:5173](http://localhost:5173)

---

## 🧪 Automated Testing

Execute the PyTest test suite verifying database repositories, persistence workflows, paginated alerts, and dashboard aggregation logic:
```bash
python3 -m pytest tests/test_phase4_repositories.py
```

---

## 🌐 Hackathon Submission Deliverables

- **GitHub Repository**: [https://github.com/gudavallirochisha-png/test-and-safety.git](https://github.com/gudavallirochisha-png/test-and-safety.git)
- **API Documentation**: Served live at `http://localhost:8000/docs`
- **Presentation Recording**: Browser session recording generated during automated end-to-end verification.
