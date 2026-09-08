# Интерактивный подсчет, вместо рекурсии 
def is_fibonacci(num):
    a, b = 0, 1   # первые два числа (F1=0, F2=1)
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

numbers = list(map(int, input("Введите числа через пробел: ").split()))

#Выполняем перебор и добавляем в список нужные числа 
result = []
for number in numbers:
    if is_fibonacci(number):
        result.append(number)
print(*result) #расспоковываем список 