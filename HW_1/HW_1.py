from mycode import int_check as IC
from mycode import digit_sum as DC
from mycode import partition


# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('TASK 2. Sum of digits of a three-digit number')
my_num = input('Enter number: ')
print('Sum of digits in', my_num, 'is', DC(my_num))


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

print()
print('TASK 4. Enter number of origami kids made: ')
my_num = IC()
if my_num > 5 and my_num % 6 == 0:
    print (round(my_num/6), round(my_num/6*4), round(my_num/6))
else:
    print("Print correct number")


# Задача 6:
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no


print()
print('TASK 6. Lucky ticket')
my_num = str(input('Enter number of the ticket: '))
if my_num.isdigit() == True and len(my_num) == 6:
    chunks = list(partition(my_num, 3))
    if DC(chunks[0]) == DC(chunks[1]):
        print("Yes! You are lucky")
    else:
        print('No. Unfortunately. May be next time.')
else:
    print('Enter correct number!')


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

print()
print('TASK 8. Chocolate')
print("Enter chocolate's bar length")
lenght = IC()
print("Enter chocolate's bar width")
width = IC()
print("How  many pieces do you need? ")
piece = IC()

if piece > 1 and (piece % lenght == 0 or piece % width == 0) and piece < lenght*width:
    print('Yes')
elif (lenght ==1 or width ==1) and piece <= lenght*width:
    print('Yes')
else:
    print('No')
