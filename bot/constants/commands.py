from telegram import BotCommand


class Commands:
    start = BotCommand(command='start', description="Botni qayta yuklash")
    admin = BotCommand(command='admin', description='admin panel')