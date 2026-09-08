"""Behavior checks for the function and the command-line interface."""

from pathlib import Path
import subprocess
import sys
import unittest

from fibonacci import fibonacci
from examples.fibonacci_recursive import fibonacci as fibonacci_recursive


PROGRAM = Path(__file__).resolve().parents[1] / "fibonacci.py"


class FibonacciTests(unittest.TestCase):
    def test_known_values(self):
        for n, expected in [(0, 0), (1, 1), (2, 1), (3, 2), (10, 55), (20, 6765)]:
            with self.subTest(n=n):
                self.assertEqual(fibonacci(n), expected)

    def test_negative_index_is_rejected(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_large_known_value(self):
        self.assertEqual(fibonacci(100), 354224848179261915075)

    def test_matches_original_for_small_indices(self):
        for n in range(21):
            with self.subTest(n=n):
                self.assertEqual(fibonacci(n), fibonacci_recursive(n))

    def test_non_integer_index_is_rejected(self):
        for value in [1.5, "10", None, True]:
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    fibonacci(value)


class CommandLineTests(unittest.TestCase):
    def run_program(self, *arguments):
        return subprocess.run(
            [sys.executable, str(PROGRAM), *arguments],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )

    def test_valid_input(self):
        for value, expected in [("0", "0"), ("1", "1"), ("10", "55"),
                                ("100", "354224848179261915075")]:
            with self.subTest(value=value):
                result = self.run_program(value)
                self.assertEqual(result.returncode, 0)
                self.assertEqual(result.stdout.strip(), expected)
                self.assertEqual(result.stderr, "")

    def test_invalid_input(self):
        for value in ["-1", "1.5", "abc"]:
            with self.subTest(value=value):
                result = self.run_program(value)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertIn("error:", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_missing_input(self):
        result = self.run_program()
        self.assertEqual(result.returncode, 2)
        self.assertIn("error:", result.stderr)


if __name__ == "__main__":
    unittest.main()
