# Python: Функции
# 6. Функции высшего порядка
# Объекты первого класса
''' В Python функции - это объекты первого класса: их можно передавать в качестве
аргументов другим функциям, возвращать как значения из других функций и
хранить в переменных или структурах данных как любой другой объект. '''
def hello(name):
    print(f'Hello, {name}!')
greeting_function = hello 
# присваиваем функцию hello переменной greeting_function и далее вызываем ее с аргументом.
greeting_function('Kate') # => Hello, Kate!

''' Пример с передачей функции в качестве аргумента другой функции: '''
def apply_function(numbers, function):
    results = []
    for number in numbers:
        result = function(number)
        results.append(result)
    return results
def square(number):
    return number ** 2
numbers = [2, 7, 10, 0, -1]
squared_numbers = apply_function(numbers, square)
print(squared_numbers)
# => [4, 49, 100, 0, 1]

''' Объекты первого класса также позволяют возвращать функции из другой функции: '''
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times_2 = make_multiplier(2)
times_3 = make_multiplier(3)

print(times_2(5)) # 10
print(times_3(5)) # 15

# Функции высшего порядка
''' Функции, которые принимают другие функции в качестве аргументов и/или возвращают
функции в качестве результатов, называются функциями высшего порядка или ФВП.  '''
def repeat(func, n):
    for i in range(n):
        func()

def hello():
    print("Hello, world!")

repeat(hello, 3)
# => Hello, world!
# => Hello, world!
# => Hello, world!

def double(function):
    def inner(argument):
        return function(function(argument))
    return inner

def multiply_by_five(x):
    return x * 5

print(double(multiply_by_five)(3))
# 75

''' Одним из полезных применений функций высшего порядка является
использование их для определения анонимных функций — лямбда-функций. '''

# Лямбда-функции
''' В Python лямбда функция — это небольшая анонимная функция, которая может быть
определена без имени. Лямбда-функции часто используются там, где требуется небольшая, одноразовая функция.
Синтаксис для определения лямбда-функции в Python следующий: '''
lambda arguments: expression
''' Здесь arguments — это список входных аргументов функции, который разделен запятыми.
А expression — это тело функции, значение которой возвращает лямбда-функция. 
Например, лямбда-функция, которая принимает два аргумента и возвращает их сумму,
может быть определена следующим образом: '''
sum = lambda x, y: x + y
''' Затем лямбда-функцию можно вызывать как любую другую функцию: '''
result = sum(2, 3)
print(result)
# 5
# Возведение в квадрат каждого элемента списка:
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, numbers)
print(list(squares))
# [1, 4, 9, 16, 25]

# Упражнение:
def get_first_name(First_Name_Last_Name):
    name = ''
    for letter in First_Name_Last_Name:
        if letter != '_':
            name += letter
        else:
            return name


def sort_by(key, users):
    copy_users = users[:]
    return sorted(copy_users, key=key)
