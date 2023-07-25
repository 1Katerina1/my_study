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


# 8. Чистые функции
# Что такое детерминированность
''' Детерминированность функций — это свойство, при котором функция всегда
возвращает один и тот же результат для одних и тех же входных данных. '''
# Пример не детерминированной функции:
import random

def get_random_number():
    return random.randint(1, 10)

# Пример детерминированной функции:
def multiply(a, b):
    return a * b

# Что такое побочные эффекты
''' Побочный эффект или side effects — это любые взаимодействия с внешней средой.
Они включают в себя изменения глобальных переменных и операции с файлами.
Например, запись в файл, чтение из файла, отправка или прием данных по сети и вывод в консоль. 
Побочные эффекты составляют одну из самых больших сложностей при разработке.
Они затрудняют логику кода и тестирование. Это приводит к большому числу ошибок.'''
# Пример функции, которая имеет побочный эффект:
def print_hello():
    print("Hello, world!")
  
# Что такое чистые функции
''' Чистые функции или pure functions — это функции, которые при вызове не влияют
на состояние программы и не имеют побочных эффектов. Они возвращают значения только
на основе входных аргументов и не изменяют их. '''
# Примеры чистых функций в Python:
def add_numbers(x, y):
    return x + y

def multiply_numbers(x, y):
    return x * y

def is_even(x):
    return x % 2 == 0

# Что такое грязные функции
''' Грязные ф-ии - могут изменять состояние программы или взаимодействовать с внешними системами, такими как базы данных или веб-сервисы. '''
# Функции, которые изменяют глобальные переменные:
count = 0

def increment():
    global count
    count += 1
    return count

increment()  # => 1
increment()  # => 2
print(count) # => 2
''' В этом примере функция increment() увеличивает значение
глобальной переменной count на единицу при каждом вызове.  '''

# Функции, которые изменяют аргументы
def append_list(my_list, element):
    my_list.append(element)
    return my_list

a = [1, 2, 3]
print(append_list(a, 4)) # => [1, 2, 3, 4]
print(a) # => [1, 2, 3, 4]

# Функции, которые работают с файлами
def write_file(text):
    with open("test.txt", "w") as file:
        file.write(text)

write_file("Hello, world!") # функция записывает строку в файл

# Функции, которые имеют побочный эффект вывода на экран
def print_and_return(value):
    print(value)
    return value

# Упражнение:
def say_True_or_False(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1

    if counter == 2:
        return True
    return False


def say_prime_or_not(num):
    print('yes' if say_True_or_False(num) else 'no')
