import telebot
from telebot import types
bot = telebot.TeleBot('5368594933:AAGpiS3UjUEaiqLqKyUIL76uFgws9r-zZUk')

@bot.message_handler(commands=['15'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://t.me/+aslO8CEq4kc4NmQy"))
    bot.send_message(message.chat.id, 'СЮДА', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nКакой трек тебя интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


bot.polling(none_stop=True)
