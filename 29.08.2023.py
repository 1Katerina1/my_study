# 5. Генераторные выражения
# Выглядят они как генераторы списков. Разница только в круглых скобках вместо квадратных:
print([x * x for x in range(10)])
# => [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print((x * x for x in range(10)))
# <generator object <genexpr> at 0x7fe76f7e5db0>
# С его помощью мы откладываем вычисление элементов последовательности до появления необходимости в них.

# Упражнение:
def is_int(x):
    return isinstance(x, int)

def each2dtest(test, matrix):
    for row in matrix:
        for elem in row:
          print(elem)
          print(test(elem))
  
    print(list((test(elem) for row in matrix for elem in row)))
    if all((test(elem) for row in matrix for elem in row)):
        return True
    return False

def each2d(test, matrix):
    return all(test(el) for row in matrix for el in row)


def some2d(test, matrix):
    return any(test(el) for row in matrix for el in row)


def sum2d(test, matrix):
    return sum(el for row in matrix for el in row if test(el))


# 6. Функции-генераторы
# Упражнение:
def my_map(f, xs):
    for el in xs:
        yield f(el)

print(list(my_map(abs, [-1, 2, -3]))) # [1, 2, 3]


def my_filter(f, xs):
    for el in xs:
        if f(el):
            yield el

print(list(my_filter(lambda x: x % 2 == 1, range(10)))) # [1, 3, 5, 7, 9]

print('-' * 12)

def replicate_each(n, xs):
    for el in xs:
        for i in range(n):
            yield el

print(list(replicate_each(1, [1, 'a'])))  # [1, 'a']
print(list(replicate_each(3, [1, 'a'])))  # [1, 1, 1, 'a', 'a', 'a']
print(list(replicate_each(0, [1, 'a'])))  # []

# Аналогично:
def replicate_each_analog(n, xs):
    for el in xs:
        yield from (el for i in range(n))

print(list(replicate_each_analog(1, [1, 'a'])))  # [1, 'a']
print(list(replicate_each_analog(3, [1, 'a'])))  # [1, 1, 1, 'a', 'a', 'a']
print(list(replicate_each_analog(0, [1, 'a'])))  # []
