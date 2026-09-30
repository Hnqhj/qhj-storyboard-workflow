"""Literal/output-example contracts only; these do not prove model behavior."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCKED_SOUND = "无 BGM，仅保留人物对白、环境音和动作音。只保留人物对白，其他声音全部关闭。"


def text_blocks(path):
    return re.findall(r"```text\n(.*?)\n```", path.read_text(encoding="utf-8"), re.S)


class LockedContracts(unittest.TestCase):
    def test_entrypoint_sound_literal_is_unchanged(self):
        blocks = text_blocks(ROOT / "SKILL.md")
        self.assertIn(LOCKED_SOUND, blocks)
        self.assertEqual(sum("无 BGM" in block for block in blocks), 1)

    def test_formal_examples_have_one_complete_sound_literal(self):
        blocks = [block for block in text_blocks(ROOT / "references/format-samples.md")
                  if "无 BGM" in block]
        self.assertEqual(len(blocks), 2)
        for block in blocks:
            self.assertEqual(block.count(LOCKED_SOUND), 1)
            self.assertNotIn("按原文", block)
            self.assertNotIn("按权威剧本", block)

    def test_formal_example_paragraph_spacing(self):
        blocks = [block for block in text_blocks(ROOT / "references/format-samples.md")
                  if "无 BGM" in block]
        for block in blocks:
            paragraphs = block.split("\n\n\n")
            self.assertGreaterEqual(len(paragraphs), 3)
            self.assertTrue(all(paragraph and "\n" not in paragraph
                                for paragraph in paragraphs))


if __name__ == "__main__":
    unittest.main()
