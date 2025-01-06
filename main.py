import telebot
from telebot import types

TOKEN = '7598191101:AAHpiaSvDb7RWKkuEGRuVfIFs1OYTOSSGC8'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    button = types.InlineKeyboardButton(
        "ilovani ochish",
        web_app=types.WebAppInfo(url="https://hubsavdo.netlify.app/")
    )
    markup.add(button)
    
    bot.send_message(message.chat.id, "SavdoHub — bu O'zbekistonda tovarlarni sotish va xarid qilish uchun mo'ljallangan savdo platformasi. Foydalanuvchilar Telegram orqali o'z e'lonlarini joylashtirib, mahsulotlarni sotib olish va sotish imkoniyatiga ega bo'lishadi. Shuningdek, ilova ichida o'z biznesini ochish imkoniyati ham mavjud.", reply_markup=markup)

# Запуск бота
bot.polling()
