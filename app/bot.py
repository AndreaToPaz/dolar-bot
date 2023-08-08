import telebot
import datetime
from flask import Flask
from telebot import types
from app.__init__ import config
from app.script import currency_list, REF_NAMES
from app.utils.help_function import currency_format, calculate_currency_exchage

#TELEGRAM BOT KEY
BOT_KEY = config ['Telegram'] ['BOT_KEY']
#BOT AUTH
BOT = telebot.TeleBot(BOT_KEY) 

#Commands

#Start command, the command to start the bot
@BOT.message_handler(commands=['start'])

def send_welcome(message):
    BOT.reply_to(message, 'Bienvenido a Dolar-Bot, ' +
                 'Bot para visualizar el último estado del dolar '+
                 'según la pagina oficial del Banco Central de Venezuela')
    
    BOT.reply_to(message, 'Escriba el comando : /cambios')
    
#Show currency changes command
@BOT.message_handler(commands=['cambios'])

def send_requested_info_by_option(message): 
    BOT.reply_to(message, 'Cambios según el Banco Central de Venezuela '
                     + '\n' + currency_format( currency_list ) )
    
    BOT.reply_to(message, '¿Desea calcular un cambio? escriba : /calcularCambio')

#Select currency changes command
@BOT.message_handler(commands=['calcularCambio'])

def select_currency(message): 
    BOT.reply_to(message, 'Para calcular el cambio selecione la moneda ' +
                        'y luego ingrese la cantidad.' + '\n' +
                        'Cambios: /EUR , /CNY , /TRY , /RUB , /USD ' + '\n' +
                        'Por ejemplo : /USD 20.12')

#Select currency changes command
@BOT.message_handler(commands=REF_NAMES)

def calculate_requested_currency(message): 
    BOT.reply_to(message, 'Ingrese cantidad para calcular con cambio de : '
                        + message.text)
    BOT.send_message(message.chat.id, calculate_currency_exchage( currency_list, message.text ) )
    

# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#    return 'Hello world!'

