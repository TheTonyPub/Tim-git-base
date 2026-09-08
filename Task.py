def fibonachi(n):
    if n < 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonachi(n - 2) + fibonachi(n - 1)   # рекурсия без запоминания

a = [12, 13, 85, 34, 47] #Пользователь вписывает сам сюда числа, а не в косоле вбивает 
b = [a[i] for i in range(len(a)) for y in range(1, 100) if fibonachi(y) == a[i]] #гинератор списка
print(*b)