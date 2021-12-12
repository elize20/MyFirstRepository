#!/usr/bin/python3
#Написать функцию, принимающую строку-пароль. Функция должна
#проверить подходит ли этот пароль условиям и вернуть True -
#если подходит; False - если не подходит.

def func(pswd):
    '''Проверка правильности пароля
    pswd - аргумент - пароль
    Возвращает True или False
    '''
    rez = False
    for s in pswd:
        if s.isdigit():
            rez = True
            break
    return rez and len(pswd) >= 6 and not pswd.isdigit() and pswd.lower().find('password') == -1

str = input('Введите пароль: ')
print(f"Пароль подходит? = {func(str)}")