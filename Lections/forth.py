# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]



spisok = [1, 2, 3, 5, 8, 15, 23, 38]

spisok2 = []
#  ===========================================================================
# def why(f, col) :
#     return[x for x  in col if f(x)]
# res = why(lambda x: x % 2 == 0, spisok)
# print(res)
# ==========================================================================
res = map(int, spisok)  
res = filter(lambda x: x % 2 == 0, spisok)
res = list(map(lambda x : (x, x**2), res))
print(res)
# ==========================================================================

# def prod(a):
#     return a * a

# def math(op, a):
#     print(op, a)
    
# for i in range(len(spisok)) :
#     if spisok[i] % 2 == 0 :
#         spisok2.append(f'{spisok[i]}, {prod(spisok[i])}')
#         # spisok2.append(f'{spisok[i]}, {spisok[i]*spisok[i]}')
# print(spisok2)