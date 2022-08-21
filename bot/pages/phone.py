from telegram import Update, ParseMode
from telegram.ext import CallbackContext
from ..constants import Messages, Keyboards
from ..database import DataBaseUsers, Languages


def greeting_with_customer_page(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    with DataBaseUsers() as dbu:
        lang = dbu.get_value(telegram_id=user_id, item=dbu.Items.language)
        first_name = dbu.get_value(telegram_id=user_id, item=dbu.Items.first_name)
    context.bot.send_message(chat_id=user_id, text=Messages.greeting[lang].format(first_name),
                             parse_mode=ParseMode.HTML)


def new_ask_phone_page(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    lang = Languages.uz
    context.bot.send_message(chat_id=user_id, text=Messages.request_phone_number[lang], parse_mode=ParseMode.HTML,
                             reply_markup=Keyboards.contact[lang])


def set_new_phone_page(update: Update, context: CallbackContext) -> bool:
    user_id = update.effective_user.id
    lang = Languages.uz
    if update.message.contact:
        phone_number = "+" + update.message.contact.phone_number
        with DataBaseUsers() as dbu:
            if dbu.check_user_by_phone(phone_number=phone_number):
                dbu.set_value_by_phone(phone_number=phone_number, item=dbu.Items.telegram_id, data=user_id)
                greeting_with_customer_page(update=update, context=context)
            else:
                context.bot.send_message(chat_id=user_id, text=Messages.phone_not_found[lang],
                                         parse_mode=ParseMode.HTML)
            return True

    else:
        context.bot.send_message(chat_id=user_id, text=Messages.request_phone_number[lang], parse_mode=ParseMode.HTML,
                                 reply_markup=Keyboards.contact[lang])
        return False

