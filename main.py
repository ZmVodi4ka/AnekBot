import random
from http.client import responses
import requests
import telebot
from bs4 import BeautifulSoup
from TokenAPI import key

url = "https://baneks.ru/random"
def parser(url):
    r = requests.get(url, timeout=60)
    soup = BeautifulSoup(r.text,'html.parser')
    anekdots = soup.find_all('article')
    return [c.text for c in anekdots]

bot = telebot.TeleBot(key)
@bot.message_handler(commands=['anek'])

def jokes(message):
    list_jokes = parser(url)
    random.shuffle(list_jokes)
    bot.send_message(message.chat.id, list_jokes)

bot.polling()