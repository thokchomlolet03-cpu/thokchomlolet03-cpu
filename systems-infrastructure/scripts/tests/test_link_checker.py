#!/usr/bin/env python3
"""Test internal link checks using only temporary synthetic documents."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from check_local_links import check, links_in


class LinkCheckerTests(unittest.TestCase):
    def test_fenced_example_is_ignored(self):
        tick = chr(96) * 3
        text = tick + "md\n[example](missing.md)\n" + tick + "\n[real](file.md)"
        self.assertEqual(["file.md"], list(links_in(text)))

    def test_valid_relative_anchor_and_remote(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "docs").mkdir()
            (root / "ok.md").write_text("# Exists", encoding="utf-8")
            doc = root / "docs/test.md"
            doc.write_text("[local](../ok.md#exists) [remote](https://example.org) [anchor](#x)", encoding="utf-8")
            self.assertEqual([], check(root, [doc]))

    def test_missing_target_and_traversal(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            doc = root / "test.md"
            doc.write_text("[missing](missing.md) [escape](../../unowned.txt)", encoding="utf-8")
            errors = check(root, [doc])
            self.assertEqual(len(errors), 2)


if __name__ == "__main__":
    unittest.main()
