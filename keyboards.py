from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def generate_google():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text='Wekipedia🌍')
    markup.add(btn)
    return markup
