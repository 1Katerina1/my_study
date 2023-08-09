# 42 Рекурсия в Python. Рекурсивная функция Часть 2
def rec(s):
    if len(s) == 1 or len(s) == 2:
        return s
    return s[0] + '(' + rec(s[1: -1]) + ')' + s[-1]
print(rec('malina')) # => m(a(li)n)a
print(rec('apple')) # => a(p(p)l)e

# Поставить между символами строки знак '*':
def stars(string):
    if len(string) == 1:
        return string
    return string[0] + '*' + stars(string[1:])
print(stars('Hello')) # => H*e*l*l*o

# Ф-я, которая возводит число x в степень n:
def power(x, n):
    if n == 0:
        return 1
    if n < 0: # отрицательная степень
        return 1/power(x, -n)
    if n % 2 != 0: # n - нечетное
        return power(x, n - 1) * x
    else:
        return power(x, n // 2) * power(x, n // 2)
print(power(2, 7)) # => 128
print(power(5, 3)) # => 125
print(power(2, 10)) # => 1024
print(power(5, -2)) # => 0.04

# Обойти все элементы списка и сказать на каком уровне вложенности они находятся
a = [1, [3, [2, 3, [4]]], 2, [2, 3, 4, [3, 4, [2, 3],5]]]

def rec(list_, level=1):
    print(*list_, 'Level =', level)
    for i in list_:
        # print(i, type(i))
        if type(i) == list:
            rec(i, level + 1)

rec(a)

print('_' * 12)

# Из "(abc(def(g" получить "(abc(def(gg)fed)cba)"
def mirror(string):
    if len(string) == 0:
        return ''
    if string[0] == '(':
        return string[0] + mirror(string[1:]) + ')'
    return string[0] + mirror(string[1:]) + string[0]

print(mirror('MI((R(R(OR')) # => MI((R(R(ORRO)R)R))IM
print(mirror('(abc(def(g')) # => (abc(def(gg)fed)cba)

# Задача: Нумеролог
# Минус этого решения в том, что оно работает только для двузначных чисел:
def numerologist(N, lvl=0):
    if len(str(N)) == 1:
        print(*[N, lvl])
    else:
        n1 = str(N)
        n11 = int(n1[0])
        n2 = str(N)
        n22 = int(n2[1])
        return numerologist(n11 + n22, lvl + 1)

numerologist(99) # => 9 2

# Это решение работает как надо:
def predskazanie(a,Level=0):
    if len(a)==1:
        return int(a), Level
    else:
        s=0
        for i in range(len(a)):
            s+=int(a[i])
        a=str(s)
        return predskazanie(a, Level+1)
print(*predskazanie('109')) # => 1 2


#  14. Рекурсия. Что такое рекурсия.
''' Рекурсия в программировании — это возможность дать определение функции,
используя в процессе саму определяемую функцию. '''
def factorial(n):
    print(f'n = {n}')
    if n <= 0: # условие, которое прекращает рекурсию
        return 1
    return n * factorial(n - 1)

n = 5
print(f'factorial of {n} = {factorial(n)}')

# Переполнение стека
''' Память для стека не бесконечна =) '''

# Пример линейной рекурсии
def collatz(n):
    print(f'n = {n}')
    if n == 1:
        return True
    if n % 2 == 0:
        return collatz(n // 2)
    return collatz(n * 3 + 1)

n = 3
print(f'Collatz of {n}')
print(collatz(n))
# Здесь в теле функции рекурсивных вызова два, но в каждом заходе используется только один.

# Пример каскадной рекурсии
def fibonacci(n):
    print(n)
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 8
print(f'Fibonacci of {n} = {fibonacci(n)}')
''' Здесь функция всегда вызывает себя два раза.
Сначала будет два вызова себя, которые превратятся в четыре — два раза по два вызова.
Затем в восемь — количество вызовов растет каскадно. '''


# Упражнение:
# Принимает список и возвращает его длину
def length(list_, L=0):
    if not list_:
        return L
    else:
        return length(list_[1:], L + 1)
print(length([1, 0, 87, 34, 2, 6, 8])) # => 7

# Принимает два числа begin и end и возвращает перевернутый список всех чисел между. 
# Для простоты договоримся, что begin <= end
def reverse_range(begin, end, l=''):
    if begin == end:
        A = list(l + str(begin))
        return list(map(int, A)) # map преобразовывает каждый элемент списка из str в int
    if end > begin:
        l = l + str(end)
        return reverse_range(begin, end-1, l)

print('1:', reverse_range(1, 1)) # => [1]
print('2:', reverse_range(1, 2)) # => [2, 1]
print('3:', reverse_range(1, 3)) # => [3, 2, 1]

# Принимает список чисел и возвращает новый только с положительными элементами
def filter_positive(L):
    if not L:
        return L
    if L[0] < 0:
        return filter_positive(L[1:])
    return [L[0]] + filter_positive(L[1:])
  
print(filter_positive([-1, 0, -2, 4, 8])) # => [0, 4, 8]
