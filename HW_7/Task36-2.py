# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть
# распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
# как, например, у операции умножения.

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

import sys, os
clear = lambda: os.system('cls')
clear ()

def print_matrix(martix):
    for i in martix:
        print(*[f"{x:> 4}" for x in i])
        # print(*i)

def operation(matrix):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(1, row):
        for j in range(1,col):
            matrix[i][j] = matrix[i][0]**matrix[0][j]

r=int(input('Enter numder of rows: '))
c=int(input('Enter numder of colums: '))

table=[[i*j for j in range(1,c+1)] for i in range(1,r+1)]

operation(table)
print_matrix(table)




