# ADR 0002: PostgreSQL & Alembic for Primary Data Storage & Migrations

## Context
Persistent data (users, rooms, room memberships, historical messages) requires a reliable relational database with ACID compliance and robust indexing capabilities.

## Decision
We select **PostgreSQL** as the relational database engine and **Alembic** for schema migration management.

## Rationale
- **ACID Guarantees**: Ensures message integrity and relational constraints across users and rooms.
- **Async Driver**: Excellent performance with Python's `asyncpg` driver in FastAPI.
- **Alembic Migrations**: Provides versioned, reproducible database migrations across environments.

## Consequences
- Requires running database migrations as part of deployment pipelines.
