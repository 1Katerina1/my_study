def capitalize(text):
    if text == '':
        return ''
    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'

print(capitalize('hello')) # => Hello
print(capitalize(''))

# Код после этого выражения не выполнится, скрипт завершится с ошибкой
raise Exception('Бум! Произошла ошибка, останавливаемся')
print('nothing'); # Никогда не выполнится

# Пример теста к ф-ии capitalize():
if capitalize('hello') != 'Hello':
    raise Exception('Ф-я работает неверно!')
if capitalize('') != '':
    raise Exception('Ф-я работает неверно!')

# Упражнение:
if get({"hello": "world"}, "hello") != "world":
    raise Exception('Функция работает неверно!')

if get({}, "hello", "kitty") != "kitty":
    raise Exception('Функция работает неверно!')

if get({"hello": "world"}, "hello", "kitty") != "world":
    raise Exception('Функция работает неверно!')
