'''Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.'''
'''Вариант 1. Решение, когда остаются только одно вхождение элемента в список
Например [1, 2, 3, 4, 3, 2, 1]  -  {1, 2, 3, 4};  [1, 1, 2, 0, -1, 3, 4, 4] - {0, 1, 2, 3, 4, -1}'''

s = input('Введите элемента списка через пробел: ')
inputList = list(map(int, s.split()))

print(inputList)

ost = set(inputList)                                #Формирование искомого списка

print('Cписок неповторяющихся элементов исходной последовательности будет равен', ost)