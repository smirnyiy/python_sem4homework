# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint

k = int(input('Введите степень К: '))
for i in range(k, 0, -1):
	factor = randint(1, 100)
	if factor ==0:
		continue
	elif factor == 1:
		factor = ''
	else:
		factor=f'{factor}*x^{i} + ' if i != 1 else f'{factor}*x +'
	print(factor, end='')

print(f'{randint(1,100)} = 0')