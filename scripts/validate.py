#!/usr/bin/env python3
"""Validate the portable skill layout without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    skill_root = root / "skills"
    errors: list[str] = []
    seen: set[str] = set()

    for skill_dir in sorted(p for p in skill_root.iterdir() if p.is_dir()):
        entrypoint = skill_dir / "SKILL.md"
        if not NAME.fullmatch(skill_dir.name):
            errors.append(f"{skill_dir}: directory name is not lowercase-hyphenated")
        if not entrypoint.is_file():
            errors.append(f"{skill_dir}: missing SKILL.md")
            continue
        text = entrypoint.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{entrypoint}: missing YAML frontmatter")
            continue
        frontmatter = text.split("---\n", 2)
        if len(frontmatter) < 3:
            errors.append(f"{entrypoint}: frontmatter is not closed")
            continue
        fields = {}
        for line in frontmatter[1].splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip().strip("'\"")
        name = fields.get("name", "")
        description = fields.get("description", "")
        if name != skill_dir.name:
            errors.append(f"{entrypoint}: name must match directory ({skill_dir.name!r})")
        if not NAME.fullmatch(name):
            errors.append(f"{entrypoint}: invalid name")
        if not description:
            errors.append(f"{entrypoint}: description is required")
        if name in seen:
            errors.append(f"duplicate skill name: {name}")
        seen.add(name)

    if errors:
        print("Validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Validated {len(seen)} skill(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
