#pip install beautifulsoup4
#pip install requests
#pip install pyTelegramBotAPI

from bs4 import BeautifulSoup
import requests
import telebot
from telebot import types

# Класс WeatherInfo для получения информации о погоде
class WeatherInfo:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url)

    def get_temperature(self):
        bs = BeautifulSoup(self.response.text, "lxml")
        temp = bs.find('span', class_='temp__value')
        return temp.text if temp else "Temperature information not found"

# Токен бота
TOKEN = ''

# Создание объекта бота
bot = telebot.TeleBot()

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn_weather = types.InlineKeyboardButton('Погода сегодня', callback_data='get_weather')
    markup.add(btn_weather)
    bot.reply_to(message, "Привет! Я бот погоды. Нажми на кнопку 'Погода сегодня', чтобы узнать текущую температуру.", reply_markup=markup)

# Обработчик нажатия на кнопку "Погода сегодня"
@bot.callback_query_handler(func=lambda call: call.data == 'get_weather')
def get_weather(call):
    url = 'https://yandex.com.am/weather?lat=55.75581741&lon=37.61764526'
    weather_info = WeatherInfo(url)
    temperature = weather_info.get_temperature()
    bot.send_message(call.message.chat.id, f"Текущая температура: {temperature}")

# Запуск бота
bot.polling(non_stop=True, interval=0)