"""Source fidelity and routing checks; these do not evaluate model behavior."""
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from audit_skill_consistency import route_problems
from build_runtime import (EXAMPLE_SOURCES, LOCAL_END, LOCAL_START, SOURCES,
                           portable_body, render, source_anchor, source_body)


class RuntimeExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.content = {}
        for index, name in enumerate(SOURCES):
            body = f'# Fixture {index}\n\nUnique source payload {index}.\n\n末句 {index}。'
            if name == 'SKILL.md':
                body = ('---\nname: fixture\n---\n\n' + body + '\n\n' +
                        '\n'.join(f'[Route {i}]({target})' for i, target in enumerate(SOURCES[1:])))
            self.write(name, body)
            self.content[name] = body

    def tearDown(self):
        self.temp.cleanup()

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')

    def test_all_runtime_sources_including_examples_are_exported_once(self):
        output = render(self.root)
        for index, name in enumerate(SOURCES):
            with self.subTest(source=name):
                self.assertEqual(1, output.count(f'<!-- source: {name} -->'))
                self.assertEqual(1, output.count(f'Unique source payload {index}.'))
                self.assertIn(f'末句 {index}。', output)
                self.assertIn(f'<a id="{source_anchor(name)}"></a>', output)
        self.assertEqual(2, len(EXAMPLE_SOURCES))
        self.assertNotIn('name: fixture', output)

    def test_maintenance_files_are_not_execution_sources(self):
        for name in ('CHANGELOG.md', 'USAGE_GUIDE.md',
                     'references/full-flow-regression.md', 'references/field-lessons.md',
                     'references/function-coverage.md'):
            self.write(name, 'maintenance-only payload')
            self.assertNotIn(name, SOURCES)
        self.assertNotIn('maintenance-only payload', render(self.root))

    def test_local_links_become_existing_internal_targets(self):
        body = ('[State](context-protocol.md)\n[Root](../SKILL.md)\n'
                '[Web](https://example.com/rules)')
        self.write('references/result-repair.md', body)
        output = render(self.root)
        self.assertIn(f'[State](#{source_anchor("references/context-protocol.md")})', output)
        self.assertIn(f'[Root](#{source_anchor("SKILL.md")})', output)
        self.assertIn('[Web](https://example.com/rules)', output)
        self.assertNotIn('[State](context-protocol.md)', output)

    def test_explicit_local_only_block_preserves_surrounding_source(self):
        name = 'references/delivery-review.md'
        self.write(name, f'Before.\n{LOCAL_START}\n[Local](../scripts/optional.py)\n'
                        f'{LOCAL_END}\nPortable capability boundary.\n'
                        f'{LOCAL_START}\nSecond optional local tool.\n{LOCAL_END}\nAfter.')
        self.assertEqual('Before.\n\nPortable capability boundary.\n\nAfter.',
                         source_body(self.root, name))
        output = render(self.root)
        self.assertIn('Portable capability boundary.', output)
        self.assertNotIn('scripts/optional.py', output)
        self.assertNotIn('Second optional local tool.', output)

    def test_unmarked_unbundled_link_fails_instead_of_faking_a_section(self):
        self.write('references/delivery-review.md', '[Maintenance](../CHANGELOG.md)')
        with self.assertRaisesRegex(ValueError, 'single-file link target is not included'):
            render(self.root)

    def test_unbalanced_or_nested_local_only_markers_fail(self):
        for body in (LOCAL_START + '\nUnclosed', LOCAL_END,
                     LOCAL_START + LOCAL_START + LOCAL_END + LOCAL_END):
            with self.subTest(body=body):
                self.write('references/delivery-review.md', body)
                with self.assertRaises(ValueError):
                    render(self.root)

    def test_missing_runtime_source_fails(self):
        (self.root / 'references/result-repair.md').unlink()
        with self.assertRaises(FileNotFoundError):
            render(self.root)
        self.assertTrue(any('missing runtime source' in item for item in route_problems(self.root)))

    def test_new_runtime_routes_are_reachable(self):
        self.assertIn('references/result-repair.md', SOURCES)
        self.assertIn('references/runtime-efficiency.md', SOURCES)
        self.assertEqual([], route_problems(self.root))

    def test_unlinked_runtime_source_is_reported(self):
        name = 'references/result-repair.md'
        skill = self.content['SKILL.md']
        self.write('SKILL.md', '\n'.join(line for line in skill.splitlines()
                                        if f']({name})' not in line))
        self.assertIn(f'runtime source is not reachable from entrypoint: {name}',
                      route_problems(self.root))

    def test_transitive_runtime_route_is_reachable(self):
        self.write('SKILL.md', '[State](references/context-protocol.md)')
        self.write('references/context-protocol.md', '\n'.join(
            f'[Route {i}]({Path(name).name})' for i, name in enumerate(SOURCES[1:])))
        self.assertEqual([], route_problems(self.root))

    def test_local_only_link_does_not_count_as_runtime_route(self):
        self.write('SKILL.md', f'{LOCAL_START}\n' + self.content['SKILL.md'] + f'\n{LOCAL_END}')
        self.assertTrue(any('not reachable from entrypoint' in item for item in route_problems(self.root)))

    def test_unchanged_source_body_is_not_summarized(self):
        name = 'references/format-samples.md'
        self.assertEqual(self.content[name], portable_body(self.root, name))


if __name__ == '__main__':
    unittest.main()
