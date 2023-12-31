# 10. Замыкания
''' Замыкания — это функция, которая запоминает значения из своей
внешней области видимости, даже если эта область уже недоступна.  
Замыкание возникает, когда функция объявляется внутри другой функции
и использует переменные из внешней функции. В этом случае внешняя
функция создает замыкание, которое хранит ссылку на внешние переменные,
используемые во внутренней функции. Замыкание позволяет внутренней функции
получить доступ к этим переменным, даже если внешняя функция уже завершилась.'''
# Пример:
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10) # closure - замыкание
print(closure(5))  # => 15
''' Замыкание closure сохраняет значение x как 10 между вызовами, поэтому оно может быть
использовано внутри inner_function даже после того, как outer_function уже завершила свою работу. '''

# Scope
''' Scope — это область видимости в Python, которая определяет доступность переменных внутри блока кода. 

В Python есть две области видимости переменных: глобальная и локальная. '''
# Пример:
x = 10  # глобальная переменная

def my_func():
    x = 5  # локальная переменная
    print("x внутри функции:", x)

my_func() # => x внутри функции: 5
print("x вне функции:", x) # => x вне функции: 10

''' Чтобы изменить значение глобальной переменной внутри функции,
нужно явно объявить ее как глобальную с помощью ключевого слова global: '''
x = 5
print(x) # => 5

def foo():
    global x
    x = 10
    print(x)

foo() # => 10
print(x) # => 10

''' nonlocal — это ключевое слово в Python, которое используется при замыканиях во внутренней функции.
Оно позволяет изменять значение переменных, определенных во внешней функции. '''
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
    print("outer:", x)
    inner()
    print("outer:", x)

outer()
''' outer — имеет переменную x со значением 1. Она выводит первоначальное значение x
и затем вызывает функцию inner. После вызова inner она выводит новое значение x.
inner — устанавливает значение x равному 2, используя ключевое слово nonlocal. '''

# Как работают замыкания
''' Замыкание состоит из двух частей: внешняя функция и внутренняя функция.
Внутренняя функция имеет доступ к переменным из внешней функции даже после того,
как внешняя функция завершила свою работу. Это происходит, так как замыкание сохраняет ссылку
на эти переменные, а не копирует их значение. Так замыкания могут использовать и изменять
значения этих переменных между вызовами.  '''

# Упражнение:
def partial_apply(fun, arg_1):
    def inner(arg_2):
        return fun(arg_1, arg_2)
    return inner

def flip(function):
    def inner_2(arg_01, arg_02):
        return function(arg_02, arg_01)
    return inner_2


# 11. Анонимные функции. Принцип работы анонимных функций
''' Анонимные функции — это функции, у которых нет имени.
Они определяются с помощью ключевого слова lambda. '''

# Рассмотрим пример, который использует анонимную функцию:
l = [1, 2, 5, 3, 4]
l.sort(key=lambda x: -x)
print(l) # => [5, 4, 3, 2, 1]

# Рассмотрим другой пример, который использует анонимную функцию вместе с функцией map():
l = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, l))
print(result) # => [2, 4, 6, 8, 10]

# Теперь рассмотрим пример работы с функцией filter:
l = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, l))
print(result) # => [2, 4]

# Еще один пример применения анонимной функции с функцией reduce:
from functools import reduce

l = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, l)
print(result) # => 120
''' функция reduce последовательно умножает каждую пару чисел в списке:
(1 * 2) * 3) * 4) * 5. Это приводит к результату 120. '''

# Особенности анонимных функций
''' 
1) Аргументы анонимных функций не заключены в скобки. Остальные средства для описания аргументов доступны в полной мере — и именованные аргументы, и *args с **kwargs.
2) Тело лямбда-функции — это всегда одно выражение, результат вычисления которого и будет возвращаемым значением.
3) Объявление функции является выражением. Функции можно конструировать и тут же вызывать, не заканчивая выражение:
'''
print(1 + (lambda x: x * 5)(8) + 1) # => 42

# Часто можно встретить возврат лямбды из функции:
def caller(arg):
    return lambda f: f(arg)

call_with_five = caller(5)
print(call_with_five(str)) # => '5'
print(call_with_five(lambda x: x + 1)) # => 6
# (здесь лямбды являются замыканиями — возвращаемая лямбда запоминает значение переменной arg.)

# Упражнение:
def make_module(step=1):
    return {
      "inc": lambda x: x + step,
      "dec": lambda x: x - step
    }
