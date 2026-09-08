"""Compute F(n), where F(0) = 0 and F(1) = 1."""

import argparse


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number using two running values."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    current, following = 0, 1
    for _ in range(n):
        current, following = following, current + following
    return current


def non_negative_integer(value: str) -> int:
    """Validate the command-line argument before starting the computation."""
    try:
        n = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("n must be an integer") from None
    if n < 0:
        raise argparse.ArgumentTypeError("n must be non-negative")
    return n


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=non_negative_integer, help="index, starting at 0")
    args = parser.parse_args()
    print(fibonacci(args.n))


if __name__ == "__main__":
    main()
