def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = 5
print("Факториал числа", n, "равен:", factorial(n))