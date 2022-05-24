# Вариант 1
# Удалить в списке все числа, которые повторяются более двух раз.
# Найти подмножество данного множества чисел такое, что сумма его элементов равна заданному числу.


import random
from collections import Counter

# n = int(input("введите размер списка чисел :"))
numlist = [random.randint(0, 99) for _ in range(int(input("введите размер списка чисел :")))]
print(f'исходный список   {numlist}')

newlist = []
counter = Counter(numlist)
# print(counter)
for k, v in counter.items():
    if v == 1:
        newlist.append(k)
print(f'список без повторных чисел {newlist}')

x = int(input("введите заданное число :"))
r = 1
f = 0
for i in range(len(numlist) - 1):
    for j in range(r, len(numlist)):
        if numlist[i] + numlist[j] == x:
            print(f'подмножество данного множества   из 2-х чисел : {numlist[i]}, {numlist[j]}')
            print(f'их сумма равна {numlist[i] + numlist[j]}')
            f += 1
    r += 1
if f == 0:
    print('нет такого подмножества')
