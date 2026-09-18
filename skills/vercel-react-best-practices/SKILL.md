---
name: vercel-react-best-practices
description: "React component best practices tailored for React + Vite single-page applications."
---

# React + Vite Best Practices

## Guidelines
1. **Component Scoping**: Keep state local to components. Avoid global state unless shared across disconnected subtrees.
2. **Immutability**: Never mutate state or props directly. Use pure state transitions.
3. **Effect Cleanups**: Every `useEffect` subscribing to events or subscriptions must return a cleanup function.
4. **Performance Optimization**: Memoize expensive computations (`useMemo`) and callbacks (`useCallback`) passed to list items.
5. **Vite Bundling**: Use dynamic imports (`import()`) for route-level code splitting.
