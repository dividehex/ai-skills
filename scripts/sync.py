#!/usr/bin/env python3
"""Install selected skills into configured agent locations."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


def load_config(root: Path) -> dict:
    example = root / "config/agents.example.json"
    local = root / "config/agents.local.json"
    config = json.loads(example.read_text(encoding="utf-8"))
    if local.exists():
        override = json.loads(local.read_text(encoding="utf-8"))
        config.update({key: value for key, value in override.items() if key != "agents"})
        config["agents"].update(override.get("agents", {}))
    return config


def source_tree(root: Path, config: dict, ref: str | None) -> tuple[Path, tempfile.TemporaryDirectory[str] | None]:
    repository = config.get("repository", ".")
    selected_ref = ref or config.get("ref", "main")
    if repository in (".", "", None):
        return root, None
    temp = tempfile.TemporaryDirectory(prefix="ai-skills-")
    subprocess.run(["git", "clone", "--depth", "1", "--branch", selected_ref, repository, temp.name], check=True)
    return Path(temp.name), temp


def selected_skills(tree: Path, selection: list[str]) -> list[Path]:
    available = {path.name: path for path in (tree / "skills").iterdir() if path.is_dir()}
    names = sorted(available) if "*" in selection else selection
    missing = [name for name in names if name not in available]
    if missing:
        raise SystemExit(f"Unknown skill(s): {', '.join(missing)}")
    return [available[name] for name in names]


def install_filesystem(skills: list[Path], destination: Path, mode: str) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    manifest_path = destination / ".ai-skills-managed.json"
    previous = set(json.loads(manifest_path.read_text()).get("skills", [])) if manifest_path.exists() else set()
    current = {skill.name for skill in skills}
    unmanaged_conflicts = [skill.name for skill in skills if (destination / skill.name).exists() and skill.name not in previous]
    if unmanaged_conflicts:
        raise SystemExit(f"Refusing to overwrite unmanaged skill(s) in {destination}: {', '.join(unmanaged_conflicts)}")
    for stale in previous - current:
        path = destination / stale
        if path.is_symlink() or path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)
    for skill in skills:
        target = destination / skill.name
        if target.exists() or target.is_symlink():
            if target.is_dir() and not target.is_symlink():
                shutil.rmtree(target)
            else:
                target.unlink()
        if mode == "symlink":
            target.symlink_to(skill, target_is_directory=True)
        else:
            shutil.copytree(skill, target)
    manifest_path.write_text(json.dumps({"skills": sorted(current)}, indent=2) + "\n", encoding="utf-8")


def install_archive(skills: list[Path], destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for old in destination.glob("*.zip"):
        old.unlink()
    for skill in skills:
        archive = destination / f"{skill.name}.zip"
        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as output:
            for path in skill.rglob("*"):
                if path.is_file():
                    output.write(path, Path(skill.name) / path.relative_to(skill))
    (destination / "README.txt").write_text(
        "Upload the generated ZIP files in this directory to the target agent product.\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, help="Alternative JSON config file")
    parser.add_argument("--ref", help="Override the configured Git ref")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    config = load_config(root)
    if args.config:
        config = json.loads(args.config.read_text(encoding="utf-8"))
    tree, temporary = source_tree(root, config, args.ref)
    try:
        skills = selected_skills(tree, config.get("skills", ["*"]))
        for name, agent in config.get("agents", {}).items():
            if not agent.get("enabled", False):
                continue
            destination = Path(agent["destination"]).expanduser()
            if agent.get("adapter", "filesystem") == "archive":
                install_archive(skills, root / destination if not destination.is_absolute() else destination)
                print(f"{name}: wrote upload archives to {destination}")
            else:
                install_filesystem(skills, destination, agent.get("mode", "copy"))
                print(f"{name}: synchronized {len(skills)} skill(s) to {destination}")
    finally:
        if temporary:
            temporary.cleanup()
    return 0


if __name__ == "__main__":
    sys.exit(main())
