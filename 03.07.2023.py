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
