# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10, "а": 1, "б": 3, "в": 1, "г": 3,
         "д": 2, "е": 1, "ё": 3, "ж": 5, "з": 5, "и": 1,
         "й": 4, "к": 2,"л": 2,"м": 2,"н": 1,"о": 1,"п": 2,
         "р": 1,"с": 1,"т": 1,"у": 2,"ф": 10,"х": 5,"ц": 5,
         "ч": 5,"ш": 8,"щ": 10,"ъ": 10,"ы": 4,"ь": 3,"э": 8,"8": 1,"я": 3}
total = 0

def scrabble_score(word):
    return sum(score[letter] for letter in word)

print(scrabble_score(input('Enter the word: ')))


# one = ('aeioulnstrавеинорст')
# two = ('dgдклмпу')
# three = ('bcmpбгёья')
# four = ('fhvwyйы')
# five = ('kжзхцч')
# eight = ('jxшэю')
# ten = ('qzфщъ')

# text = input('Enter the word: ')
# res = 0
# for i in text:
#     if i in one:
#         res +=1
#     elif i in two:
#         res +=2
#     elif i in three:
#         res +=3
#     elif i in four:
#         res +=4
#     elif i in five:
#         res +=5
#     elif i in eight:
#         res +=8
#     elif i in ten:
#         res +=10
# print(res)
