from logger import input_data, print_data, delit_data, change_data

def interface():
    print("Добрый день! Вы попали на специальный бот-справочник от GeekBrains! \n1 - запись данных \n2 - вывод данных" 
        "\n3 - изменение данных \n4 - удаление данных")
    command = int(input("Введите число: "))

    while 1 > command > 4:
        print("Неправильный ввод")
        command = int(input("введите число: "))

    if command == 1: 
        input_data()
    if command == 2:
        print_data()
    if command == 3:
        change_data()
    elif command == 4:
        delit_data()

