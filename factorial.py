def factorial_recursive(n):
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

if __name__ == "__main__":
    number = int(input("Введите число для вычисления факториала: "))
    print(f"Факториал {number} равен {factorial_recursive(number)}")