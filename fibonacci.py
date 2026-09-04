"""Вычисление N-го числа Фибоначчи."""

import argparse


def fibonacci(n: int) -> int:
    """Вернуть N-е число Фибоначчи за линейное время и постоянную память."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("Номер числа Фибоначчи должен быть целым числом")
    if n < 0:
        raise ValueError("Номер числа Фибоначчи должен быть неотрицательным")

    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


def main() -> None:
    """Прочитать N из аргументов командной строки и вывести результат."""
    parser = argparse.ArgumentParser(description="Вычисление N-го числа Фибоначчи")
    parser.add_argument("n", type=int, help="неотрицательный номер числа")
    args = parser.parse_args()
    # Оставляем только значение: такой вывод удобно использовать в конвейерах.
    print(fibonacci(args.n))


if __name__ == "__main__":
    main()
