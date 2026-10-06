"""Regression: exercise the installed console command away from the source tree."""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


class InstalledLinkChecker(unittest.TestCase):
    def test_installed_command_checks_real_targets(self):
        command = shutil.which('profile-check-links')
        self.assertIsNotNone(command, 'Install the built wheel before running this regression')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'guide.md').write_text('# Guide\n', encoding='utf-8')
            (root/'README.md').write_text('[guide](guide.md)\n', encoding='utf-8')
            ok = subprocess.run([command], cwd=root, capture_output=True, text=True, timeout=10)
            self.assertEqual(ok.returncode, 0, ok.stderr)
            (root/'README.md').write_text('[missing](missing.md)\n', encoding='utf-8')
            bad = subprocess.run([command], cwd=root, capture_output=True, text=True, timeout=10)
            self.assertEqual(bad.returncode, 1, bad.stderr)
            self.assertIn('BROKEN:', bad.stdout)


if __name__ == '__main__':
    unittest.main()
