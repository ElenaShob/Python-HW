'''Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
 с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 '''


# def f(a, b):
#     sum = 0
#     if b == 1:
#         return a
#     sum += a * f(a, b-1)
#     return sum

# a = int(input())
# b = int(input())
# print(f(a, b))

""" Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4 """
# def f(a, b):
#     if b == -a:
#         return 0
#     sum = 0
#     sum += 1 + f(a, b-1)
    
#     return sum

# a = int(input())
# b = int(input())
# print(f(a, b))