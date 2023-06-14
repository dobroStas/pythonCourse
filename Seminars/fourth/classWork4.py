# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()




# .split() - позволяет одним вводом формировать списки; пробелы как разделители

# text = 'a a a b c a a d c d d'
# myList = text.split()
# dict = {}
# count = str()
# for letter in myList:
#     if letter in dict.keys():
#         dict[letter] += 1
#         count += f'{letter}_{dict[letter]} ' 
#     else :
#         dict[letter] = 0
#         count += f'{letter} '
# print(text)
# print(count)

# ===================================================================================

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure. So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


# text = str(" She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure . So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells").upper()
# print(set(text.split()))
# print(len((set(text.split()))))



