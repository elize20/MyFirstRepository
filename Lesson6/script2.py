#!/usr/bin/python3
def min(a, b):
    try:
        if a < b:
            return a
        else:
            return b
    except TypeError:
        print('Это должны быть действительные числа')

try:
    with open('input1.txt') as f:
        text = f.read()
except FileNotFoundError:
    print('Файл не найден')
    quit()

l = text.strip().split(' ')
rez = True
kol = 0
for str in l:
    kol += 1
    if not str.isdigit():
        rez = False
        print('Неверные данные в файле')
if kol != 3:
    rez = False
    print('Должно быть 3 числа')
if rez == True:
    c = int(l[0]) // 2
    h = int(l[1]) // 6
    o = int(l[2])
    minKol = min(min(c, h), o)
    with open('output1.txt', 'w') as f:
        f.write(f"Максимальное кол-во молекул спирта = {minKol}")
    
