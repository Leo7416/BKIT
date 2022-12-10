import telebot
from telebot import types

bot = telebot.TeleBot('5890914425:AAEgAgq_iDoJeLST7-UbAxjLLkyPQPKaKXU')

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    phrase1 = types.KeyboardButton('Круто, я тоже более за GSW')
    phrase2 = types.KeyboardButton('Я не являюсь фанатом GSW')
    markup.add(phrase1, phrase2)
    bot.send_message(message.chat.id, 'Привет, я бот-фанат GSW, который показывает статистику игроков данной команды', reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def answer(message):
    if (message.text == 'Я не являюсь фанатом GSW'):
        bot.send_message(message.chat.id, 'Тогда тебе здесь не рады, приходи когда начнешь болеть за GSW')

    elif (message.text == 'Круто, я тоже более за GSW'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        phrase0 = types.KeyboardButton('Вернутся в главное меню')
        phrase1 = types.KeyboardButton('Игроков основы')
        phrase2 = types.KeyboardButton('Запасных игроков')
        markup.add(phrase1, phrase2, phrase0)
        bot.send_message(message.chat.id, 'Статистику каких игроков хочешь узнать?', reply_markup=markup)

    elif (message.text == 'Игроков основы'):
        markup1 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton('Стэф Карри', url = 'https://www.sports.ru/steph-curry/stat/')
        url_button2 = types.InlineKeyboardButton('Клэй Томпсон', url = 'https://www.sports.ru/klay-thompson/stat')
        url_button3 = types.InlineKeyboardButton('Дрэймонд Грин', url = 'https://www.sports.ru/draymond-green/stat')
        url_button4 = types.InlineKeyboardButton('Эндрю Уигинс', url = 'https://www.sports.ru/andrew-wiggins/stat')
        url_button5 = types.InlineKeyboardButton('Кевон Луни', url = 'https://www.sports.ru/kevon-grant-looney/stat')
        markup1.add(url_button1, url_button2, url_button3, url_button4, url_button5)
        bot.send_message(message.chat.id, 'Лови статистику стартовой пятерки', reply_markup=markup1)

    elif (message.text == 'Запасных игроков'):
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton('Джордан Пул', url='https://www.sports.ru/jordan-poole/stat/')
        url_button2 = types.InlineKeyboardButton('Донте Дивинченцо', url='https://www.sports.ru/tags/161079478/stat')
        url_button3 = types.InlineKeyboardButton('Джамайкл Грин', url='https://www.sports.ru/tags/161079478/stat')
        url_button4 = types.InlineKeyboardButton('Джонатан Куминга', url='https://www.sports.ru/jonathan-kuminga/stat')
        url_button5 = types.InlineKeyboardButton('Мозес Муди', url='https://www.sports.ru/moses-moody/stat')
        markup2.add(url_button1, url_button2, url_button3, url_button4, url_button5)
        bot.send_message(message.chat.id, 'Лови статистику запасных игроков', reply_markup=markup2)

    elif (message.text == 'Вернутся в главное меню'):
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        phrase1 = types.KeyboardButton('Круто, я тоже более за GSW')
        phrase2 = types.KeyboardButton('Я не являюсь фанатом GSW')
        markup3.add(phrase1, phrase2)
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню', reply_markup=markup3)

    else:
        bot.send_message(message.chat.id, 'Пожалуйста не уходи от темы')

bot.polling(none_stop = True)