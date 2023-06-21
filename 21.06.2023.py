from colorama import Fore, Back, Style

print(Fore.YELLOW)
print(Back.GREEN)

what = input("Что делаем? (+, -): ")
print(Back.CYAN)
a = float(input("Введите первое число: ")) 
b = float(input("Введите второе число: "))
# float() - вещественное число
print(Fore.WHITE)
print(Back.YELLOW)
if what == "+":
  c = a + b
  print("Результат: " + str(c))

elif what == "-":
  c = a - b
  print("Результат: " + str(c))

else:
  print("Выбрана неверная операция!")