from telebot import TeleBot

API_TOKEN = '6779226413:AAEOnToeoYGYfOE_A7DnzJ836_N4MmRSPaA'

bot = TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        f'Привет, я Эхобот. Я здесь для того, чтобы повторять за вами ваши добрые слова. Просто скажите что-нибудь приятное, и я скажу вам то же самое!'
    )


@bot.message_handler()
def echo(message):
    bot.send_message(
        message.chat.id,
        message.text
    )


bot.infinity_polling()
