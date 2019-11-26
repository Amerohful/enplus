import telebot
import DB

data = DB.DB()
name = data.get_users()
nameid = name[len(name) - 1][0]
lp = data.check_user(name[len(name) - 1][1], name[len(name) - 1][2])
bot1 = data.get_botid(lp[0][0])
bot = ""
try:
    if len(str(bot1[0][7])) == 0:
        print("Токен не существует. Использован стандартный токен")
        bot = telebot.TeleBot('1024164452:AAFQrAuvv5c8xqhEu3rYFM5vZYU2Q1K7FUw')
    else:
        print("токен верный")
        bot = telebot.TeleBot(bot1[0][7])
    botid = bot1[len(bot1) - 1][0]
except TypeError as e:
    print("Бот не найден. Бот работать не будет")
    bot = telebot.TeleBot('1024164452:AAFQrAuvv5c8xqhEu3rYFM5vZYU2Q1K7FUw')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,  str(bot1[0][3]))


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == "стикер":
        bot.send_sticker(message.chat.id, 'CAADAgADHAADwDZPE8GCGtMs_g7hFgQ')
    else:
        quest = data.get_ansquest(botid)
        if message.text.lower() == "/help":
            bot.send_message(message.chat.id, 'Вот что я знаю')
            i = 0
            question = ""
            while i < len(quest):
                question = question + quest[i][1] + '\n'
                i = i + 1
            bot.send_message(message.chat.id, question)
        else:

            i = 0
            while i < len(quest):
                if quest[i][1].lower() == message.text.lower():
                    bot.send_message(message.chat.id, quest[i][2])
                    break
                i = i + 1
            if i == len(quest):
                bot.send_message(message.chat.id, 'Я незнаю ответ на это :(')


@bot.message_handler(content_types=['sticker'])
def send_text(message):
    print(message)


bot.polling()
