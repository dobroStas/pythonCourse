# Задача 2: 
# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# a = int(input('Введите трехзначное число: '))
# if 100 <= a and a <= 999:
#     res = 0
#     res = (a // 100) + ((a // 10) % 10) + (a % 10)
#     print(res)
# else:
#         print('Введите трехначное число!')

# =========================================================================================================
# =========================================================================================================


# Задача 4: 
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

#!!!!всего в sum 6 частей: 1-петя,1-сережа, 2*(петя+сережа)-катя

# sum = int(input('Введите общее количество журавликов: '))
# x = sum//6                                                                
# p = x
# s = p
# k = 2 * (p + s)
# print(p, k, s)

# ======================================================================================================
# ======================================================================================================

# Задача 6: 
# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# n = str(input('Number ticket: '))
# if len(n) == 6:
#     a = int(n[0])
#     b = int(n[1])
#     c = int(n[2])
#     d = int(n[3])
#     e = int(n[4])
#     f = int(n[5])
#     if (a + b + c) == (d + e + f):
#         print('ticket is lucky')
#     else: print("ticket is not lucky")
# else: print('please, enter number ticket from 6 simbol')


# ============================================================================================

# Задача 8: 
# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

# n = int(input('enter size the chocolate: '))
# m = int(input())
# k =int(input('enter piece size: '))

# if k%m == 0 or k%n == 0: print('YES')
# else: print('NO')