"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке 
возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств."""

# print("Введите количество элементов первого множества: " )
# n = int(input())
# print("Введите количество элементов второго множества: " )
# m = int(input())
# a = set()
# b = set()
# print("Введите элементы первого множества: " )
# for i in range(n):
#     a.add(int(input()))
# print("Введите элементы второго множества: " )
# for i in range(m):
#     b.add(int(input()))
# res = a.intersection(b)
# res = list(res)
# for i in res:
#     for i in range(len(res) - 1):
#         if res[i + 1] < res[i]:
#             t = res[i + 1]
#             res[i + 1] = res[i]
#             res[i] = t
# print(f"Числа, встречающиеся в обоих множествах: {res}")

"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только 
по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте 
выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля 
и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
"""
# print("Сколько кустов растет на грядке: ")
# n = int(input())
# list = []
# k = 3
# max = 0
# print("Введите урожайность кустов: ")
# for i in range(n):
#     list.append(int(input()))

# for i in range(k-1):
#     list.append(list[i])

# max = 0
# max_kust = ()
# sum = 0
# for i in range(n):
#     sum = list[i] + list[i + 1] + list[i + 2]
#     if sum > max:
#         max = sum
#         max_kust = (list[i], list[i + 1], list[i + 2])

# print(f"Будем собирать кусты с урожайностью: {max_kust}")
# print(f"Всего соберем: {max}")
    




    


