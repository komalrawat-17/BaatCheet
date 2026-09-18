---
name: auth-jwt-oauth
description: "OWASP-compliant JWT authentication, token rotation, secret management, and OAuth2 integration patterns."
---

# Auth JWT & OAuth2 Security Skill

## Guidelines
1. **Token Security**: Issue short-lived access tokens (e.g. 15 minutes) and HTTP-only, secure, SameSite refresh cookies.
2. **Algorithm Enforcement**: Explicitly specify strong signing algorithms (e.g. `HS256` or `RS256`). Disallow `none` algorithm.
3. **OWASP Best Practices**: Prevent XSS by storing access tokens securely and avoiding `localStorage` for sensitive credentials.
4. **Token Revocation**: Maintain token blacklist or rotation tracking in Redis for prompt logout invalidation.
