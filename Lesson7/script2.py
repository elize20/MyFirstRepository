#С помощью библиотеки numpy создать массив 3х3 со случайными
#значениями, вывести его. Транспонировать его и вывести

#Необходимые модули содержаться в файле requirements.txt
import numpy as np

matrix = np.random.randint(0, 100, (3, 3))
print(f"Матрица:\n{matrix}")
print(f"Транспонированная матрица:\n{matrix.transpose()}")