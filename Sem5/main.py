"""
Задача 31. Найти N-e число Фибоначчи
а0 = 0, а1 = 1, аК = аК-1 + аК-2 (k>1)
Input 7
Output 8
"""

# def find_fib(n):
#     if n in [1, 2]:
#         return 1
#     if n == 0:
#         return 0
#     return find_fib(n - 1) + find_fib(n - 2)

# n = int(input())
# print(find_fib(n - 1))

"""
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные - на минимальные.
Input 5 - 1 3 3 3 4
Output 1 3 3 3 1"""


# n = int(input())
# list = []
# for i in range(n):
#     list.append(int(input()))
# min = min(list)
# max = max(list)

# for i in range(n):
#     if list[i] == max:
#        list[i] = min
# print(list)

"""
Задача 35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым. Простое число - 
это число, которое делится на 1 и на само себя.
Input 5
Output yes"""
"""Это мое решение:"""
# def simple(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return("no")
#     return("yes")
"""Решение преподавателя:"""
# def prime(n):
#     flag = True
#     i = 2
#     while i < n and flag:
#         if n % i == 0:
#             flag = False
#         i += 1
#     if flag:
#         return "yes"
#     else:
#         return "no"

# a = int(input())
# print(simple(a))

"""
Задача 37. Дано натуральное число N и последовательность из N элементов. 
Требуется вывести эьту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы(даже для ввода и вывода).
Input 2 - 3 4
Output 4 3
"""

# def f(n):
#     if n == 0:
#         return ''
#     k = int(input())
#     return f(n - 1) + f"{k}"

# n = int(input())
# print(f(n))

"""
"""


