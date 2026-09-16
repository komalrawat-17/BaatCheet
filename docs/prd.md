# BaatCheet — Product Requirements Document (PRD)

> **Version**: 1.0 · **Last Updated**: 2026-10-06 · **Status**: Active

---

## 1. Executive Summary

**BaatCheet** (Hindi: "conversation") is a real-time, multi-room chat platform built for low-latency messaging, live presence tracking, and cloud-native DevOps delivery. It targets student teams, remote engineering squads, and anyone who needs a fast, self-hosted communication tool without the bloat of mainstream alternatives.

---

## 2. Problem Statement

| Pain Point | Impact |
|:---|:---|
| **High Latency & Polling Overhead** | HTTP polling overloads infrastructure and delivers delayed notifications. |
| **Horizontal Scaling Bottlenecks** | Single-node WebSocket servers fail when traffic is distributed across multiple instances. |
| **Unreliable Online Presence** | Users cannot tell whether peers are online, typing, or disconnected in a given room. |
| **Security Vulnerabilities** | Improper token management exposes apps to XSS, CSRF, and credential theft. |

---

## 3. Target Personas

### 3.1 Alex — Remote Student / Developer
- **Role**: CS student & open-source contributor.
- **Goal**: Fast, distraction-free environment to collaborate on project channels and see peer availability in real time.
- **Pain**: Bloated desktop chat apps that consume gigabytes of RAM and take seconds to refresh.
- **Need**: Sub-second delivery, dark mode, simple room joining, clean layout.

### 3.2 Maya — DevOps Engineer
- **Role**: DevOps lead responsible for infrastructure.
- **Goal**: Deploy, monitor, and scale communication services with zero manual overhead using IaC and container orchestration.
- **Pain**: Monolithic apps with opaque deploy steps, hardcoded DB connections, and no health checks.
- **Need**: Multi-stage Dockerfiles, Helm charts, Terraform IaC, automated CI/CD, clean env-var management.

---

## 4. Core Functional Requirements

### FR-1: User Authentication & Authorization
- Registration with unique username + email; Argon2 password hashing.
- JWT access tokens (15 min) + HTTP-only Secure SameSite refresh cookies.
- Token refresh endpoint and `/auth/me` self-lookup.

### FR-2: Multi-Room Chat Engine
- Create public or private rooms with name and description.
- Real-time bidirectional message streaming via RFC 6455 WebSockets.
- Persistent message history stored in PostgreSQL.

### FR-3: Presence & Typing Indicators
- Online / offline status tracked via Redis key TTL heartbeats (30 s).
- Typing indicator events broadcasted to all active room participants.

### FR-4: Room Management
- List rooms, get room by ID.
- Paginated message history for any room (limit + offset).

---

## 5. Non-Functional Requirements

| Attribute | Target |
|:---|:---|
| **Latency** | < 100 ms WebSocket message delivery; < 50 ms REST API response |
| **Scalability** | Stateless FastAPI workers connected via Redis Pub/Sub backplane |
| **Reliability** | Client-side exponential backoff reconnect on WS disconnect |
| **Security** | OWASP-compliant JWT handling; no tokens in localStorage |
| **Observability** | `/health` endpoint for liveness & readiness probes |

---

## 6. User Stories & Epics

### Epic 1 — User Onboarding & Auth
| ID | Story |
|:---|:---|
| US-1.1 | As a new user, I want to create an account so I can join chat rooms. |
| US-1.2 | As a returning user, I want to log in securely and receive a token so my session persists. |

### Epic 2 — Room Discovery & Real-Time Chat
| ID | Story |
|:---|:---|
| US-2.1 | As a participant, I want to select a room and view its message history. |
| US-2.2 | As a participant, I want my messages delivered instantly to all connected members. |

### Epic 3 — Presence & Availability
| ID | Story |
|:---|:---|
| US-3.1 | As a user, I want to see an online badge next to active users. |
| US-3.2 | As a user, I want to see a typing indicator when someone is composing a message. |

### Epic 4 — DevOps & Infrastructure
| ID | Story |
|:---|:---|
| US-4.1 | As a DevOps engineer, I want a single `docker-compose up` command to start the full stack locally. |
| US-4.2 | As a DevOps engineer, I want automated CI/CD that tests, builds, and publishes Docker images on every push. |

---

## 7. Tech Stack Summary

| Layer | Technology |
|:---|:---|
| Backend API | Python 3.12, FastAPI, Uvicorn |
| Database | PostgreSQL 16, Async SQLAlchemy 2.0, Alembic |
| Cache / Pub-Sub | Redis 7 |
| Auth | python-jose (JWT), Passlib / Argon2 |
| WebSockets | FastAPI native WS, RFC 6455 |
| Containers | Docker multi-stage builds |
| Orchestration | Docker Compose, Kubernetes, Helm |
| IaC | Terraform |
| CI/CD | GitHub Actions |

---

## 8. Success Metrics & KPIs

1. WebSocket round-trip latency ≤ 100 ms at P99 under 500 concurrent connections.
2. Backend Docker image ≤ 150 MB compressed.
3. All API endpoints return correct HTTP status codes with ≥ 90 % unit test coverage.
4. Zero critical or high OWASP findings on auth endpoints.
5. `docker-compose up` boots a fully working stack in < 60 seconds on a cold pull.
