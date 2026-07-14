---
name: 'Specification Traceability'
description: 'Use when defining requirements or acceptance criteria, creating implementation plans, implementing approved specifications, writing tests, or producing verification evidence.'
---

# Specification Traceability

- Use `REQ-###` for a unique functional or non-functional requirement.
- Use `AC-###` for an observable acceptance criterion and associate it with at
  least one requirement.
- Use `EXP-###` for a time-bounded hypothesis test.
- Use `ADR-###` for a material decision with alternatives and consequences.
- Define an identifier once in its owning artifact. Other artifacts reference
  it by identifier and repository-relative link.
- Never renumber an accepted identifier. Mark removed items as deprecated and
  explain the replacement or reason.
- Every implementation task must cite the requirements it addresses and the
  acceptance criteria it will verify.
- Every acceptance criterion must have a verification method and evidence, or
  be explicitly marked unverified with a reason and risk.
- Treat requirements with no plan entry, plan entries with no requirement, and
  acceptance criteria with no evidence as traceability failures.
- When a requirement changes, inspect linked plans, tests, decisions,
  experiments, and verification reports before implementation.

## Minimum Mapping

| Source | Must map to |
| --- | --- |
| `REQ-###` | One or more plan tasks |
| `AC-###` | A test or explicit verification procedure |
| Plan task | Changed file or deliberate no-code outcome |
| Verification result | Command, test, log, screenshot, or artifact path |

Do not infer approval from the existence of a document. Approval status must be
explicit in the owning specification or plan.
