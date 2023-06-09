


def change_variant(change_element):
    print("Как Вы хотите изменить запись: \n1 - поменять имя \n2 - поменять фамилию "
          "\n3 - поменять номер телефона \n4 - поменять адрес ")
    change_var = int(input("Введите число: "))
     
    while 1 > change_var > 4:
        print("Неправильный ввод")
        change_var = int(input("введите число: "))
    if type(change_element) == list:
        new_el = input("Введите новое значение: ")
        change_element[change_var - 1] = new_el + "\n"
    else:
        change_el = change_element.split(';')
        new_el = input("Введите новое значение: ")
        if change_var == 4:
            change_el[change_var - 1] = new_el + '\n'
            change_element = ';'.join(change_el)
        else:
            change_el[change_var - 1] = new_el
            change_element = ';'.join(change_el)
        
    
    return(change_element)
    
           


