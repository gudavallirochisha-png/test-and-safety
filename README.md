# Enterprise AI Trust & Safety Platform 🛡️🛒

An enterprise-grade, multi-modal **AI Trust & Safety Platform** designed specifically for high-throughput e-commerce marketplaces. This architecture is engineered to evaluate seller risk, detect fake/toxic product reviews, and verify product authenticity using a scalable, microservice-ready micro-agent ecosystem.

---

## 🎯 Purpose of the Project

In modern e-commerce marketplaces, trust and security are critical. The platform addresses three major pillars of risk:
1. **Seller & Transaction Risk**: High-risk seller onboarding, fraudulent transactions, and anomalous payout requests (evaluated via **XGBoost** risk models).
2. **Review & Content Safety**: Fake reviews, incentivized feedback, toxicity, spam, and policy violations in user-generated text (evaluated via **DistilBERT** NLP models).
3. **Product & Visual Authenticity**: Counterfeit item listings, brand logo trademark violations, and manipulated product imagery (evaluated via **YOLO** object detection models).

*Note: Phase 1 provides the production-ready initialization, Clean Architecture scaffold, directory structure, configuration setups, and type definitions.*

---

## 🛠️ Technology Stack

### Frontend
- **Framework & Runtime**: React 19 (TypeScript)
- **Build Tool**: Vite
- **Styling**: Tailwind CSS (Utility-first design system)
- **Routing**: React Router v6
- **Data Fetching & Caching**: TanStack React Query v5
- **State Management**: Zustand
- **HTTP Client**: Axios

### Backend
- **Framework**: FastAPI (Async Python 3.12)
- **Validation & Serialization**: Pydantic v2
- **ASGI Server**: Uvicorn
- **Architecture**: Clean Architecture (Layered: API -> Services -> Domain -> Data)

### Database & Storage
- **Database**: MongoDB (Async Motor driver)
- **Model Cache & Artifacts**: Local / S3-compatible Object Storage

### Intelligent Agent & AI Ecosystem (Future Integration Scope)
- **Risk Assessment Agent**: XGBoost (Structured tabular feature evaluation)
- **Review Analysis Agent**: DistilBERT (Transformers NLP classification)
- **Authenticity Agent**: YOLO (Ultralytics visual object detection & visual feature extraction)

---

## 📁 Directory & Architecture Structure

```
trust-safety-platform/
├── frontend/                   # React 19 + TypeScript + Vite + Tailwind CSS Frontend Application
│   └── src/
│       ├── assets/             # Branding, static SVGs, and media assets
│       ├── components/         # Reusable presentation & atomic UI components
│       ├── layouts/            # Page layouts and global UI structural wrappers
│       ├── pages/              # View layer page components and route entrypoints
│       ├── routes/             # Client-side route declarations and navigation guards
│       ├── hooks/              # Custom reusable React hooks
│       ├── services/           # Axios API client instances and REST endpoint services
│       ├── store/              # Zustand global state management stores
│       ├── types/              # TypeScript interfaces, DTOs, and domain model definitions
│       └── utils/              # Pure utility functions and formatters
│
├── backend/                    # FastAPI Async Clean Architecture Backend Application
│   └── app/
│       ├── api/                # API Router endpoints (v1 REST controllers)
│       ├── config/             # Environment & settings management via Pydantic BaseSettings
│       ├── core/               # Cross-cutting concerns (logging, exceptions, security base)
│       ├── database/           # Async MongoDB lifecycle & session management
│       ├── models/             # ODM database models
│       ├── schemas/            # Request and Response Pydantic DTO validation schemas
│       ├── services/           # Service layer interfaces containing business domain abstractions
│       ├── utils/              # Pure helper functions and shared utilities
│       └── main.py             # FastAPI application entrypoint, middleware, and CORS configuration
│
├── agents/                     # Intelligent Multi-Modal AI Agent Subsystem
│   ├── risk_agent/             # Seller & Transaction Risk Scoring Agent (XGBoost tabular engine)
│   ├── review_agent/           # Review Sentiment, NLP & Toxicity Analysis Agent (DistilBERT NLP engine)
│   └── authenticity_agent/     # Product Image & Brand Counterfeit Agent (YOLO computer vision engine)
│
├── models/                     # Trained ML model weights storage directory (.pt, .onnx, .json)
├── datasets/                   # Benchmark datasets (Raw, Processed, Synthetic e-commerce samples)
├── docs/                       # Architecture specs, OpenAPI specs, ethics guidelines & workflows
├── tests/                      # Enterprise Test Suite (Unit, Integration, and E2E test suites)
│   ├── unit/                   # Isolated component and service unit tests
│   ├── integration/            # API integration and database adapter tests
│   └── e2e/                    # End-to-end user scenario validation
│
└── scripts/                    # DevOps, database migration/seeding, and AI training helpers
```

---

## 🏗️ Future Architecture & Agent Interaction Flow

```
[ E-Commerce Marketplace Client ] 
               │
               ▼
[ Frontend (React 19 + Zustand) ]
               │ (Axios REST / JSON)
               ▼
[ FastAPI Gateway (backend/app/api) ]
               │
       ┌───────┼──────────────────┐
       │       │ (Async Dispatch) │
       ▼       ▼                  ▼
  [Risk Agent] [Review Agent] [Authenticity Agent]
   (XGBoost)   (DistilBERT)       (YOLO)
       │       │                  │
       └───────┼──────────────────┘
               ▼
    [ MongoDB Storage Layer ]
```

1. **Ingestion Layer**: High-frequency transactions, customer reviews, and product image listings arrive at the FastAPI Gateway via async REST endpoints.
2. **Orchestration Layer**: The API service routes jobs asynchronously to specialized evaluation agents (`risk_agent`, `review_agent`, `authenticity_agent`).
3. **Execution Layer**:
   - Tabular seller metrics pass through **XGBoost** inference.
   - Textual review content passes through fine-tuned **DistilBERT**.
   - Product imagery passes through **YOLO** inference for trademark verification.
4. **Persistence Layer**: Evaluation verdicts, risk scores, and audit trails persist in MongoDB for compliance and reporting.

---

## ⚡ Development Setup

### Prerequisites
- **Node.js**: v18.x or higher
- **Python**: v3.12.x
- **MongoDB**: Local MongoDB instance or MongoDB Atlas URI

### 1. Environment Setup
Clone the repository and copy the environment template:
```bash
cp .env.example .env
```

### 2. Backend Initialization
Navigate to the backend directory, set up a virtual environment, and install dependencies:
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install backend dependencies
pip install -r requirements.txt

# Launch FastAPI development server
uvicorn backend.app.main:app --reload --port 8000
```
API Documentation will be accessible at: `http://localhost:8000/docs`

### 3. Frontend Initialization
Navigate to the frontend directory and install dependencies:
```bash
cd frontend
npm install

# Start Vite dev server
npm run dev
```
Frontend Web Interface will be accessible at: `http://localhost:5173`

---

## 🛡️ Principles & Governance

- **Clean Architecture**: Strict unidirectional dependencies (API -> Domain Interfaces -> Infrastructure Adapters).
- **SOLID Principles**: Highly decoupled modules, single-responsibility services, open for agent expansion.
- **Type Safety**: Strictly enforced TypeScript interfaces on the web and Pydantic v2 models on the server.
