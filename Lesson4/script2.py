#!/usr/bin/python3

from typing import Deque


d = dict()
n = int(input('Введите кол-во элементов словаря = '))
print('Введите ключи(кодировка цвета)-значения(3 целых числа rgb) словаря')
for i in range(n):
    key = input(f"Кодировка цвета №{i} = ")
    print(f"3 числа rgb цвета №{i}")
    a = int(input())
    b = int(input())
    c = int(input())
    l = (a, b, c)
    d.update({key:l})
print(d)

