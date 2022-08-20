from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from .commands import Commands


class AdminStates:
    prepare_mailing = 1
    received_mailing = 2
    receive_new_tests = 3


class AdminCallbackData:
    statistics = 'statistics'
    mailing = 'mailing'
    backup = 'backup'


class AdminReplyButtons:
    send_mailing = KeyboardButton(text='Send')
    preview_mailing = KeyboardButton(text='Preview')
    cancel_mailing = KeyboardButton(text='Cancel')


class AdminKeyboard:
    main = ReplyKeyboardMarkup([[f'/{Commands.admin.command}']], resize_keyboard=True)

    admin = InlineKeyboardMarkup([
        [InlineKeyboardButton('Check statistics', callback_data=AdminCallbackData.statistics)],
        [InlineKeyboardButton('Create broadcast', callback_data=AdminCallbackData.mailing)],
        [InlineKeyboardButton('Backup database', callback_data=AdminCallbackData.backup)],
    ], resize_keyboard=True)

    mailing = ReplyKeyboardMarkup([
        [AdminReplyButtons.send_mailing],
        [AdminReplyButtons.preview_mailing, AdminReplyButtons.cancel_mailing]
    ], resize_keyboard=True)


class AdminMessages:

    # admin panel
    admin = 'Welcome to the admin panel!'

    statistics = (
        "Bot's statistics:\n\n"
        'Users in total: <b>{total_users}</b>\n'
        'Active users: <b>{active_users}</b>'
    )

    mailing = 'Send a messaged for the broadcast'

    received_mailing = "The message has been received. What's next?"

    mailing_canceled = 'Broadcast has been cancelled'

    mailing_started = 'Broadcast had started'

    mailing_finished = (
        'Message has been sent:\n\n'
        'Users that perceived the message: {sent_count}'
    )

    unexpected_error = '<code>Telegram Error: {error}.\n\n{update}</code>'

    backup = 'Backup of the database ({})'

    database_not_found = 'Database not found'
