#!/usr/bin/python3

def func(*arg):
    sum = 0
    try:
        for el in arg:
            sum += el
    except:
        print('Аргументы должны быть числами')
        sum = -1
    return sum

print(func(1,2,3,4))

