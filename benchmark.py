"""Compare recursive and iterative Fibonacci using timeit."""

import platform
import timeit

from examples.fibonacci_recursive import fibonacci as fibonacci_recursive
from fibonacci import fibonacci


def seconds_per_call(function, n, number):
    measurements = timeit.repeat(lambda: function(n), number=number, repeat=5)
    return min(measurements) / number


def main():
    print(f"Python: {platform.python_version()} ({platform.python_implementation()})")
    print(f"System: {platform.platform()}")
    print("Best of 5 repeats; recursive: 3 calls/repeat; iterative: 10000 calls/repeat")
    print("Times include function-call overhead and depend on the machine and load.")
    print("n | result | recursive seconds/call | iterative seconds/call | ratio")
    for n in [10, 20, 30]:
        expected = fibonacci_recursive(n)
        actual = fibonacci(n)
        if expected != actual:
            raise RuntimeError(f"Algorithms disagree for n={n}")
        recursive_seconds = seconds_per_call(fibonacci_recursive, n, number=3)
        iterative_seconds = seconds_per_call(fibonacci, n, number=10000)
        ratio = recursive_seconds / iterative_seconds
        print(
            f"{n} | {actual} | {recursive_seconds:.9f} | "
            f"{iterative_seconds:.9f} | {ratio:.1f}"
        )


if __name__ == "__main__":
    main()
