#!/usr/bin/env python3
"""Check this distribution without external dependencies."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def quoted_fields(text: str) -> dict[str, str]:
    """Read our intentionally simple YAML subset (JSON quoted string values)."""
    result = {}
    for line in text.splitlines():
        if not line.strip():
            continue
        match = re.fullmatch(r"\s*([a-z_]+):\s*(.+)", line)
        if not match:
            raise ValueError(f"Unsupported metadata line: {line}")
        key, raw = match.groups()
        if key in result:
            raise ValueError(f"Duplicate metadata key: {key}")
        value = json.loads(raw) if raw.startswith('"') else raw
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Empty or non-string field: {key}")
        result[key] = value
    return result


def inspect(root: Path) -> tuple[int, list[str]]:
    errors = []
    try:
        manifest = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
        entries = manifest["skills"]
        if not isinstance(entries, list) or len(entries) != 10:
            raise ValueError("Catalog must contain exactly ten skills")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return 0, [f"catalog.json: {exc}"]
    try:
        license_text = (root / "LICENSE").read_text(encoding="utf-8")
        if not license_text.startswith("MIT License\n"):
            errors.append("Root LICENSE must contain the MIT license")
    except OSError as exc:
        return 0, [f"LICENSE: {exc}"]
    names = []
    for entry in entries:
        try:
            name = entry["name"]
            if not re.fullmatch(r"jbh-[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
                raise ValueError("Invalid skill name")
            names.append(name)
            directory = root / "skills" / name
            expected = f"skills/{name}/SKILL.md"
            if entry["entrypoint"] != expected:
                raise ValueError("Catalog entrypoint must match directory")
            text = (directory / "SKILL.md").read_text(encoding="utf-8")
            match = re.match(r"\A---\n(.*?)\n---\n(.+)\Z", text, re.S)
            if not match:
                raise ValueError("Missing frontmatter or instructions")
            front = quoted_fields(match[1])
            if front.get("name") != name or front.get("license") != "MIT":
                raise ValueError("Frontmatter name/license mismatch")
            if not front.get("description") or len(front["description"]) > 1024:
                raise ValueError("Missing or oversized description")
            if re.search(r"\[TODO:|\bREPLACE_ME\b", text):
                raise ValueError("Unfinished scaffold")
            ui = (directory / "agents" / "openai.yaml").read_text(encoding="utf-8")
            if not ui.startswith("interface:\n"):
                raise ValueError("Missing interface metadata")
            interface = quoted_fields(ui.split("\n", 1)[1])
            if interface.get("display_name") != entry["title"]:
                raise ValueError("Display name differs from catalog")
            short = interface.get("short_description", "")
            if not 25 <= len(short) <= 64:
                raise ValueError("Short description must be 25-64 characters")
            if f"${name}" not in interface.get("default_prompt", ""):
                raise ValueError("Default prompt must invoke its skill")
            if (directory / "LICENSE").read_text(encoding="utf-8") != license_text:
                raise ValueError("Skill must retain the complete distribution license")
            for key in ("summary", "example", "inspiration"):
                if not entry.get(key):
                    raise ValueError(f"Missing catalog field: {key}")
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f"{entry.get('name', '(unnamed)') if isinstance(entry, dict) else '(invalid entry)'}: {exc}")
    if len(names) != len(set(names)):
        errors.append("Duplicate skill names")
    actual = {p.name for p in (root / "skills").iterdir() if p.is_dir()} if (root / "skills").is_dir() else set()
    if actual != set(names):
        errors.append("Skill directories differ from catalog")
    for document in root.rglob("*.md"):
        if ".git" in document.parts:
            continue
        text = document.read_text(encoding="utf-8")
        # This package uses relative links without spaces and no absolute local links.
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            path = target.split("#", 1)[0]
            if path and not (document.parent / path).exists():
                errors.append(f"{document.relative_to(root)}: broken link {target}")
    return len(entries), errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        count, errors = inspect(args.root.resolve())
    except (OSError, ValueError, TypeError) as exc:
        count, errors = 0, [str(exc)]
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {count} skills; metadata, catalog, licenses and local links are consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
