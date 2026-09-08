def factorial(n):
    """
    Вычисление факториала числа n (итеративная версия)
    Преимущества: быстрее, нет ограничения по глубине рекурсии
    """
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    try:
        n = int(input("Введите число для вычисления факториала: "))
        result = factorial(n)
        print(f"Факториал {n}! = {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()