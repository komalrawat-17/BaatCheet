---
name: webapp-testing
description: "Automated end-to-end web testing guidelines using Playwright for verification of UI components, flows, and accessibility."
---

# WebApp Testing Skill (Playwright)

## Guidelines
1. **Selector Strategy**: Prefer user-visible roles, text contents, and explicit `data-testid` attributes over brittle CSS selectors or deep XPaths.
2. **Asynchronous Waiting**: Rely on Playwright's built-in auto-waiting (`expect(locator).toBeVisible()`) rather than arbitrary `sleep` or hardcoded timeouts.
3. **Isolated Test Execution**: Ensure tests run independently with clean browser contexts and isolated test states.
4. **Visual & Console Verification**: Capture screenshots on failure and monitor browser console output for unexpected JS errors.
