# AI Skills

A public, portable collection of reusable skills for coding agents and AI
workspaces.

## Design

The `skills/` directory is the source of truth. Each skill is a directory with
a `SKILL.md` entrypoint and optional supporting resources. Skills should be
vendor-neutral; installation details belong to the sync tool and adapters.

## Configure and sync

```sh
cp config/agents.example.json config/agents.local.json
# Edit config/agents.local.json: enable only the agents you use.
python3 scripts/validate.py
python3 scripts/sync.py
```

Create a new skill skeleton with its required frontmatter and Markdown heading:

```sh
python3 scripts/new_skill.py code-review "Review code for correctness, security, and maintainability"
```

This creates `skills/code-review/SKILL.md` and refuses to overwrite an existing
skill directory.

When this repository is checked out beside the private profile repository at
`../ai-profile`, the sync tool automatically uses that profile's configuration
and synchronizes both layers. A standalone clone without that sibling falls
back to the public example configuration.

To use a private profile checkout elsewhere, pass it explicitly:

```sh
python3 scripts/sync.py --profile-source /path/to/ai-profile
```

The public repository never needs to contain personal information. Profile
files are installed only for enabled agents that define `profile_destination`.

The local config is ignored by Git. Filesystem agents can use `copy` for stable
installations or `symlink` while developing. The sync tool refuses to overwrite
an unmanaged skill directory.

To synchronize a public release instead of the checkout, set `repository` to
this repository's Git URL and set `ref` to an immutable tag such as `v0.1.0`.
You can also use `python3 scripts/sync.py --ref v0.1.0`.

Archive adapters write ZIP files under `.build/` for products whose skills are
managed through an application workspace or upload flow. Review and upload
those archives using that product's normal interface.

## Release policy

Use repository-wide semantic-version tags (`vMAJOR.MINOR.PATCH`). Every release
must pass validation and receive a changelog entry. Consumers should pin a tag,
not silently follow `main`; update intentionally when a new release is ready.

## Contributing

Skills are public. Do not include secrets, private filesystem paths, personal
account details, or instructions that assume access to a private service.

## License

MIT. See [LICENSE](LICENSE).
