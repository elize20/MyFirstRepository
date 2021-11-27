#!/usr/bin/python3

import math
print('Введите коэффициенты квадратного уравнения:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a == 0 and b == 0 and c == 0:
    print('Все действительные числа')
elif a == 0 and b == 0 and c != 0:
    print('Корней нет')
elif a == 0 and c == 0 and b != 0:
    print('x = 0')
elif a == 0:
    print('x = %f' % (-c / b))
else:
    d = pow(b, 2) - 4 * a * c
    if d < 0:
        print('Действительных корней нет')
    elif d == 0:
        print('x = %f' % (-b / 2 / a))
    else:
        d = math.sqrt(d)
        print('x1 = %f, x2 = %f' % ((-b + d) / 2 / a, (-b - d) / 2 / a))
