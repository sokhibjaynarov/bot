from telegram import Update, Message as TelegramMessage, TelegramError, Bot, PhotoSize, Animation, Video, ParseMode
from telegram.ext import CallbackContext, ConversationHandler

from threading import Thread
import logging
import time

from ..constants import AdminMessages, AdminKeyboard, AdminStates
from ..database import DataBaseUsers


def __send_photo(bot: Bot, message: TelegramMessage, user_id: int):
    photo = PhotoSize(
        file_id=message.photo[0].file_id,
        file_unique_id=message.photo[0].file_unique_id,
        width=message.photo[0].width,
        height=message.photo[0].height,
        file_size=message.photo[0].file_size
    )

    bot.send_photo(
        chat_id=user_id,
        photo=photo,
        caption=message.caption_html,
        parse_mode=ParseMode.HTML,
        reply_markup=message.reply_markup
    )


def __send_animation(bot: Bot, message: TelegramMessage, user_id: int):
    animation = Animation(
        file_id=message.animation.file_id,
        file_unique_id=message.animation.file_unique_id,
        width=message.animation.width,
        height=message.animation.height,
        duration=message.animation.file_size
    )

    bot.send_animation(
        chat_id=user_id,
        animation=animation,
        caption=message.caption_html,
        parse_mode=ParseMode.HTML,
        reply_markup=message.reply_markup
    )


def __send_video(bot: Bot, message: TelegramMessage, user_id: int):
    video = Video(
        file_id=message.video.file_id,
        file_unique_id=message.video.file_unique_id,
        width=message.video.width,
        height=message.video.height,
        duration=message.video.file_size
    )

    bot.send_video(
        chat_id=user_id,
        video=video,
        caption=message.caption_html,
        parse_mode=ParseMode.HTML,
        reply_markup=message.reply_markup
    )


def __send_message(bot: Bot, message: TelegramMessage, user_id: int):
    if message.photo:
        __send_photo(bot, message, user_id)

    if message.animation:
        __send_animation(bot, message, user_id)

    if message.video:
        __send_video(bot, message, user_id)

    elif message.text:
        bot.send_message(
            chat_id=user_id,
            text=message.text_html,
            parse_mode=ParseMode.HTML,
            reply_markup=message.reply_markup
        )


def __send_mailing(context: CallbackContext):
    message = context.user_data['mailing_message']
    with DataBaseUsers() as dbu:
        users = dbu.get_users()
    sent_count = 0

    for user in users:
        try:
            __send_message(bot=context.bot, message=message, user_id=user)
            sent_count += 1
            time.sleep(1 / 10)

            logging.info(f'Mailing message sent to user {user} (total: {sent_count})')

        except TelegramError as ex:
            if ex.message == 'Forbidden: bot was blocked by the user' or ex.message == 'Forbidden: user is deactivated'\
                    or ex.message == 'Chat not found':
                with DataBaseUsers() as dbu:
                    dbu.set_value(telegram_id=user, item=dbu.Items.isActive, data=False)

                logging.info(f'User {user} became inactive')

            else:
                logging.error(ex)

        except Exception as ex:
            logging.error(ex)

    return sent_count


def mailing_message_callback(update: Update, context: CallbackContext):
    context.user_data['mailing_message'] = update.message

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=AdminMessages.received_mailing,
        reply_markup=AdminKeyboard.mailing
    )

    return AdminStates.received_mailing


def preview_mailing_callback(update: Update, context: CallbackContext):
    message = context.user_data['mailing_message']
    __send_message(context.bot, message, update.effective_user.id)
    return AdminStates.received_mailing


def cancel_mailing_callback(update: Update, context: CallbackContext):
    del context.user_data['mailing_message']

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=AdminMessages.mailing_canceled,
        reply_markup=AdminKeyboard.main
    )

    return ConversationHandler.END


def __send_mailing_callback(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=AdminMessages.mailing_started,
        reply_markup=AdminKeyboard.main
    )

    logging.info('Mailing has started')
    sent_count = __send_mailing(context)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=AdminMessages.mailing_finished.format(sent_count=sent_count)
    )

    logging.info('Mailing has finished')
    return ConversationHandler.END


def send_mailing_callback(update: Update, context: CallbackContext):
    mailing_thread = Thread(target=__send_mailing_callback, args=(update, context))
    mailing_thread.start()
