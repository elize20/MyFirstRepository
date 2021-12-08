#!/usr/bin/python3

def func(s):
    try:
        l = list()
        for str in s:
            l.append(str.encode('utf-8'))
        return l
    except AttributeError:
        print('Список должен состоять из строк')
    except TypeError:
        print('Это должен быть список')

def oppfunc(s):
    try:
        l = list()
        for bytes in s:
            l.append(bytes.decode('utf-8'))
        return l
    except AttributeError:
        print('Список должен состоять из байт кодов')
    except TypeError:
        print('Это должен быть список')


l = ['Hello', 'Bye', '12345', 'qwerty']
print('Список строк --> Список байт кодов')
print(f"Список строк: {l}")
print(f"Список байт кодов: {func(l)}")

b = [b'Hello', b'World', b'125', b'str']
print('----------------------------')
print('Список байт кодов --> Список строк')
print(f"Список байт кодов: {b}")
print(f"Список строк: {oppfunc(b)}")