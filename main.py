import os 
import telebot
from flask import Flask, request

TOKEN = '5285103968:AAE3xP9345eWCFN7FkxGKA7sdihXiqj2WPQ'
APP_URL = f'https://adftest12.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo(message):
    bot.reply_to(message, message.text)

@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data(). decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.ste_webhook(url=APP_URL)
    return '!', 200

if __name__ == '__main__':
    derver.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))