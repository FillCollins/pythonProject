import telebot

bot = telebot.TeleBot("5591519910:AAGDMvw5GfkxK_LMpuiFubdJ2R1iF0WIV6c", parse_mode=None)

#обработчик событий
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Andrew, how are you doing, Boss?")


@bot.message_handler(func=lambda message: "Good")
def echo_all(message):
	bot.reply_to(message, "Fine, you are Super")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()





