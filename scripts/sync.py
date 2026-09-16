#!/usr/bin/env python3
"""Install selected skills and an optional private profile into agent locations."""

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


def install_profile(profile: Path, agent_name: str, agent: dict, root: Path) -> None:
    """Install a profile file or create a product-specific upload archive."""
    source = profile / "adapters" / f"{agent_name}.md"
    if not source.is_file():
        source = profile / "profile.md"
    destination = Path(agent["profile_destination"])
    if agent.get("profile_adapter", "filesystem") == "archive":
        destination = destination if destination.is_absolute() else root / destination
        destination.mkdir(parents=True, exist_ok=True)
        archive = destination / f"profile-{agent_name}.zip"
        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as output:
            output.write(source, source.name)
        print(f"{agent_name}: wrote private profile archive to {destination}")
        return
    destination = destination.expanduser()
    marker = destination.with_name(destination.name + ".ai-profile-managed")
    if destination.exists() and not marker.exists():
        raise SystemExit(f"Refusing to overwrite unmanaged profile file: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    marker.write_text("Managed by ai-skills sync.py; do not edit the generated file.\n", encoding="utf-8")
    print(f"{agent_name}: synchronized private profile to {destination}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, help="Alternative JSON config file")
    parser.add_argument("--ref", help="Override the configured Git ref")
    parser.add_argument("--profile-source", type=Path, help="Private profile checkout or Git repository")
    parser.add_argument("--profile-ref", help="Git ref for a remote private profile")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    if args.config:
        config = json.loads(args.config.read_text(encoding="utf-8"))
    else:
        profile_config = root.parent / "ai-profile" / "config" / "sync.json"
        config = json.loads(profile_config.read_text(encoding="utf-8")) if profile_config.is_file() else load_config(root)
    tree, temporary = source_tree(root, config, args.ref)
    try:
        skills = selected_skills(tree, config.get("skills", ["*"]))
        profile = args.profile_source or (root.parent / "ai-profile" if (root.parent / "ai-profile").is_dir() else None)
        profile_temp = None
        if profile and not profile.is_dir():
            profile_temp = tempfile.TemporaryDirectory(prefix="ai-profile-")
            subprocess.run(["git", "clone", "--depth", "1", "--branch", args.profile_ref or "main", str(profile), profile_temp.name], check=True)
            profile = Path(profile_temp.name)
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
            if profile and agent.get("profile_destination"):
                install_profile(profile, name, agent, root)
        if profile_temp:
            profile_temp.cleanup()
    finally:
        if temporary:
            temporary.cleanup()
    return 0


if __name__ == "__main__":
    sys.exit(main())
