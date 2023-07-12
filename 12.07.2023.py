# Лекция №4
def max2(x, y):
    if x > y:
        return x
    return y

print(max2(4, 8)) # => 8

def max3(x, y, z):
    return max2(x, max2(y, z))

print(max3(3, 6, 0)) # => 6
print(max3(2.6, -2, 9)) # => 9
print(max3("ab", "abc", "abf")) # => abf

# sep — это может быть строка, которую необходимо вставлять между значениями, значение по умолчанию — пробел.
def hello_separated(name='World', separator='-'):
    print('Hello,', name, sep=separator)
hello_separated('John', '***') # => Hello,***John
hello_separated(separator='***') # => Hello,***World
hello_separated(separator='***', name='John') # => Hello,***John

print('Hello,', 'Kate') # => Hello, Kate
print('Hello,', 'Kate', sep="*") # => Hello,*Kate


def is_simple_number(x):
    '''Определяет, является ли число простым.
       x - целое положительное число.
       Если простое, то возвращает True, 
       а иначе - False.
    '''
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True

print(is_simple_number(4)) # => False
print(is_simple_number(19)) # => True
# help(is_simple_number)

def factorize_number(x):
    '''Раскладывает число на множители.
       Печатает множители н аэкран.
       x - целое положительное число.
    '''
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1

print(factorize_number(1024))
print(factorize_number(999))


'''
    Hexlet: Реализуйте функцию fib(), находящую положительные Числа Фибоначчи.
    Аргументом функции является порядковый номер числа.
        Формула:
        f(0) = 0
        f(1) = 1
        f(n) = f(n-1) + f(n-2)

    fib(3)  # 2
    fib(5)  # 5
    fib(10)  # 55
'''

# Мое решение:
def fib(x):
    numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    return numbers[x]

# Решение учителя:
def fib(num):
    if num == 0:
        return 0

    if num == 1:
        return 1

    first, second = 0, 1
    result = first + second

    index = 2
    while index <= num:
        result = first + second
        first, second = second, result

        index += 1

    return result


'''
    Hexlet: Назовем счастливыми те числа, сумма квадратов цифр которого,
    в результате ряда преобразований, превратятся в единицу.
    
    Например:
    7   -> 7^2 = 49
    49  -> 4^2 + 9^2 = 97
    97  -> 9^2 + 7^2 = 130
    130 -> 1^2 + 3^2 + 0^2 = 10
    10  -> 1^2 + 0^2 = 1
    Вывод: исходное число 7 — счастливое.

    Реализуйте функцию is_happy_number(), которая возвращает True,
    если число счастливое, и False — если нет.
    Количество итераций процесса поиска необходимо ограничить числом 10.
    Подсказки:
    Воспользуйтесь вспомогательной функцией sum_of_square_digits(),
    которая принимает на вход число и возвращает сумму квадратов цифр этого числа.
'''
def sum_of_square_digits(number):
    return sum(int(x) ** 2 for x in str(number))

# Мое решение:
def is_happy_number(x):
    i = 1
    while i < 11:
        result = sum_of_square_digits(x)
        x = result
        i += 1
    if x == 1:
        return True
    return False

# Решение учителя:
def is_happy_number(number):
    for _ in range(10):
        if number == 1:
            return True
        number = sum_of_square_digits(number)
    return False
