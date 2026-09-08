'''
Простой рекурсивный алгоритм
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


#Ввод от пользователя
num = int(input('Введите число: '))

#Вычисление и вывод
res = factorial(num)
print(f'Факториал числа {num} = {res}')