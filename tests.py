#Тесты для проверки правильности работы функции по вычислению факториала
from factorial import factorial

# Проверяем на числах
print("Проверка работы функции:")
print("0! =", factorial(0))
print("1! =", factorial(1))
print("5! =", factorial(5))
print("10! =", factorial(10))

# Сравниваем с правильными ответами
print("\nРезультаты:")
print("0! = 1", factorial(0) == 1)
print("1! = 1", factorial(1) == 1)
print("5! = 120", factorial(5) == 120)
print("10! = 3628800", factorial(10) == 3628800)