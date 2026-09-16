# System Architecture Document: BaatCheet

## 1. High-Level Architectural Design

```mermaid
flowchart TB
    subgraph Client Layer
        Clients["Web/Mobile Clients"]
    end

    subgraph API & Gateway Layer
        FastAPI["FastAPI Web Server (Async ASGI)"]
        WSManager["WebSocket Connection Manager"]
    end

    subgraph Data & Messaging Layer
        Redis["Redis (Pub/Sub & Presence TTL)"]
        Postgres[(PostgreSQL Relational DB)]
    end

    Clients -->|REST API (HTTPS)| FastAPI
    Clients <-->|Real-Time Chat (WSS)| WSManager
    FastAPI -->|Async SQLAlchemy| Postgres
    WSManager -->|Publish / Subscribe| Redis
    WSManager -->|Async DB Write| Postgres
```

## 2. Component Descriptions
- **FastAPI ASGI Server**: High-concurrency Python backend using `asyncio` for non-blocking I/O. Handles REST endpoints for Auth, Rooms, and Messages.
- **WebSocket Manager**: Manages real-time RFC 6455 connections, handles JWT validation on handshake, and tracks local connections per pod.
- **Redis Broker**: Enables cross-pod message fanout using Pub/Sub. Manages user presence heartbeats (`EX 30` seconds) to avoid heavy DB writes.
- **PostgreSQL Database**: Relational database storing users, rooms, and historical messages. Accessed asynchronously via `asyncpg` and SQLAlchemy 2.0.
