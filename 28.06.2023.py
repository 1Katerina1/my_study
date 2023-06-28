# Урок №16
# Тип данных None означает пустоту, этим типом можно обозначать, что переменная пуста:
test = None
print(test)
# Если преобразовывать этот тип данных в булево значение, будет возвращаться False

# Тип данных None возвращается из ф-ий, которые сами по себе ничего не возвращают:
def test():
    print('TEST')
print(test())

# Тип данных Dictionary (словарь):
dic = {
    "key1": "value1",
    "key2": "value2"
}

print(dic["key1"]) # => value1

try:
    print(dic["key3"])
except KeyError:
    print('Такого ключа не существует!')


# В качестве значений словаря могут выступать любые типы данных.
# В качестве ключей словаря могут выступать только "простые" типы данных, напр.: числа, дробные числа, строки.
dic2 = {
    "key1": "value1",
    "key2": {
    "nested_key": "nested_value"
    },
    123: "One hundred and twenty three"
}

print(dic2["key2"]) # => {'nested_key': 'nested_value'}
print(dic2[123]) # => One hundred and twenty three


# Существует ли тот или иной ключ в словаре? (in/not in)
if 163 in dic2:
    print('Ключ существует.')
else:
    print('Ключ не существует.')


if 123 not in dic2:
    print('Ключ не существует.')
else:
    print('Ключ существует.')

# Следующий пример:
contacts = {
    "Зайкин Александр": "+79523573301",
    "Коровкин Артем": "+79517659932",
    "Змеевец Надежда": "+79504566322"
}
name = input('Кого ищем: ')

if name in contacts:
    print('Контакт найден:', contacts[name])
else:
    print('Контакт не найден.')

# .get(key) - выводит значение ключа, но если ключа не существует, выводит None
# .get(key, "доп. инф-я") - выводит значение ключа, но если ключа не существует, выводит "доп. инф-я"
print(contacts.get("Зайкин вАлександр")) # => None
print(contacts.get("Зайкин Александр")) # => +79523573301
print(contacts.get("Зайкин вАлександр", "Такого контакта нет")) # => Такого контакта нет
print(contacts.get("Зайкин Александр", "Такого контакта нет")) # => +79523573301


# Урок №17
''' Многострочный
Необходим, если нужно оставить
большой комментарий
к коду
комментарий '''

print('Hello')

# pass - команда, которая ничего не делает, она нужна для создания пустых блоков кодов
def main():
    pass


# Кортеж (англ. Tuple) - ведет себя как и списки, но элементы кортежа не могут быть изменены в ходе программы
# Пример списка:
names = ["John", "James", "Jack"]

names[0] = "Michael"

print(names[0])

# Пример кортежа:
names2 = ("John", "James", "Jack")

# names2[0] = "Kate" - ошибка, кортеж не поддерживает присваивание элементов

print(names2[0])

# Кортеж так же можно объявить без скобок:
names3 = "John", "James", "Jack"
print(names3[2]) # => Jack

# И это тоже кортеж:
digits = 1, 2, 3, 5, 8, 3
print(digits[4]) # => 8

''' !!! Если необходимо определить в коде какой-нибудь список,
который точно не изменится в ходе программы,
тогда такой список необходимо создать с помощью кортежа,
потому что Python тратит меньше усилий на кортеж
и такой код будет более быстрый. '''
