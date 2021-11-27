#!/usr/bin/python3

x = 0
y = 0
print('Стоп-слово: exit')
while True:
    s = input('Введите направление персонажа: left, right, up, down\n')
    if s == 'exit':
        break
    kol = int(input('На сколько позиций: '))
    print('%s (%f, %f)' % ('Начальное значение:', x, y))
    if s == 'left':
        x -= kol
    elif s == 'right':
        x += kol
    elif s == 'up':
        y += kol
    elif s == 'down':
        y -= kol
    print('%s (%f, %f)' % ('Новое значение:', x, y))
print('end')

