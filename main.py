# -*- coding: utf8 -*-

import telebot
import os
import random
import urllib.request as urllib2
token='565239514:AAHLJKeZNtk1bsK0FjPNJe9YO9cSD67vqG4'

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/stop')
    user_markup.row('понедельник', 'вторник', 'среда')
    user_markup.row('четверг', 'пятница', 'суббота')
    bot.send_message(message.from_user.id,'Welcome!', reply_markup=user_markup)

bot.polling(none_stop=True, interval=0)
