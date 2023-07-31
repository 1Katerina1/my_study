# Замыкания в Python. Closure Python. (egoroff_channel)
def main_func():
    def inner_func():
        print('Hello my friend!')
    inner_func()

main_func() # => Hello my friend!
a = main_func() # => Hello my friend!
print(a) # => None


def main_func_2():
    def inner_func_2():
        print('Hello my friend!')
    return inner_func_2
  
b = main_func_2()
print(b)
# => <function main_func_2.<locals>.inner_func_2 at 0x7.....>
b() # => Hello my friend!

c = main_func_2()
c() # => Hello my friend!

''' 
Замыканием называется такая ситуация, когда вложенная ф-я пользуется переменными,
которые не объявлены в ее теле. После того как основная ф-я отработает,
переменная name не будет удалена.
Теперь для замыкания нам не хватает только переменной: '''
def main_func_3():
    name = 'Kate'
    def inner_func_3():
        print('Hello my friend! ' + name + '!')
    return inner_func_3

d = main_func_3()
d() # => Hello my friend! Kate!


def main_func_4(value):
    name = value
    def inner_func_4():
        print('Hello my friend! ' + name + '!')
    return inner_func_4

r = main_func_4('Alice')
r() # => Hello my friend! Alice!

v = main_func_4('Sam')
v() # => Hello my friend! Sam!
''' Каждый раз, когда мы вызываем main_func_4, мы создаем свою область видимости и в ней будут храниться свои значения,
они будут отдельно от тех значений, которые будут вызываться этой же ф-ей, но при присваивании её другой переменной. '''


def main_func_5(name):
    def inner_func_5():
        print('Hello my friend! ' + name + '!')
    return inner_func_5

y = main_func_5('Jhon')
y() # => Hello my friend! Jhon!


def adder(value):
    def inner(x):
        return value + x
    return inner

A2 = adder(2) # создался scope (область видимости), в которую мы положили значение value = 2.
# И это все сохранилось в переменной A.
print(A2(5)) # => 7 (x = 5)

A5 = adder(5)
print(A5(10)) # => 15

# Сколько раз вызывается ф-я:
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

q = counter()
print(q()) # => 1
print(q()) # => 2
print(q()) # => 3
print(q()) # => 4

w = counter()
print(w()) # => 1
print(w()) # => 2
