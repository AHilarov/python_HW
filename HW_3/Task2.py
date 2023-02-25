# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
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
lst2 = [abs(x-i) for i in my_list]
print(my_list[lst2.index(min(lst2))])