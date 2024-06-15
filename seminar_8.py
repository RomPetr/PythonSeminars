"""
# Телефонный справочник
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
second_name, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
   записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
"""
from csv import DictReader, DictWriter


def get_info():
    first_name = "Иван"
    second_name = "Иванов"
    phone_number = "89143092345"
    return [first_name, second_name, phone_number]


def create_file(file_name):
    with open(file_name, 'w', encoding='utf8') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()


def write_file(file_name):
    res = read_file(file_name)
    user_data = get_info()
    new_obj = {'first_name': user_data[0], 'second_name': user_data[1], 'phone_number': user_data[2]}
    res.append(new_obj)
    with open(file_name, 'w', encoding='utf8') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()
        f_w.writerows(res)


def read_file(file_name):
    with open(file_name, encoding='utf8') as data:
        f_r = DictReader(data)
        return list(f_r)  # вернет список словарей

