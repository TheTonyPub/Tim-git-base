# Рекурсивная версия (была)
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

# Итеративная версия (ОПТИМИЗИРОВАННАЯ)
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Примеры вызова для проверки
print("Рекурсивный факториал 5:", factorial_recursive(5))
print("Итеративный факториал 5:", factorial_iterative(5))