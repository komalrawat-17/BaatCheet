---
name: chat-websockets
description: "RFC 6455 and FastAPI WebSocket architecture patterns, connection lifecycle, heartbeats, and message frame protocols."
---

# Chat WebSockets Architecture Skill

## Guidelines
1. **Connection Lifecycle**: Enforce explicit connection handshake, auth token verification during handshake, message ping/pong heartbeats, and graceful disconnection cleanups.
2. **Frame Protocol**: Use structured JSON payloads for WebSocket messages containing `{ "type": "...", "payload": {...}, "timestamp": "..." }`.
3. **Reconnection & Backoff**: Client UI must implement exponential backoff with jitter on WebSocket disconnects.
4. **Error Handling**: Handle socket exceptions gracefully without crashing the server event loop.
