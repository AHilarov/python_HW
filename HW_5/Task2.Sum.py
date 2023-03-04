# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2 ->  4


def sum(numA, numB):
    if numA == 0:
        return numB
    if numA > 0:
        return sum(numA-1, numB+1)


a = int(input('Enter number A: '))
b = int(input('Enter number B: '))

print(f'{a} plus {b} equals {sum (a, b)}')

# Альтернатива

def sum2(a, b):
    if a == 0:
        return b
    else:
        sum2(a-1, b+1)

print(f'{a} plus {b} equals {sum2 (a, b)}')
