

import func


# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию



# import func
#                                 # print(func.serchFibanachi(7))
# from func import serchFibanachi
#  # print(serchFibanachi(7))




# ===========================================================================================================


# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


# n = int(input('Введите количество оцкнок: '))
# arr = list()
# for i in range(n):
#     a = int(input('Введите оценки: '))
#     arr.append(a)
# print(arr)

# for i in range(len(arr)) :
#     if arr[i] == max(arr) :
#         arr[i] = min(arr)
# print(arr)








# ===========================================================================================================



# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes



# num = int(input('Input num: '))

# def prostoe(num) :
#     if num > 2 and (num % 2) != 0 :
#         for i in range(3, num // 2) :
#             if num % i == 0 :
#                 return False
#         return True
#     return False

# print(prostoe(num))
    

# ===========================================================================================================


# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

num = int(input('Input num: '))
func.ReverseRange(num)


















