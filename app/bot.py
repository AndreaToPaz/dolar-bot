import telebot
import datetime
from flask import Flask
from telebot import types
from app.__init__ import config, BOT_KEY
from app.script import currency_list, REF_NAMES
from app.utils.help_function import currency_format, calculate_currency_exchage


#BOT AUTH
BOT = telebot.TeleBot(BOT_KEY) 

#Commands

#Start command, the command to start the bot
@BOT.message_handler(commands=['start'])

def send_welcome(message):
    BOT.send_message(message.chat.id, 'Bienvenido a Dolar-Bot.' + '\n' +
                 'Bot para visualizar el último estado de las mesas de cambios '+
                 'según la pagina oficial del Banco Central de Venezuela')
    
    BOT.send_message(message.chat.id, 'Escriba el comando : /cambios ' 
                                    + 'para visualizar el último estado de las mesas de cambios '
                                    + 'según la pagina oficial del Banco Central de Venezuela ')
    
#Show currency changes command
@BOT.message_handler(commands=['cambios'])

def send_requested_info_by_option(message): 
    BOT.send_message(message.chat.id, 'Cambios según el Banco Central de Venezuela '
                                    + '\n' + currency_format( currency_list ) )
    
    BOT.send_message(message.chat.id, '¿Desea calcular un cambio? escriba : /calcularCambio')

#Select currency changes command
@BOT.message_handler(commands=['calcularCambio'])

def select_currency(message): 
    BOT.send_message(message.chat.id, 'Para calcular el cambio selecione la moneda ' +
                                    'y luego ingrese la cantidad.' + '\n' +
                                    'Cambios: /EUR , /CNY , /TRY , /RUB , /USD ' + '\n' +
                                    'Por ejemplo : /USD 20.12')

#Select currency changes command
@BOT.message_handler(commands=REF_NAMES)
def calculate_requested_currency(message): 
    try:
        # comment: try for cacth answer without an amount to 
        # calculate exchange
        BOT.send_message(message.chat.id, 'El monto en bolivares del cambio: '
                                    + message.text +
                                    ' es de : ' +
                                    calculate_currency_exchage( currency_list, message.text ) +
                                    ' Bs'
                                    )
    except TypeError as e:
        BOT.send_message(message.chat.id, 'Debe agregar una cantidad'+
                         'para hacer calculos'+ '\n' +
                         'Por ejemplo : /USD 20.12')
        print('Handling run-time error:', e)
    # end try
