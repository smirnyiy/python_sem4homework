# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


list = list(map(int, input('Введите числа через пробел: ').split()))
print(f'Список из введенных чисел: {list}')

list_without_repeat = []
[list_without_repeat.append(i) for i in list if i not in list_without_repeat]
print(f'Список без повторяющих элементов: {list_without_repeat}')