from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import fishes

API_TOKEN = '6779226413:AAEOnToeoYGYfOE_A7DnzJ836_N4MmRSPaA'

bot = TeleBot(API_TOKEN)



@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    search = InlineKeyboardButton(f'Искать', callback_data='search')
    markup.row(search)
    bot.send_message(
        message.chat.id,
        f'Привет, в данном боте ты можешь найти информацию о рыбах Беларуси.',
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda callback: True)
def get_callback(callback):
    if callback.data == 'search':
        bot.send_message(callback.message.chat.id, f'Введите название рыбы:')
        bot.register_next_step_handler(callback.message, search)


def search(message):
    if message.text.lower() == 'окунь':
        bot.send_message(message.chat.id, fishes.perch)


bot.infinity_polling()
