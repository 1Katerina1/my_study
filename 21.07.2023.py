# Python: Функции
# 5. Операторы упаковки и распаковки
# Оператор *
''' Оператор * используется для упаковки и распаковки итерируемых объектов, таких как списки или кортежи. При использовании перед итерируемым объектом, во время вызова
функции, оператор * распаковывает его: '''
def sum_of_values(a, b, c):
    return (a + b + c)
values = [5, 1, 4]
print(sum_of_values(*values))

''' Также оператор * можно использовать, чтобы распаковывать итерабельные переменные. Это позволяет присваивать их отдельным переменным: '''
my_list = [3, 6, 0, 7, 2]
a, b, *c = my_list
print(a, b, c) # => 3 6 [0, 7, 2]
a, *b, c = my_list
print(a, b, c) # => 3 [6, 0, 7] 2

''' Оператор * можно использовать для распаковки итерируемого
списка в новый список или кортеж: '''
my_list2 = [0, 1, 2]
new_my_list2 = [*my_list2, 3, 4, 5]
print(new_my_list2) # => [0, 1, 2, 3, 4, 5]

my_tuple = (8, 7, 6)
new_my_tuple = (*my_tuple, 5, 4)
print(new_my_tuple) # => (8, 7, 6, 5, 4)

# Оператор **
''' Оператор ** используется для упаковки и распаковки словарей.
При использовании перед словарем во время вызова функции оператор **
упаковывает пары ключ-значение словаря в аргументы ключевых слов,
которые могут быть переданы в функцию: '''
def print_details(name, age):
    print(f'NAME: {name}')
    print(f'AGE: {age}')

print_details('Kate', 21) # пример обычного вызова ф-ии
# => NAME: Kate
# => AGE: 21

dic = {'name': 'Katya', 'age': 21}
print_details(**dic) # ** используется для распаковки словаря и
# перечачи его пар ключ-значение в качестве аргументов 
# => NAME: Katya
# => AGE: 21

''' Оператор ** также можно использовать для создания словаря
из последовательности пар ключ-значение: '''
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
combined_dict = {**dict1, **dict2}
print(combined_dict) # => {'a': 1, 'b': 2, 'c': 3, 'd': 4}

''' Если ключи дублируются, то значение из второго словаря перезапишет значение из первого словаря: '''
dict3 = {'x': 10, 'y': 12}
dict4 = {'x': 8, 'z': 0}
combined_dict2 = {**dict3, **dict4}
print(combined_dict2) # => {'x': 8, 'y': 12, 'z': 0}

# Упражнение:
def get_unique(*args):
    new_unique = []
    for i in args:      
        new_unique += [*i]
    return list(set(new_unique))
print(get_unique([1, 2, 3], [3, 3, 4, 5]))