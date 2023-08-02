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
