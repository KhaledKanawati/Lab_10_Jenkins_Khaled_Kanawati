"""Unit tests for the greeting and command-line entry point."""

from contextlib import redirect_stdout
import io
from pathlib import Path
import runpy
import unittest

from app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(
            greet("World"), "Hello, World from Khaled Kanawati!"
        )

    def test_other_name(self):
        self.assertEqual(
            greet("Jenkins"), "Hello, Jenkins from Khaled Kanawati!"
        )

    def test_empty_name(self):
        self.assertEqual(greet(""), "Hello,  from Khaled Kanawati!")

    def test_script_entry_point(self):
        output = io.StringIO()
        app_path = Path(__file__).resolve().parents[1] / "app.py"
        with redirect_stdout(output):
            runpy.run_path(str(app_path), run_name="__main__")
        self.assertEqual(
            output.getvalue(), "Hello, World from Khaled Kanawati!\n"
        )
