# Agent configuration

Copy `agents.example.json` to `agents.local.json` and edit the enabled agents,
destination paths, and skill selection. The local file is ignored by Git.

Examples:

- Use `"skills": ["code-review", "git-release"]` to install only selected skills.
- Use `"mode": "symlink"` for a local development checkout.
- Set `repository` to the public Git URL and `ref` to an immutable release tag
  such as `v0.1.0` when synchronizing from a release.
