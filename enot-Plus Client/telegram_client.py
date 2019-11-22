import telebot
from telebot import TeleBot

bot = telebot.TeleBot('876545007:AAE7_VAtsw_C4BCK9bQ--vHClakQNLMRLcc')
proxy = ""


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Вас приветствует бот енот)")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message.from_user)
    bot.reply_to(message, message.text)


def start_Tbot():
    bot.polling(none_stop=True, interval=0)
    print("Бот запущен")


def stop_Tbot():
    bot.stop_polling()
    print("Бот остановлен")

    # def send_Message(self):
