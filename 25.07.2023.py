# 7. Знакомство с map, filter и reduce (позволяют работать с коллекциями данных)
# Map
''' Например, у нас есть список чисел. Мы хотим получить новый список,
в котором каждый элемент будет возводиться в квадрат, а затем вычитаться десять.
Эту задачу можно решить через цикл, но можно через map: '''
def process_number(num): # ф-я, которую мы хотим применить к каждому элементу списка
    squared = num ** 2
    subtracted = squared - 10
    return subtracted
print(process_number(2)) # => -6

numbers = [1, 2, 3, 4, 5]
new_numbers = list(map(process_number, numbers))
print(new_numbers) # => [-9, -6, -1, 6, 15]

# Filter
''' Позволяет отфильтровать элементы коллекции на основе заданного условия и
вернуть новую коллекцию с элементами, которые удовлетворяют этому условию.
Пр.: Допустим, у нас есть список чисел, и мы хотим получить только те числа, которые больше пяти: '''
def greater_than_five(num):
    return num > 5
print(greater_than_five(1)) # => False
print(greater_than_five(7)) # => True

numbers = [2, 7, 1, 8, 4, 5]
result = list(filter(greater_than_five, numbers))
print(result) # => [7, 8]

# Reduce
from functools import reduce
''' С помощью функции reduce можно последовательно применить операции к
элементам списка,чтобы получить единственное значение.
На вход функции reduce передаются три аргумента:
    func — функция, которую мы будем применять к элементам iterable
    iterable — итерируемый объект, элементы которого мы будем обрабатывать функцией func
    initial — начальное значение, которое будет использоваться при первом вызове функции func

Допустим, у нас есть список чисел, и мы хотим получить их сумму и произведение: '''
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers, 0)
print(result) # => 15

result = reduce(multiply, numbers, 1)
print(result) # => 120

# Упражнение:
def filter_map(function, iterable):
    result = []
    for i in iterable:
        if function(i)[0]:
            r = function(i)[1]
            result.append(r)
    return result
