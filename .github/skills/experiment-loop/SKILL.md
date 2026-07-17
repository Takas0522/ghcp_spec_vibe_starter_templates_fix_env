---
name: 'experiment-loop'
description: 'Design and record a reproducible, time-bounded experiment with one changed variable, baseline, controlled conditions, evidence, and an adopt/iterate/reject decision. Use for uncertain approaches, prototypes, spikes, prompt trials, or performance comparisons.'
argument-hint: 'Describe the uncertainty, proposed change, baseline, and measurable outcome.'
---

# Experiment Loop

Use an experiment when evidence is needed before accepting a requirement,
architecture choice, dependency, or optimization.

## Procedure

1. State the uncertainty and link the related hypothesis or `REQ-###`.
2. Define one principal changed variable and list controlled conditions.
3. Record the baseline, inputs or dataset version, environment, reproduction
   command, success threshold, timebox, and stop condition.
4. Create an `EXP-###` entry using the
   [Experiment Log](../../../docs/04_experiments.md).
5. Run the procedure without silently changing conditions.
6. Record actual values, evidence paths, and deviations.
7. Conclude `Adopt`, `Iterate`, `Reject`, or `Inconclusive`.
8. Link the conclusion to a specification, plan, ADR, or next experiment.

Do not treat a successful demo as general evidence unless the tested inputs,
environment, and threshold represent the stated hypothesis.
