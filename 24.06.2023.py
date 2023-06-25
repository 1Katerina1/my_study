# Оператор not:
name = 'Nastya'

if not name == 'Kate':
    print("Hello, I don't know your name!")
print('-' * 12)


# Циклы:
i = 1
while i <= 5:
  print(i)
  i += 1
print('-' * 12)


j = 1
while 1 == 1:
    print('Hello, ' + str(j))
    j += 1

    if j == 11:
        break # принудительно останавливает исполнение цикла
print('-' * 12)


number = 0
while number <= 20:
    number += 1
    if (number % 2) != 0:
        continue; # пропускает текущую итерацию
    print("Четное число: " + str(number))
print('-' * 12)


# Списки:
test = [3, 5, 8, 3, 7]
print(test)
print(test * 2) # => [3, 5, 8, 3, 7, 3, 5, 8, 3, 7]
print(test + [4, 0]) # => [3, 5, 8, 3, 7, 4, 0]
print(test[3]) # [3] - индекс элемента списка

test2 = [1, 2, 3, [4, 5, 6]] # вложенный список
print(test2[3][1]) # => 5

test3 = ['a', 'b', 'c', ['d', 'e', 'f']]
print(test3[3][2]) # => 'f'

# in - проверяет наличие чего-либо в списке
test4 = ['hello', 'Kate', 'kit']
if 'kit' in test4:
    print('kit is in list')
if 'BigKit' not in test4:
    print('BigKit is not in list')

# Чтобы пременить какой-либо метот к объекту необходимо поставить точку после названия объекта и указать метод; список - это объект; append() - это метод списка
test0 = []
test0.append('Hello') # добавляет элемент в конец списка
test0.append(6)
test0.append([2, 3, 4])
print(test0) # => ['Hello', 6, [2, 3, 4]]

# len() - это функция
test5 = [4, 5, 7, 2, 0, 1]
print('В массиве test5 находится ' + str(len(test5)) + ' элементов.')

test5.remove(0) # этот метод удаляет объект из массива
print(test5) # => [4, 5, 7, 2, 1]

# insert(a, b) - метод, добавляет элемент в список: a - индекс, на который надо добавить элемент, b - сам элемент
test6 = [2, 5, 10, 4, 61]
test6.insert(2, 'Hi!')
print(test6) # => [2, 5, 'Hi!', 10, 4, 61]

# max() - функуция, предназначена для того, чтобы вывести на экран наибольший элемент, находящийся в списке
# min() - функция, выводит наименьший элемент из списка
test7 = [1, 10, 34, 0, 4, 10, 12, 10]
print(max(test7)) # => 34
print(min(test7)) # => 0

# count() - метод, считает кол-во какого-либо элемента, входящего в список 
test8 = ['momy', 'dad', 'grandmather', 'momy']
print(test8.count('momy')) # => 2
print(test7.count(10)) # => 3

# reverse() - метод, "переворачивает" массив
test9 = [1, 2, 3, 4, 5, 6, 7]
test9.reverse()
print(test9) # => [7, 6, 5, 4, 3, 2, 1]

# sort() - метод, сортирует значения по возрастанию 
test10 = [44, 77, 11, 55, 22, 99, 88, 33, 66]
test10.sort()
print(test10)
