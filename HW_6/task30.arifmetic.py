# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a = int(input('Enter 1st elem: '))
d = int(input('Enter delta: '))
n = int(input('Enter number of elem: '))


# Вариант 1
arr = list(range(a, a+(n)*d, d))
print('Вариант 1:', *arr)


# Вариант 2
arr = [a]
i = 0
while i < n-1:
    arr.append(arr[i]+d)
    i += 1
print('Вариант 2:', *arr)


# Вариант 3
arr = [a]

def arith1(arr, d, n) -> list:
    if n == 1:
        return arr
    a = arr[-1]
    arr.append(a + d)
    return arith1(arr, d, n-1)


print('Вариант 3:', *arith1(arr, d, n))

# Вариант 4

def arith4(a, d, n):
    if n == 1:
        return [a]
    return (second := arith4(a, d, n-1)) + [second[-1]+d]

print('Вариант 4:', *arith4(a, d, n))
