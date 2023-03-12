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

def print_operation_table(operation, num_rows, num_columns):
    return operation(num_rows, num_columns)

def mult_table (r,c):
    table=[[i*j for j in range(1,c+1)] for i in range(1,r+1)]
    print_matrix(table)
    # for i in table:
    #     print(i)

def sum_table (r,c):
    table=[[i+j for j in range(c+1)] for i in range(r+1)]
    print_matrix(table)
    
    # for i in table:
    #     print(i)

def print_matrix(martix):
    for i in martix:
        print(*[f"{x:> 4}" for x in i])
        # print(*i)

# def padding_chk(a,b):
#     if len(str(a))>len(str(b)):
#         return int(len(str(a)))
#     return int(len(str(b)))
    

mult_= mult_table
sum_ = sum_table

r=int(input('Enter numder of rows: '))
c=int(input('Enter numder of colums: '))
print('The multiplication table')
print_operation_table(mult_, r,c)
print('The sum table')
print_operation_table(sum_, r,c)




