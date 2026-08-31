#!/usr/bin/env python3
"""Validate the ScientificAgent profile without importing scientific packages."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
OPENCODE_ROOT = PROJECT_ROOT / ".opencode"
PROFILE_PATH = OPENCODE_ROOT / "config" / "scientific-skills.json"
PROJECT_SKILLS_PATH = OPENCODE_ROOT / "config" / "project-skills.json"
OPENCODE_CONFIG_PATH = OPENCODE_ROOT / "opencode.json"
AGENT_PATH = OPENCODE_ROOT / "agent" / "subagents" / "science" / "scientific-agent.md"
OPENCODER_PATH = OPENCODE_ROOT / "agent" / "core" / "opencoder.md"
CODER_AGENT_PATH = OPENCODE_ROOT / "agent" / "subagents" / "code" / "coder-agent.md"
METADATA_PATH = OPENCODE_ROOT / "config" / "agent-metadata.json"
EXPECTED_SKILL_COUNT = 87
EXPECTED_PROJECT_SKILLS = {"jupyter-notebook", "sql-queries", "pdf-authoring"}

PROJECT_SKILL_AGENTS = {
    "OpenCoder": OPENCODER_PATH,
    "CoderAgent": CODER_AGENT_PATH,
    "ScientificAgent": AGENT_PATH,
}

CATEGORY_NAVIGATION = {
    "scientific-databases": "databases/navigation.md",
    "cheminformatics-drug-discovery": "cheminformatics/navigation.md",
    "machine-learning-deep-learning": "machine-learning/navigation.md",
    "engineering-simulation": "engineering-simulation/navigation.md",
    "data-analysis-visualization": "data-analysis/navigation.md",
    "scientific-communication-publishing": "communication/navigation.md",
    "document-processing-conversion": "document-processing/navigation.md",
    "research-methodology-proposals": "research-methodology/navigation.md",
    "analysis-methodology": "analysis-methodology/navigation.md",
}


def load_json(path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing JSON file: {path.relative_to(PROJECT_ROOT)}")
        return {}
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in {path.relative_to(PROJECT_ROOT)}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"JSON root must be an object: {path.relative_to(PROJECT_ROOT)}")
        return {}
    return value


def skill_frontmatter_name(skill_file: Path) -> str | None:
    return skill_frontmatter_value(skill_file, "name")


def skill_frontmatter_value(skill_file: Path, key: str) -> str | None:
    text = skill_file.read_text(encoding="utf-8")
    match = re.search(rf"(?m)^{re.escape(key)}:\s*[\"']?([^\"'\n]+?)[\"']?\s*$", text)
    return match.group(1).strip() if match else None


def agent_skill_permissions(agent_path: Path, errors: list[str]) -> tuple[dict[str, str], str]:
    try:
        agent_text = agent_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append(f"missing agent prompt: {agent_path.relative_to(PROJECT_ROOT)}")
        return {}, ""
    skill_block_match = re.search(r"(?ms)^  skill:\n(?P<body>.*?)(?=^---\s*$)", agent_text)
    if skill_block_match is None:
        errors.append(f"missing skill permission block: {agent_path.relative_to(PROJECT_ROOT)}")
        return {}, agent_text
    permission_entries = dict(
        re.findall(
            r'^\s{4}[\"\']?([^\"\':\n]+)[\"\']?:\s*[\"\'](allow|ask|deny)[\"\']\s*$',
            skill_block_match.group("body"),
            re.MULTILINE,
        )
    )
    return permission_entries, agent_text


def git_head(repo: Path) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def vendored_tree_digest(root: Path, skill_names: list[str]) -> str:
    """Hash relative paths and bytes for every file in the selected skill trees."""
    digest = hashlib.sha256()
    for name in sorted(skill_names):
        for path in sorted((root / name).rglob("*")):
            if not path.is_file():
                continue
            digest.update(path.relative_to(root).as_posix().encode("utf-8"))
            digest.update(b"\0")
            with path.open("rb") as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(chunk)
            digest.update(b"\0")
    return digest.hexdigest()


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    profile = load_json(PROFILE_PATH, errors)
    project_profile = load_json(PROJECT_SKILLS_PATH, errors)
    opencode_config = load_json(OPENCODE_CONFIG_PATH, errors)

    project_skills = project_profile.get("skills", {})
    if not isinstance(project_skills, dict):
        errors.append("project support profile: skills must be an object")
        project_skills = {}
    project_skill_names = sorted(project_skills)
    if set(project_skill_names) != EXPECTED_PROJECT_SKILLS:
        errors.append(
            "project support profile: expected exactly "
            f"{sorted(EXPECTED_PROJECT_SKILLS)}, found {project_skill_names}"
        )
    for name, settings in project_skills.items():
        if not isinstance(settings, dict):
            errors.append(f"project support profile: {name!r} settings must be an object")
            continue
        expected_path = f".opencode/skills/{name}"
        configured_path = settings.get("path")
        if configured_path != expected_path:
            errors.append(
                f"project support profile: {name!r} path must be {expected_path!r}, "
                f"found {configured_path!r}"
            )
            continue
        skill_root = PROJECT_ROOT / configured_path
        skill_file = skill_root / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"missing project support skill: {skill_file.relative_to(PROJECT_ROOT)}")
            continue
        declared_name = skill_frontmatter_name(skill_file)
        if declared_name != name:
            errors.append(f"project support skill name mismatch for {name}: {declared_name!r}")
        declared_license = skill_frontmatter_value(skill_file, "license")
        if declared_license != settings.get("license"):
            errors.append(
                f"project support skill license mismatch for {name}: "
                f"{declared_license!r} != {settings.get('license')!r}"
            )
        if not (skill_root / "LICENSE.txt").is_file():
            errors.append(f"missing project support license: {(skill_root / 'LICENSE.txt').relative_to(PROJECT_ROOT)}")
        configured_agents = settings.get("agents")
        if not isinstance(configured_agents, list) or set(configured_agents) != set(PROJECT_SKILL_AGENTS):
            errors.append(
                f"project support profile: {name!r} agents must be "
                f"{sorted(PROJECT_SKILL_AGENTS)}, found {configured_agents!r}"
            )

    categories = profile.get("categories", {})
    if not isinstance(categories, dict):
        errors.append("scientific profile: categories must be an object")
        categories = {}

    unknown_categories = sorted(set(categories) - set(CATEGORY_NAVIGATION))
    missing_categories = sorted(set(CATEGORY_NAVIGATION) - set(categories))
    if unknown_categories:
        errors.append(f"scientific profile: missing navigation mapping for {unknown_categories}")
    if missing_categories:
        errors.append(f"scientific profile: categories absent from manifest: {missing_categories}")

    skills: list[str] = []
    for category, category_skills in categories.items():
        if not isinstance(category_skills, list) or not all(isinstance(item, str) for item in category_skills):
            errors.append(f"scientific profile: category {category!r} must be string[]")
            continue
        skills.extend(category_skills)

    if len(skills) != EXPECTED_SKILL_COUNT:
        errors.append(f"scientific profile: expected {EXPECTED_SKILL_COUNT} entries, found {len(skills)}")
    duplicates = sorted({name for name in skills if skills.count(name) > 1})
    if duplicates:
        errors.append(f"scientific profile: duplicate skills: {duplicates}")
    overlap = sorted(set(skills) & set(project_skill_names))
    if overlap:
        errors.append(f"scientific and project support profiles overlap: {overlap}")

    source = profile.get("source", {})
    installation = profile.get("installation", {})
    installation_mode = installation.get("mode") if isinstance(installation, dict) else None
    vendored_root_value = installation.get("root") if isinstance(installation, dict) else None
    vendored_root = PROJECT_ROOT / vendored_root_value if isinstance(vendored_root_value, str) else None
    if installation_mode != "vendored":
        errors.append(f"scientific profile: expected vendored installation, found {installation_mode!r}")
    if vendored_root is None or not vendored_root.is_dir():
        errors.append(f"scientific profile: vendored root does not exist: {vendored_root_value!r}")
    else:
        for name in skills:
            skill_file = vendored_root / name / "SKILL.md"
            if not skill_file.is_file():
                errors.append(f"missing skill entrypoint: {skill_file.relative_to(PROJECT_ROOT)}")
                continue
            declared_name = skill_frontmatter_name(skill_file)
            if declared_name != name:
                errors.append(f"skill name mismatch for {name}: SKILL.md declares {declared_name!r}")
        vendored_symlinks = [
            path.relative_to(PROJECT_ROOT).as_posix()
            for name in skills
            for path in (vendored_root / name).rglob("*")
            if path.is_symlink()
        ]
        if vendored_symlinks:
            errors.append(f"vendored scientific skills must not contain symlinks: {vendored_symlinks}")
        expected_digest = installation.get("content_sha256") if isinstance(installation, dict) else None
        actual_digest = vendored_tree_digest(vendored_root, skills)
        if actual_digest != expected_digest:
            errors.append(f"vendored content hash differs from manifest: {actual_digest} != {expected_digest}")

    configured_paths = opencode_config.get("skills", {}).get("paths", [])
    # OpenCode resolves project config paths from the project working directory,
    # not from the directory containing .opencode/opencode.json.
    expected_paths = [f"{vendored_root_value}/{name}" for name in skills]
    if configured_paths != expected_paths:
        missing = sorted(set(expected_paths) - set(configured_paths)) if isinstance(configured_paths, list) else expected_paths
        extra = sorted(set(configured_paths) - set(expected_paths)) if isinstance(configured_paths, list) else []
        errors.append(f"opencode skills.paths differs from manifest; missing={missing}, extra={extra}")

    review_required = profile.get("review_required", [])
    if not isinstance(review_required, list) or not all(isinstance(item, str) for item in review_required):
        errors.append("scientific profile: review_required must be string[]")
        review_required = []
    unknown_review = sorted(set(review_required) - set(skills))
    if unknown_review:
        errors.append(f"scientific profile: review_required contains unknown skills: {unknown_review}")

    global_skill_permissions = opencode_config.get("permission", {}).get("skill", {})
    if not isinstance(global_skill_permissions, dict):
        errors.append("opencode permission.skill must be an object")
        global_skill_permissions = {}
    globally_exposed_support = sorted(set(project_skill_names) & set(global_skill_permissions))
    if globally_exposed_support:
        errors.append(
            "project support skills must use agent-specific permissions, not global permissions: "
            f"{globally_exposed_support}"
        )

    permissions_by_agent: dict[str, dict[str, str]] = {}
    text_by_agent: dict[str, str] = {}
    for agent_name, agent_path in PROJECT_SKILL_AGENTS.items():
        permissions, agent_text = agent_skill_permissions(agent_path, errors)
        permissions_by_agent[agent_name] = permissions
        text_by_agent[agent_name] = agent_text
        if permissions.get("*") != "deny":
            errors.append(f"{agent_name} must deny unlisted skills")
        for name, settings in project_skills.items():
            if not isinstance(settings, dict) or agent_name not in settings.get("agents", []):
                continue
            if permissions.get(name) != "allow":
                errors.append(f"{agent_name} must allow project support skill {name!r}")
        if ".opencode/config/project-skills.json" not in agent_text:
            errors.append(f"{agent_name} does not reference project-skills.json")

    permission_entries = permissions_by_agent.get("ScientificAgent", {})
    if permission_entries.get("*") != "deny":
        errors.append("ScientificAgent must deny unlisted skills")
    expected_skill_permissions = {
        name: "ask" if name in review_required else "allow" for name in skills
    }
    expected_skill_permissions.update({name: "allow" for name in project_skill_names})
    actual_skill_permissions = {
        name: action for name, action in permission_entries.items() if name != "*"
    }
    if actual_skill_permissions != expected_skill_permissions:
        missing_or_wrong = {
            name: action
            for name, action in expected_skill_permissions.items()
            if actual_skill_permissions.get(name) != action
        }
        extra_permissions = sorted(set(actual_skill_permissions) - set(expected_skill_permissions))
        errors.append(
            "ScientificAgent skill permissions differ from manifest; "
            f"missing_or_wrong={missing_or_wrong}, extra={extra_permissions}"
        )

    for agent_name in ("OpenCoder", "CoderAgent"):
        unexpected_scientific = sorted(set(skills) & set(permissions_by_agent.get(agent_name, {})))
        if unexpected_scientific:
            errors.append(f"{agent_name} must not load scientific profile skills: {unexpected_scientific}")

    opencoder_text = text_by_agent.get("OpenCoder", "")
    if not re.search(r'(?m)^\s{4}ScientificAgent:\s*[\"\']allow[\"\']\s*$', opencoder_text):
        errors.append("OpenCoder does not grant task permission to ScientificAgent")
    if ".opencode/context/scientific/navigation.md" not in opencoder_text:
        errors.append("OpenCoder does not reference scientific navigation")

    metadata = load_json(METADATA_PATH, errors)
    metadata_agents = metadata.get("agents", [])
    if isinstance(metadata_agents, dict):
        metadata_agents = list(metadata_agents.values())
    scientific_metadata = [item for item in metadata_agents if isinstance(item, dict) and item.get("id") == "scientific-agent"]
    if len(scientific_metadata) != 1:
        errors.append(f"agent metadata must contain one scientific-agent entry, found {len(scientific_metadata)}")

    navigation_root = OPENCODE_ROOT / "context" / "scientific"
    if not (navigation_root / "navigation.md").is_file():
        errors.append("missing scientific root navigation")
    for category, relative_path in CATEGORY_NAVIGATION.items():
        nav_path = navigation_root / relative_path
        if not nav_path.is_file():
            errors.append(f"missing category navigation for {category}: {nav_path.relative_to(PROJECT_ROOT)}")
            continue
        nav_text = nav_path.read_text(encoding="utf-8")
        for name in categories.get(category, []):
            if f"`{name}`" not in nav_text:
                errors.append(f"category navigation {relative_path} does not list {name}")

    pinned_version = source.get("plugin_version") if isinstance(source, dict) else None
    pinned_commit = source.get("commit") if isinstance(source, dict) else None
    repository = source.get("repository") if isinstance(source, dict) else None
    if not isinstance(repository, str) or not repository:
        errors.append("scientific profile: source.repository must be a non-empty string")
    if not isinstance(pinned_version, str) or not pinned_version:
        errors.append("scientific profile: source.plugin_version must be a non-empty string")
    if not isinstance(pinned_commit, str) or not re.fullmatch(r"[0-9a-f]{40}", pinned_commit):
        errors.append("scientific profile: source.commit must be a full lowercase Git SHA")

    requirements_value = installation.get("requirements") if isinstance(installation, dict) else None
    requirements_path = PROJECT_ROOT / requirements_value if isinstance(requirements_value, str) else None
    if requirements_path is None or not requirements_path.is_file():
        errors.append(f"scientific profile: vendored requirements file does not exist: {requirements_value!r}")
    else:
        actual_requirements_hash = hashlib.sha256(requirements_path.read_bytes()).hexdigest()
        if actual_requirements_hash != installation.get("requirements_sha256"):
            errors.append("vendored requirements hash differs from manifest")

    license_value = installation.get("license") if isinstance(installation, dict) else None
    license_path = PROJECT_ROOT / license_value if isinstance(license_value, str) else None
    if license_path is None or not license_path.is_file():
        errors.append(f"missing vendored Scientific Agent Skills license: {license_value!r}")
    else:
        actual_license_hash = hashlib.sha256(license_path.read_bytes()).hexdigest()
        if actual_license_hash != installation.get("license_sha256"):
            errors.append("vendored Scientific Agent Skills license hash differs from manifest")

    # If the optional upstream checkout is present, use it as an additional
    # provenance check. The vendored harness remains valid without that checkout.
    upstream_checkout = PROJECT_ROOT / "scientific-agent-skills"
    plugin_path = upstream_checkout / "plugin.json"
    if plugin_path.is_file():
        plugin = load_json(plugin_path, errors)
        if plugin.get("version") != pinned_version:
            errors.append(f"upstream plugin version differs from manifest: {plugin.get('version')!r} != {pinned_version!r}")
        actual_commit = git_head(upstream_checkout)
        if actual_commit is not None and actual_commit != pinned_commit:
            errors.append(f"upstream commit differs from manifest: {actual_commit} != {pinned_commit}")

    if errors:
        print("Scientific integration validation: FAILED", file=sys.stderr)
        for error in errors:
            print(f"- ERROR: {error}", file=sys.stderr)
        for warning in warnings:
            print(f"- WARNING: {warning}", file=sys.stderr)
        return 1

    print("Scientific integration validation: OK")
    print(f"- skills: {len(skills)} across {len(categories)} categories")
    print(f"- project support skills: {len(project_skill_names)}")
    print(f"- review-required skills: {len(review_required)}")
    print(f"- installation: vendored at {vendored_root_value}")
    print(f"- content sha256: {installation.get('content_sha256')}")
    print(f"- upstream: {repository}@{pinned_version} ({str(pinned_commit)[:12]})")
    for warning in warnings:
        print(f"- WARNING: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
