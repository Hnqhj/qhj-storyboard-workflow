"""Deterministic regression tests; these do not simulate an LLM or certify media."""
import hashlib
import json
import re
from pathlib import Path
import shutil
import stat
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from audit_delivery import audit_tree, prompt_content, safe_extract
from audit_skill_consistency import audit, tracked_files
from build_runtime import render, TARGET

PROMPT = '自然日光，画面清楚。\n\n\n35mm全景，甲站在门边，乙坐在桌旁。\n\n\n50mm过肩人物关系镜头，甲说：“明天见。”\n\n\n85mm过肩人物关系镜头，乙说：“明天见。”'


class DeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def write(self, name, content='payload'):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding='utf-8')
        return p

    def manifest(self, paths, kind='file'):
        return {'schema_version': 1, 'files': [
            {'path': name, 'kind': kind, 'status': 'adopted',
             'sha256': hashlib.sha256((self.root / name).read_bytes()).hexdigest()}
            for name in paths]}

    def check(self, manifest, prompts=False):
        return audit_tree(self.root, formal_delivery=True, require_prompts=prompts, manifest=manifest)[0]

    def test_empty_directory_rejected(self):
        self.assertIn('delivery is empty', audit_tree(self.root)[0])

    def test_nested_empty_directory_rejected_beside_valid_file(self):
        self.write('1-1/提示词/1-1A.txt', PROMPT)
        (self.root / '1-1/资产/道具').mkdir(parents=True)
        problems = audit_tree(self.root)[0]
        self.assertIn('empty directory: 1-1/资产/道具', problems)
        self.assertNotIn('delivery is empty', problems)

    def test_nested_directories_with_files_pass(self):
        self.write('1-1/提示词/1-1A.txt', PROMPT)
        self.write('1-1/资产/道具/P01.txt')
        self.assertEqual([], audit_tree(self.root)[0])

    def test_directory_only_tree_rejected(self):
        (self.root / '1-1/资产/道具').mkdir(parents=True)
        problems = audit_tree(self.root)[0]
        self.assertIn('empty directory: 1-1/资产/道具', problems)
        self.assertIn('delivery is empty', problems)

    def test_formal_needs_explicit_scope(self):
        self.write('1-1A.txt', PROMPT)
        self.assertTrue(self.check(None, True))

    def test_description_is_not_prompt(self):
        p = self.write('提示词使用说明.txt', '这里只说明文件夹用途，不包含视频生成提示词。')
        self.assertFalse(prompt_content(p))
        self.assertTrue(self.check(self.manifest([p.name], 'prompt'), True))

    def test_numbered_prompt_accepted(self):
        p = self.write('1-1A.txt', PROMPT)
        self.assertTrue(prompt_content(p))
        self.assertEqual([], self.check(self.manifest([p.name], 'prompt'), True))

    def test_prompt_detection_ignores_name(self):
        self.write('1-1A.txt', PROMPT)
        self.assertEqual([], audit_tree(self.root, require_prompts=True)[0])

    def test_plot_failure_word_not_candidate(self):
        self.write('道具/P01_失败实验样机_定稿.txt')
        self.assertEqual([], self.check(self.manifest(['道具/P01_失败实验样机_定稿.txt'])))

    def test_candidate_status_rejected(self):
        self.write('P01.txt')
        m = self.manifest(['P01.txt'])
        m['files'][0]['status'] = 'candidate'
        self.assertTrue(self.check(m))

    def test_candidate_directory_rejected(self):
        self.write('候选稿/P01.txt')
        self.assertTrue(self.check(self.manifest(['候选稿/P01.txt'])))

    def test_missing_expected_copy(self):
        p = self.write('1-2/P01.txt')
        m = self.manifest(['1-2/P01.txt'])
        p.unlink()
        self.assertTrue(any('missing expected file' in s for s in self.check(m)))

    def test_unexpected_copy_rejected(self):
        self.write('P01.txt')
        m = self.manifest(['P01.txt'])
        self.write('P02.txt')
        self.assertTrue(any('unexpected file' in s for s in self.check(m)))

    def test_hash_mismatch(self):
        self.write('P01.txt')
        m = self.manifest(['P01.txt'])
        self.write('P01.txt', 'different')
        self.assertTrue(any('hash mismatch' in s for s in self.check(m)))

    def test_missing_hash(self):
        self.write('P01.txt')
        m = self.manifest(['P01.txt'])
        del m['files'][0]['sha256']
        self.assertTrue(self.check(m))

    def test_empty_file(self):
        self.write('P01.txt', '')
        self.assertTrue(self.check(self.manifest(['P01.txt'])))

    def test_metadata(self):
        self.write('.DS_Store')
        self.assertTrue(self.check(self.manifest(['.DS_Store'])))

    def test_symlink_rejected(self):
        self.write('P01.txt')
        (self.root / 'P02.txt').symlink_to(self.root / 'P01.txt')
        self.assertTrue(audit_tree(self.root)[0])

    def test_invalid_manifest_path(self):
        self.assertTrue(self.check({'schema_version': 1, 'files': [{'path': '../outside', 'kind': 'file'}]}))

    def test_duplicate_manifest_path(self):
        self.write('P01.txt')
        m = self.manifest(['P01.txt', 'P01.txt'])
        self.assertTrue(self.check(m))

    def test_missing_scene(self):
        self.write('P01.txt')
        m = self.manifest(['P01.txt'])
        m['required_scenes'] = ['1-1', '1-2']
        m['scenes'] = {'1-1': ['P01.txt']}
        self.assertTrue(any('1-2' in s for s in self.check(m)))

    def test_scene_copies_declared_individually(self):
        paths = ['1-1/P01.txt', '1-2/P01.txt']
        for name in paths:
            self.write(name)
        m = self.manifest(paths)
        m['required_scenes'] = ['1-1', '1-2']
        m['scenes'] = {'1-1': [paths[0]], '1-2': [paths[1]]}
        self.assertEqual([], self.check(m))

    def test_canonical_assets_reject_same_content_under_two_names(self):
        self.write('未编号生成稿.txt', 'same asset bytes')
        self.write('P01_正式编号稿.txt', 'same asset bytes')
        problems = audit_tree(self.root, canonical_assets=True)[0]
        self.assertTrue(any('duplicate canonical asset content' in s for s in problems))

    def test_same_content_scene_copies_allowed_outside_canonical_mode(self):
        paths = ['1-1/P01.txt', '1-2/P01.txt']
        for name in paths:
            self.write(name, 'same adopted asset')
        self.assertEqual([], audit_tree(self.root)[0])

    def image_manifest(self, size=(3840, 2160), fmt='PNG', extension='.png'):
        from PIL import Image
        p = self.root / ('P01' + extension)
        Image.new('RGB', size, 'white').save(p, format=fmt)
        m = self.manifest([p.name], 'image')
        m['files'][0]['image'] = {'width': 3840, 'height': 2160, 'format': 'PNG'}
        return m

    def test_4k_image_passes(self):
        self.assertEqual([], self.check(self.image_manifest()))

    def storyboard_manifest(self, name='3-1_比赛/分镜参考/3-1，分镜1.png'):
        m = self.image_manifest()
        target = self.root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        (self.root / 'P01.png').rename(target)
        m['files'][0].update(path=name, role='storyboard_reference',
                             scene='3-1', shot=1, status='self_reviewed')
        return m

    def test_self_reviewed_storyboard_accepted(self):
        self.assertEqual([], self.check(self.storyboard_manifest()))

    def test_storyboard_wrong_filename_rejected(self):
        self.assertTrue(self.check(self.storyboard_manifest('3-1_比赛/分镜参考/K09.png')))

    def test_storyboard_wrong_directory_rejected(self):
        self.assertTrue(self.check(self.storyboard_manifest('3-1_比赛/镜头定帧/3-1，分镜1.png')))

    def test_storyboard_wrong_scene_rejected(self):
        self.assertTrue(self.check(self.storyboard_manifest('3-2_比赛/分镜参考/3-1，分镜1.png')))

    def test_storyboard_invalid_shot_rejected(self):
        m = self.storyboard_manifest()
        for shot in (0, -1, True, '1'):
            with self.subTest(shot=shot):
                m['files'][0]['shot'] = shot
                self.assertTrue(self.check(m))

    def test_storyboard_generic_file_cannot_bypass(self):
        self.write('3-1/分镜参考/3-1，分镜1.txt')
        m = self.manifest(['3-1/分镜参考/3-1，分镜1.txt'])
        m['files'][0].update(role='storyboard_reference', scene='3-1',
                             shot=1, status='self_reviewed')
        self.assertTrue(self.check(m))

    def test_master_asset_self_review_is_not_adoption(self):
        m = self.image_manifest()
        m['files'][0]['status'] = 'self_reviewed'
        self.assertTrue(self.check(m))

    def test_wrong_size_fails(self):
        self.assertTrue(any('expected' in s for s in self.check(self.image_manifest((1920, 1080)))))

    def test_wrong_format_fails(self):
        self.assertTrue(any('format expected' in s for s in self.check(self.image_manifest(fmt='JPEG'))))

    def test_no_image_target_fails(self):
        m = self.image_manifest()
        del m['files'][0]['image']
        self.assertTrue(self.check(m))

    def test_corrupt_image_fails(self):
        self.write('P01.png', 'not png')
        self.assertTrue(self.check(self.manifest(['P01.png'], 'image')))

    def test_image_cannot_bypass_as_generic_file(self):
        m = self.image_manifest()
        m['files'][0]['kind'] = 'file'
        self.assertTrue(self.check(m))

    def test_zip_paths_symlinks_and_duplicates(self):
        for kind in ('traversal', 'symlink', 'duplicate'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as temp:
                archive = Path(temp) / 'bad.zip'
                with zipfile.ZipFile(archive, 'w') as z:
                    if kind == 'traversal':
                        z.writestr('../outside.txt', 'bad')
                    elif kind == 'symlink':
                        info = zipfile.ZipInfo('link')
                        info.create_system = 3
                        info.external_attr = (stat.S_IFLNK | 0o777) << 16
                        z.writestr(info, '../outside')
                    else:
                        z.writestr('same', 'one')
                        z.writestr('same', 'two')
                with self.assertRaises(ValueError):
                    safe_extract(archive, Path(temp) / 'out')

    def test_valid_zip_roundtrip(self):
        self.write('1-1A.txt', PROMPT)
        m = self.manifest(['1-1A.txt'], 'prompt')
        with tempfile.TemporaryDirectory() as temp:
            archive = Path(temp) / 'valid.zip'
            with zipfile.ZipFile(archive, 'w') as z:
                z.write(self.root / '1-1A.txt', '1-1A.txt')
            destination = Path(temp) / 'out'
            safe_extract(archive, destination)
            self.assertEqual([], audit_tree(destination, formal_delivery=True, require_prompts=True, manifest=m)[0])

    def test_zip_empty_directory_entries_rejected(self):
        for include_file in (False, True):
            with self.subTest(include_file=include_file), tempfile.TemporaryDirectory() as temp:
                archive = Path(temp) / 'empty-directories.zip'
                with zipfile.ZipFile(archive, 'w') as z:
                    z.writestr('1-1/', '')
                    z.writestr('1-1/资产/', '')
                    z.writestr('1-1/资产/道具/', '')
                    if include_file:
                        z.writestr('1-1/提示词/1-1A.txt', PROMPT)
                destination = Path(temp) / 'out'
                safe_extract(archive, destination)
                problems = audit_tree(destination)[0]
                self.assertIn('empty directory: 1-1/资产/道具', problems)
                self.assertEqual(not include_file, 'delivery is empty' in problems)

    def test_zip_nonempty_directory_entries_pass(self):
        with tempfile.TemporaryDirectory() as temp:
            archive = Path(temp) / 'directories-with-files.zip'
            with zipfile.ZipFile(archive, 'w') as z:
                z.writestr('1-1/', '')
                z.writestr('1-1/提示词/', '')
                z.writestr('1-1/提示词/1-1A.txt', PROMPT)
            destination = Path(temp) / 'out'
            safe_extract(archive, destination)
            self.assertEqual([], audit_tree(destination, require_prompts=True)[0])


class SourceChecks(unittest.TestCase):
    def test_runtime_matches_sources(self):
        self.assertEqual(render(), (ROOT / TARGET).read_text(encoding='utf-8'))

    def test_current_structure(self):
        self.assertEqual([], audit(ROOT, structural_only=True))

    def test_version_malformed_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'copy'
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('__pycache__'))
            p = root / 'SKILL.md'
            p.write_text(re.sub(r'(?m)^(\s*version:) "[^"]+"$', r'\1 "2.0.not-a-version"',
                                p.read_text(encoding='utf-8')), encoding='utf-8')
            self.assertTrue(any('entrypoint version' in s for s in audit(root, structural_only=True)))

    def test_version_drift_in_guides_rejected(self):
        for name, prefix in (('USAGE_GUIDE.md', '适用版本：'), ('CHANGELOG.md', '当前版本：')):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temp:
                root = Path(temp) / 'copy'
                shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('__pycache__'))
                p = root / name
                p.write_text(p.read_text(encoding='utf-8').replace(prefix, 'outdated:'), encoding='utf-8')
                self.assertIn(f'version mismatch: {name}', audit(root, structural_only=True))

    def test_broken_and_nonportable_links_rejected(self):
        for link in ('missing-reference.md', '../../outside.md'):
            with self.subTest(link=link), tempfile.TemporaryDirectory() as temp:
                root = Path(temp) / 'copy'
                shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('__pycache__'))
                p = root / 'references/format-samples.md'
                p.write_text(p.read_text(encoding='utf-8') + f'\n[Broken]({link})\n', encoding='utf-8')
                problems = audit(root, structural_only=True)
                self.assertTrue(any('broken or nonportable reference' in s and link in s for s in problems))

    def test_changed_runtime_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'copy'
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('__pycache__'))
            p = root / TARGET
            p.write_text(render(root) + '\nUnmaintained export addition.\n', encoding='utf-8')
            self.assertIn('single-file runtime differs from maintained sources', audit(root, structural_only=True))

    def test_changed_rules_invalidate_review(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'copy'
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('__pycache__'))
            # Fixture baseline only, not a real semantic approval.
            version = re.search(r'(?m)^[ \t]*version: "([^"]+)"$', (root / 'SKILL.md').read_text()).group(1)
            snapshot = {'version': version, 'review_type': 'maintainer-text-review',
                        'sha256': {n: hashlib.sha256(p.read_bytes()).hexdigest() for n, p in tracked_files(root).items()}}
            (root / 'review-snapshot.json').write_text(json.dumps(snapshot), encoding='utf-8')
            p = root / 'references/format-samples.md'
            p.write_text(p.read_text(encoding='utf-8') + '\n非结尾镜头必须持续说话并完全不交代人物位置。\n', encoding='utf-8')
            # Even regeneration of the export must not silently refresh the review baseline.
            (root / TARGET).write_text(render(root), encoding='utf-8')
            self.assertTrue(any('changed since recorded text review' in s for s in audit(root)))


if __name__ == '__main__':
    unittest.main()
