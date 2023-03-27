import os
import telebot   #import api wrapper

bot = telebot.TeleBot("5853259409:AAFuy-OQ4tsmO6vP_XLK4uuZaBuyCLqYtnE", parse_mode=None)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()