from telegram import Update, ChatAction
from telegram.ext import CallbackContext

from ..utils import send_action
from ..pages import set_new_phone_page


@send_action(ChatAction.TYPING)
def contact_callback(update: Update, context: CallbackContext) -> None:
    set_new_phone_page(update=update, context=context)


@send_action(ChatAction.TYPING)
def text_messages_callback(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="🙂")

