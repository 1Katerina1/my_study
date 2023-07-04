Существует два варианта выполнения программы на Python:
1) Интерактивный вариант (консоль Python/Shell)
2) Файловый вариант (стандартный вариант)

Программа - это набор инструкций, который описывает компьютеру 
определенную последовательность действий.

Пример программы из двух инструкций:
print('Hello!')
print(2, "?")

Каждая инструкция создает или обрабатывает объекты, например в этой строчке:
print(5 + 6) складывается два объекта числа.
Здесь: print('Hello, Kate') мы имеем дело с объектом "строка"
и она выводится как есть.


# Также в модуле math можно найти многие другие математиеские ф-ии
print(round(34.56709)) # => 35 (Второй аргумент по умолчаию 0)
print(round(34.56709, 0)) # => 35.0
print(round(34.56709, 2)) # => 34.57
print(round(583.602, -2)) # => 600.0

print(type(4)) # => <class 'int'>
print(type('Hello')) # => <class 'str'>
print(type({1: 'one', 2: 'two'})) # => <class 'dict'>


''' Hexlet:
В рамках этого испытания вы реализуете небольшой набор функций, 
работающих с отрезками прямых на двухмерной плоскости.
Отрезок в нашем случае будет кодироваться в виде пары пар и выглядеть как-то так:
((x1, y1), (x2, y2)) (вложенные пары — это концы отрезка).
Вам нужно реализовать четыре функции:

    is_degenerated() должна возвращать истину,
    если отрезок вырожден в точку (начало и конец совпадают)

    is_vertical() должна возвращать истину,
    если отрезок — вертикальный

    is_horizontal() должна возвращать истину,
    если отрезок — горизонтальный

    is_inclined() должна возвращать истину,
    если отрезок — наклонный (не вертикальный и не горизонтальный)

line1 = (0, 10), (100, 130)
is_vertical(line1)  # False
is_horizontal(line1)  # False
is_degenerated(line1)  # False
is_inclined(line1)  # True

line2 = (42, 1), (42, 2)
is_vertical(line2)  # True
line3 = (100, 50), (200, 50)
is_horizontal(line3)  # True '''

# Решение учителя:
def is_vertical(line):
    (x1, y1), (x2, y2) = line
    # ^ sometimes it is just fine to unpack such nested structures
    return x1 == x2 and y1 != y2


def is_horizontal(line):
    (x1, y1), (x2, y2) = line
    return x1 != x2 and y1 == y2


def is_degenerated(line):
    p1, p2 = line
    return p1 == p2


def is_inclined(line):
    return not (
        is_vertical(line) or is_horizontal(line) or is_degenerated(line)
    )

# Мое решение:
def is_degenerated(line):
    pair1, pair2 = line
    (x1, y1) = pair1
    (x2, y2) = pair2
    if (x1 == x2) and (y1 == y2):
        return True


def is_vertical(line):
    pair1, pair2 = line
    (x1, y1) = pair1
    (x2, y2) = pair2
    if (x1 == x2) and (y1 != y2):
        return True


def is_horizontal(line):
    pair1, pair2 = line
    (x1, y1) = pair1
    (x2, y2) = pair2
    if (x1 != x2) and (y1 == y2):
        return True


def is_inclined(line):
    pair1, pair2 = line
    (x1, y1) = pair1
    (x2, y2) = pair2
    if (x1 != x2) and (y1 != y2):
        return True
