# Вариант 2
# Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
# Найдите минимальный по модулю элемент списка.


from random import randrange

# список со случ числами от -10 до 50
numlist = [randrange(-10, 20) for i in range(int(input("введите размер списка чисел :")))]
print(f'исходный список {numlist}')

list_1 = list(map(lambda x: x if x % 2 != 0 else -12, numlist))
print(list_1)
print(max(list_1))
