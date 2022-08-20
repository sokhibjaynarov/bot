from telegram.ext import Updater

from configparser import ConfigParser
import logging

from bot.callbacks import error_callback

from bot.handlers import (
    start_handler, admin_handler, text_messages_handler, contact_handler,
    statistics_handler, backup_handler, mailing_conversation_handler, photoAdminHandler,
)

from bot.set_commands import set_commands

# set up logger
logging.basicConfig(
    format='%(asctime)s – %(levelname)s – %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO
)

# parse config
config = ConfigParser()
config.read('config.ini')

# create updater
updater = Updater(token=config.get('bot', 'token'), use_context=True, workers=512)
dispatcher = updater.dispatcher


# bound handlers to dispatcher
def bound_handlers():
    # noinspection PyTypeChecker
    dispatcher.add_error_handler(error_callback)

    # general command handlers
    dispatcher.add_handler(admin_handler)
    dispatcher.add_handler(start_handler)

    # admin handlers
    dispatcher.add_handler(statistics_handler)
    dispatcher.add_handler(backup_handler)
    dispatcher.add_handler(photoAdminHandler)

    # mailing handlers
    dispatcher.add_handler(mailing_conversation_handler)

    # user's commands handler

    # user's message handlers
    dispatcher.add_handler(contact_handler)
    dispatcher.add_handler(text_messages_handler)


# set up webhook
def configure_webhook():
    pass


def main():
    # setting commands
    set_commands(bot=updater.bot)

    # setting up application
    bound_handlers()
    # configure_webhook()

    # start bot
    updater.start_polling()
    logging.info('hugecarwashbot has started')


if __name__ == '__main__':
    main()
