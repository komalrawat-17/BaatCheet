# BaatCheet — Technical Specification

## 1. System Overview
BaatCheet is a full-stack, real-time chat application utilizing a modern async Python backend and a React-based frontend.

## 2. Backend Stack
- **Framework**: FastAPI (Python 3.12)
- **Database**: PostgreSQL 16
- **ORM**: SQLAlchemy 2.0 (Async)
- **Migrations**: Alembic
- **Caching & Pub/Sub**: Redis 7
- **Authentication**: Passlib (Argon2), python-jose (JWT)

## 3. Frontend Stack (Deprecated in Current Scope)
- *Note: Frontend implementation has been rolled back per user request, but the intended stack was React 18, Vite, and Vanilla CSS.*

## 4. Infrastructure & DevOps
- **Containerization**: Docker (multi-stage builds)
- **Orchestration**: Docker Compose (local), Kubernetes (production)
- **Package Management**: Helm
- **IaC**: Terraform (AWS targeted)
- **CI/CD**: GitHub Actions
