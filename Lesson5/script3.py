#!/usr/bin/python3

def func(n):
    if n < 2:
        return n
    else:
        return func(n-1) + func(n-2)

s = input('Введите номер числа Фибоначчи = ')
if not s.isdigit():
    print('Это должно быть целое неотрицательное число')
else:
    print(f"Число = {func(int(s))}")
