# Программа для копирования текстовых файлов:
filename1 = input('Введите название копируемого файла: ')
filename2 = input('Введите куда скопировать файл: ')

file1 = open(filename1, 'r')
file2 = open(filename2, 'w')

file2.write(file1.read())

file1.close()
file2.close()

print('Копирование успешно завершено!')


# Программа для копирования файлов с изображением:
# (Так же подходит и для копирования обычных файлов)
filename3 = input('Какой файл забэкапить: ')
filename4 = 'backup' + filename3

file3 = open(filename3, 'rb')
file4 = open(filename4, 'wb')

file4.write(file3.read())

file3.close()
file4.close()

print('Бэкап успешно завершен!')


# readlines - метод, возвращает список из всех строк данного файла
file = open('teest.txt', 'r')

strings = file.readlines()
print(strings)

for string in strings:
    print(string)

file.close()
print('-' * 12)


# Конструкция with автоматически закрывает файл после исполнения, нет необходимости писать f.close()
with open('teest.txt', 'r') as f:
    print(f.read(11))
    print('-' * 12)
    print(f.read(6))
