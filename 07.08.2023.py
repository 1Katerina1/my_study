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
