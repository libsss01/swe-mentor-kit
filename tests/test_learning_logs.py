"""Real filesystem regression tests for the optional project-local learning log helper."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("learning_logs", ROOT / "scripts" / "learning_logs.py")
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class LearningLogTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.project = Path(self.tmp.name) / "student-project"
        self.project.mkdir()

    def test_init_creates_four_local_logs_only(self):
        made = module.initialize(self.project)
        self.assertEqual({p.name for p in made}, {f"{kind}.md" for kind in module.KINDS})
        self.assertTrue(all(p.parent == self.project / ".swe-mentor" / "learning" for p in made))
        self.assertFalse((ROOT / "learning").exists())

    def test_init_preserves_previous_work(self):
        module.initialize(self.project)
        note = module.log_dir(self.project) / "mistakes.md"
        note.write_text("Important original reasoning\n", encoding="utf-8")
        made_again = module.initialize(self.project)
        self.assertEqual(made_again, [])
        self.assertEqual(note.read_text(encoding="utf-8"), "Important original reasoning\n")

    def test_append_does_not_overwrite(self):
        module.initialize(self.project)
        first = module.append(self.project, "mistakes", "Round-trip", "I expected an object to survive a restart")
        module.append(self.project, "mistakes", "Compatibility", "My original assumption was wrong")
        contents = first.read_text(encoding="utf-8")
        self.assertIn("Round-trip", contents)
        self.assertIn("Compatibility", contents)
        self.assertIn("original assumption", contents)

    def test_append_requires_explicit_initialized_log(self):
        with self.assertRaises(FileNotFoundError):
            module.append(self.project, "review", "Next week", "Try another serialization example")
        self.assertFalse((self.project / ".swe-mentor").exists())

    def test_reject_empty_and_unsupported_entries(self):
        module.initialize(self.project)
        with self.assertRaises(ValueError):
            module.append(self.project, "concepts", "", "Some content")
        with self.assertRaises(ValueError):
            module.append(self.project, "not-a-log", "Title", "Some content")

    def test_logs_are_scoped_to_one_project(self):
        module.initialize(self.project)
        other = Path(self.tmp.name) / "different-project"
        other.mkdir()
        self.assertFalse(module.log_dir(other).exists())


if __name__ == "__main__":
    unittest.main()
