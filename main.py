def factorial(n):
    if n < 0:
        return "Ошибка"

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Введите число: "))
print(f"{num}! = {factorial(num)}")