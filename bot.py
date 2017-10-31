#!/usr/bin/python

import logging
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters, CallbackQueryHandler
import requests
import time, threading

r = 0

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
#Variable global con el precio

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hola! acabo de iniciarme, como estas?")

def get_price(bot, update):
    global r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR")
    #bot.send_message(chat_id=update.message.chat_id, text="Cuando este completo, aqui te devolvere el precio")
    #print r.content
    bot.send_message(chat_id=update.message.chat_id, text=r.content)


def update_price():
    global r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR")
    threading.Timer(30, update_price).start()
    

def main():

    logger.info('Start!!!')

    updater = Updater(token='404730621:AAGIEK7qkzXrmJiGZ5-FnkDOmubmDRWRYoA')

    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", start)
    price_handler = CommandHandler("getPrice", get_price)
    update_price()

    dispatcher.add_handler(price_handler)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
