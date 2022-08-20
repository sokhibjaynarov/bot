from config import config
import pandas as pd
import psycopg2
import urllib.parse as up
from configparser import ConfigParser


class Languages:
    uz = "uz"
    ru = "ru"


# parse config
conf = ConfigParser()
conf.read('config.ini')

db = config(filename='config.ini', section='database')

up.uses_netloc.append("postgres")
url = up.urlparse(db["database_url"])


class DataBaseUsers:

    class Items:
        id = 'Id'
        first_name = '"FirstName"'
        last_name = '"LastName"'
        phone_number = '"PhoneNumber"'
        telegram_id = '"TelegramId"'
        step = '"Step"'
        car_number = '"CarNumber"'
        car_model = '"CarModel"'
        state = '"State"'
        updated_by = '"UpdatedBy"'
        isActive = '"IsActive"'
        language = '"Language"'

    class Tables:
        users = '"Users"'
        orders = '"Orders"'
        employees = '"Employees"'

    def __init__(self, name='"Users"'):
        self.connection = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )

        self.cur = self.connection.cursor()
        self.name = name

    def __enter__(self):
        return self

    def __exit__(self, ex_type, value, traceback):
        self.close()

    def close(self):
        self.connection.close()

    def check_user(self, telegram_id):
        stat = f'SELECT EXISTS(SELECT 1 FROM {self.name} WHERE {self.Items.telegram_id} = %s);'
        self.cur.execute(stat, (str(telegram_id),))
        result = self.cur.fetchone()[0]
        return result

    def check_user_by_phone(self, phone_number):
        stat = f'SELECT EXISTS(SELECT 1 FROM {self.name} WHERE {self.Items.phone_number} = %s)'
        self.cur.execute(stat, (phone_number,))
        result = self.cur.fetchone()[0]
        return result

    def set_value(self, telegram_id, item, data):
        if self.check_user(telegram_id):
            try:
                query = f'UPDATE {self.name} SET {item} = %s WHERE {self.Items.telegram_id} = %s;'
                self.cur.execute(query, (data, str(telegram_id)))
                self.connection.commit()
            except psycopg2.Error:
                return False
        else:
            return True

    def set_value_by_phone(self, phone_number, item, data):
        if self.check_user_by_phone(phone_number):
            try:
                query = f'UPDATE {self.name} SET {item} = %s WHERE {self.Items.phone_number} = %s;'
                self.cur.execute(query, (data, phone_number))
                self.connection.commit()
            except psycopg2.Error:
                return False
        else:
            return True

    def get_value(self, telegram_id, item):
        if self.check_user(telegram_id):
            try:
                query = f'SELECT {item} FROM {self.name} WHERE {self.Items.telegram_id} = %s'
                self.cur.execute(query, (str(telegram_id),))
                result = self.cur.fetchone()[0]
                return result
            except psycopg2.Error:
                return False

    # def add_user(self, id):
    #     if not self.check_user(id):
    #         stat = f'INSERT INTO {self.name} ({self.Items.id}, {self.Items.step}, {self.Items.isActive}) ' \
    #                f'VALUES (%s, 0, 1) ON CONFLICT ({self.Items.id}) DO NOTHING;'
    #         self.cur.execute(stat, (id, ))
    #         self.connection.commit()

    def update_user(self, phone_number, telegram_id):
        pass

    def get_users_amount(self):
        stat = f'SELECT Count(*) FROM {self.name};'
        self.cur.execute(stat)
        return self.cur.fetchone()[0]

    def get_users(self):
        self.cur.execute(f"SELECT {self.Items.telegram_id} FROM {self.name}")
        rows = self.cur.fetchall()
        return [row[0] for row in rows]

    def get_actives(self):
        stat = f'SELECT Count(*) FROM {self.name} WHERE {self.Items.isActive} = True'
        self.cur.execute(stat)
        inactive_users = self.cur.fetchone()[0]
        users = self.get_users_amount()
        active_users = users - inactive_users
        return active_users

    def get_table(self, file_name, table_name):
        stat = f"COPY (SELECT * FROM {table_name}) TO STDOUT WITH CSV DELIMITER ','"
        with open(file_name, 'w') as f:
            self.cur.copy_expert(stat, f)
