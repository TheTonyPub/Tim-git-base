"""Тесты для функции вычисления чисел Фибоначчи."""

import unittest

from fibonacci import fibonacci


class FibonacciTestCase(unittest.TestCase):
    """Проверка базовых значений и обработки ошибочного ввода."""

    def test_base_values(self) -> None:
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)

    def test_tenth_value(self) -> None:
        self.assertEqual(fibonacci(10), 55)

    def test_large_value(self) -> None:
        self.assertEqual(fibonacci(100), 354224848179261915075)

    def test_negative_value(self) -> None:
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_non_integer_value(self) -> None:
        with self.assertRaises(TypeError):
            fibonacci(2.5)  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            fibonacci(True)


if __name__ == "__main__":
    unittest.main()
