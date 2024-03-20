from telebot import TeleBot, InlineKeyboardMarkup

API_TOKEN = '6779226413:AAEOnToeoYGYfOE_A7DnzJ836_N4MmRSPaA'

bot = TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(
        f'Искать',
        callback_data='search'
    )
    bot.send_message(
        message.chat.id,
        f'Привет, в этом боте ты можешь найти информацию о рыбах которые обитают в Беларуси, где их ловить и другую информацию.',
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda callback: True)
def callback_query_handler(callback):
    if callback.data == 'search':
        bot.send_message(callback.id, "Вы нажали Кнопку 1")


@bot.message_handler()
def echo(message):
    bot.send_message(
        message.chat.id,
        message.text
    )


bot.infinity_polling()
