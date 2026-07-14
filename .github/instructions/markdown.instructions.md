---
name: 'Specification Markdown Standards'
description: 'Use when creating or editing specifications, plans, architecture notes, experiments, decisions, verification reports, or repository documentation.'
applyTo: '**/*.md'
---

# Markdown Standards

- Start each document with exactly one level-one heading. YAML front matter may
  precede it only when the file format requires metadata.
- Use hierarchical headings without skipping levels. Prefer no deeper than
  level three.
- Surround headings, lists, tables, and fenced code blocks with blank lines.
- Add a language identifier to every fenced code block. Use `text` for plain
  text and `mermaid` for diagrams.
- Use repository-relative Markdown links for related specifications, plans,
  decisions, experiments, source files, and verification evidence.
- Use `-` for unordered lists and `1.` for ordered lists. Keep tables compact
  and add spaces around table pipes.
- Keep prose concise and separate facts, assumptions, decisions, and open
  questions. Do not present an assumption as an approved requirement.
- Write testable statements. Replace words such as "fast", "easy", and
  "appropriate" with an observable threshold or mark them as unresolved.
- Use identifiers consistently: `REQ-###` for requirements, `AC-###` for
  acceptance criteria, `EXP-###` for experiments, and `ADR-###` for decisions.
- Preserve template placeholders in files ending with `.template.md`. In
  instantiated documents, resolve placeholders or mark them explicitly as
  `[NEEDS CLARIFICATION]`.
- End every file with one newline. Prefer lines shorter than 100 characters,
  excluding links, tables, and code that cannot be wrapped safely.

## Front Matter

Front matter is required only by a consuming format such as `.instructions.md`,
`.prompt.md`, `.agent.md`, or `SKILL.md`. Ordinary documents under `docs/` and
the repository root do not require front matter.

For Copilot customization files:

- Keep YAML between `---` delimiters.
- Quote descriptions containing a colon.
- Use keyword-rich descriptions that state when the customization applies.
- Do not add blog metadata such as author, publication date, categories, or
  featured image.

## Traceability

- Define each identifier once in its owning artifact.
- Link implementation plans and verification reports back to their source
  requirements and acceptance criteria.
- Record evidence as commands, test names, logs, screenshots, or artifact
  paths. Do not use "verified" without reproducible evidence.
- Keep unresolved questions visible and block implementation when an answer can
  materially change behavior, interfaces, data, security, or scope.
