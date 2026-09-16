# ADR 0003: Redis Pub/Sub and Key Expiration for Presence Tracking & Scaling

## Context
When scaling FastAPI across multiple worker instances, WebSocket connections are distributed across pods. Instances need a mechanism to broadcast messages to all room participants regardless of which pod holds their socket connection. Additionally, real-time presence requires active heartbeats.

## Decision
We select **Redis** for Pub/Sub message broadcasting and key TTL presence tracking (`SET user:presence:{id} online EX 30`).

## Rationale
- **In-Memory Speed**: Sub-millisecond pub/sub message propagation.
- **Key Expiration (TTL)**: Automatically clears inactive user presence if a heartbeat is missed without writing heavy DB operations.

## Consequences
- Requires running a Redis instance/cluster alongside the application backend.
