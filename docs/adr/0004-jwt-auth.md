# ADR 0004: OWASP JWT Access & HTTP-Only Refresh Token Security Architecture

## Context
User authentication must be secure against Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF) attacks while supporting stateless REST and WSS connections.

## Decision
We implement short-lived **JWT access tokens** (15 minutes) passed in request headers/query params for WebSockets, paired with **HTTP-only, Secure, SameSite refresh cookies**.

## Rationale
- **OWASP Compliance**: HTTP-only cookies prevent JavaScript access to long-lived refresh credentials.
- **Stateless Verification**: Access tokens can be cryptographically verified by backend services without constant database lookups.

## Consequences
- Requires an explicit refresh endpoint on the backend and automatic token rotation on the frontend client.
