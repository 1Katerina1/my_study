# Калькулятор 
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


# Прогноз погоды
from pyowm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('a4274abe4e931706f8097b83310bfbb3', config_dict)
mgr = owm.weather_manager()
place = input('Введите город: ')

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]
hum = w.humidity
wind = w.wind()["speed"]

print("В городе " + place + " сейчас " + w.detailed_status + ".")
print("Температура около " + str(round(temp)) + "°C")
print("Влажность воздуха " + str(hum) + "%")
print("Скорость ветра " + str(wind) + "м/с")