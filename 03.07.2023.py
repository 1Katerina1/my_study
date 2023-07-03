# Урок №19
# Форматирование строк (%/.format())
name = 'Kate'
age = 21
print('Привет, %s!\nТебе уже %d год!' %(name, age))
# %s - плэйсхолдер строки
# %d - плэйсхолдер числа
# %f - плэйсхолдер дроби
# Существуют и другие плэйсхолдеры

print('Привет, {}!\nТебе уже {} год!'.format(name, age))
print('{0}{1}{0}'.format('abra', 'cad'))
print('Привет, {0}!\nТебе уже {1} год!'.format(name, age))


person_name = 'Kate'
person_age = 21
print('Привет, {name}!\nТебе уже {age} год!'.format(name = person_name, age = person_age))


person = {
    "name": "Kate",
    "age": 21
}
print('Имя: {name}\nВозраст: {age}'.format(name = person["name"], age = person["age"]))
# ИЛИ
print('Имя: {person[name]}\nВозраст: {person[age]}'.format(person = person))
# (person(имя аргумента) = person(значение аргумента))


input_str = 'Jessy'
input_str2 = 'Jumi'
# Jessy*** <
# ***Jessy >
# **Jessy* ^
print('{0:*^11}'.format(input_str)) # => ***Jessy***
print('Hello, {:*^11}'.format(input_str, input_str2))
# {0:*^10}, где 0 - аргумент ф-ии format(0, 1, 2...),
# * - символ заполнения (***Jessy***)
# 10 - кол-во символов, в которое необходимо вместить форматированную переменную
print('{0:^11}'.format(input_str)) # =>    Jessy   
print('{0:$^9}'.format("Sam")) # => $$$Sam$$$

# Всегда будет выводить имя ровно по середине символов заполнения *
length = 14
if ((length - len(input_str))%2):
    length += 1
print(('{0:*^' + str(length) + '}').format(input_str))


# Урок №20: Функции для работы со строками и числами
# join, replace, startswith, endswith, lower, upper, split (строки)
# min, max, abs, sum (числа)
fruits = ['Лимоны', 'Яблоки', 'Киви', 'Ананас', 'Клубника']

# join
print(', '.join(fruits)) # => Лимоны, Яблоки, Киви, Ананас, Клубника
print(' - '.join(fruits)) # => Лимоны - Яблоки - Киви - Ананас - Клубника

# replace
print('Hello, Artyom!'.replace('Artyom', 'Kate')) # => Hello, Kate!

# startswith
# Программа проверяет, начинается ли Ваше имя на A (англ.)
name = input('Введите Ваше имя: ')
if (name.startswith('A')):
    print("Добро пожаловать! Вы в клубе имен, начинающихся с 'A'!")
else:
    print("Добро пожаловать!")

# lower
# Программа проверяет, начинается ли Ваше имя на A или a (англ. и рус.)
name2 = input('Введите Ваше имя: ')
if (name.lower().startswith('a') or name.lower().startswith('а')):
    print("Добро пожаловать! Вы в клубе имен, начинающихся с 'A'!")
else:
    print("Добро пожаловать!")

# Программа переделывает всю строку в строку с нижним регистром:
any = input('Введите что-нибудь: ')
print(any.lower())

# endswith
word = 'evening'
if word.endswith('ing'):
    print('Слово "' + word + '" заканчивается на "ing".')
else:
    print('Слово "' + word + '" не заканчивается на "ing".')

# Программа переделывает всю строку в строку с верхним регистром:
print('Hello!'.upper()) # => HELLO!

# split
members = 'James,Jonny,Jessie,Jack,John'
print(members.split(',')) # => ['James', 'Jonny', 'Jessie', 'Jack', 'John']


# min - принимает либо список, либо кортеж
print(min(2, 10, 0, 34, -1, 54)) # => -1
print(min([2, 10, 0, 34, 90, 54])) # => 0
print(min((2, 10, 0, 34, -6, 54))) # => -6

# max - принимает либо список, либо кортеж
print(max((2, 10, 0, 34, -6, 54))) # => 54

# abs() - возвращает модуль числа
print(abs(-125)) # => 125
print(abs(1245)) # => 1245

# sum() - принимает либо список, либо кортеж
print(sum([2, 5, 111])) # => 118
print(sum([-56, 8382, -83654, 0, 11, -331, 648])) # => -75000
