# 1.	В матрице найти номер строки, сумма чисел в которой максимальна.

from random import randrange, random
import random
import numpy as np

rows = int(input("введите количество строк матрицы :"))
columns = int(input("введите количество столбцов матрицы :"))
arr = []
for i in range(rows):
    cols = []
    for j in range(columns):
        cols.append(random.randint(-30, 30))
    arr.append(cols)
    print(cols, '     | sum of row is ', sum(cols))
# print(arr)
print('***************************\n')
print('checking and finding')
arr = np.array(arr)
print(arr)
index_of_maxSumRow_list = []
for i in range(len(arr)):
    index_of_maxSumRow_list.append(sum(arr[i]))
print('номер строки, сумма чисел в которой максимальна  -- №', index_of_maxSumRow_list.index(max(index_of_maxSumRow_list))+1)

