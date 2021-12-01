#!/usr/bin/python3
n = int(input('Введите кол-во элементов списка = '))
print('Введите элементы списка (через Enter)')
l = list()
for i in range(n):
    l.append(input())
for i in range(len(l) - 1):
    for j in range(len(l) - 2, i - 1, -1):
        if l[j] > l[j + 1]:
            t = l[j]
            l[j] = l[j + 1]
            l[j + 1] = t
print(l)