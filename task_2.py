"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
# sqlite, postgres, db_api, orm

import hashlib
from uuid import uuid4


def func_cash(salt):
    password = input('Введите пароль: ')
    return hashlib.sha256(f'{password}'.encode() + salt.encode()).hexdigest()


def check_password():
    salt = uuid4().hex
    res_1 = func_cash(salt)
    file = open('pwd_date.txt', 'w')
    file.write(res_1)
    print(f'В базе хранится строка: {res_1}')
    file.close()
    check = open('pwd_date.txt', 'r')
    res_2 = func_cash(salt)
    if res_2 == check.read():
        return 'Вы ввели правильный пароль!'
    else:
        return 'Вы ввели неверный пароль!'


print(check_password())