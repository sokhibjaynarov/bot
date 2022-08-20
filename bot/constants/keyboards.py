from telegram import ReplyKeyboardMarkup, KeyboardButton
from bot.constants.messages import Messages


class Languages:
    uz = "uz"
    ru = "ru"


class LanguagesText:
    uz = "O'zbek tili"
    ru = "Русский язык"


class KeyboardText:
    # menu keyboard words
    order = dict(
        uz="🛍 Buyurtma berish",
        ru="🛍 Заказать"
    )

    info = dict(
        uz="ℹ Ma'lumot",
        ru="ℹ Информация"
    )

    feedback = dict(
        uz="✍ Fikr bildirish",
        ru="✍ Оставить отзыв"
    )

    settings = dict(
        uz="⚙ Sozlamalar",
        ru="⚙ Настройки"
    )

    # settings menu keyboard

    fio = dict(
        uz="FIO ni o'zgartirish",
        ru="Изменить ФИО"
    )

    phoneNum = dict(
        uz="Raqamni o'zgartirish",
        ru="Изменить номер"
    )

    language = dict(
        uz="🇺🇿 Tilni tanlang",
        ru="🇷🇺 Выберите язык"
    )

    back = dict(
        uz="⬅ Orqaga",
        ru="⬅ Назад"
    )

    # order menu keyboard location

    location = dict(
        uz="📍 Mening Lokatsiyam",
        ru="📍 Мое местонахождение"
    )

    submit = dict(
        uz="✅ Ha mening manzilim",
        ru="✅ Да мой адрес"
    )

    send_location_again = dict(
        uz="🔄 Qayta yuborish",
        ru="🔄 Отправь снова"
    )

    cart = dict(
        uz="📥 Savat",
        ru="📥 Корзина"
    )

    make_order = dict(
        uz="🚘 Buyurtma berish",
        ru="🚘 Оформить заказ"
    )

    clear = dict(
        uz="🔄 Tozalash",
        ru="🔄 Очистить"
    )

    deliver = dict(
        uz="🚘 Yetkazib berish",
        ru="🚘 Доставка"
    )

    take_away = dict(
        uz="🏃 Olib ketish",
        ru="🏃 Самовывоз"
    )

    payment_cash = dict(
        uz="💵 Naqt",
        ru="💵 Наличные"
    )

    payment_card = dict(
        uz="💳 Plastik karta",
        ru="💳 Пластик карта"
    )


    end_order = dict(
        uz="Oldinga",
        ru="Вперед"
    )


class Keyboards:
    lang = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=LanguagesText.uz),
                KeyboardButton(text=LanguagesText.ru),
            ],
        ],
        resize_keyboard=True
    )

    contact = dict(
        uz=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="📞Yuborish", request_contact=True)
                ],
            ],
            resize_keyboard=True,
        ),
        ru=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="📞Отправить", request_contact=True)
                ],
            ],
            resize_keyboard=True,
        ),
        en=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="📞Send", request_contact=True)
                ],
            ],
            resize_keyboard=True,
        ),
    )

    # main menu keyboard
    def main_menu(lang: str) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=KeyboardText.order[lang])
                ],
                [
                    KeyboardButton(text=KeyboardText.info[lang]),
                    KeyboardButton(text=KeyboardText.feedback[lang])
                ],
                [
                    KeyboardButton(text=KeyboardText.settings[lang])
                ],
            ],
            resize_keyboard=True,
        )

    # settings menu keyboard

    def settings_keyboard(lang: str) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=KeyboardText.fio[lang]),
                    KeyboardButton(text=KeyboardText.phoneNum[lang])
                ],
                [
                    KeyboardButton(text=KeyboardText.language[lang])
                ],
                [
                    KeyboardButton(text=KeyboardText.back[lang])
                ],
            ],
            resize_keyboard=True,
        )

    # settings menu language keyboards
    def lang_keyboard(lang: str) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=LanguagesText.uz),
                    KeyboardButton(text=LanguagesText.ru)
                ],
                [
                    KeyboardButton(text=KeyboardText.back[lang])
                ]
            ],
            resize_keyboard=True,
        )

    # settings menu back keyboard
    def back_keyboard(lang: str) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=KeyboardText.back[lang])
                ]
            ],
            resize_keyboard=True,
        )

    # settings menu contact keyboard
    def contact_keyboard(lang: str) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=Messages.request_phone_number[lang], request_contact=True)
                ],
                [
                    KeyboardButton(text=KeyboardText.back[lang])
                ]
            ],
            resize_keyboard=True,
        )

    # settings menu feedback keyboard
    def feedback(lang: str) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="⭐⭐⭐")
                ],
                [
                    KeyboardButton(text="⭐⭐")
                ],
                [
                    KeyboardButton(text="⭐")
                ],
                [
                    KeyboardButton(text=KeyboardText.back[lang])
                ],
            ],
            resize_keyboard=True,
        )

    # order menu keyboard location
    def send_location(lang: str) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=KeyboardText.location[lang], request_location=True)
                ],
                [
                    KeyboardButton(text=KeyboardText.back[lang])
                ],
            ],
            resize_keyboard=True,
        )

    def submit_location(lang: str) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=KeyboardText.submit[lang])
                ],
                [
                    KeyboardButton(text=KeyboardText.send_location_again[lang])
                ],
            ],
            resize_keyboard=True,
        )

    def quantity_keyboard(lang) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="1"),
                    KeyboardButton(text="2"),
                    KeyboardButton(text="3")
                ],
                [
                    KeyboardButton(text="4"),
                    KeyboardButton(text="5"),
                    KeyboardButton(text="6")
                ],
                [
                    KeyboardButton(text="7"),
                    KeyboardButton(text="8"),
                    KeyboardButton(text="9")
                ],
                [
                    KeyboardButton(text=KeyboardText.cart[lang]),
                    KeyboardButton(text=KeyboardText.back[lang])
                ]
            ], resize_keyboard=True
        )

    def make_order(lang) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=KeyboardText.deliver[lang]),
                    KeyboardButton(text=KeyboardText.take_away[lang])
                ],
                [
                    KeyboardButton(text=KeyboardText.back[lang])
                ]
            ], resize_keyboard=True
        )

    def payment_type(lang) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=KeyboardText.payment_card[lang]),
                    KeyboardButton(text=KeyboardText.payment_cash[lang])
                ]
            ], resize_keyboard=True
        )

    def confirm_payment(lang) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=KeyboardText.end_order[lang]),
                    KeyboardButton(text=KeyboardText.back[lang])
                ]
            ], resize_keyboard=True
        )


