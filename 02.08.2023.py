# Замыкания в Python Часть 2. Closure Python part 2 (egoroff_channel)
def average_numbers():
    numbers = []
    def inner(number):
        numbers.append(number)
        return sum(numbers) / len(numbers)
    return inner

r1 = average_numbers()
print(r1(5)) # => 5.0
print(r1(10)) # => 7.5

r2 = average_numbers()
print(r2(3)) # => 3.0


def average_numbers_2():
    numbers = []
    def inner(number):
        numbers.append(number)
        print(numbers)
        return sum(numbers) / len(numbers)
    return inner

r3 = average_numbers_2()
print(r3(10)) 
# => [10]
# => 10.0 (среднее арифметическое)

print(r3(14))
# => [10, 14]
# => 12.0

print(r3(18))
# => [10, 14, 18]
# => 14.0


# Та же задача, что и выше, только без списка:
def average_numbers_3():
    summa = 0
    count = 0
    def inner(number):
        nonlocal summa
        nonlocal count
        summa += number
        count += 1
        return summa / count
    return inner

k = average_numbers_3()
print(k(10)) # => 10.0
print(k(20)) # => 15.0
print(k(6)) # => 12.0


from datetime import datetime

def timer():
    start = datetime.now()
    def inner():
        return datetime.now() - start
    return inner
t = timer()
print(t())
print(t()) # выведет на экран разницу во времени между первым вызовом ф-ии и текущем


# Такая же ф-я, что и предыдущая, только выводит время в более удобном формате:
from time import perf_counter

def timer_2():
    start = perf_counter()
    def inner():
        return perf_counter() - start
    return inner

w = timer_2()
print(w())
print(w())


print(abs.__name__) # => abs

# Посчитаем сколько раз вызывалась ф-я:
def add(a, b):
    return a + b

def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Функция {func.__name__} вызывалась {count} раз(а).')
        return func(*args, **kwargs)
    return inner

c = counter(add)
print(c(20, 5)) # Функция add вызывалась 1 раз(а). 25
print(c(0, -5)) # Функция add вызывалась 2 раз(а). -5
print(c(0, 2)) # Функция add вызывалась 3 раз(а). 2

def mult(a, b, c):
    return a * b * c

m = counter(mult)
print(m(1, 3, 5)) # Функция mult вызывалась 1 раз(а). 15


# Декораторы в Python Часть 1. Decorator Python (egoroff_channel)
def decorator(func):
    def inner():
        print('Start decorator ...')
        func()
        print('Finish decorator ...')
    return inner

def say():
    print('Hello, World!')

say = decorator(say)
say() # Теперь при вызове say результатом ф-ии является работа самой ф-ии и декоратора
# => Start decorator ...
# => Hello, World!
# => Finish decorator ...

def buy():
    print('Buy, World!')

buy = decorator(buy)
buy()
# => Start decorator ...
# => Buy, World!
# => Finish decorator ...

# теперь ф-я будет принимать один аргумент:
def say_hello(name):
    print(f'Hello, {name}!')

def decor(func):
    def inner(n):
        print('Start decorator ...')
        func(n)
        print('Finish decorator ...')
    return inner

say_hello = decor(say_hello)
say_hello('Jhon')
# => Start decorator ...
# => Hello, Jhon!
# => Finish decorator ...

# теперь ф-я будет принимать два аргумента:
def say_hello2(name, surname):
    print(f'Hello, {name} {surname}!')

def decor(func):
    def inner(n, s):
        print('Start decorator ...')
        func(n, s)
        print('Finish decorator ...')
    return inner

say_hello2 = decor(say_hello2)
say_hello2('Sam', 'Polyvianniy')
# => Start decorator ...
# => Hello, Sam Polyvianniy!
# => Finish decorator ...

# Ф-я может принимать различное кол-во аргументов и чтобы каждый раз не изменять декоратор,
# можно использовать *args и **kwargs:
def say_hello3(name, surname, age):
    print(f'Hello, {name} {surname}! Тебе уже {age}!')

def decor(func):
    def inner(*args, **kwargs):
        print('Start decorator ...')
        func(*args, **kwargs)
        print('Finish decorator ...')
    return inner

say_hello3 = decor(say_hello3)
say_hello3('Sam', 'Polyvianniy', 27)
# => Start decorator ...
# => Hello, Sam Polyvianniy! Тебе уже 27!
# => Finish decorator ...

# Другой пример с двумя декораторами:
def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')
    return inner

def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    return inner

def SAY(name):
    print(f'Hello, {name}!')

SAY = table(header(SAY)) # но обычно ф-ии так не декорируют
SAY('Sam')
# => <table>
# => <h1>
# => Hello, Sam!
# => </h1>
# => </table>

# Декораторы принято навешивать с помощью значка '@' перед ф-ей:
@header # SAY = header(SAY)
@table # SAY = header(table(SAY))
def SAY(name):
    print(f'Hello, {name}!')

SAY('Kate')
# => <h1>
# => <table>
# => Hello, Kate!
# => </table>
# => </h1>


# Декораторы в Python Часть 2. Декоратор wraps. Decorator Python (egoroff_channel)
def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    return inner

def say():
    ''' Печатает на экран 'Hello, World!' '''
    print(f'Hello, World!')

#help(say) # => Печатает на экран 'Hello, World!'
print(say.__name__) # => say

say = table(say)
say()
# => <table>
# => Hello, World!
# => </table>

#help(say) # После декорирования ф-ии мы больше не можем обратиться к ее документации,
# а так же мы теряем ее имя:
print(say.__name__) # => inner

print('-----')
# Вот как можно решить проблему потери имени и документации:
def table2(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner

def say2():
    ''' Печатает на экран 'Hello, World!' '''
    print(f'Hello, World!')

#help(say2) # Печатает на экран 'Hello, World!'
print(say2.__name__) # => say2

say2 = table2(say2)
print(say2.__name__) # => say2

print('-----')
# Есть второй способ решить эту проблему:
from functools import wraps

def table3(func):
    @wraps(func) # В качестве аргумента - ф-я, которую мы декорируем
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    return inner

def say3():
    ''' Печатает на экран 'Hello, World!' '''
    print(f'Hello, World!')

say3() # => Hello, World!
say3 = table3(say3)
print(say3.__name__) # => say3
