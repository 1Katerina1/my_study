import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('a4274abe4e931706f8097b83310bfbb3', config_dict)
mgr = owm.weather_manager()
bot = telebot.TeleBot("6103551193:AAH3XXuMM7MzMQ4QkpU_j8m4F0t-l4EBOjg")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    hum = w.humidity
    wind = w.wind()["speed"]

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + ".\n"
    answer += "Температура около " + str(round(temp)) + "°C\n"
    answer += "Влажность воздуха " + str(hum) + "%\n"
    answer += "Скорость ветра " + str(wind) + "м/с"
    bot.send_message(message.chat.id, answer)

bot.infinity_polling(none_stop = True)