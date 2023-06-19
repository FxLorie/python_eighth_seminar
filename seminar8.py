# Задача №49. Создать телефонный справочник с возможностью импорта
# и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска
# определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def read_csv(filename: str):    ## возвращает данные в формате списка из словарей
    data = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_csv(filename: str, data: list):   ## запись в файл с нуля
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def print_result(data: list):   ## вывод всех значений в консоль
    for dict in data:
        print(*dict.values())
        
def get_search_name():          ## ввод имени или фамилии
    return input('Введите искомое имя или фамилию: ').lower()

def find_by_name(data: list, name: str): ## поиск по имени или фамилии
    for dict in data:
        if name in dict['Фамилия'].lower() or name in dict['Имя'].lower():
            value = list(dict.values())
            return value
    return 'Такого имени в справочнике нет'
                                
def get_search_number():        ## ввод номера телефона
    return input('Введите искомый номер: ')

def find_by_number(data: list, number: str): ## поиск по номеру телефона
    for dict in data:
        if number in dict['Телефон']:
            value = list(dict.values())
            return value
    return 'Такого телефона в справочнике нет'

def get_new_user():             ## ввод данных о новом человеке
    dict = {}
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    for item in fields:
        dict[item] = (input(f'{item}: '))
    return dict
    
def add_user(data: list, new_text: dict):  ## добавление нового человека в справочник
    data.append(new_text)
        
def get_file_name():            ## ввод имени файла в который хотим сохранить данные
    return input('Введите имя файла: ') + '.txt'

def write_txt(filename, data):  ## сохранение файла txt
    with open(filename, 'w', encoding='utf-8') as file:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            file.write(f'{s[:-1]}\n')

def show_menu():                ## вывод главного меню
    print('1 - Вывести справочник')
    print('2 - Поиск по имени или фамилии')
    print('3 - Поиск по номеру телефона')
    print('4 - Добавить новую информацию')
    print('5 - Создать текстовый файл-справочник в формате txt')
    print('6 - Изменить информацию')
    print('7 - Выход из программы')
    i = int(input('Введите 1, 2, 3, 4, 5, 6 или 7: '))
    return i

def change_user_data(data: list, name: str):    ## изменение информации
    for dict in data:
        if name in dict['Фамилия'].lower() or name in dict['Имя'].lower():
            for keys in dict:
                old_item = dict[keys]
                new_item = input(f'Введите новое значение {dict[keys]} или нажмите enter, чтобы пропустить: ')
                if new_item == '':
                    dict[keys] = old_item
                else: dict[keys] = new_item
            return data
    return 'Такого имени в справочнике нет'

def delete_user_data(data: list, name: str):    ## удаление информации
    for dict in data:
        if name in dict['Фамилия'].lower() or name in dict['Имя'].lower():
            data.pop(data.index(dict))
            return data
    return 'Такого имени в справочнике нет'


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while (choice != 8):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('phonebook.csv', phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        elif choice == 6:
            name = get_search_name()
            change_user_data(phone_book, name)
            write_csv('phonebook.csv', phone_book)
        elif choice == 7:
            name = get_search_name()
            delete_user_data(phone_book, name)
            write_csv('phonebook.csv', phone_book)
        choice = show_menu()

work_with_phonebook()


