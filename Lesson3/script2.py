#!/usr/bin/python3
#Написать скрипт для движения персонажа влево, вправо,
#вверх и вниз по координатам x и y по координатной оси,
#начальная позиция персонажа (0;0)
#Скрипт бесконечный (каждый раз спрашивается куда движение и
#выводится результат). Обязательно стоп-слово

#x и y - координаты персонажа
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

