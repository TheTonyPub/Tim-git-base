from functools import *
@lru_cache(None) #Применяем lru_cache чтобы запоминать результат работы функции, а не рассчитывать их заново 
 
def fibonachi(n):
    if n<0:
        return None
    if n==1:
        return 0
    if n==2:
        return 1
    return fibonachi(n-2)+fibonachi(n-1)
a = list(map(int, input("Введите числа через пробел: ").split())) #Пользователь вводит числа через пробел
b=[a[i] for i in range(len(a)) for y in range(1,100) if fibonachi(y)==a[i] ] 
print(*b)
