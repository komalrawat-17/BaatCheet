# ADR 0001: Selection of WebSockets (RFC 6455) for Real-Time Communication

## Context
BaatCheet requires bidirectional, low-latency communication between clients and backend servers for instant message exchange and live typing notifications.

## Decision
We select **RFC 6455 WebSockets** over HTTP Long-Polling and Server-Sent Events (SSE).

## Rationale
- **Bidirectional Streaming**: Allows full-duplex communication over a single TCP connection.
- **Low Overhead**: Eliminates HTTP request header overhead for every message frame.
- **Widespread Browser Support**: Native support across all modern web browsers.

## Consequences
- Requires persistent connection state management and connection heartbeat (ping/pong) monitoring on the backend.
