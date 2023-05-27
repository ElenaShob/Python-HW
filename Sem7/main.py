"""
Задача 47. Есть код, который мы не хотим менять:
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 13, 23 ,29]
transformed_values = list(map(tramsformation, values))

Единственный способ взаимодействия с кодом написать функцию transformation.
Однако вы поняли, что для текущей задачи вам не нужно никак преобразовывать список значений, а нужно 
его получить как есть.
Напишите такое лямбда-выражение transformation, что бы transformed_values получился копией values. 
Ввод:
values = [2, 3, 5, 7, 11, 13, 17, 13, 23 ,29]
transformed_values = list(map(tramsformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
Вывод:
ок
"""
# tramsformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 13, 23 ,29]
# transformed_values = list(map(tramsformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

"""
Задача 49. Планеты вращаются вокруг звезд по эллитическим орбитам. Назовем самой далекой планетой, ту орбита которой имеет
самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет тУ, по
которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы занете, что у вашей звезды таких планет нет, зато искусственные спутники
были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты.
Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi * a *b,
где a и b - длины полуосей эллипса.  При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага:
сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такою площадь. Гарантируется, что самая далекая планета
ровно одна.
ВВод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
Вывод:
2.5 10
"""
# from math import pi

# def find_farthest_orbit(list_of_orbits):
#     list1 = [i for i in list_of_orbits if i[0] != i[1]] 
#     list_s = [pi + i[0] + i[1] for i in list1]
#     max_s = list_s.index(max(list_s)) # index выводит индекс элемента, max ищет максимальное в списке
#     return list1[max_s]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

"""
Задача 51
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, 
и возвращают True, если это так. Если значение характеристики для разных объектов оьличается - то False. Для пустоко набора объектов, функция 
должна возвращать True. Аргумент characteristic - это функция, котораяя принимает объект и вычисляет его характеристику.
Ввод:
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
Вывод:
same
"""
# def same_by(characteristic, object):
#     result = True
#     list1 = [characteristic(x) for x in object]
#     for i in range(len(list1) - 1):
#         if list1[i] !=list1[i + 1]:
#             result = False
#     return result
    
# values = [0, 3, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')



data = input()
data = list(map(str, data.split()))
print(data)
glas = ['а', 'о', 'у', 'и', 'е', 'ы', 'э', 'ю', 'я']

for i in data:
    count = 0
    for j in i:
        if j in glas:
            count += 1


print(count)

# def print_operation_table(operation, num_rows, num_columns):
        
#     for i in range(1, num_columns + 1):
#         list1 = list()
#         for j in range(1, num_rows + 1):
#             list1.append(operation(i, j))
#         print(*list1)
   
# print_operation_table(lambda x, y: x * y, 6, 6)