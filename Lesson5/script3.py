#!/usr/bin/python3

def func(n):
    assert n > 0, 'n - натуральное число!'
    if n < 3:
        return 1
    else:
        return func(n-1) + func(n-2)

s = input('Введите номер числа Фибоначчи = ')
if not s.isdigit() or s == '0':
    print('Это должно быть натуральное число')
else:
    print(f"Число = {func(int(s))}")
