import telebot
from telebot import types

TOKEN = '7598191101:AAHpiaSvDb7RWKkuEGRuVfIFs1OYTOSSGC8'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    button = types.InlineKeyboardButton(
        "Открыть приложение",
        web_app=types.WebAppInfo(url="https://hubsavdo.netlify.app/")
    )
    markup.add(button)
    
    bot.send_message(message.chat.id, "Добро пожаловать в SavdoHub! 🌟", reply_markup=markup)

# Запуск бота
bot.polling()
