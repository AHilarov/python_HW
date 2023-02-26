# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input('Enter number: '))
squares = [2 ** i for i in range(0,n) if 2**i<n]
print(squares)

