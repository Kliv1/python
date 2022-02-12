1
def sal():
    try:
        time = float(input('Выработка в часах '))
        salary = int(input('Ставка '))
        bonus = int(input('Премия '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')
sal()

2
in_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_list = [number for i, number in enumerate(in_list) if i > 0 and in_list[i] > in_list[i - 1]]
res_list = [num1 for num1, num2 in zip(in_list[1:], in_list[:-1]) if num1 > num2]
print(res_list)

3
print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

4
list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list2 = [el for el in list1 if list1.count(el) == 1]
print(list2)

5
from functools import reduce

def my_func(el_p, el):
    return el_p * el

print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

6
from itertools import count
for el in count(int(input('Введите стартовое число '))):
    if el > 10:
        break
    else:
        print(el)

from itertools import cycle
с = 0
my_list = ['ABC', 123, None]
for el in cycle(my_list):
    if с > 10:
        break
    print(el)
    с += 1

7
from itertools import count
from math import factorial
def factgen():
    for el in count(1):
        yield factorial(el)
gen = factgen()
n = 0
for elem in gen: #цикл выводит только первые 6 чисел
    if n < 6:
        print(elem)
        n += 1
    else:
        break