# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import Random, randint

number = int(input("Введите натуральную степень k: "))
st = ""
start = number
f = open('homework4.txt', 'w')

while start >= 0:
    num = randint(0, 100)
    if start > 1:
        st += f'{num}x^{start}'
    elif start == 1:
        st += f'{num}x'
    elif start == 0:
        st += f'{num} = 0'
    if start > 0:
        st += ' + '
    start -= 1

f.write(str(st))
f.close()

print(st)