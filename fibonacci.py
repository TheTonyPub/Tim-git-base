"""Вычисление N-го числа Фибоначчи."""

import argparse


def fibonacci(n: int) -> int:
    """Вернуть N-е число Фибоначчи рекурсивным способом."""
    if n < 0:
        raise ValueError("Номер числа Фибоначчи должен быть неотрицательным")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main() -> None:
    """Прочитать N из аргументов командной строки и вывести результат."""
    parser = argparse.ArgumentParser(description="Вычисление N-го числа Фибоначчи")
    parser.add_argument("n", type=int, help="неотрицательный номер числа")
    args = parser.parse_args()
    print(fibonacci(args.n))


if __name__ == "__main__":
    main()
