import telebot
from flask import Flask
from telebot import types
from app.__init__ import config
from app.script import currency_list
from app.utils.help_function import currency_format

#TELEGRAM BOT KEY
BOT_KEY = config ['Telegram'] ['BOT_KEY']
#BOT AUTH
BOT = telebot.TeleBot(BOT_KEY) 

#Option variables
option = ['Mostrar Cambios',
          'Calcular Cambio']

#Inline keyboard buttons
markup = types.ReplyKeyboardMarkup(row_width=2)
item_btn_a = types.KeyboardButton(option[0])
item_btn_b = types.KeyboardButton(option[1])
markup.add(item_btn_a, item_btn_b)

#Commands

#Start command, the command to start the bot
@BOT.message_handler(commands=['start'])
def send_welcome(message):
    BOT.reply_to(message, 'Bienvenido a Dolar-Bot,' +
                 'Bot para visualizar el último estado del dolar '+
                 'según la pagina oficial del Banco Central de Venezuela')
    BOT.send_message(message.chat.id, 'Escoga una opción', reply_markup=markup)
    
#Selection command
@BOT.message_handler(func=lambda message: True)
def send_requested_info_by_option(message):
    
    if (message.text == option[0]):
        BOT.reply_to(message, 'Cambios según el Banco Central de Venezuela '+ '\n' + currency_format(currency_list))
    elif (message.text == option[1]):
        BOT.reply_to(message, 'Cambio del dolar segun '+ option[1])
    
BOT.infinity_polling()


# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#    return 'Hello world!'

