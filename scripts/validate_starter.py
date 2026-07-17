#!/usr/bin/env python3
"""Validate the structure and contracts of the spec-driven starter."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


REQUIRED_FILES = (
    "README.md",
    "CONTRIBUTING.md",
    ".markdownlint.json",
    ".github/copilot-instructions.md",
    ".github/instructions/markdown.instructions.md",
    ".github/instructions/spec-traceability.instructions.md",
    ".github/agents/spec.agent.md",
    ".github/agents/plan.agent.md",
    ".github/agents/implement.agent.md",
    ".github/agents/verify.agent.md",
    ".github/skills/spec-driven-workflow/SKILL.md",
    ".github/skills/requirements-traceability/SKILL.md",
    ".github/skills/experiment-loop/SKILL.md",
    ".github/prompts/define-feature.prompt.md",
    ".github/prompts/plan-change.prompt.md",
    ".github/prompts/verify-change.prompt.md",
    ".github/workflows/validate-starter.yml",
    "docs/01_vision.md",
    "docs/02_scope.md",
    "docs/03_architecture.md",
    "docs/04_experiments.md",
    "docs/05_decisions.md",
    "docs/specs/README.md",
    "docs/specs/feature-spec.template.md",
    "docs/plans/implementation-plan.template.md",
    "docs/quality/verification.template.md",
    "examples/hooks/README.md",
    "examples/hooks/validate-on-stop.json",
)

REQUIRED_TEMPLATE_HEADINGS = {
    "docs/specs/feature-spec.template.md": (
        "Requirements",
        "Acceptance Criteria",
        "Traceability",
        "Approval Checklist",
    ),
    "docs/plans/implementation-plan.template.md": (
        "Implementation Tasks",
        "Verification Strategy",
        "Requirement Mapping",
        "Definition of Done",
    ),
    "docs/quality/verification.template.md": (
        "Results",
        "Unverified Items",
        "Traceability Summary",
        "Verdict Rationale",
    ),
}

FRONT_MATTER_PATTERNS = {
    "*.instructions.md": ("description",),
    "*.agent.md": ("name", "description", "tools"),
    "*.prompt.md": ("name", "description", "agent"),
    "SKILL.md": ("name", "description"),
}


@dataclass(frozen=True)
class Issue:
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.path}: {self.message}"


def parse_front_matter(path: Path) -> tuple[dict[str, str], str | None]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}, "missing opening YAML delimiter"
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, "missing closing YAML delimiter"

    values: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z][A-Za-z0-9-]*):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip("'\"")
    return values, None


def required_front_matter(path: Path) -> tuple[str, ...] | None:
    if path.name == "SKILL.md":
        return FRONT_MATTER_PATTERNS["SKILL.md"]
    for pattern in ("*.instructions.md", "*.agent.md", "*.prompt.md"):
        if path.match(pattern):
            return FRONT_MATTER_PATTERNS[pattern]
    return None


def validate_front_matter(root: Path, issues: list[Issue]) -> None:
    customization_root = root / ".github"
    if not customization_root.exists():
        return

    paths = set(customization_root.rglob("*.md"))
    for path in sorted(paths):
        required = required_front_matter(path)
        if not required:
            continue
        relative = path.relative_to(root).as_posix()
        values, error = parse_front_matter(path)
        if error:
            issues.append(Issue(relative, error))
            continue
        for key in required:
            if not values.get(key):
                issues.append(Issue(relative, f"missing front matter key '{key}'"))

        if path.name == "SKILL.md":
            skill_name = values.get("name", "")
            if skill_name != path.parent.name:
                issues.append(
                    Issue(
                        relative,
                        f"skill name '{skill_name}' must match directory '{path.parent.name}'",
                    )
                )
            if not re.fullmatch(r"[a-z0-9-]{1,64}", skill_name):
                issues.append(Issue(relative, "skill name must use lowercase letters, numbers, and hyphens"))


def collect_named_customizations(root: Path, folder: str, suffix: str) -> set[str]:
    names: set[str] = set()
    base = root / ".github" / folder
    if not base.exists():
        return names
    for path in base.glob(f"*{suffix}"):
        values, error = parse_front_matter(path)
        if not error and values.get("name"):
            names.add(values["name"])
    return names


def validate_agent_references(root: Path, issues: list[Issue]) -> None:
    agents = collect_named_customizations(root, "agents", ".agent.md")
    agent_root = root / ".github" / "agents"
    if agent_root.exists():
        for path in agent_root.glob("*.agent.md"):
            text = path.read_text(encoding="utf-8")
            relative = path.relative_to(root).as_posix()
            for target in re.findall(r"^\s+agent:\s*['\"]?([^'\"\n]+)['\"]?\s*$", text, re.MULTILINE):
                if target not in agents:
                    issues.append(Issue(relative, f"handoff references unknown agent '{target}'"))

    prompt_root = root / ".github" / "prompts"
    if prompt_root.exists():
        for path in prompt_root.glob("*.prompt.md"):
            values, error = parse_front_matter(path)
            target = values.get("agent") if not error else None
            if target and target not in agents:
                relative = path.relative_to(root).as_posix()
                issues.append(Issue(relative, f"prompt references unknown agent '{target}'"))


def validate_markdown(root: Path, issues: list[Issue]) -> None:
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        relative = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        if not text.endswith("\n"):
            issues.append(Issue(relative, "file must end with a newline"))
        body = text
        if text.startswith("---\n"):
            parts = text.split("---\n", 2)
            body = parts[2] if len(parts) == 3 else ""
        h1_count = len(re.findall(r"^# [^#].+$", body, re.MULTILINE))
        if h1_count != 1:
            issues.append(Issue(relative, f"expected exactly one H1, found {h1_count}"))


def validate_template_headings(root: Path, issues: list[Issue]) -> None:
    for relative, headings in REQUIRED_TEMPLATE_HEADINGS.items():
        path = root / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if not re.search(rf"^#+\s+{re.escape(heading)}(?:\s|$)", text, re.MULTILINE):
                issues.append(Issue(relative, f"missing required heading '{heading}'"))


def instantiated_markdown_files(folder: Path) -> list[Path]:
    if not folder.exists():
        return []
    return [
        path
        for path in folder.glob("*.md")
        if path.name != "README.md" and not path.name.endswith(".template.md")
    ]


def validate_traceability(root: Path, issues: list[Issue]) -> None:
    specification_files = instantiated_markdown_files(root / "docs" / "specs")
    definitions: set[str] = set()
    for path in specification_files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root).as_posix()
        requirement_definitions = re.findall(r"^#{2,4}\s+(REQ-\d{3})\b", text, re.MULTILINE)
        criterion_definitions = re.findall(r"^\s*-\s+`(AC-\d{3})`:", text, re.MULTILINE)
        for identifier in requirement_definitions + criterion_definitions:
            definitions.add(identifier)
        for identifier in set(requirement_definitions + criterion_definitions):
            if (requirement_definitions + criterion_definitions).count(identifier) > 1:
                issues.append(Issue(relative, f"identifier '{identifier}' is defined more than once"))

    artifact_files = instantiated_markdown_files(root / "docs" / "plans")
    artifact_files += instantiated_markdown_files(root / "docs" / "quality")
    for path in artifact_files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root).as_posix()
        for identifier in sorted(set(re.findall(r"\b(?:REQ|AC)-\d{3}\b", text))):
            if identifier not in definitions:
                issues.append(Issue(relative, f"references undefined identifier '{identifier}'"))


def validate_repository(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            issues.append(Issue(relative, "required file is missing"))
    validate_front_matter(root, issues)
    validate_agent_references(root, issues)
    validate_markdown(root, issues)
    validate_template_headings(root, issues)
    validate_traceability(root, issues)
    return sorted(issues, key=lambda issue: (issue.path, issue.message))


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    issues = validate_repository(root)
    if issues:
        print(f"Starter validation failed with {len(issues)} issue(s):")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Starter validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())