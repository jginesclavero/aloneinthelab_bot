#!/usr/bin/python

import logging
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters, CallbackQueryHandler
import requests
import time, threading
import re
import json

r = 0
limit = 1.0
bot_global = 0
update_global = 0

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hola! acabo de iniciarme, como estas?")

def get_price(bot, update):
    global r
    global bot_global
    global update_global
    logger.info('getPrice recibido')
    #logger.info(r.content)
    msg = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETN&tsyms=USD,EUR")
    data = json.loads(msg.content)
    bot.send_message(chat_id=update.message.chat_id, text=data)
    bot_global = bot
    update_global = update


def update_price():
    global r
    global limit
    global bot_global
    global update_global
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETN&tsyms=USD,EUR")
    threading.Timer(30, update_price).start()
    data = json.loads(r.content)
    #print (data["USD"])
    if float(data["USD"]) >= limit:
        bot_global.send_message(chat_id=update_global.message.chat_id, text="ETN tiene un valor de 1$, ya teneis para un viaje a Maldivas")

def get_help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="AloneInTheLab Bot, Mision ETN. Monitorizacion de precio y aviso cuando se alcance el valor de 1$. Comandos: /getPrice (Obtener precio actual del ETN)")


def main():

    logger.info('Start!!!')

    updater = Updater(token='404730621:AAGIEK7qkzXrmJiGZ5-FnkDOmubmDRWRYoA')

    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", start)
    price_handler = CommandHandler("getPrice", get_price)
    help_handler = CommandHandler("help", get_help)


    update_price()

    dispatcher.add_handler(price_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
