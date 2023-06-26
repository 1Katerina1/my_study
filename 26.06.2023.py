# Урок №14
# Какие бывают исключения:
# ImportError - произведен неверный импорт
# IndexError - попытка получить доступ к какой-либо ячейке списка, которой в списке нет
# NameError - попытка использовать несуществующую переменную
# SyntaxError - допущена синтаксическая ощибка
# TypeError - попытка передать в ф-ю какой-либо аргумент, с типом которого ф-я не совместима
# ValueError - тип переданной переменной или переданного значения тот, что нужен, но значение не такое, как нужно

# После появления исключения, программа завершается, но ->
# Мы можем контролировать процесс появления исключений и программа не будет завершаться:
try:
    print(7 / 0)
except ZeroDivisionError:
    print('Поймано исключение: деление на ноль.')
print('Программа завершена.')
print('-' * 12)

# Если не хотим ничего выводить на экран в случае исключения:
try:
    print(7 / 0)
except ZeroDivisionError:
    pass # пропустить
print('Программа завершена.')
print('-' * 12)

# Если мы не укажем конкретное исключение, пойманы будут все исключения:
try:
    print(7 / 1)
    mm
except:
    print('Поймано исключение.')
print('Программа завершена.')
print('-' * 12)

# Чтобы поймать синтаксическую ошибку, необходимо воспользоваться ф-ей eval():
try:
    eval('print(7 / 1)n')
except ZeroDivisionError:
    print('Поймано исключение: деление на ноль.')
except SyntaxError:
    print('Поймано исключение: синтаксическая ошибка.')
except:
    print('Поймано какое- то исключение.')
print('Программа завершена.')
print('-' * 12)

try:
    print(number / 0)
except (ZeroDivisionError, NameError, ValueError, TypeError):
    print('Поймано какое-то исключение.')
print('Программа завершена.')
print('-' * 12)

# Весь код, написанный в блоке finally, будет в любом случае исполнен:
try:
    print(6 / 2)
except (ZeroDivisionError, NameError, ValueError, TypeError):
    print('Поймано какое-то исключение.')
except:
    print('Поймано какое- то еще исключение.')
finally:
    print('Конец поимки!')
print('Программа завершена.')
print('-' * 12)

# Также можно выбрасывать свои собственные исключения:
try:
    pogoda = 'Плохая'
    if pogoda == 'Плохая':
        raise TypeError
except TypeError:
    print('Поймано исключение TypeError.')
print('-' * 12)

pogoda = 'Хорошая'
if pogoda == 'Плохая':
    raise TypeError

pogoda = 'Плохая'
if pogoda == 'Плохая':
    raise TypeError('Тест')
print('-' * 12)

try:
    print(7 / 0)
except:
    print('Тест')
    raise

# Создадим свое собственное исключение:
class KateError(Exception):
    pass
raise KateError('TEST')

# Урок №15
# Выводит на экран AssertionError, если аргумент ф-ии - пустая строка:
def exc(text):
    assert text != ''
    print(str(text) + '!')
exc('HI')
print('-' * 10)

# Выводит на экран ошибку, если аргумент ф-ии - отрицательное число или 0:
def test(number):
    assert number > 0, "Number should be bigger than zero."
    print(number)
test(15)
print('-' * 10)

# Допустим, есть файл teest.txt, содержащий текстовую инф-ю, чтобы прочесть его, напишем следующий код:
file = open('teest.txt', 'r')

print(file.read()) # file.read(x), x - необязательный аргумент, если ввести число x - количество байт, то ф-я выведет на экран только то количество текста, которое занимает x байт

file.close()

# r - чтение файла
# w - перезапись файла
# a - добавление в файл

# b - Binary mode

# Посчитаем кол-во символов в файле:
filename = input("Укажите файл: ")
file = open(filename, 'r')
print("В данном файле " +  str(len(file.read())) + " символов.")
file.close()

# режим 'w' - перезаписывает файл: если файл существует, из него будет удалено содержимое, если файла не существует, он появится:
file = open('teest.txt', 'w')

file.close()

# Если нам нужно записать текст в файл:
file = open('teest.txt', 'w')
file.write('Hello, World!')
file.close()

# Программа спрашивает имя файла, создает файл, затем спрашивает текст и записывает его в файл:
filename2 = input('Введите желаемое имя файла: ')
text2 = input('Какой текст необходимо поместить в файл? ')
file2 = open(filename2, 'w')
file2.write(text2)
file2.close()
