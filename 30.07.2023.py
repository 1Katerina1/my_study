# 12. Декораторы
''' Декораторы в Python — это функции, которые принимают другую функцию в качестве аргумента,
добавляют к ней некоторую дополнительную функциональность и возвращают функцию с измененным поведением. '''
# Пример:
def debug_decorator(func):
    def wrapper(*args, **kwargs):
        print("Вызов функции:", func.__name__)
        print("Аргументы:", args, kwargs)
        result = func(*args, **kwargs)
        print("Результат:", result)
        return result
    return wrapper

@debug_decorator
def add_numbers(x, y):
    return x + y

add_numbers(2, 3)
# Вызов функции: add_numbers
# Аргументы: (2, 3) {}
# Результат: 5

# Как связаны декораторы и замыкания
''' Внутренняя функция wrapper декоратора обычно ссылается на
переменные из внешней функции, что создает замыкание. '''

# Упражнение:
def memoized(func):
    def wrapper(val):
        if val in func.d:
            res = func.d[val]
        else:
            res = func(val)
            func.d[val] = res
        return res
 
    func.d = {}
    return wrapper
