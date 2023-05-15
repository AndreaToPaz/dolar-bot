from flask import Flask
import tweepy
import configparser
import telebot
from telebot import types


# READ KEYS FROM CONFIG INI
config = configparser.ConfigParser()
config.read('config.ini')

#TWITTER KEYS
API_KEY = config ['Twitter'] ['API_KEY']
API_KEY_SECRET = config ['Twitter'] ['API_KEY_SECRET']
ACCESS_TOKEN = config ['Twitter'] ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config ['Twitter'] ['ACCESS_TOKEN_SECRET']
#TWITTER AUTH
TWITTER_AUTH = tweepy.OAuthHandler(API_KEY,API_KEY_SECRET)
TWITTER_AUTH.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
TWITTER_API = tweepy.API(TWITTER_AUTH)

#TELEGRAM BOT KEY
BOT_KEY = config ['Telegram'] ['BOT_KEY']
#BOT AUTH
BOT = telebot.TeleBot(BOT_KEY) 


# #INLINE KEYBOARD BUTTONS
# markup = types.ReplyKeyboardMarkup(row_width=2)
# item_btn_a = types.KeyboardButton('BancoCentral')
# item_btn_b = types.KeyboardButton('DolarParalelo')
# item_btn_c = types.KeyboardButton('Ambos')
# markup.add(item_btn_a, item_btn_b, item_btn_c)

# #COMMANDS
# @BOT.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     BOT.reply_to(message, B'ienvenido a Dolar-Bot, Bot para ver el cambio del dolar')
#     BOT.send_message(message.chat.id, 'Escoga una opción', reply_markup=markup)

# @BOT.message_handler(commands=['BancoCentral', 'DolarParalelo','Ambos'])
# def send_requested_info(message):
#     #La cosa de aqui que no se como hacer
#     BOT.send_message(message.chat.id, 'Escoga una opción', reply_markup=markup)
    
# BOT.infinity_polling()

#SETTING 
#username = 'BCV_ORG_VE'
username = 'monitordolarvla'
tweets_list= TWITTER_API.user_timeline(screen_name = username, count=1, tweet_mode='extended')
tweet= tweets_list[0] # An object of class Status (tweepy.models.Status)
print(tweet.created_at) # Print the datetime object for the tweet
print(tweet.full_text) # Print the text of the tweet
print(tweet.entities['media'][0]['media_url_https'])

@BOT.message_handler(commands=['start', 'help'])
def send_welcome(message):
    BOT.reply_to(message, 'Bienvenido a Dolar-Bot, Bot para ver el cambio del dolar')
    BOT.reply_to(message, tweet.entities['media'][0]['media_url_https'])
    
BOT.infinity_polling()


# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#    return 'Hello world!'