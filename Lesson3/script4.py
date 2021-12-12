#!/usr/bin/python3
#Написать скрипт решения квадратного уравнения
#С обработкой отрицательного дискриминанта
#Коэффициенты являются комплексными числами

import math

print('Введите коэффициенты квадратного уравнения:')
a = complex(float(input('real of a = ')), float(input('imag of a = ')))
b = complex(float(input('real of b = ')), float(input('imag of b = ')))
c = complex(float(input('real of c = ')), float(input('imag of c = ')))

if a == 0 and b == 0 and c == 0:
    print('Все действительные числа')
elif a == 0 and b == 0 and c != 0:
    print('Корней нет')
elif a == 0 and c == 0 and b != 0:
    print('x = 0')
elif a == 0:
    print(f"x = {-c / b}")
else:
    d = pow(b, 2) - 4 * a * c
    if d == 0:
        print(f"x = {-b / 2 / a}")
    else:
        d = pow(d, 1/2)
        print(f"x1 = {(-b + d) / 2 / a}, x2 = {(-b - d) / 2 / a}")
        
