import random
import requests
import telebot
from bs4 import BeautifulSoup



url = "https://www.anekdot.ru/random/anekdot/"
Api_key = '7456021931:AAGrkjybpKpqmfrqPXj1CQlwOWbjr4hQxJ8'
def parser(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    anekdots = soup.find_all('div',class_='text')
    return [c.text for c in anekdots]

bot = telebot.TeleBot(Api_key)
@bot.message_handler(commands=['anek'])

def jokes(message):
    list_jokes = parser(url)
    random.shuffle(list_jokes)
    bot.send_message(message.chat.id, list_jokes)

bot.polling()