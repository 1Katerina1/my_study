# 9. Встроенные map, filter, reduce
# functools.reduce
# Объявление функции reduce :
from functools import reduce
reduce(function, sequence[, initial]) -> value

''' 
    function — функция, которая будет применена к элементам коллекции для их объединения
    sequen объявление функции reduce ce — коллекция данных, которую нужно объединить
    initial (опционально) — начальное значение аккумулятора,
    которое будет использовано в качестве первого аргумента при объединении
    (Если мы не указываем initial, то функция reduce будет использовать
    в качестве начального значения первый элемент передаваемой коллекции sequence. )
'''
# Пример работы функции functools.reduce:
from functools import reduce

numbers = [2, 3, 8]

def get_maximum(first_num, second_num):
    return first_num if first_num > second_num else second_num

print(reduce(get_maximum, numbers, 10))  # => 10
print(reduce(get_maximum, numbers))  # => 8
''' Функция, которая передается в качестве первого аргумента в reduce,
должна принимать два аргумента и возвращать одно значение. '''

# filter
# Пример работы функции filter:
numbers = [2, 3, 8, 15, 34, 42]

def is_even(num):
    return num % 2 == 0

print(filter(is_even, numbers))  # => <filter object at ...>
print(list(filter(is_even, numbers)))  # => [2, 8, 34, 42]
''' Функция, которая передается в качестве первого аргумента в filter,
должна принимать один аргумент и возвращать значение True или False.  '''

# map
# Вот пример применения функции map к паре источников:
from operator import mul

print(map(mul, "abc", [3, 5, 7]))  # => <map object at ...>
print(list(map(mul, "abc", [3, 5, 7])))  
# => ['aaa', 'bbbbb', 'ccccccc']

''' !!!Когда мы используем встроенные функции высшего порядка, следует руководствоваться следующим правилом:
применяемые с их помощью функции по возможности должны быть чистыми!!! 
Если вы видите, что в ФВП просится не чистая функция — перепишите на цикл. '''

# Упражнение:
from operator import getitem
from functools import reduce
from operator import truth


def keep_truthful(iterable_source):
    return filter(truth, iterable_source)


def function_abs_sum(a, b):
    return sum([abs(a), abs(b)])


def abs_sum(iterable_numbers):
    return reduce(function_abs_sum, iterable_numbers, 0)


def walk(dic, iterable_string):
    copy = dic.copy()
    for i in iterable_string:
        copy = getitem(copy, i)
    return copy
