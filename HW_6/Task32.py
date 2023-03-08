# # Задача 32: Определить индексы элементов массива (списка),
# # значения которых принадлежат заданному диапазону (т.е. не
# # меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint as RI

n = int(input('n = '))
my_list = [RI(-10,10) for _ in range(n)]
print(my_list)
print(list(enumerate(my_list)))
min_ = int(input('min = '))
max_ = int(input('max = '))

for i in range(len(my_list)):
    if max_ >= my_list[i] >= min_:
        print(i, end=' ')

