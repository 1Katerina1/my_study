# Python: Функции
# 2. Позиционные аргументы
def function(*args): # * - оператор
    print(type(args)) # => <class 'tuple'>
    print(args) # => ('Hello', 2, 11, None, True)
function('Hello', 2, 7 + 4, None, True) 
'''Оператор * упаковывает все передаваемые в функцию аргументы
от текущей позиции и до конца в переменную как кортеж. '''

# Если мы хотим использовать дополнительные аргументы, помимо аргументов с оператором *:
def function2(x, *args):
    print("Обязательный аргумент x =", x)
    for a in args:
        print('Другой аргумент из args:', a)
function2('Hi', 45, True, 'Kate')

# Передача аргументов в форме коллекции:
def greet(*names):
    for name in names:
        print(f'Hello, {name}!')
N = ["Kate", "Alice", "Mila"]
greet(*N) 
# => Hello, Kate!
# => Hello, Alice!
# => Hello, Mila!

greet(
  'Bob', *['Mary', 'Clair'], 'Sam',
   *('Henry', 'John')
)
# => Hello, Bob!
# => Hello, Mary!
# => Hello, Clair!
# => Hello, Sam!
# => Hello, Henry!
# => Hello, John!

# 3. Именованные аргументы
''' Именованные аргументы используются, когда при вызове ф-ии
необходимо передать аргументы в хаотичном порядке. '''
def bar(length, char1, char2):
    return (char1 + char2) * length
print(bar(3, '-', '*')) # => -*-*-*
print(bar(char1='-', char2='*', length=3)) # => -*-*-*

# Значения аргументов по умолчанию
''' При вызове ф-ии мы можем не указывать значения аргументов
по умолчанию (если таковые имеются), в таком случае эти аргументы
будут равны своему значению по умолчанию :) '''
def bar(length, char1='-', char2='*'):
    return (char1 + char2) * length
print(bar(5, '#', '^')) # => #^#^#^#^#^
print(bar(char2='$', length=5)) # => -$-$-$-$-$
print(bar(6)) # => -*-*-*-*-*-*
print(bar(4, '|', ':')) # => |:|:|:|:

def f(*args, x=None, y=None):
    print(f'args = {args}, x = {x}, y = {y}')
f(*(1, 2), x='a', *[3, 4, 5], y=0, *(6, 7))
# => args = (1, 2, 3, 4, 5, 6, 7), x = a, y = 0
f(*(13, 2), x='a', *[0, 10, 14], *(9, 7))
# => args = (13, 2, 0, 10, 14, 9, 7), x = a, y = None

''' Широко практикуется такой подход: если функция принимает больше
трех аргументов, нужно хотя бы часть из них указать по имени: '''
def make(shape, x, y, radius, line_pattern, line_width, fill):
    pass
make(
    shape='circle',
    x=300, y=150, radius=10,
    line_pattern=None,
    line_width=2.5,
    fill=False
)
# Так читаемость хуже:
make('circle', 300, 150, 10, None, 2.5, False)

# 4. Больше об именованных аргументах
# Получение именованных аргументов в виде словаря
def g(**kwargs):
    return kwargs
print(g(x=1, y=3, z=None)) # => {'x': 1, 'y': 3, 'z': None}

# Порядок вызовов смешанных аргументов
''' Заметим, что *args всегда указывается перед **kwargs,
иначе будет ошибка. '''
def f(*args, **kwargs):
    return (args, kwargs)
print(f(1, 2, 3, 4, kx = 'x', ky = 'y', kz = 'z'))
# => ((1, 2, 3, 4), {'kx': 'x', 'ky': 'y', 'kz': 'z'})

''' Действует следующий порядок расстановки аргументов:
    1. Обычные позиционные аргументы
    2. Аргумент *args
    3. Аргументы со значением по умолчанию
    4. Аргумент **kwagrs
'''
def f2(x, *args, y=None, **kwargs):
    return (x, args, y, kwargs)
print(f2(3, *('Hi', 'mom'), kx='a', ky='b'))
# => (3, ('Hi', 'mom'), None, {'kx': 'a', 'ky': 'b'})
print(f2(3, *('Hi', 'mom'), kx='a', ky='b', *(0, -1), y=4))
# => (3, ('Hi', 'mom', 0, -1), 4, {'kx': 'a', 'ky': 'b'})

# Передача именованных аргументов с помощью словаря
def coords(x, y):
    return (x, y)
print(coords(x=3, **{'y': 4})) # => (3, 4)


def f(x, y, *args, kx=None, ky=42, **kwargs):
    return (x, y, args, kx, ky, kwargs)
positional = (2, 3)
named = dict(ky='b', kz='c')
print(f(1, *positional, 4, kx='a', **named))
# (1, 2, (3, 4), 'a', 'b', {'kz': 'c'})

# Keyword-only аргументы
''' Рекомендуется использовать либо keyword-only аргументы,
либо **kwargs, но не оба вместе. 
Ниже * выступает разделителем — отделяет обычные аргументы от
строго именованных. Вызвать такую ф-ю можно только через передачу
этих аргументов по именам. '''

def fun(x, *, y=6, z=10):
    return (x, y, z)
print(fun(3, y=4, z=5)) # => (3, 4, 5)
print(fun(x=3, y=4, z=5)) # => (3, 4, 5)
# print(fun(3, 4, z=5)) - ошибка

# Порядок аргументов при вызове функций
''' Одиночные именованные аргументы могут идти вперемешку с
подстановками наборов позиционных. '''
def f(x, y, *args, kx=None, ky=42, **kwargs):
    return (x, y, args, kx, ky, kwargs)

foo = [1, 2, 3]
bar = "abc"
print(f(kx=42, *foo, ky=100, *bar))
# (1, 2, (3, 'a', 'b', 'c'), 42, 100, {})
