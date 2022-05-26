# Вариант 1
# Удалить в списке все числа, которые повторяются более двух раз.
# Найти подмножество данного множества чисел такое, что сумма его элементов равна заданному числу.


import random
from collections import Counter

# n = int(input("введите размер списка чисел :"))
numlist = [random.randint(0, 10) for _ in range(int(input("введите размер списка чисел :")))]
print(f'исходный список {numlist}')

newlist = []
nums_to_del = []
counter = Counter(numlist)
#print(counter)
for k, v in counter.items():
    if v > 2:
        nums_to_del.append(k)
if len(nums_to_del) < 1:
    print('нет чисел для удаления')
else:
    print(f'эти числа будут удалены из списка  {nums_to_del}')

for i in range(len(numlist)):
    if numlist.count(numlist[i]) < 3:
        newlist.append(numlist[i])
print(f'новый список после удаления {newlist}')


# second tart
x = int(input("введите заданное число :"))
r = 1
f = 0
for i in range(len(newlist) - 1):
    for j in range(r, len(newlist)):
        if newlist[i] + newlist[j] == x:
            print(f'подмножество данного множества   из 2-х чисел : {newlist[i]}, {newlist[j]}')
            print(f'их сумма равна {newlist[i] + newlist[j]}')
            f += 1
    r += 1
if f == 0:
    print('нет такого подмножества')
