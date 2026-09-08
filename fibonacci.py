import sys
import time

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    n = 35
    start = time.time()
    result = fibonacci(n)
    end = time.time()
    print(f"Fibonacci({n}) = {result}")
    print(f"Time taken: {end - start:.6f} seconds")
