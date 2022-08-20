# from configparser import ConfigParser
#
# config = ConfigParser()
# config.read('config.ini')
# card_number = config.get(section='branch info', option='card_number')
# phone_number = config.get(section='branch info', option='phone_number')


class Messages:

    greeting = dict(
        uz="Assalomu alaykum, {}!\nBizni tanlaganingizdan xursandmiz!"
    )

    phone_not_found = dict(
        uz="Sizning ma'lumotlaringiz topilmadi. Adminga murojaat qiling."
    )

    ask_language = "Tilni tanlang!\n" \
                   "Выберите язык!"

    request_phone_number = dict(
        uz="Kontakt yuboring",
        ru="Отправить контакт"
    )

    request_fullname = dict(
        uz="Ism familiyangizni kiriting!",
        ru="Введите свое имя и фамилию!"
    )

    request_birthdate = dict(
        uz="Tug'ilgan kuningiz bilan qachon tabriklaylik? \nShu formatda kiriting KK.OO.YYYY",
        ru="Когда вас поздравить с Днём Рождения ? \nУкажите в формате ДД.ММ.ГГГГ "
    )

    home = dict(
        uz="Juda yaxshi! Birgalikda buyurtma beramizmi? 😃",
        ru="Супер! Хотите ещё что-то заказать ?"
    )

    info = dict(
        uz="Biz sizni kutamiz! \n\nTelefon :  +998 99 480 88 77 \n\nManzil : C-5, Yunusobod tumani, 60/62",
        ru="Мы ждем вас! \n\nТелефон: +998 99 480 88 77 \n\nАдрес: Юнусабадский р-н, Ц-5, 60/62"
    )

    feedback = dict(
         uz="✅Sushi yummy ni tanlaganingiz uchun raxmat. Agar Siz bizning xizmatlarimiz sifatini yaxshilashga "
            "yordam bersangiz benihoya xursand bo'lamiz. Buning uchun 3 ballik tizim asosida baholang",
         ru="✅Контроль сервиса доставки Sushi yummy Мы благодарим за сделанный выбор и будем рады, "
            "если Вы поможете улучшить качество нашего сервиса! Оцените нашу работу по 3 бальной шкале."
     )

    response_feedback = dict(
        uz="Fikr va mulohazalaringiz uchun raxmat!",
        ru="Спасибо за ваш отзыв!"
    )

    feedback_reason = dict(
        uz="Xizmatlarimizda qanday muomma va kamchiliklar bo'lsa yozib qoldirishingiz mumkin!",
        ru="Вы можете записать любые проблемы и недостатки в наши услуги!"
    )

    settings = dict(
        uz="⚙ Sozlamalar",
        ru="⚙ Настройки"
    )

    request_location = dict(
        uz="Qayerdasiz 👀? Agar lokatsiyangizni📍 yuborsangiz, sizga eng yaqin filialni aniqlaymiz",
        ru="Где вы находитесь 👀? Если вы отправите локацию 📍, мы определим ближайший к вам филиал"
    )

    submit_location = dict(
        uz="Lokatsiyangizni tastiqlaysizmi?",
        ru="Вы подтверждаете свое местоположение?"
    )

    distance = dict(
        ru="Ориентировочное расстояние от филиала: {} км.",
        uz="Shaxobchagacha bo'lgan taxminiy masofa: {} km."
    )

    order_menu = dict(
        ru="С чего начнем?",
        uz="Nimadan boshlaymiz?"
    )

    select_sub_category = dict(
        uz="Kategoriyani tanlang",
        ru="Выбрать категорию"
    )

    select_product = dict(
        uz="Mahsulotni tanlang",
        ru="Выберите продукт"
    )

    quantity = dict(
        uz="Miqdorini kiriting:",
        ru="Введите количество:"
    )

    empty_cart = dict(
        uz="Sizning savatingiz bo'sh, buyurtma berish uchun mahsulot tanlang.",
        ru="Ваша корзина пуста, выберите товар для заказа."
    )

    cart_info = dict(
        uz="📥 Savat:\n\n{}\nUmumiy: {} so'm",
        ru="📥 Корзина:\n\n{}\nИтого: {} сум"
    )

    cart_info_payment = dict(
        uz="📥 Savat:\n\n{}\nYetkazib berish narxi:\n{} so'm\n\nUmumiy: {} so'm",
        ru="📥 Корзина:\n\n{}\nСтоимость доставки:\n{} сум\n\nИтого: {} сум"
    )

    currency = dict(
        uz="so'm",
        ru="сум"
    )

    cart_clear = dict(
        uz="«❌ Mahsulot nomi» - savatdan o'chirish \n"
           "«🔄 Tozalash» - savatni butunlay bo'shatish",
        ru="«❌ Наименование » - удалить одну позицию \n"
           "«🔄 Очистить » - полная очистка корзины"
    )

    deliver_or_take = dict(
        uz="Buyurtmani o'zingiz olib keting yoki Yetkazib berishni tanlang.",
        ru="Заберите заказ сами или выберите Доставку."
    )

    near_location = dict(
        uz="📍 Bizning sizga eng yaqin filialimiz.",
        ru="📍 Наш ближайший к вам филиал."
    )

    take_order = dict(
        uz="Ushbu filialimizdan buyurtmangizni olib ketishiniz mumkin. 😊",
        ru="Вы можете забрать свой заказ в этом отделении. 😊"
    )

    payment_type = dict(
        uz="To'lovni qaysi turda amalga oshirasiz.",
        ru="В каком раунде вы делаете платеж."
    )

    online_payment = dict(
        uz="Ushbu plastik raqamga to'lovni amalga oshirasiz: \n\n 8600000000000000",
        ru="Вы платите за этот пластиковый номер: \n\n 8600000000000000"
    )

    offline_payment = dict(
        uz="Buyurtmalaringiz tez orada yetkazib beriladi.",
        ru="Ваши заказы будут доставлены в ближайшее время."
    )

    # payment_info = dict(
    #     uz=f"Ushbu plastik raqamga to'lovni amalga oshirishingiz mumkin.\n<code>{card_number}</code>\n\n"
    #        "Yoki yetkazib beruvchi xodimimizga naqt pul shaklida to'lov qilishingiz mumkin.\n"
    #        f"Aloqa uchun: <code>{phone_number}</code>",
    #     ru=f"Вы можете произвести оплату на этот пластиковый номер.\n<code>{card_number}</code>\n\n"
    #        "Или вы можете заплатить нашему сотруднику службы доставки наличными.\n"
    #        f"Контакт: <code>{phone_number}</code>"
    # )

    order_received = dict(
        uz="Buyurtmangiz qabul qilindi.✅",
        ru="Ваш заказ передан на обработку! \nОжидайте звонок от оператора!"
    )

    order_info_for_staff = dict(
        uz="Buyurtma: \n\n{}\nUmumiy: {} so'm\n\n"
           "Kimdan <b>{}</b>\n"
           "📞 <code>{}</code>\n"
           "Lokatsiya: <code>{}</code>\n\n"
           "{}\n\n"
           "{}",
        ru="Заказ:\n\n{}\nИтого: {} сум\n\n"
           "От кого: <b>{}</b>\n"
           "📞 <code>{}</code>\n"
           "Локация: <code>{}</code>\n\n"
           "{}\n\n"
           "{}"
    )

    order_info_for_staff_deliver = dict(
        uz="Buyurtma: \n\n{}\nYetkazib berish:\n<b>{}</b> so'm\n\nUmumiy: {} so'm\n\n"
           "To'lov turi: {}\n\n"
           "Kimdan <b>{}</b>\n"
           "📞 <code>{}</code>\n"
           "Lokatsiya: <code>{}</code>\n\n"
           "{}\n\n"
           "Manzil:\n{}\n\n"
           "{}",
        ru="Заказ:\n\n{}\nСтоимость доставки:\n<b>{}</b> сум\n\nИтого: {} сум\n\n"
           "Тип оплаты: {}\n\n"
           "От кого: <b>{}</b>\n"
           "📞 <code>{}</code>\n"
           "Локация: <code>{}</code>\n\n"
           "{}\n\n"
           "Адрес:\n{}\n\n"
           "{}"
    )

    to_deliver = dict(
        uz="Yetkazib berish kerak.",
        ru="Нужно доставить."
    )

    to_take = dict(
        uz="Olib ketadi",
        ru="Сам(а) забрать"
    )

    our_location = dict(
        uz="Bizning manzilimiz. Sizni kutamiz.",
        ru="Наш адресс. Мы ждем вас."
    )

    happy_birthday = dict(
        uz="Tug'ilgan kuningiz bilan 🎉 \n\nSushi Yummy'dan siz uchun kichik sovg'a🎁 "
           "bor, 99 480 88 77 raqami orqali bilib olishingiz mumkin.",
        ru="Поздравляем вас с днем рождения 🎉 \n\nДля вас есть небольшой подарок🎁"
           " от Sushy Yummy, можете узнать по контакту 99 480 88 77"
    )

    full_address = dict(
        uz="To'liq manzillingizni yozing.\nNamuna: Mahalla, Ko'cha, Uy/Xonadon.\n"
           "Qaysi vaqtda siz o'z buyurtmangizni qabul/olib ketishni xohlaysiz?",
        ru="Введите свой полный адрес. \nПример: Район, Улица, Дом/Квартира.\n"
           "В какое время вы хотите получить/забрать свою доставку?"
    )

    time_limit = dict(
        uz="Xizmatdan faqat 9.00 va 23.00 oralig'ida foydalana olasiz!",
        ru="Воспользоваться услугой можно только с 9.00 до 23.00!"
    )

    ask_payment_type = dict(
        uz="To'lov turini tanlang",
        ru="Выберите тип оплаты"
    )

    reject_order = dict(
        uz="Buyurtma sizga yetqazilishi uchun eng kamida 80 000 so'mlik nahsulotlarni xarid qilishingiz kerak!",
        ru="Вам необходимо купить продукции на сумму не менее 80 000 сумов, чтобы заказ был доставлен Вам!"
    )



