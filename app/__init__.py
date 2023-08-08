import configparser

# Read URL from config.ini
config = configparser.ConfigParser()
config.read('config.ini') 

#TELEGRAM BOT KEY
BOT_KEY = config ['Telegram'] ['BOT_KEY']
#BANK URL
BANK_URL = config ['BancoDeVenezuela'] ['BANK_URL'] 