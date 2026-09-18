---
name: ponytail
description: "Prioritizes code reuse, standard library utilities, and platform capabilities over writing custom code. Emphasizes minimal, YAGNI solutions."
---

# Ponytail Skill

## Guidelines
1. **Reuse Existing Code**: Before writing a new function or helper, check if an existing helper in the codebase already fulfills the requirement.
2. **Prefer Standard Library & Native Platform APIs**: Use built-in language features and standard libraries before pulling in third-party dependencies.
3. **YAGNI (You Ain't Gonna Need It)**: Implement strictly what is required for the task. Do not over-engineer or add premature abstractions.
4. **Precedence**: This skill's rules are subordinate to `baatcheet-global`, GSD workflow, and domain skills. Never reduce test coverage, security, validation, or accessibility.
