from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_starter.py"
SPEC = importlib.util.spec_from_file_location("validate_starter", MODULE_PATH)
assert SPEC and SPEC.loader
validate_starter = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validate_starter
SPEC.loader.exec_module(validate_starter)


class StarterValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.addCleanup(self.temporary_directory.cleanup)

    def write(self, relative: str, content: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def make_minimal_valid_repository(self) -> None:
        for relative in validate_starter.REQUIRED_FILES:
            if relative.endswith("SKILL.md"):
                name = Path(relative).parent.name
                content = f"---\nname: '{name}'\ndescription: 'Use when testing.'\n---\n\n# Skill\n"
            elif relative.endswith(".agent.md"):
                name = Path(relative).stem.removesuffix(".agent").title()
                content = (
                    f"---\nname: '{name}'\ndescription: 'Use when testing.'\n"
                    "tools: ['read']\n---\n\n# Agent\n"
                )
            elif relative.endswith(".prompt.md"):
                content = (
                    "---\nname: 'Prompt'\ndescription: 'Use when testing.'\n"
                    "agent: 'Spec'\n---\n\n# Prompt\n"
                )
            elif relative.endswith(".instructions.md"):
                content = "---\ndescription: 'Use when testing.'\n---\n\n# Instructions\n"
            else:
                content = "# Document\n"
            self.write(relative, content)

        for relative, headings in validate_starter.REQUIRED_TEMPLATE_HEADINGS.items():
            content = "# Template\n\n" + "\n\n".join(f"## {heading}" for heading in headings) + "\n"
            self.write(relative, content)

    def messages(self) -> list[str]:
        return [str(issue) for issue in validate_starter.validate_repository(self.root)]

    def test_accepts_minimal_valid_repository(self) -> None:
        self.make_minimal_valid_repository()
        self.assertEqual([], self.messages())

    def test_reports_missing_required_file(self) -> None:
        self.make_minimal_valid_repository()
        (self.root / "README.md").unlink()
        self.assertIn("README.md: required file is missing", self.messages())

    def test_reports_missing_front_matter_key(self) -> None:
        self.make_minimal_valid_repository()
        self.write(
            ".github/agents/spec.agent.md",
            "---\nname: 'Spec'\ntools: ['read']\n---\n\n# Agent\n",
        )
        self.assertIn(
            ".github/agents/spec.agent.md: missing front matter key 'description'",
            self.messages(),
        )

    def test_reports_skill_name_mismatch(self) -> None:
        self.make_minimal_valid_repository()
        self.write(
            ".github/skills/experiment-loop/SKILL.md",
            "---\nname: 'wrong-name'\ndescription: 'Use when testing.'\n---\n\n# Skill\n",
        )
        self.assertIn(
            ".github/skills/experiment-loop/SKILL.md: skill name 'wrong-name' must match directory 'experiment-loop'",
            self.messages(),
        )

    def test_reports_unknown_prompt_agent(self) -> None:
        self.make_minimal_valid_repository()
        self.write(
            ".github/prompts/define-feature.prompt.md",
            "---\nname: 'Prompt'\ndescription: 'Use when testing.'\nagent: 'Unknown'\n---\n\n# Prompt\n",
        )
        self.assertIn(
            ".github/prompts/define-feature.prompt.md: prompt references unknown agent 'Unknown'",
            self.messages(),
        )

    def test_reports_orphaned_requirement_reference(self) -> None:
        self.make_minimal_valid_repository()
        self.write(
            "docs/specs/example.md",
            "# Feature\n\n## Requirements\n\n### REQ-001: Known\n\n- `AC-001`: Works.\n",
        )
        self.write(
            "docs/plans/example.md",
            "# Plan\n\n## Mapping\n\nReferences `REQ-999` and `AC-001`.\n",
        )
        self.assertIn(
            "docs/plans/example.md: references undefined identifier 'REQ-999'",
            self.messages(),
        )


if __name__ == "__main__":
    unittest.main()