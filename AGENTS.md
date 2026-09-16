# Repository instructions

This is a public, portable collection of agent skills.

- Canonical skills live in `skills/<skill-name>/`.
- Every skill must contain a `SKILL.md` with `name` and `description` frontmatter.
- Keep `SKILL.md` portable: do not assume a specific agent, shell, vendor, account, or private filesystem.
- Put optional, task-specific material in `references/`, `scripts/`, `templates/`, or `assets/`.
- Agent-specific installation behavior belongs in `scripts/sync.py` and documentation, not in the canonical skill body.
- Never commit personal paths, credentials, local agent selections, or generated output.

Run `python3 scripts/validate.py` before proposing a release.
