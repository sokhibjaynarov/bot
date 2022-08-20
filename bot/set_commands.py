from telegram import Bot
from .constants import Commands

CommandsList = [
    Commands.start,
]


def set_commands(bot: Bot):
    bot.set_my_commands(commands=CommandsList)

