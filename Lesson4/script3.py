#!/usr/bin/python3

import random
a = set({random.randint(0, 10) for i in range(5)})
b = set({random.randint(0, 10) for i in range(5)})
print(a)
print(b)
print(f"Входят одновременно в оба = {a & b}")
print(f"Входят только в первое, но не входят во второе = {a - b}")
print(f"Входят только во второе, но не входят в первое = {b - a}")
print(f"Входят в первое или во второе, но не в оба из них одновременно = {a ^ b}")