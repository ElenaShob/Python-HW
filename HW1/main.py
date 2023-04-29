'''
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 
'''

# a = int(input())
# sum = (a % 10 + a // 10 % 10 + a // 100)
# print(sum)

'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал 
каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза 
больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
'''
# s = int(input())
# if s % 6 != 0:
#     print(-1)
# else:
#     print(s // 6, s // 6 * 4, s // 6)

'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость 
билета.

*Пример:*

385916 -> yes
123456 -> no
'''

# n = int(input())
# n1 = n // 100000 + n // 10000 % 10 + n // 1000 % 10
# print(n1)
# n2 = n // 100 % 10 + n // 10 % 10 + n % 10 
# print(n2)

# if n1 == n2:
#     print('yes')
# else:
#     print('no')

'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом 
по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
'''

# m = int(input())
# n = int(input())
# k = int(input())

# if k <= m * n and (k % m == 0 or k % n == 0):
#     print("yes")
# else:
#     print("no")