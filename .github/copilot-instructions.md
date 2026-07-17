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

### Back End

- Implement the API server with **Python / FastAPI** only. Do not introduce
  alternative frameworks (Django, Flask, etc.) without an approved ADR.
- Use **SQLite** as the sole persistent store via the standard `sqlite3` module
  or `SQLAlchemy` with a SQLite URL. Do not introduce other database engines
  unless explicitly approved in a feature specification.
- Protect every non-public endpoint with **JWT bearer tokens** (HS256 or RS256).
  Issue tokens from a dedicated `/auth/token` endpoint. Validate signatures and
  expiry on every protected route using `python-jose` or `PyJWT`. Never embed
  secrets in source code; read them from environment variables.
- Store passwords with `passlib` (bcrypt). Never store or log plaintext
  credentials.
- Place the FastAPI application under `/src`. Define DB schema migrations as
  plain SQL scripts under `/src/migrations` or use `Alembic`.

### Front End

- Implement UI as vanilla HTML, CSS (Tailwind via CDN), and JavaScript only.
  Do not introduce build tools, bundlers, transpilers, or front-end frameworks.
- Communicate with the back end exclusively through the FastAPI REST endpoints.
  Store the JWT access token in `sessionStorage` (not `localStorage` or cookies)
  to limit XSS exposure. Clear it on logout.

### General

- Do not add external services, cloud storage, or message brokers unless
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
