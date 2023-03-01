# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.


from random import randint as RI

def intCheck():
    while True:
        try:
            int_num = int(input())
            return int_num
        except:
            print('You need to enter an INTEGER number!')

print('Enter how many bushes there are: ')
bushes = [RI(0, 10) for _ in range(intCheck())]
print(bushes)

# Вариант 1
bushes.append(bushes[0]) 
bushes.append(bushes[1])

# Вариант 1.1
m = 0
for i in range(len(bushes)-2):
    a=bushes[i]+bushes[i+1]+bushes[i+2]
    if a>m:
        m = a
print(m)

# Вариант 1.2
m=[]
for i in range(len(bushes)-2):
    a=bushes[i]+bushes[i+1]+bushes[i+2]
    m.append(a)
print(max(m))

# Вариант 2
m=[]
for _ in range(len(bushes)-2):
    a=bushes[0]+bushes[1]+bushes[2]
    bushes.append(bushes[0])
    bushes.remove(bushes[0])
    m.append(a)
print(max(m))


