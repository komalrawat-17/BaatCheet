# BaatCheet — Lessons Learned

> **Last Updated**: 2026-10-06

This document tracks key technical discoveries, bug resolutions, and architectural lessons learned during the development of BaatCheet.

## 1. FastAPI WebSockets
- **Lesson**: FastAPI's `WebSocketDisconnect` exception needs to be caught specifically to gracefully handle client disconnections without crashing the event loop.
- **Action**: Implemented a robust `ConnectionManager` that catches `WebSocketDisconnect` and general `Exception` to ensure cleanup.

## 2. Redis Pub/Sub
- **Lesson**: When scaling across multiple uvicorn workers, local in-memory active connections are not shared. 
- **Action**: Used Redis Pub/Sub as a backplane to fan-out messages to all connected clients across different pods/workers.

## 3. JWT Security
- **Lesson**: Storing access tokens in `localStorage` exposes them to XSS.
- **Action**: The architecture mandates short-lived access tokens and HTTP-only, secure cookies for refresh tokens (ADR-0004).
