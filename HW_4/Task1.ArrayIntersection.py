# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств


# Это просто решение

Array1 = [0, 1, 2, 3, 4, 5, 6, 6, 33]
Array2 = [10, 9, 8, 7, 33, 4, 5, 6]

# Вариант 1
# res = set()
# for i in Array1:
#     for j in Array2:
#         if i == j:
#             res.add(i)


# Вариант 2
set1 = set(Array1)
set2 = set(Array2)
res = list(set1 & set2)
print(sorted(res))

# А тут я решил попробовать усложнить задачу, чтоб можно было сливать любое количество множеств. 
# Правда, написать все проверки уже сил не хватило
from random import randint as RI

def intCheck():
    while True:
        try:
            int_num = int(input())
            return int_num
        except:
            print('You need to enter an INTEGER number!')

print('Enter how many lists you want to be generated')
n = intCheck()
if n < 2:
    print('You need at least 2 lists')

print('For each list write Min number, Max number and Lenght in format "MIN MAX LENGHT":')

lists_dict = dict()
amount=1
while amount <=n:
    my_list = input(f'For list {amount}: ').split()
    int_list=[int(i) for i in my_list]
    array = [RI(int_list[0], int_list[1]) for _ in range(int_list[2])]
    lists_dict[amount] = array
    print(lists_dict)
    amount+=1

def MergeArrays(Array1, Array2):
    set1 = set(Array1)
    set2 = set(Array2)
    res = list(set1 & set2)
    return sorted(res)

count = 2
while count <=n:
    templst = list()
    templst = MergeArrays(lists_dict.get(count-1), lists_dict.get(count))
    lists_dict[count] = templst
    count+=1
print(lists_dict.get(count-1))


