def min(a, b):
    '''Возвращает минимальное из двух действительных чисел'''
    try:
        if a < b:
            return a
        else:
            return b
    except TypeError:
        print('Это должны быть действительные числа')

def max(a, b):
    '''Возвращает максимальное из двух действительных чисел'''
    try:
        if a > b:
            return a
        else:
            return b
    except TypeError:
        print('Это должны быть действительные числа')

def averageValue(*args):
    '''Возвращает среднее арифметическое чисел - параметров'''
    sum = 0
    try:
        for i in args:
            sum += i
        return sum / len(args)
    except TypeError:
        print('Это должны быть числа')