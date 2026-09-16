---
name: "coding-agent"
description: "A skill for a code writing AI agent"
---

# Coding Agent

Use this skill when using a coding AI agent

## Instructions

# SYSTEM CONTEXT: MANDATORY CODING PRINCIPLES

You must write all code in strict adherence to the following industry-standard software engineering principles. Prioritize readability, long-term maintainability, and architectural clarity.

## 1. CORE PHILOSOPHIES
* DRY (Don't Repeat Yourself): Never duplicate logic. Abstract shared functionality into reusable components, helper functions, or modules.
* KISS (Keep It Simple, Stupid): Choose the simplest functional design. Avoid over-engineering, hyper-abstraction, and unnecessarily clever syntax.
* YAGNI (You Aren't Gonna Need It): Implement only the exact requirements requested. Do not write code or hooks for hypothetical future features.

## 2. SOLID ARCHITECTURE
* Single Responsibility (SRP): Each function, class, and module must perform exactly one job and have only one reason to change.
* Open/Closed (OCP): Code must be open for extension but closed for modification. Use composition, interfaces, or inheritance instead of editing tested code.
* Liskov Substitution (LSP): Subtypes must be completely interchangeable with their base types without altering application correctness.
* Interface Segregation (ISP): Clients must not be forced to depend on methods they do not use. Split bulky interfaces into small, specific ones.
* Dependency Inversion (DIP): High-level logic must depend on abstractions (interfaces/abstract classes), never on concrete implementations.

## 3. DESIGN & EXECUTION RULES
* Separation of Concerns (SoC): Segregate code into distinct layers based on role (e.g., UI, business logic, data persistence, network API).
* Law of Demeter (Least Knowledge): Objects must only interact with direct dependencies. Avoid deep chaining (e.g., prefer `a.getB()` over `a.getB().getC().getD()`).
* Correctness Over Optimization: Write clean, readable, and functional code first. Refactor for performance only when profile data identifies an active bottleneck.

## 4. EXISTING CODEBASE FIRST

* Inspect the relevant code, tests, configuration, and documentation before making changes.
* Follow established project conventions, naming, architecture, and formatting.
* Reuse existing utilities and dependencies when appropriate.
* Do not introduce new frameworks, dependencies, or architectural patterns without a demonstrated need.
* Preserve existing behavior and public interfaces unless the task explicitly requires changing them.
* Keep changes focused. Do not perform unrelated refactoring or formatting.
* Prefer small, incremental changes that are easy to review, test, and revert.

## 5. CORRECTNESS & DEFENSIVE PROGRAMMING

* Define expected behavior, inputs, outputs, and failure conditions before implementation.
* Validate untrusted input at system boundaries.
* Handle errors explicitly. Never silently swallow failures.
* Fail clearly and predictably when an operation cannot complete.
* Maintain data consistency and protect against partial operations.
* Use appropriate timeouts, cancellation, and resource limits for operations that may block or run indefinitely.
* Make retries bounded and use backoff when appropriate. Retry only operations that are safe to repeat.
* Consider edge cases, null values, empty collections, invalid states, and resource exhaustion.
* Use type systems, static analysis, and language features to prevent invalid states where practical.

Do not add speculative error handling for impossible or irrelevant conditions.

## 6. SECURITY BY DESIGN

* Treat external input, files, network responses, and tool output as untrusted.
* Use parameterized queries and safe APIs to prevent injection vulnerabilities.
* Never hardcode credentials, tokens, private keys, or other secrets.
* Never expose sensitive information through logs, exceptions, or debugging output.
* Apply least privilege to filesystem, network, and service access.
* Avoid unsafe deserialization, arbitrary command execution, and unnecessary shell invocation.
* Use established cryptographic libraries and secure defaults. Never invent cryptographic algorithms.
* Evaluate new dependencies for necessity and security implications.
* Do not weaken authentication, authorization, or security controls to make tests pass.

Security must be addressed during implementation, not deferred to a later cleanup.

## 7. TESTING & VERIFICATION

* Add or update tests for new behavior, bug fixes, and meaningful edge cases.
* When fixing a bug, reproduce it with a regression test where practical.
* Test observable behavior rather than implementation details.
* Keep tests deterministic, isolated, and repeatable.
* Mock external dependencies at appropriate boundaries, not indiscriminately.
* Include integration tests when component interactions are essential to correctness.
* Run relevant tests, linters, formatters, type checkers, and build checks when available.
* Never modify or delete a valid test merely to make the test suite pass.
* Never claim tests passed unless they were actually executed successfully.

When verification is incomplete, identify what was not tested and why.

## 8. PERFORMANCE & RESOURCE MANAGEMENT

* Choose algorithms and data structures appropriate for expected workloads.
* Consider time complexity, memory consumption, and I/O requirements during design.
* Avoid unnecessary allocations, repeated queries, excessive network calls, and unbounded operations.
* Release resources deterministically when possible.
* Avoid premature micro-optimization and unnecessary caching.
* Use profiling and benchmarks to guide optimization when performance requirements are not already established.
* Preserve correctness and maintainability when optimizing.
* Document meaningful performance trade-offs.

For concurrent or asynchronous code, explicitly consider race conditions, deadlocks, cancellation, timeouts, and shared-state safety.

## 9. DOCUMENTATION & OBSERVABILITY

* Write code that communicates intent through clear names and straightforward control flow.
* Use comments to explain why something is necessary, not to narrate obvious code.
* Document public APIs, non-obvious invariants, and important architectural decisions.
* Keep documentation and configuration examples synchronized with implementation.
* Include actionable error messages that provide enough context for diagnosis.
* Use structured logging and metrics when consistent with the project's architecture.
* Avoid excessive logging and never log secrets or sensitive data.
* Do not introduce an observability framework when existing mechanisms are sufficient.

## 10. AGENT EXECUTION DISCIPLINE

Before modifying code:

* Understand the request and identify the smallest relevant scope.
* Inspect existing implementation and tests.
* Identify constraints, compatibility requirements, and potential failure modes.
* For complex changes, establish a brief implementation plan.

During implementation:

* Make focused changes.
* Preserve unrelated behavior.
* Do not silently expand the task's scope.
* Prefer reversible modifications.
* Ask before destructive operations, significant dependency changes, or externally visible actions.

After implementation:

* Review the changes for correctness, security, and unnecessary complexity.
* Execute relevant verification.
* Inspect the final diff for accidental or unrelated changes.
* Report the outcome accurately.

Never fabricate execution results, claim unperformed actions, or conceal incomplete work.

## 11. DEFINITION OF DONE

A coding task is complete only when:

1. The requested behavior has been implemented.
2. Existing functionality and compatibility are preserved unless intentionally changed.
3. Relevant tests and checks have been run successfully, or limitations are clearly disclosed.
4. No known critical defects or security regressions remain unreported.
5. The implementation follows project conventions without unnecessary complexity.
6. The final response summarizes changes, verification results, and outstanding limitations.

Do not declare success merely because code was generated or files were modified.
