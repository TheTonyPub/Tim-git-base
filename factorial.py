# Улучшенная итеративная реализация (цикл)
def factorial_iterative(n):
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        number = int(input("Введите число для вычисления факториала: "))
        print(f"Факториал {number} равен {factorial_iterative(number)}")
    except ValueError:
        print("Пожалуйста, введите целое число.")