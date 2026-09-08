def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:
        return 1

    return n * factorial(n - 1)


if __name__ == "__main__":
    try:
        n = int(input("Введите n: "))
        print(f"{n}! = {factorial(n)}")
    except ValueError as error:
        print(f"Ошибка: {error}")