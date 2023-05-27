"""
Задача 39. Даны два массива чисел. Требуется вывести те элементы первого массива ( в том порядке, в каком они
идут в первом массиве), которых нет во втором массиве. Пользователь вводит число N - кол-во элементов в первом массиве,
затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы
второго массива.
Ввод:
7
3 1 3 4 2 4 12
6
 15 43 1 15 1
 (каждое число вводится с новой строки)
 Вывод
 3 3 2 12"""

# n = int(input())
# list_1 = []
# for i in range(n):
#     list_1.append(int(input()))
# m = int(input())
# list_2 = []
# for i in range(m):
#     list_2.append(int(input()))

# count = 0
# for i in range(n):
#     for j in range(m):
#         if list_1[i] == list_2[j]:
#             count +=1
#     if count == 0:
#         print(list_1[i])

"""
Задача 41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном масссиве определит
количество элементов, у которых оба соседних элемента меньше данного. Сначала вводится число N - количество
элементов  в массиве, далее элементы массива. Массив состоит из целых чисел.
Ввод:
5
1 2 3 4 5
Вывод
0
Ввод
5
1 5 1 5 1
Вывод
2"""

# n = int(input())
# list = []
# for i in range(n):
#     list.append(int(input()))
# count = 0
# for i in range(1, n-1):
#     if list[i + 1] < list[i] > list[i - 1]:
#         count += 1
# print(count)

"""
Задача 43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что
любые эва элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных строках.
Ввод
1 2 3 2 3
Вывод
2
"""
# n = int(input())
# list = []
# for i in range(n):
#     list.append(int(input()))
# print(list)
# count = 0
# for i in range(n):
#     for j in range (i + 1, n):
#         if list[i] == list[j]:
#             count += 1
            
# print(count)

""" Задача 45. Два различных натуральных числа n и m называются дружественными, если сумма делителей числа
n (вклюяая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 - дружественные числа.
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит число k, не 
превосходящее 10 в 5 степени. Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит  k.
Пары необходимо выводить по одной в строке, разделяя пробелами Каждая пара должна быть выведена только один раз
(перестановка чисел новую пару не дает).
Ввод
300
Вывод
220 284 """

# k = int(input())
# list1 = list()

# for i in range(k):
#     summa = 0
#     for j in range(1, i//2 + 1):
#         if i % j == 0:
#             summa += j
#     list1.append(tuple([i, summa]))

# for i in range(len(list1)):
#     for j in range(i, len(list1)):
#         if i != j and list1[i][0] == list1[j][1] and list1[i][1] == list1[j][0]:
#             print(*list1[i])
   
