import os
# import webbrowser

import telebot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEBOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Hello!")


@bot.message_handler(commands=["info"])
def get_info(message):
    bot.send_message(message.chat.id, message)

# OPENS WEBSITE LOCALLY!!
# @bot.message_handler(commands=["web", "site"])
# def open_website(_):
#     webbrowser.open("https://www.usalearns.org/")


@bot.message_handler()
def general_message_handler(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id,
                         f"Hello {message.from_user.first_name}")
    if message.text.lower() == 'id':
        bot.reply_to(message, f"ID: {message.from_user.id}")


bot.polling(none_stop=True)
