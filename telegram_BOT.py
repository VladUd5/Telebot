from logging import exception
import telebot
from telebot import types
from time import sleep



bot = telebot.TeleBot('5476737675:AAFNgmRL0gGvkwOTuR7fUIHs5HPNyTB6oLY')  


@bot.message_handler(commands=['start'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("today")
    btn2 = types.KeyboardButton("tomorrow")
    btn3 = types.KeyboardButton("week")
    markup.add(btn1, btn2,btn3)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот для расписаний и домашней работы".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "/start":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь? Если нужна помощь напиши /help")
    elif message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Пока существует 3 команды:\n 1. today  -  выводит расписание занятий на сегодня.\n 2. tomorrow  -  выводит расписание занятий на завтра.\n 3.week  -  выводит расписание занятий на неделю")
        button_message()
    elif message.text.lower()== "/today":
        
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Кнопка":
        bot.send_message(message.user.id,"https://habr.com/ru/users/lubaznatel/")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запомню : )')
try:
    bot.polling(none_stop=True, interval=0)
except Exception: 
    sleep(5)