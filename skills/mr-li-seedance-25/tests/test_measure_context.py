"""Accounting safeguards for explicit text-rule measurements."""

import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest


SPEC = importlib.util.spec_from_file_location("measure_context", Path(__file__).resolve().parents[1] / "scripts" / "measure_context.py")
measure_context = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(measure_context)


@unittest.skipUnless(importlib.util.find_spec("tiktoken"), "Optional measurement tests require tiktoken==0.12.0")
class MeasurementTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / "rule.md").write_bytes("规则\r\n对白。\n".encode("utf-8"))
        (self.root / "unused.md").write_text("An unselected large reference. " * 100, encoding="utf-8")
        self.config = {
            "schema_version": 1, "status": "ready", "label": "fixture",
            "tokenizer": {"package": "tiktoken", "version": "0.12.0", "encoding": "o200k_base"},
            "scenarios": [{"id": "prompt", "label": "prompt", "basis": "explicit fixture", "files": ["rule.md"]}],
        }

    def test_explicit_files_only_and_exact_bytes(self):
        result = measure_context.measure(self.root, self.config)
        self.assertEqual(set(result["files"]), {"rule.md"})
        record = result["files"]["rule.md"]
        self.assertEqual(record["bytes"], len("规则\r\n对白。\n".encode("utf-8")))
        self.assertEqual(record["unicode_codepoints"], len("规则\r\n对白。\n"))
        self.assertGreater(record["tokens"], 0)

    def test_duplicate_file_rejected(self):
        self.config["scenarios"][0]["files"] *= 2
        with self.assertRaisesRegex(ValueError, "duplicate-free"):
            measure_context.measure(self.root, self.config)

    def test_traversal_and_symlink_escape_rejected(self):
        with self.assertRaises(ValueError):
            measure_context.source_path(self.root, "../rule.md")
        (self.root / "escape").symlink_to(self.root.parent)
        with self.assertRaisesRegex(ValueError, "escapes"):
            measure_context.source_path(self.root, "escape/file")

    def test_pending_route_cannot_be_reported(self):
        self.config["status"] = "pending"
        with self.assertRaisesRegex(ValueError, "not ready"):
            measure_context.measure(self.root, self.config)

    def test_comparison_retains_increase_and_discloses_dilution(self):
        before = measure_context.measure(self.root, self.config)
        after = copy.deepcopy(before)
        before["scenarios"][0]["text_rule_tokens"] = 100
        after["scenarios"][0]["text_rule_tokens"] = 60
        comparison = measure_context.compare(before, after, [0, 900])
        row = comparison["scenarios"][0]
        self.assertEqual(row["text_rule_reduction_percent"], 40)
        self.assertEqual(row["illustrative_sensitivity_not_measured_usage"][1]["illustrative_total_reduction_percent"], 4)
        after["scenarios"][0]["text_rule_tokens"] = 110
        self.assertEqual(measure_context.compare(before, after, [0])["scenarios"][0]["text_rule_reduction_percent"], -10)

    def test_incompatible_measurements_rejected(self):
        before = measure_context.measure(self.root, self.config)
        after = copy.deepcopy(before)
        after["tokenizer"]["version"] = "different"
        with self.assertRaisesRegex(ValueError, "different tokenizer"):
            measure_context.compare(before, after, [0])
        after = copy.deepcopy(before)
        after["scenarios"][0]["id"] = "another"
        with self.assertRaisesRegex(ValueError, "IDs must match"):
            measure_context.compare(before, after, [0])


if __name__ == "__main__":
    unittest.main()
