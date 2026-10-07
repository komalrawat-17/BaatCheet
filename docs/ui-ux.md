# BaatCheet — UI/UX Design System (Deprecated/Decoupled)

> **Note**: Per the scope rollback on 2026-10-06, the frontend has been removed from this repository. The API is designed to support the following UI/UX paradigms for any decoupled client.

## 1. Design Principles
1. **Rich Aesthetics**: Vibrant HSL color palettes, dark modes, dynamic gradients, and smooth glassmorphism.
2. **Modern Typography**: Clean font stacks (e.g., Inter, Outfit, Roboto) with distinct visual hierarchies.
3. **Micro-Animations**: Subtle CSS hover effects, active states, and fluid transitions to keep the interface feeling responsive.

## 2. Interaction Design
- **Real-Time Feedback**: Instant message rendering via WebSockets without page reloads.
- **Presence Indicators**: Visual cues (e.g., green dot) indicating active users in a room.
- **Typing Status**: Animated "User is typing..." indicators that timeout automatically.
- **Graceful Degradation**: Clear error states and automatic reconnection logic if the WebSocket drops.

## 3. Recommended Color Palette
- **Background**: `#0b0f19` (Dark Mode Default)
- **Surface**: `rgba(17, 24, 39, 0.75)` (Glassmorphism Cards)
- **Primary Accent**: `#6366f1` (Indigo)
- **Secondary Accent**: `#06b6d4` (Cyan)
- **Success/Online**: `#10b981` (Emerald)
