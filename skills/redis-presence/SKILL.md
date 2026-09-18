---
name: redis-presence
description: "Redis pub/sub channels, presence tracking, online status heartbeats, and room broadcasting."
---

# Redis Pub/Sub & Presence Skill

## Guidelines
1. **Pub/Sub Channels**: Segregate Redis channels by scope (`chat:room:{room_id}`, `chat:user:{user_id}`).
2. **Presence Management**: Use Redis Key Expiration (TTL) for active user heartbeats (`SET user:presence:{user_id} online EX 30`).
3. **Distributed Messaging**: Broadcast WebSocket events across horizontal FastAPI app instances using Redis Pub/Sub backplane.
4. **Clean Termination**: Ensure Redis connections and subscriptions are properly closed on worker shutdown.
