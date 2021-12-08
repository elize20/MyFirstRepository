#!/usr/bin/python3


def func(text, key):
    try:
        byteText = bytearray(text.encode('utf-8'))
        byteKey = bytearray(key.encode('utf-8'))
        new = bytearray(byteText)
        for i in range(len(byteText)):
            new[i] = byteText[i] ^ byteKey[i % len(byteKey)]
        return new.decode('utf-8')
    except AttributeError:
        print("Аргументы должны быть строками")

try:
    with open('input2.txt') as f:
        data = f.read()
except FileNotFoundError:
    print('Файл не найден')
    quit()

key = input('Введите ключ шифрования: ')
with open('output2.txt', 'w') as f:
    f.write(func(data, key))

#g = open('symbols.txt', 'w')
#for i in range(256):
    #g.write(f"{i} = {chr(i)}\n")
#g.close()