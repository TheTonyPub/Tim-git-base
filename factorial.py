def factorial(n):
    """
    Вычисление факториала числа n (рекурсивная версия)
    """
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    try:
        n = int(input("Введите число для вычисления факториала: "))
        result = factorial(n)
        print(f"Факториал {n}! = {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()