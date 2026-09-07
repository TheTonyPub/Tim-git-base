def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Введите число: "))
print(f"{num}! = {factorial(num)}")