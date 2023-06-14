# # list_1 = [] # создание пустого списка
# # list_2 = list()  #создание пустого списка функцией
# # list_1 = [7, 9, 11, 13, 15, 17, 19]
# # print(list_1)  #со скобками
# # print(*list_1) #без скобок
# # print(list_1[0]) #7

# # for i in list_1 :
# #     print(i)

# # print(len(list_1))
# # list_1.append(8) # добавить элемент в конец списка
# # print(*list_1) 
# # list_1.append(76) # добавить элемент в конец списка
# # print(*list_1) 

# # list_1 = []
# # print(list_1)
# # for i in range(5) :
# #     list_1.append(i)
# #     print(list_1)


# # list_1 = [12, 7, -1, 21, 0]
# # list_1.pop() # удаление последнего элемента изи списка
# # print(list_1)    
# # print(list_1.pop()) # вывод удаленного последнего элемента

# # Удаление конкретного элемента
# # list_1 = [1, 2, 3, 4]
# # print(list_1.pop(1))
# # print(*list_1)


# # добавление элемента на нужнуу позицию
# # list_1 = [1, 2, 3, 4]
# # print(list_1.insert(2, 11))
# # print(*list_1)



# # # Срезы
# # list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(list_1[0])                  # 1
# # print(list_1[1])                  # 2
# # print(list_1[-1])                 # 10
# # print(list_1[-5])                 # 6
# # print(list_1[:])                  # 1 2 3 4 5 6 7 8 9 10
# # print(list_1[:2])                 # 1 2
# # print(list_1[5:])                 # 6 7 8 9 10
# # print(list_1[-2:])                # 9 10
# # print(list_1[2:9])                # 3 4 5 6 7 8 9 
# # print(list_1[0:len(list_1): 6])   # 1 7
# # print(list_1[::6])                # 1 7


# # # Кортеж - то же что и список, но неизменяемый

# # t = ()
# # print(type(t))  #class 'tuple'
# # t = (1)
# # print(type(t))  #class 'int'
# # t = (1,)
# # print(type(t))  #class 'tuple'


# # v = [1, 3, 5]
# # print(v)
# # print(type(v))

# # v = tuple(v)
# # print(v)
# # print(type(v))


# # # a, b, c = 1, 2, 3


# # a, b, c = v
# # print(a, b, c)


# # Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
# # В списках в качестве ключа используется индекс элемента. В словаре для определения
# # элемента используется значение ключа (строка, число).

# dictionary = {}
# # dictionary = dict()
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# # print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# # print(dictionary['left']) # ← типы ключей могут отличаться
# # print(dictionary['up']) # ↑ типы ключей могут отличаться
# # dictionary['left'] = '⇐'
# # print(dictionary['left']) # ⇐
# # print(dictionary['type']) # KeyError: 'type'
# # del dictionary['left'] # удаление элемента

# # dictionary[895] = 576576 #добавление элемента в словарь
# # print(dictionary)

# # for item in dictionary :     
# #     # print(item) # обращение ко всем ключам
# #     print('{}: {}'.format(item, dictionary[item]))
    
# # for (k,v) in dictionary.items() :
# #     print(k, v)


# # print(dictionary.items())

# # # Множества
# # # Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
# # # Одно множество может содержать значения любых типов. Если у Вас есть два множества,
# # # Вы можете совершать над ними любые стандартные операции, например, объединение,
# # # пересечение и разность. Давайте разберем их.
# # colors = {'red', 'green', 'blue'}
# # print(colors) # {'red', 'green', 'blue'}
# # colors.add('red')
# # print(colors) # {'red', 'green', 'blue'}
# # colors.add('gray')
# # print(colors) # {'red', 'green', 'blue','gray'}
# # colors.remove('red')
# # print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# # colors.discard('red') # ok

# # Операции со множествами в Python:
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}

# # Неизменяемое или замороженное множество(frozenset) — множество, с которым не будут
# # работать методы удаления и добавления.
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8}



