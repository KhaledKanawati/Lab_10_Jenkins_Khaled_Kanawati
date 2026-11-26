"""Check that local deployment produces a usable release."""

import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from deploy import deploy, ROOT


class TestDeploy(unittest.TestCase):
    def test_release_files_and_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "release"
            manifest = deploy(destination)
            target = destination / "app.py"
            self.assertEqual(
                target.read_bytes(), (ROOT / "app.py").read_bytes()
            )
            self.assertEqual(
                manifest["sha256"],
                hashlib.sha256(target.read_bytes()).hexdigest(),
            )
            saved = json.loads(
                (destination / "manifest.json").read_text(encoding="utf-8")
            )
            self.assertEqual(saved, manifest)
            self.assertEqual(
                saved["smoke_output"], "Hello, World from Khaled Kanawati!"
            )

    def test_repeated_deployment_and_build_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "release"
            deploy(destination)
            metadata = {"BUILD_NUMBER": "42", "GIT_COMMIT": "test-commit"}
            with patch.dict("os.environ", metadata):
                manifest = deploy(destination)
            self.assertEqual(manifest["build_number"], "42")
            self.assertEqual(manifest["commit"], "test-commit")

    def test_failed_smoke_check_blocks_release_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "release"
            with patch("deploy.runpy.run_path",
                       return_value={"greet": lambda name: "wrong output"}):
                with self.assertRaisesRegex(RuntimeError, "smoke check"):
                    deploy(destination)
            self.assertFalse((destination / "manifest.json").exists())
