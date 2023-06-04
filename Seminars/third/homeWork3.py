# # Задача 16: Требуется вычислить, сколько раз встречается некоторое
# # число X в массиве A[1..N]. Пользователь в первой строке вводит
# # натуральное число N – количество элементов в массиве. В последующих
# # строках записаны N целых чисел Ai
# # . Последняя строка содержит число X

# # пример 

# # 5
# # 1 2 3 4 5
# # 3
# # -> 1



# from random import randint
# myList = []
# a = int(input('input quantity elements: '))
# i = 0
# for i in range(a):
#     myList.append(randint(0, 10))
# x = int(input('input number: '))
# count = 0
# for item in myList :
#     if x == item :
#         count += 1 
# print(*myList)
# print('-> ',count)




# # ======================================================================================

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X


# приимер 

# 5
# 1 2 3 4 5
# 6
# -> 5


# from random import randint
# myList = []
# a = int(input('input quantity elements: '))
# i = 0
# for i in range(a):
#     myList.append(randint(0, 10))
# print(*myList)
# x = int(input('input number: '))

# min = abs(x - myList[0])
# index = 0
# for i in range(1, len(myList)):
#     count = abs(x - myList[i])
#     if count < min:
#          min = count
#          index = i
# print('->', myList[index])




# # ========================================================================================

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


# пример

# Ввод:
# ноутбук
# Вывод:
# 12

list_eng = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
                4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
list_rus = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
                4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}

word = input('input word: ')

if word[0].upper() in str(list_eng.values()):
    summa = 0
    for i in range(len(word)):
            for key, value in list_eng.items():
                if word[i].upper() in value:
                    summa += key
    print(summa)
else: 
    if word[0].upper() in str(list_rus.values()):
        summa = 0
        for i in range(len(word)):
            for key, value in list_rus.items():
                if word[i].upper() in value:
                    summa += key
        print(summa)





