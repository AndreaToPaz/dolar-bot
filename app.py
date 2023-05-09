from flask import Flask
import tweepy
import configparser
import telebot


# Read KEYS from Config file
config = configparser.ConfigParser()
config.read('config.ini')

#Twitter Keys
API_KEY = config ['Twitter'] ['API_KEY']
API_KEY_SECRET = config ['Twitter'] ['API_KEY_SECRET']
ACCESS_TOKEN = config ['Twitter'] ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config ['Twitter'] ['ACCESS_TOKEN_SECRET']

#Telegram Bot Key
#BOT_KEY = config ['Telegram'] ['BOT_KEY']

#COMMAND
bot = telebot.TeleBot('6202663089:AAFEAGaFqRPoayB2rbZxH5Y0LvvNSsLpmJU')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

bot.infinity_polling()


# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#    return 'Hello world!'