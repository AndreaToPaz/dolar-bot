# 💸💸Dolar-bot💸💸
Telegram Bot to calculate the exchange rate between Venezuelan currency and currencies supported by the Central Bank of Venezuela (EUR, CNY, TRY, RUB, USD).

**It is called "dolar-bot" because is the most common exchange operation use in Venezuela**

To use and edit this bot a **config.ini** file needs to be add in the root of the project. 
The document needs to have the following structure :

```
[Telegram]
BOT_KEY = Your Bot Key
[BancoDeVenezuela]
BANK_URL = https://www.bcv.org.ve/
```
Your bot key is the Bot key provide by the **[BotFather]([https://eff.org](https://t.me/BotFather)https://t.me/BotFather)** when you create a telegram bot.

**THIS BOT WORK BY DOING WEB SCRAPING TO THE WEB PAGE OF EL BANCO CENTRAL DE VENEZUELA**

This means it will not working with **OTHER** currency exchange information pages.
