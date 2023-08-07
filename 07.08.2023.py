# 13. Больше о декораторах
# Упражнение:

from functools import wraps


def memoizing(max_):
    def wrapper(func):
        list_of_keys = []
        list_of_value = []

        @wraps(func)
        def inner(x):
            if x in list_of_keys:
                index = list_of_keys.index(x)
                return list_of_value[index]

            else:
                y = func(x)
                list_of_keys.append(x)
                list_of_value.append(y)
                if (len(list_of_keys) > max_):
                    list_of_keys.pop(0)
                    list_of_value.pop(0)
                return y
        return inner
    return wrapper

# Испытание: Фибоначчи (Hexlet)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# 41 Рекурсия в Python. Рекурсивная функция Часть 1
def rec(x):
    print(x)
    rec(x)

# rec(1)
''' Возникнет ошибка - maximum recursion depth exceeded while calling a Python object,
т.к. есть ограничение на глубину вызова внутри рекурсии '''

# Оценим, сколько раз мы можем рекурсивно вызывать ф-ю:
def rec(x):
    print(x)
    rec(x + 1)
# rec(1) # 996

def rec2(x):
    if x < 4:
        print(x)
        rec2(x + 1)
        print(x)
rec2(1)
# => 1
# => 2
# => 3
# => 3
# => 2
# => 1

def fact(x):
    if x == 1:
        return 1
    return fact(x - 1) * x
print(fact(5)) # => 120

def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(11)) # => 55

# Проверим на палиндром ('шалаш', '', 'a', 'bdgtrrtgdb')
def palindrom(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    else:
        return palindrom(string[1:-1])
print(palindrom('шалаш'))
