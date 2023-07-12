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
