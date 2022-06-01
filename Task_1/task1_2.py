# Вариант 2
# Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
# Найдите минимальный по модулю элемент списка.

from random import randrange

# список со случ числами от -10 до 50
numlist = [randrange(-20, 20) for i in range(int(input("введите размер списка чисел :")))]
print(f'исходный список {numlist}')

list_1 = list(map(lambda x: x if x % 2 != 0 else False, numlist))
print(list_1)
print(f'наибольший нечетный элемент {max(list_1)}')

list_2 = list(map(lambda x: abs(x), numlist))
print(list_2)
print(f'минимальный по модулю элемент списка {min(list_2)}')



