# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random
n = int(input('Enter number of coins: '))
a = [random.randint(0, 1) for _ in range(n)]
print(a)
if a.count(0) < a.count(1) or a.count(0) == a.count(1):
    print('You need to turn', a.count(0), 'coins')
else:
    print('You need to turn', a.count(1), 'coins')
