from telegram import Update, ChatAction, ParseMode
from telegram.ext import CallbackContext

from ..constants import (
    AdminMessages, AdminKeyboard, Messages, Keyboards, Steps
)
from ..utils import send_action
from ..database import DataBaseUsers

from ..pages import greeting_with_customer_page, new_ask_phone_page


# admin panel
@send_action(ChatAction.TYPING)
def admin_command_callback(update: Update, context: CallbackContext) -> None:

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=AdminMessages.admin, reply_markup=AdminKeyboard.admin
    )


# start command callback
@send_action(ChatAction.TYPING)
def start_command_callback(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    with DataBaseUsers() as dbu:

        if dbu.check_user(telegram_id=user_id):
            greeting_with_customer_page(update=update, context=context)

        else:
            new_ask_phone_page(update=update, context=context)
