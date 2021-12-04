#!/usr/bin/python3

def func(pswd):
    rez = False
    for s in pswd:
        if s in '0123456789':
            rez = True
            break
    return rez and len(pswd) >= 6 and not pswd.isdigit() and pswd.lower().find('password') == -1

str = input('Введите пароль: ')
print(f"Пароль подходит? = {func(str)}")