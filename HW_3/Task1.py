# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint as RI

def intCheck():
    while True:
        try:
            int_num = int(input())
            return int_num
        except:
            print('You need to enter an INTEGER number!')

print('Enter the lenght of the list to be generated')
my_list = [RI(-10,10) for _ in range(intCheck())]
print(my_list)
print('What number you are looking for? ')
x=intCheck()
print('Number', x, 'occurs', my_list.count(x), 'times')
