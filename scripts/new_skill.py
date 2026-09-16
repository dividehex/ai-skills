#!/usr/bin/env python3
"""Create a minimal skill directory and SKILL.md entrypoint."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", help="Lowercase hyphenated skill name")
    parser.add_argument("description", help="Description used for skill discovery")
    parser.add_argument("--path", type=Path, default=None, help="Skills directory (default: repository skills/)")
    args = parser.parse_args()

    if not NAME.fullmatch(args.name):
        parser.error("name must contain lowercase letters, digits, and single hyphens")
    if not args.description.strip():
        parser.error("description must not be empty")

    root = Path(__file__).resolve().parents[1]
    skills_root = args.path.resolve() if args.path else root / "skills"
    skill_dir = skills_root / args.name
    entrypoint = skill_dir / "SKILL.md"
    if skill_dir.exists():
        parser.error(f"skill directory already exists: {skill_dir}")

    heading = args.name.replace("-", " ").title()
    entrypoint_text = (
        "---\n"
        f"name: {json.dumps(args.name)}\n"
        f"description: {json.dumps(args.description.strip())}\n"
        "---\n\n"
        f"# {heading}\n\n"
        f"Use this skill when {args.description.strip().rstrip('.')}.\n\n"
        "## Instructions\n\n"
        "Add the instructions for this skill here.\n"
    )
    skill_dir.mkdir(parents=True)
    entrypoint.write_text(entrypoint_text, encoding="utf-8")
    print(entrypoint)
    return 0


if __name__ == "__main__":
    sys.exit(main())
