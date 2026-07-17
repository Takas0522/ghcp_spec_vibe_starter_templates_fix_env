# Contributing

Changes to this starter affect the instructions and guardrails inherited by
future repositories. Keep changes small, reviewable, and backed by executable
evidence.

## Before Editing

1. Identify the requirement or maintenance reason for the change.
2. Read the nearest customization or template that owns the behavior.
3. Record a material trade-off in [Decision Log](docs/05_decisions.md).
4. Use [Experiment Log](docs/04_experiments.md) for a hypothesis-driven trial.

Do not combine unrelated cleanup with a harness change.

## Customization Checklist

- Instructions contain one concern and a targeted `applyTo` or discoverable
  description.
- Agents have one role, minimal tools, clear boundaries, and no circular
  handoffs.
- Handoffs across approval gates use `send: false`.
- Skill folder names match the `name` field and use lowercase hyphenated names.
- Skill resources are referenced with relative links and loaded progressively.
- Prompt files remain thin entry points and do not duplicate agent or skill
  procedures.
- Preview features remain opt-in and are documented as unstable.

## Local Validation

On macOS or Linux:

```bash
python -m unittest discover -s tests -p "test_*.py"
python scripts/validate_starter.py
npx --yes markdownlint-cli2@0.18.1 "**/*.md" "#node_modules"
```

On Windows with the Python Launcher:

```powershell
py -3 -m unittest discover -s tests -p "test_*.py"
py -3 scripts/validate_starter.py
npx --yes markdownlint-cli2@0.18.1 "**/*.md" "#node_modules"
```

Also open VS Code Chat Customization Diagnostics and confirm that all
instructions, agents, skills, prompts, and enabled hooks load without errors.

## Pull Request Evidence

Describe:

- The requirement, issue, or maintenance objective.
- Changed customizations and inherited behavior.
- Commands and test names run, with results.
- Manual Diagnostics or handoff checks performed.
- Unverified platforms, Preview behavior, and residual risks.

Do not claim compatibility from inspection alone when an executable check is
available.
