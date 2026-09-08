'''
Итеративный алгоритм вычисления факториала
'''
def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


if __name__ == "__main__":
    #Ввод от пользователя
    num = int(input('Введите число: '))

    if num < 0:
        print('Ошибка: число не может быть отрицательным')
    else:
        res = factorial(num)
        print(f'Факториал числа {num} = {res}')