from telegram import Update, ParseMode
from telegram.ext import CallbackContext


from configparser import ConfigParser
from datetime import datetime
import os


from ..constants import AdminMessages, AdminStates
from ..database import DataBaseUsers


def statistics_callback(update: Update, context: CallbackContext):
    with DataBaseUsers() as dbu:
        total_users = dbu.get_users_amount()
        active_users = dbu.get_actives()

    response = AdminMessages.statistics.format(total_users=total_users, active_users=active_users)
    context.bot.edit_message_text(
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.message_id,
        text=response, parse_mode=ParseMode.HTML
    )


def mailing_callback(update: Update, context: CallbackContext):
    context.bot.edit_message_text(
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.message_id,
        text=AdminMessages.mailing
    )
    return AdminStates.prepare_mailing


def backup_callback(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    date = datetime.today().strftime('%d.%m.%Y')
    users = f"users_db_{date}.csv"
    employees = f"employees_db_{date}.csv"
    orders = f"orders_db_{date}.csv"

    try:
        with DataBaseUsers() as dbu:
            dbu.get_table(file_name=users, table_name=dbu.Tables.users)
        with open(users, 'rb') as f:
            context.bot.send_document(
                chat_id=update.effective_chat.id,
                caption=AdminMessages.backup.format(date),
                document=f
            )

        with DataBaseUsers() as dbu:
            dbu.get_table(file_name=employees, table_name=dbu.Tables.employees)
        with open(employees, 'rb') as f:
            context.bot.send_document(
                chat_id=update.effective_chat.id,
                caption=AdminMessages.backup.format(date),
                document=f
            )

        with DataBaseUsers() as dbu:
            dbu.get_table(file_name=orders, table_name=dbu.Tables.orders)
        with open(orders, 'rb') as f:
            context.bot.send_document(
                chat_id=update.effective_chat.id,
                caption=AdminMessages.backup.format(date),
                document=f
            )

    except Exception as e:
        context.bot.send_message(chat_id=user_id, text=str(e))

    # config = ConfigParser()
    # config.read('config.ini')
    # database_path = config.get('database', 'sqlite')
    #
    # date = datetime.today().strftime('%d.%m.%Y')
    #
    # context.bot.delete_message(
    #     chat_id=update.effective_chat.id,
    #     message_id=update.effective_message.message_id
    # )
    #
    # if os.path.isfile(database_path):
    #     with open(database_path, 'rb') as file:
    #         context.bot.send_document(
    #             chat_id=update.effective_chat.id,
    #             caption=AdminMessages.backup.format(date),
    #             document=file
    #         )
    #
    # else:
    #     context.bot.send_message(
    #         chat_id=update.effective_chat.id,
    #         text=AdminMessages.database_not_found
    #     )


def photo_callback(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    message_id = update.message.message_id
    document = update.message.document
    file_name = document.file_name
    try:
        with open('photos/' + file_name, 'wb') as f:
            context.bot.get_file(update.message.document).download(out=f)
        with open('photos/' + file_name, 'rb') as f:
            file_id = context.bot.send_photo(chat_id=user_id, photo=f).photo[-1].file_id
        context.bot.send_message(chat_id=user_id, text=f"<code>{file_id}</code>", reply_to_message_id=message_id,
                                 parse_mode=ParseMode.HTML)

    except Exception as e:
        context.bot.send_message(chat_id=user_id, text=str(e), reply_to_message_id=message_id)
