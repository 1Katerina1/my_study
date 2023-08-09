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
