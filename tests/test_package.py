"""Observable checks for packaging errors and non-overwriting installs."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHELL = shutil.which("pwsh") or shutil.which("powershell")


class PackagingTests(unittest.TestCase):
    def test_valid_distribution(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/validate.py")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_link_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "package"
            shutil.copytree(ROOT, package, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            with (package / "README.md").open("a", encoding="utf-8") as stream:
                stream.write("\n[Missing artifact](docs/no-such-artifact.md)\n")
            result = subprocess.run([sys.executable, str(ROOT / "scripts/validate.py"), "--root", str(package)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("broken link", result.stderr)


@unittest.skipUnless(SHELL, "PowerShell is needed for install checks")
class InstallTests(unittest.TestCase):
    def run_install(self, destination, *arguments):
        return subprocess.run([SHELL, "-NoProfile", "-NonInteractive", "-File", str(ROOT / "scripts/install.ps1"), "-Destination", str(destination), *arguments], capture_output=True, text=True, encoding="utf-8", errors="replace")

    def test_preview_writes_nothing(self):
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "skills"
            result = self.run_install(destination, "-WhatIf")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(destination.exists())

    def test_single_skill_is_portable(self):
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "skills"
            entries = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))["skills"]
            for entry in entries:
                name = entry["name"]
                with self.subTest(skill=name):
                    target = destination / name
                    result = self.run_install(target, "-Skill", name)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual([p.name for p in target.iterdir()], [name])
                    source = ROOT / "skills" / name
                    expected = {p.relative_to(source) for p in source.rglob("*") if p.is_file()}
                    actual = {p.relative_to(target / name) for p in (target / name).rglob("*") if p.is_file()}
                    self.assertEqual(actual, expected)
                    for file in expected:
                        self.assertEqual((target / name / file).read_bytes(), (source / file).read_bytes())

    def test_conflict_prevents_all_writes(self):
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "skills"
            existing = destination / "work-handoff"
            existing.mkdir(parents=True)
            sentinel = existing / "SKILL.md"
            sentinel.write_text("User custom skill", encoding="utf-8")
            result = self.run_install(destination)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "User custom skill")
            self.assertEqual([p.name for p in destination.iterdir()], ["work-handoff"])


if __name__ == "__main__":
    unittest.main()
