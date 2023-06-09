'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  
строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1
'''
# print("Введите количество элементов в массиве: ")
# n = int(input())
# list = []
# for i in range(n):
#     print("Введите элемент массива: ")
#     list.append(int(input()))
# print("Введен массив: ")
# print(list)
# print("Введите искомое число: ")
# x = int(input())
# count = 0
# for i in range(n):
#     if list[i] == x:
#         count += 1
# print(f"Число {x} встречается {count} раз.")

"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  
строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
    
"""
# print("Введите количество элементов в массиве: ")
# n = int(input())
# list = []
# for i in range(n):
#     print("Введите элемент массива: ")
#     list.append(int(input()))
# print("Введен массив: ")
# print(list)
# print("Введите искомое число: ")
# x = int(input())
# min_pol = x
# min_otr = x * -1

# for i in list:
#     if i - x >= 0 and i - x <= min_pol:
#         min_pol = i - x
#     elif i - x < 0 and i - x > min_otr:
#         min_otr = i - x

# if i - x == 0:
#     print(i)
     
# elif min_pol == min_otr * -1:
#     print(min_pol + x, min_otr + x)
# elif min_pol > min_otr * - 1:
#     print(min_otr + x)
# else:
#     print(min_pol + x)


"""
Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом 
очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; 
K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, 
 что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*

ноутбук
    12
"""
# dict = {1: "A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т", 2: "D, G, Д, К, Л, М, П, У", \
#        3: "B, C, M, P, Б, Г, Ё, Ь, Я", 4: "F, H, V, W, Y, Й, Ы", 5: "K, Ж, З, Х, Ц, Ч", \
#        8: "J, X, Ш, Э, Ю", 10: "Q, Z, Ф, Щ, Ъ"}
# print("Введите слово: ")
# text = input()
# text = text.upper()
# list_res = []
# sum = 0
# for i in text:
#     for (k, v) in dict.items():
#         if i in v:
#             list_res.append(k)
# for i in list_res:
#     sum += i
# print(sum)



