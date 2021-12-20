#!/usr/bin/python3
#Написать скрипт решения квадратного уравнения
#Если все действительные числа, то return 1
#Если корней нет, то return 0

import math

def func(a, b, c):
    l = list()
    if a == 0 and b == 0 and c == 0:
        return 1
    elif a == 0 and b == 0 and c != 0:
        return 0
    elif a == 0 and c == 0 and b != 0:
        l.append(0)
        return l
    elif a == 0:
        l.append(-c / b)
        return l
    else:
        d = pow(b, 2) - 4 * a * c
        if d < 0:
            return 0
        elif d == 0:
            l.append(-b / 2 / a)
            return l
        else:
            d = math.sqrt(d)
            l.append((-b + d) / 2 / a)
            l.append((-b - d) / 2 / a)
            return l