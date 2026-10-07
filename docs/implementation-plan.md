# BaatCheet — 2-Month Implementation Plan

> A week-by-week roadmap focusing on product features, backend services, frontend experience, and testing.

---

## 📌 Executive Summary

This plan outlines the complete engineering journey for **BaatCheet**, spanning two months (8 weekly phases). 
- **Month 1** establishes the foundation: database schemas, security, REST APIs, real-time WebSocket communication, and automated backend tests.
- **Month 2** focuses on the user experience: building the React interface, authentication screens, live chat interaction, presence indicators, responsive design, and end-to-end testing.

---

## 🗓️ Month 1: Backend Services, Real-Time Engine & Testing

### Phase 1 (Week 1) — Architecture & Database Design `[COMPLETED]`
- Defined system architecture and selected modern async Python (FastAPI + Asyncpg).
- Designed PostgreSQL relational schemas for `User`, `Room`, and `Message` models.
- Set up Async SQLAlchemy engine, session lifecycle management, and database configuration.
- Established Pydantic validation models for strict request/response data integrity.

### Phase 2 (Week 2) — Authentication & Security Layer `[COMPLETED]`
- Implemented Argon2 password hashing via Passlib for secure credential storage.
- Created JWT (JSON Web Token) generation, signing, and verification utilities.
- Implemented `POST /api/v1/auth/register` to onboard new users with unique usernames and emails.
- Implemented `POST /api/v1/auth/login` to authenticate users and issue access tokens.
- Created reusable dependency injection (`get_current_user`) to protect API routes.

### Phase 3 (Week 3) — Chat Rooms & Message History `[COMPLETED]`
- Built `POST /api/v1/rooms` to allow users to create public and private chat channels.
- Built `GET /api/v1/rooms` to retrieve accessible chat rooms.
- Created `GET /api/v1/messages/{room_id}` with timestamp sorting for historical message retrieval.
- Linked user profiles to sent messages so names and avatars appear alongside chat logs.

### Phase 4 (Week 4) — Real-Time WebSockets & Backend Test Suite `[COMPLETED]`
- Implemented RFC 6455 WebSocket gateway at `/ws/chat/{room_id}` with JWT handshake validation.
- Integrated Redis Pub/Sub for horizontal message fanout across active channels.
- Added heartbeat ping/pong protocol and typing indicator message frames.
- Built automated backend test suite using `pytest` and `pytest-asyncio` with in-memory SQLite fixtures.

---

## 🗓️ Month 2: Frontend Client, Real-Time UX & Verification

### Phase 5 (Week 5) — Frontend Foundation & Design System `[UPCOMING]`
- Initialize frontend application using Vite and React.
- Craft a custom CSS design system with curated typography, harmonious color palettes, and dark mode.
- Build reusable UI component primitives:
  - Buttons (primary, ghost, danger)
  - Text inputs and form error wrappers
  - User avatar bubbles with status dots
  - Modal dialogs and alert banners
- Establish application layout shell (sidebar, navigation header, main content area).

### Phase 6 (Week 6) — Authentication & Room Navigation UI `[UPCOMING]`
- Design and build welcoming Login and Sign-Up screens with client-side form validation.
- Store authentication state securely with automatic token refresh handling.
- Build protected route wrappers to prevent unauthorized access to chat channels.
- Create Room Sidebar displaying:
  - List of joined channels
  - Unread message counters
  - "Create New Room" modal dialog
  - Search bar to filter channels quickly

### Phase 7 (Week 7) — Live Chat Interface & Interactive Features `[UPCOMING]`
- Implement WebSocket client connection lifecycle inside React (connect, disconnect, auto-reconnect).
- Build the core Chat Message Feed:
  - Grouped message bubbles (distinguishing own messages from peer messages)
  - Timestamps and sender profile avatars
  - Auto-scroll to latest message on incoming traffic
- Implement live typing indicator ("*Komal is typing...*").
- Implement live room presence sidebar showing online members and their status.
- Add optimistic UI updates so sent messages display instantly before server roundtrip.

### Phase 8 (Week 8) — End-to-End Testing, Polish & Launch Readiness `[UPCOMING]`
- Write automated end-to-end tests using Playwright:
  - Verify complete user registration flow.
  - Verify login and session persistence.
  - Verify multi-user real-time message exchange between two browser instances.
- Refine responsive layouts for seamless usability on mobile devices, tablets, and desktops.
- Add micro-animations (smooth hover states, fade-ins for messages, skeleton loaders).
- Conduct accessibility audit (contrast ratios, keyboard navigation, screen reader labels).
- Finalize user guides and developer handover documentation.

---

## 📊 Summary Timeline Matrix

| Phase | Focus Area | Key Deliverables | Status |
| :---: | :--- | :--- | :---: |
| **Phase 1** (Week 1) | Data Modeling | PostgreSQL models, async DB engine, Pydantic schemas | Done |
| **Phase 2** (Week 2) | Security & Auth | Argon2 hashing, JWT tokens, Register/Login APIs | Done |
| **Phase 3** (Week 3) | Room & Message APIs | Room management, message history, protected routes | Done |
| **Phase 4** (Week 4) | WebSockets & Tests | RFC 6455 gateway, Redis fanout, automated pytest suite | Done |
| **Phase 5** (Week 5) | Frontend Design System | Vite + React setup, custom CSS tokens, base UI components | Upcoming |
| **Phase 6** (Week 6) | Auth & Navigation UI | Login/Register pages, route guards, room browser sidebar | Upcoming |
| **Phase 7** (Week 7) | Real-Time Chat Feed | Live WebSocket feed, typing indicators, presence tracking | Upcoming |
| **Phase 8** (Week 8) | E2E Testing & Polish | Playwright tests, mobile responsiveness, final UX polish | Upcoming |
