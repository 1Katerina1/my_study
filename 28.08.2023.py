# 3. Генераторы списков
# "Функция chain() модуля itertools"
from itertools import chain
iterable_sequence1 = range(0, 6)
iterable_sequence2 = range(10, 16)
print(*iterable_sequence1) # => 0 1 2 3 4 5
print(*iterable_sequence2) # => 10 11 12 13 14 15
print(list(chain(iterable_sequence1, iterable_sequence2))) # => 10 11 12 13 14 15

print(list(chain('ABC', 'DEF', 'as'))) # => ['A', 'B', 'C', 'D', 'E', 'F', 'a', 's']

# Хотим получить список чисел вида [0, 0, 2, 2, 4, 4...] — то есть по две копии возрастающих четных чисел:
# Шаг 1: Получаем поток четных чисел
def is_even(x):
    return x % 2 == 0 # Возвращает True/False

print(list(filter(is_even, range(20))))
# => [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Шаг 2: Удваиваем каждое
def dup(x):
    return [x, x]

print(list(map(dup, filter(is_even, range(20)))))
# => [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18]]

# Шаг 3: Делаем конвейер опять плоским
from itertools import chain
print(list(chain(*map(dup, filter(is_even, range(20))))))
# => [0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18]

# Вариант в виде однострочника (аналогично)
print(list(chain(*map(lambda x: [x, x], filter(lambda x: x % 2 == 0, range(20))))))

# Оба варианта выше неудобны. У Python есть синтаксис, который может упростить работу с конвейерами.

# Генераторы списков
# Попробуем решить ту же задачу другим способом:
print([x for num in range(20) for x in [num, num] if num % 2 == 0])
# => [0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18]

# Попробуем отформатировать все выражение:
[x
   for num in range(20)
       for x in [num, num]
           if num % 2 == 0
]

# Теперь код стал похож на два вложенных цикла. Похожий код можно написать и на обычных циклах:
res = []
for y in range(20):
    for x in [y, y]:
        if y % 2 == 0:
            res.append(x)
print(res) # => [0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18]

# Генератор списков описывается так:
# [ВЫРАЖЕНИЕ for ПЕРЕМЕННАЯ in ИСТОЧНИК if УСЛОВИЕ]

# Еще примеры:
# квадраты чисел
print([x*x for x in [1, 2, 3]])
# [1, 4, 9]

# Коды прописных букв из заданной строки
print([ord(c) for c in "Hello!!" if c.isalpha() and c.islower()])
# [101, 108, 108, 111]

# Индексы пар, элементы которых равны друг другу
print([i for i, (x, y) in enumerate([(1, 2), (4, 4), (5, 7), (0, 0)]) if x == y])
# [1, 3]

# Пример посложнее: отфильтруем во вложенных списках четные элементы, затем оставим списки длиннее трех элементов
list_of_lists = [[1, 2, 3, 5], [7, 11, 8, 0], [21, 12, 2, 7, 1], [1, 3]]

# Генерируем внутренний список списков и оставляем только нечетные элементы
# Отфильтруем список списков и оставим только списки длиннее 3 
print([ x for x in [[elem for elem in l if elem % 2 == 1] for l in list_of_lists] if len(x) >= 3])
# [[1, 3, 5], [21, 7, 1]]

print([[elem for elem in l if elem % 2 == 1] for l in list_of_lists])

print('-' * 12)

def f(x):
    if not x:
        return 0
print(f([]))

# упражнение:
def non_empty_truths(lists):
    return [x for x in [[el for el in l_ if el] for l_ in lists] if x]
print(non_empty_truths([[False, 2, 3, 0], []]))
print(non_empty_truths([[0, ''], [False, None]]))


# 4. Генераторы множеств и словарей
# Генераторы множеств:
squares = {x * x for x in range(10)}
print(squares) # => {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(5 * 5 in squares) # => True
print(10 * 10 in squares) # => False

# Генераторы словарей. Нужно сгенерировать не только значение, но и ключ. При этом ключ надо указать через двоеточие:
char_positions = {char: pos for char, pos in enumerate("Hello, World!")}
print(char_positions)
# => {0: 'H', 1: 'e', 2: 'l', 3: 'l', 4: 'o', 5: ',', 6: ' ', 7: 'W', 8: 'o', 9: 'r', 10: 'l', 11: 'd', 12: '!'}
print(char_positions[4]) # => 'o'

print([(char, pos) for pos, char in enumerate("Hello, World!") if char == 'l'])
# => [('l', 2), ('l', 3), ('l', 10)]

# Упражнение:
def number_of_unique_letters(string):
    return len({x.lower() for x in string if x.isalpha()})

print(number_of_unique_letters('Hello.//Hh')) # => 4
print(number_of_unique_letters('o_O')) # => 1
print(number_of_unique_letters('A-a-a-a-a-a!')) # => 1
print(number_of_unique_letters('AaBbCcDd')) # => 4
