
import telebot
import random
from telebot import types

words = ["apple", "banana", "cherry"]
numbers_range = range(1, 101)

bot = telebot.TeleBot('')

# Создаем переменную для хранения данных
user_data = {}
@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, "Здраствуй путник! Как твое имя?")
    bot.register_next_step_handler(msg, ask_name )

def ask_name(message):
    # Соохраняем имя пользователя
    name = message.text

    # Заполняем словарь с информацией о пользователе
    user_data['name'] = name
    user_data['level'] = 1
    user_data['lives'] = 5
    user_data['score'] = 0
    # Создаем кнопку начать игру

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('Начать')
    msg =  bot.send_message(message.chat.id, f"Достаточно ли ты смел, {name}? Чтобы начать поход в Подземелье!?", reply_markup=markup)
    bot.register_next_step_handler(msg, start_game)


def start_game(message):
    if message.text.lower() == 'начать':
        send_game_info(message)
        start_level_1(message)


def send_game_info(message):
    bot.send_message(
        message.chat.id,
        f"Игрок: {user_data['name']}\nУровень: {user_data['level']}\nКоличество жизней: {user_data['lives']}\nОчки: {user_data['score']}")


def start_level_1(message):
    # Немного пугаем игрока
    bot.send_message(message.chat.id, f"Ты встретил Кощея! У него есть для тебя испытание!")
    bot.send_photo(message.chat.id, open('Kosheq.jpg.jpg', 'rb'))
    # Выбираем случайное слово, чтобы Кощей мог его загадать
    word = random.choice(words)
    # Ограничиваем попытки дать правильный ответ согласно длинне слова
    user_data['current_attempts'] = len(words)

    # Перемешиваем буквы в слове
    secret_word = list(word)
    random.shuffle(secret_word)
    secret_word = ''.join(secret_word)
    msg = bot.send_message(message.chat.id,
                           f"Угадай слово: {secret_word}\nУ тебя {user_data['current_attempts']} попыток")
    bot.register_next_step_handler(msg, check_word, word)


def check_word(message, word):
    if message.text.lower() == word.lower():
        user_data['score'] += 50
        user_data['level'] += 1
        bot.send_message(message.chat.id, f"Поздравляю вы перешли на новый уровень!")
        send_game_info(message)
        start_level_2(message)

    else:
        user_data['current_attempts'] -= 1
        if user_data['current_attempts'] > 0:
            msg = bot.send_message(message.chat.id,
                                   f"Неправильно. Попробуй еще. Осталось попыток: {user_data['current_attempts']}")
            bot.register_next_step_handler(msg, check_word, word)
        else:
            user_data['lives'] -= 1
            if user_data['lives'] > 0:
                send_game_info(message)
                start_level_1(message)
            else:
                bot.send_message(message.chat.id, "К сожалению, все жизни закончились. Игра окончена.")
                user_data.clear()


def start_level_2(message):
    chosen_word = random.choice(words)
    print(chosen_word)
    user_data['current_attempts'] = len(chosen_word)  # Можно также задать фиксированное число попыток
    # Формируем шаблон слова для отгадывания
    masked_word = "*" * len(chosen_word)
    bot.send_message(message.chat.id, f"Тебе встретился Леший")
    bot.send_photo(message.chat.id, open('Leshiy.jpg', 'rb'))
    msg = bot.send_message(message.chat.id,
                           f"Угадай слово: {masked_word}\nУ тебя {user_data['current_attempts']} попыток")
    bot.register_next_step_handler(msg, check_letter, chosen_word, masked_word)


def check_letter(message, chosen_word, masked_word):
    # Переводим слово в нижний регистр
    letter = message.text.lower()
    # Проверяем, что пользователь выслал 1 букву
    if len(letter) != 1 or not letter.isalpha():
        msg = bot.send_message(message.chat.id, "Пожалуйста, введите одну букву.")
        bot.register_next_step_handler(msg, check_letter, chosen_word, masked_word)
        return
    # Если буква есть в слове, то открываем ее
    if letter in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == letter:
                masked_word = masked_word[:i] + letter + masked_word[i + 1:]
        # Отправляем обновленную маску
        msg = bot.send_message(message.chat.id, f"Вы угадали букву! \n {masked_word}")
        bot.register_next_step_handler(msg, check_letter, chosen_word, masked_word)
    # Если буквы нет в слове
    if letter not in chosen_word:
        msg = bot.send_message(message.chat.id, f"Вы не угадали букву! \n {masked_word}")
        bot.register_next_step_handler(msg, check_letter, chosen_word, masked_word)

    # Если пользователь угадал все буквы:
    if masked_word == chosen_word:
        user_data['score'] += 50
        user_data['level'] += 1
        bot.send_message(message.chat.id, f"\nПоздравляем, вы угадали слово - {chosen_word}")
        bot.send_message(message.chat.id, f"Поздравляю вы перешли на новый уровень!")
        send_game_info(message)
        start_level_3(message)


def start_level_3(message):
    bot.send_message(message.chat.id, f"Тебе встретилась Ведьма")
    bot.send_photo(message.chat.id, open('Vedma.jpg', 'rb'))
    user_data['target_number'] = random.randint(1, 100)
    print(user_data['target_number'])
    msg = bot.send_message(message.chat.id, "Угадай число от 1 до 100")
    bot.register_next_step_handler(msg, check_number)


def check_number(message):
    guess = int(message.text)
    if guess == user_data['target_number']:
        user_data['score'] += 100  # Награда за верный ответ
        send_game_info(message)
        bot.send_message(message.chat.id, f"Поздравляю ты прошел Подземелье!\nЗабери награду")
        bot.send_photo(message.chat.id, open('Syndyk.jpg', 'rb'))

    else:
        hint = "меньше" if guess > user_data['target_number'] else "больше"
        msg = bot.send_message(message.chat.id, f"Неправильно, попробуй число {hint}")
        bot.register_next_step_handler(msg, check_number)


def end_game(message):
    bot.send_message(message.chat.id, "Ура, ты прошел всю игру!")
if __name__ == '__main__':
    bot.polling(none_stop=True)

