from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
#Кнопка для отправки номера телефона
def phone_number_kb():
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    button=KeyboardButton("Поделиться контактом",request_contact=True)
    kb.add(button)
    return kb

#Кнопка для отправки локации
def location_kb():
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    button=KeyboardButton("Поделиться геолокацией",request_location=True)
    kb.add(button)
    return kb

# Кнопка для выбоора пола
def gender_kb():
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    button=KeyboardButton("Мужчина")
    button1 = KeyboardButton("Женщина")
    kb.add(button,button1)
    return kb

# Кнопки для выбора количества
def product_count():
    kb = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    buttons=[KeyboardButton(str(i)) for i in range(1,10)]
    back = KeyboardButton("Назад")
    kb.add(*buttons,back)
    return kb

# Кнопки для корзины
def cart_kb():
    kb=ReplyKeyboardMarkup(resize_keyboard=True)
    button=KeyboardButton("Очистить")
    button1 = KeyboardButton("Оформить")
    button2= KeyboardButton("Редактировать")
    button3=KeyboardButton("Назад")
    kb.add(button,button1,button2,button3)
    return kb

# кнопки при выборе способа оплаты
def pay_type_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Наличные")
    button1 = KeyboardButton("Картой")
    button3 = KeyboardButton("Назад")

    kb.add(button, button1,button3)
    return kb
# Кнопки для оформления заказа
def confirmation_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Подтвердить")
    button1 = KeyboardButton("Отменить")
    button3 = KeyboardButton("Назад")

    kb.add(button, button1, button3)
    return kb




#Кнопки с названиями товара
def products_kb():
    pass