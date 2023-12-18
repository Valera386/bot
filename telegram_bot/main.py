import telebot
from telebot import types
import os

token = "6635008588:AAGHFE47NT3BdGlgP_FMWPDrtsAlM3iaq84"

bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    markup_create_bot = types.InlineKeyboardButton("каталог товаров", callback_data="catalog")
    markup_info = types. InlineKeyboardButton("Информация", callback_data="info")
    markup_my_bots = types.InlineKeyboardButton("Помощ", callback_data="help")

    markup.add(markup_create_bot ,markup_info, markup_my_bots)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!".format(message.from_user), reply_markup= markup)


@bot.message_handler(commands=['back'])
def back(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    markup_back = types.InlineKeyboardButton("назад", callback_data="back")
            
    markup.add(markup_back)
    bot.send_message(message.chat.id, text="назад", reply_markup= markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == "catalog":
            bot.send_message(call.message.chat.id, "Вы в каталоге товаров")
            back(call.message)
            

        if call.data == "help":
            bot.send_message(call.message.chat.id, "Вы в разделе помощи")
            back(call.message)
        

        if call.data == "info":
            bot.send_message(call.message.chat.id, "Вы в разделе информации")
            back(call.message)

            
        if call.data == "back":
            start(call.message)


bot.polling(none_stop=True)