#!/usr/bin/python3
#Написать функцию, преобразующую список строк в список байт кодов.
#Написать обратную функцию

import time

def decorator_log(func):
    def wrapper(arg):
        print(f"***Функция func() запущена***")
        func(arg)
        print(f"***Функция func()) завершила работу***")
    return wrapper

def decorator_time(func):
    def wrapper(arg):
        start = time.time()
        func(arg)
        print(f"Функция выполнилась за {time.time() - start} seconds")
    return wrapper

def decorator_sleep(func):
    def wrapper(arg):
        time.sleep(3)
        func(arg)
    return wrapper

@decorator_log
#@decorator_time
#@decorator_sleep
def func(s):
    '''Принимает список строк
    Возвращает список байт кодов
    '''
    try:
        l = list()
        for str in s:
            l.append(str.encode('utf-8'))
        print(f"Список байт кодов: {l}")
    except AttributeError:
        print('Список должен состоять из строк')
    except TypeError:
        print('Это должен быть список')

l = ['Hello', 'Bye', '12345', 'qwerty']
print(f"Список строк: {l}")
func(l)
