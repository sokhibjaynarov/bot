import datetime
from functools import wraps

import pytz
from telegram import Update
from telegram.ext import CallbackContext


def send_action(action):
    def decorator(func):
        @wraps(func)
        def command_func(update: Update, context: CallbackContext, *args, **kwargs):
            context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=action)
            return func(update, context, *args, **kwargs)

        return command_func

    return decorator


def time_in_range() -> bool:
    start = datetime.time(9, 0, 0)
    end = datetime.time(23, 0, 0)
    tz = pytz.timezone('Asia/Tashkent')
    current = datetime.datetime.now(tz).time()
    """Returns whether current is in the range [start, end]"""
    return start <= current <= end



