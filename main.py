from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardRemove
from keyboards import generate_google
import wikipedia
TOKEN = '7177311582:AAH2yBjBlVOoeC9rAWLqBJR1WTSH4lnfJrs'

bot = TeleBot(TOKEN, parse_mode='html')


@bot.message_handler(commands=['start'])
def command_start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "<i>Salom! Men wikipedia botiman!</i>",
                     reply_markup=generate_google())


@bot.message_handler(regexp='Wekipedia🌍')
def ask_word(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "O'zingizga qiziq bo'lgan so'zni kiriting ☺️",
                           reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, answer_to_user)


def answer_to_user(message: Message):
    chat_id = message.chat.id
    text = message.text
    wikipedia.set_lang('uz')
    try:
        data = wikipedia.summary(text)
        bot.send_message(chat_id, data)
    except:
        bot.send_message(chat_id, "Bunday malumot yo'q")
    ask_again(message)


def ask_again(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Yana so'z kiriting !")
    bot.register_next_step_handler(msg, answer_to_user)


bot.polling(none_stop=True)
