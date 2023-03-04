# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def calc(op, a, b):
#     return op(a, b)


def degree (numA, numB):
    if numB == 1:
        return numA
    if numB !=1:
        return numA*degree (numA, numB-1)

a = int(input('Enter number A: '))
b = int(input('Enter number B: '))

print(f'{a} to the power of {b} equals {degree (a, b)}')
