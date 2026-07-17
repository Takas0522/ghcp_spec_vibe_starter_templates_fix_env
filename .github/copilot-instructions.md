# Copilot Instructions

## Operating Contract

- Start from the approved feature specification and cite the relevant
  `REQ-###` and `AC-###` identifiers before changing code.
- Read [scope](../docs/02_scope.md) and the nearest architecture or decision
  record before proposing a structural change.
- Do not implement unresolved behavior, expand scope, or silently rewrite a
  requirement. Surface the gap and request human approval.
- Make the smallest change that can satisfy the approved acceptance criteria.
- After the first substantive edit, run the narrowest executable check that can
  disprove the change before editing further.
- Report verification as reproducible evidence: command, test name, result, and
  any unverified risk. Never claim completion from inspection alone when an
  executable check exists.
- Preserve traceability from specification to plan, changed files, tests, and
  verification report. Follow the repository's identifier rules.
- Record a material trade-off in [decisions](../docs/05_decisions.md) and a
  hypothesis-driven trial in [experiments](../docs/04_experiments.md).
- Keep implementation simple and replaceable. This repository favors learning
  and fast iteration over speculative production optimization.
- Create application source code under `/src`. Keep tests under `/tests`,
  harness utilities under `/scripts`, and documentation under `/docs`; do not
  place application source code at the repository root or in these support
  directories.
- Use English identifiers in code. Japanese or English may be used in
  documentation, but keep terminology consistent within each artifact.

## Technology Constraints

- Implement UI as vanilla HTML, CSS, and JavaScript only. Do not introduce
  build tools, bundlers, transpilers, or front-end frameworks.
- All runtime data is stored in-memory (JavaScript variables or the DOM).
  Data does not need to persist across page reloads; treat every reload as a
  clean slate.
- Do not add a back-end server, database, or external storage layer unless
  explicitly approved in a feature specification.

## Human Approval Gates

Human approval is required before moving from specification to planning and
from planning to implementation. Agent handoffs suggest the next step but must
not auto-submit it.

## References

- [Vision](../docs/01_vision.md)
- [Scope](../docs/02_scope.md)
- [Architecture](../docs/03_architecture.md)
- [Feature specification template](../docs/specs/feature-spec.template.md)
- [Implementation plan template](../docs/plans/implementation-plan.template.md)
- [Verification template](../docs/quality/verification.template.md)
