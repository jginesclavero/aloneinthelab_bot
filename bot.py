#!/usr/bin/python

import logging
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters, CallbackQueryHandler


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hola! acabo de iniciarme, como estas?")

def get_price(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Cuando este completo, aqui te devolvere el precio")

def main():

    logger.info('Start!!!')

    updater = Updater(token='404730621:AAGIEK7qkzXrmJiGZ5-FnkDOmubmDRWRYoA')

    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", start)
    price_handler = CommandHandler("getPrice", get_price)

    dispatcher.add_handler(price_handler)
    dispatcher.add_handler(start_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
