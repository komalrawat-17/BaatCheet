---
name: postgres-best-practices
description: "PostgreSQL database architecture, schema design, indexing strategies, query performance tuning, and connection pooling."
---

# PostgreSQL Best Practices

## Guidelines
1. **Schema Design**: Use canonical naming (lowercase snake_case for tables and columns). Always include `id UUID PRIMARY KEY`, `created_at TIMESTAMPTZ`, and `updated_at TIMESTAMPTZ`.
2. **Indexing**: Add indexes on foreign keys and columns frequently used in `WHERE`, `JOIN`, and `ORDER BY` clauses. Use composite or partial indexes where appropriate.
3. **Query Optimization**: Avoid `SELECT *`. Explicitly select required columns. Inspect `EXPLAIN ANALYZE` for slow queries.
4. **Connection Pooling**: Use connection poolers (e.g. AsyncPG pool or PgBouncer) for FastAPI service efficiency.
5. **Migrations**: Apply all schema changes using versioned migration scripts (Alembic).
