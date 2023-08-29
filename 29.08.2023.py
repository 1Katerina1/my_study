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
