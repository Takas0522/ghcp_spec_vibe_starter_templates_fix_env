---
name: 'requirements-traceability'
description: 'Audit REQ requirements and AC acceptance criteria across feature specifications, implementation plans, changed files, tests, and verification evidence. Use to find missing, orphaned, duplicate, or contradictory traceability before implementation or sign-off.'
argument-hint: 'Provide the specification, plan, or verification report to audit.'
---

# Requirements Traceability

## Procedure

1. Extract definitions of `REQ-###` and `AC-###` from the selected feature
   specification.
2. Detect duplicate identifiers and criteria that reference no requirement.
3. Extract plan tasks and their referenced requirements and criteria.
4. Extract changed files, tests, commands, and evidence from implementation and
   verification artifacts.
5. Build a matrix with one row per acceptance criterion.
6. Classify each row and report blocking gaps before summaries.

## Classifications

- `Covered`: Requirement, task, check, and evidence all exist and agree.
- `Planned`: Requirement and check exist, but implementation evidence is not yet
  expected.
- `Missing plan`: Accepted requirement has no plan task.
- `Orphan task`: Plan task cites no accepted requirement.
- `Missing check`: Criterion has no executable or explicit verification method.
- `Missing evidence`: A completed change has no reproducible result.
- `Contradiction`: Artifacts describe incompatible expected behavior.

## Output

| Requirement | Criterion | Plan task | Check | Evidence | Status |
| --- | --- | --- | --- | --- | --- |
| `REQ-###` | `AC-###` | `TASK-###` | `<test or procedure>` | `<artifact>` | `<classification>` |

After the table, list duplicate identifiers, contradictions, and the smallest
artifact update needed to close each gap. Do not infer evidence from source
inspection when an executable check exists.
