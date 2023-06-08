from data_create import surname_data, phone_data, adress_data, name_data
from data_change import change_variant

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{adress}\n\n"
    f"2 вариант: \n"
    f"{name};{surname};{phone};{adress}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("введите число: "))
    
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{adress}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{adress}\n")


def print_data():
    print('Вывожу данные из 1 файла: \n')
        
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            data_first_list = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_list.append(''.join(data_first[j:i+1]))
                    j = i
            for i in enumerate(data_first_list):
                print(*i)

    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        for i in enumerate(data_second):
            print(*i)


def change_data():
    var = int(input("В каком файле заменить данные в 1 или 2: "))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("введите число: "))
    number = int(input("Введите номер записи, которую надо изменить: "))

    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            change_element = list()
        while number * 5 > len(data_first) - 1:
            print("Неправильный ввод")
            number = int(input("Введите номер записи, которую надо изменить: "))
        for i in range(number * 5, number * 5 + 5):
            change_element.append(data_first[i])
        change_list_new = change_variant(change_element) 

        data_first_new = list()
        for i in range(0, number * 5):
            data_first_new.append(data_first[i])
        for i in range(5):
            data_first_new.append(change_list_new[i])
        for i in range(number * 5 + 5, len(data_first)):
            data_first_new.append(data_first[i])
        print(data_first_new)
        # with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
        #     f.writelines(data_first_new)

    if var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
        while number > len(data_second) - 1:
            print("Неправильный ввод")
            number = int(input("Введите номер записи, которую надо изменить: "))
        change_element = data_second[number]
        change_element_new = change_variant(change_element)
        data_second_new = list()
        for i in range(0, number):
            data_second_new.append(data_second[i])
        data_second_new.append(change_element_new)
        for i in range(number + 1, len(data_second)):
            data_second_new.append(data_second[i])
        print(data_second_new)
        # with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
        #     f.writelines(data_second_new)
    
    print(f"Запись {number} успешно изменена")

change_data()


def delit_data():
    var = int(input("В каком файле удалить данные в 1 или 2: "))
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("введите число: "))
    number = int(input("Введите номер записи, которую надо удалить: "))

    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            while number * 5 > len(data_first) - 1:
                print("Неправильный ввод")
                number = int(input("Введите номер записи, которую надо удалить: "))
            data_first_new = list()
            for i in range(0, number * 5):
                data_first_new.append(data_first[i])
            for i in range(number * 5 + 5, len(data_first)):
                data_first_new.append(data_first[i])
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_first_new)
            
    if var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            while number > len(data_second) - 1:
                print("Неправильный ввод")
                number = int(input("Введите номер записи, которую надо удалить: "))
            data_second_new = list()
            for i in range(0, number):
                data_second_new.append(data_second[i])
            for i in range(number + 1, len(data_second)):
                data_second_new.append(data_second[i])
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_second_new)
    print(f"Запись {number} успешно удалена")


           
                
     
