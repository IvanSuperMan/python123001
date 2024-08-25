import telebot
val = " "
old_val = " "
bot = telebot.TeleBot("")
# InlineKeyboardMarkup контейнер для массива кнопок InlineKeyboardButton
# С его помощью создается интерактивная клавиатура, которая отобржается прямо под текстом сообщения или под формой запроса
# InlineKeyboardButton это сама кнопка, которая располагется на интеркативной клавиатуре.

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data = 'no'),
             telebot.types.InlineKeyboardButton('C', callback_data = 'C'),
             telebot.types.InlineKeyboardButton('<=', callback_data = '<='),
             telebot.types.InlineKeyboardButton('/', callback_data = '/')
             )

keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data = '1'),
             telebot.types.InlineKeyboardButton('2', callback_data = '2'),
             telebot.types.InlineKeyboardButton('3', callback_data = '3'),
             telebot.types.InlineKeyboardButton('*', callback_data = '*')
             )

keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data = '4'),
             telebot.types.InlineKeyboardButton('5', callback_data = '5'),
             telebot.types.InlineKeyboardButton('6', callback_data = '6'),
             telebot.types.InlineKeyboardButton('-', callback_data = '-')
             )

keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data = '7'),
             telebot.types.InlineKeyboardButton('8', callback_data = '8'),
             telebot.types.InlineKeyboardButton('9', callback_data = '9'),
             telebot.types.InlineKeyboardButton('+', callback_data = '+')
             )

keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data = 'no'),
             telebot.types.InlineKeyboardButton('0', callback_data = '0'),
             telebot.types.InlineKeyboardButton(',', callback_data = ','),
             telebot.types.InlineKeyboardButton('=', callback_data = '=')
             )
@bot.message_handler(commands=['start', 'calc'])

def start_message(message):
    global val
    if val == " ":
        bot.send_message(message.from_user.id, 'Введите значение', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, val, reply_markup = keyboard)
    #bot.send_meessage(message.from_user.id, 'Введите значение', reply_markup = keyboard)

@bot.callback_query_handler(func = lambda call: True)
def callback_func(query):
    global val, old_val
    data = query.data

    if data == 'no':
        pass
    elif data == 'C':
        val = ' '
    elif data == '<=' and val != ' ':
        val = '0'
    elif data == '=':
        val = str(eval(val))

    else:
        val += data

    if val != old_val:
        if val == " ":
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0',
                                  reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=val,
                                  reply_markup=keyboard)
    old_val = val


bot.polling(non_stop=True, interval=0)