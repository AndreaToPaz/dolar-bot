from flask import Flask
import configparser
import telebot
from telebot import types


# READ KEYS FROM CONFIG INI
config = configparser.ConfigParser()
config.read('config.ini')


#TELEGRAM BOT KEY
BOT_KEY = config ['Telegram'] ['BOT_KEY']
#BOT AUTH
BOT = telebot.TeleBot(BOT_KEY) 

#SETTING VARIABLES
option = ['Banco Central de Venezuela',
          'Monitor Dolar Vla','Ambos cambios']

# #INLINE KEYBOARD BUTTONS
markup = types.ReplyKeyboardMarkup(row_width=2)
item_btn_a = types.KeyboardButton(option[0])
item_btn_b = types.KeyboardButton(option[1])
item_btn_c = types.KeyboardButton(option[2])
markup.add(item_btn_a, item_btn_b, item_btn_c)

# #COMMANDS
@BOT.message_handler(commands=['start', 'help'])
def send_welcome(message):
    BOT.reply_to(message, 'Bienvenido a Dolar-Bot, Bot para visualizar el ultimo estado del dolar')
    BOT.send_message(message.chat.id, 'Escoga una opción', reply_markup=markup)
    

username = ['BCV_ORG_VE','monitordolarvla']
@BOT.message_handler(func=lambda message: True)
def send_requested_info_by_option(message):
    if (message.text == option[0]):
        BOT.reply_to(message, 'Cambio del dolar segun '+ option[0])
   
        
    elif (message.text == option[1]):
        BOT.reply_to(message, 'Cambio del dolar segun '+ option[1])
      
    else:
        BOT.send_message(message.chat.id, 'Escoga una opción', reply_markup=markup)
BOT.infinity_polling()


# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#    return 'Hello world!'

