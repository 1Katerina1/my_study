# Лекция №5
A = [1, 2, 3, 4, 5]
print(A) # => [1, 2, 3, 4, 5]
for x in A:
    print(x)
# 1
# 2
# 3
# 4
# 5
print('-' * 12)

A = [0] * 100 # Список, размером 100
print(A)

D = [0, 3, 6, 8]
C = D
print(D) # => [0, 3, 6, 8]
print(C) # => [0, 3, 6, 8]

S = [0] * 4
for k in range(4):
    S[k] = D[k]
print(S) # => [0, 3, 6, 8] (поэлементное копирование)

D[0] = 999
print(D[0]) # => 999
print(C[0]) # => 999
print(S[0]) # => 0

x = 1
y = x
y += 1
print(y) # => 2 (любая арифметическая операция создает новое число)
print(x) # => 1

X1 = [9, 6, 21, 8]
X2 = list(X1) # такая записть тоже поэлементно копирует список
print(X2[0]) # => 9
X1[0] = 10
print(X2[0]) # => 9

# Линейный поиск в массиве
def array_search(A:list, N:int, x:int):
    for k in range(N):
        if A[k] == x:
            return k
    return -1

print(array_search([1, 6, 0, 10, 11], 5, 10)) # => 3

# Алгоритм обращения массива
def invert_array(A:list, N:int):
    for k in range(N // 2):
        A[k], A[N - 1 - k] = A[N - 1 - k], A[k]

a = [1, 2, 3, 4, 5]
print(a)
invert_array(a, 5)
print(a) # => [5, 4, 3, 2, 1]

# Решето Эратосфена
N = 20
A = [True] * N
A[0] = A[1] = False
for k in range(2, N):
    if A[k]:
        for m in range(2 * k, N, k):
            A[m] = False
for k in range(N):
    print(k, '-', "простое" if A[k] else "составное")
