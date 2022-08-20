from telegram.ext import (
    CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler, Filters
)
from configparser import ConfigParser

from .constants import Commands, AdminCallbackData, AdminStates, AdminReplyButtons
from .callbacks import *

# parse config
config = ConfigParser()
config.read('config.ini')

# parser admin list
admins = tuple(map(int, config.get('bot', 'admins').split(',')))

# general command handlers
admin_handler = CommandHandler(
    command=Commands.admin.command, callback=admin_command_callback,
    filters=Filters.user(user_id=admins),
    run_async=True
)

start_handler = CommandHandler(
    filters=Filters.chat_type.private,
    command=Commands.start.command,
    callback=start_command_callback,
    run_async=True
)

# admin handlers
statistics_handler = CallbackQueryHandler(
    pattern=AdminCallbackData.statistics,
    callback=statistics_callback,
    run_async=True
)

backup_handler = CallbackQueryHandler(
    pattern=AdminCallbackData.backup,
    callback=backup_callback,
    run_async=True
)

photoAdminHandler = MessageHandler(
    filters=Filters.user(user_id=admins) & Filters.document,
    callback=photo_callback,
    run_async=True
)

# mailing handlers
mailing_conversation_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(pattern=AdminCallbackData.mailing, callback=mailing_callback)],
    states={
        AdminStates.prepare_mailing: [MessageHandler(callback=mailing_message_callback, filters=Filters.all)],
        AdminStates.received_mailing: [
            MessageHandler(filters=Filters.text(AdminReplyButtons.preview_mailing.text),
                           callback=preview_mailing_callback),
            MessageHandler(filters=Filters.text(AdminReplyButtons.cancel_mailing.text),
                           callback=cancel_mailing_callback),
            MessageHandler(filters=Filters.text(AdminReplyButtons.send_mailing.text), callback=send_mailing_callback)
        ]
    },
    fallbacks=[]
)

contact_handler = MessageHandler(
    filters=Filters.contact & Filters.chat_type.private & ~Filters.user(user_id=admins),
    callback=contact_callback,
    run_async=True
)

text_messages_handler = MessageHandler(
    filters=Filters.text & ~Filters.contact & ~Filters.command & Filters.chat_type.private &
            ~Filters.user(user_id=admins),
    callback=text_messages_callback,
    run_async=True
)