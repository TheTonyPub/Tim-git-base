def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    result = 1

    for i in range(2, n + 1):
        result *= i

    return result


if __name__ == "__main__":
    try:
        n = int(input("Введите n: "))
        print(f"{n}! = {factorial(n)}")
    except ValueError as error:
        print(f"Ошибка: {error}")