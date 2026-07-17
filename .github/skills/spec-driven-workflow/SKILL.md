---
name: 'spec-driven-workflow'
description: 'Guide a feature through vision, scope, specification, human approval, implementation planning, implementation, independent verification, and learning. Use when starting work, asking what phase comes next, checking readiness, or coordinating a spec-driven change.'
argument-hint: 'Describe the feature or provide its current artifact path.'
---

# Spec-Driven Workflow

Use this skill to identify the current phase and the next smallest valid action.
Do not skip approval gates or create later artifacts from unresolved behavior.

## Procedure

1. Find the relevant vision, scope, specification, plan, implementation, and
   verification artifacts.
2. Classify the feature state using the table below.
3. Check the entry criteria for the next phase.
4. Recommend one next action, its owning agent, required inputs, and expected
   artifact.
5. Stop at a human approval gate and ask for approval explicitly.

| Current state | Next action | Owner | Output |
| --- | --- | --- | --- |
| Problem or idea only | Define scenarios and requirements | `Spec` | Feature specification draft |
| Specification has gaps | Resolve Ready checklist gaps | `Spec` | Ready specification |
| Specification approved | Map code and verification | `Plan` | Implementation plan draft |
| Plan has gaps | Resolve task or coverage gaps | `Plan` | Approvable plan |
| Plan approved | Implement one task and validate | `Implement` | Code and focused evidence |
| Implementation complete | Independently verify all criteria | `Verify` | Verification report |
| Result changes understanding | Record experiment or decision | Human with agent support | `EXP-###` or `ADR-###` |

## Required References

- [Definition of Ready](../../../docs/specs/README.md)
- [Feature specification](../../../docs/specs/feature-spec.template.md)
- [Implementation plan](../../../docs/plans/implementation-plan.template.md)
- [Verification report](../../../docs/quality/verification.template.md)
- [Experiment log](../../../docs/04_experiments.md)
- [Decision log](../../../docs/05_decisions.md)

## Response Format

- Current phase and evidence
- Missing entry criteria
- Next action and owning agent
- Artifact to create or update
- Required human decision
