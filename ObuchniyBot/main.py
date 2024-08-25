# подключение библиотеки
import telebot
import random


# иницилизация бота
bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def start_message(message):
    # message аргумент который хранит в себе сообщение пользователя также хранит id дату и время отправки сообщения
    # message.chat.id позволяет добыть айди диалога пользователя
    # send_message функция для отправки сообщений
    bot.send_message(message.chat.id,'Привет! Мама Наташа!')

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id,'Команды: \n /start')

@bot.message_handler(commands=['photo'])
def photo(message):
    # сохраняем изображение в переменную
    image = open("Images/td.jpg", "rb")
    image2 = open("Images/tigr2.png", "rb")
    # команда для отправки пользователю сообщения с изображением
    bot.send_photo(message.chat.id, image)
    bot.send_photo(message.chat.id, image2)


@bot.message_handler(content_types=['text'])
def echo_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, random.choice(["Привет", "Добрый день"]))
    if message.text.lower() == 'как дела?':
        bot.send_message(message.chat.id, random.choice(["Все отлично", "мне нужна помощь", "Нормально"]))
    if message.text.lower() == 'какая погода сегодня?':
        bot.send_message(message.chat.id, random.choice(["Ясная", "Облачная", "Дождливая", "Пурга", "Ливень", "Гроза с дождем"]))
    if message.text.lower() == 'как настроение?':
        bot.send_message(message.chat.id, random.choice(["Все отлично", "мне нужна помощь", "Нормально", "Не очень"]))
    if message.text.lower() == 'какой фильм посоветуете?':
        bot.send_message(message.chat.id, random.choice(["Без тормозов", "Хатико", "Звездные войны", "Spiderman"]))
    if message.text.lower() == 'какое ваше любимое время года?':
        bot.send_message(message.chat.id, random.choice(["Зима", "Лето", "Весна", "Осень"]))
    if message.text.lower() == 'покажи тигра':
        tg1 = open("Images/td.jpg", "rb")
        tg2 = open("Images/tigr2.png", "rb")
        bot.send_photo(message.chat.id, tg1)
    # bot.send_message(message.chat.id, message.text)

# запуск бота
bot.polling()
