import telebot
import socket
import socks
import json
from telebot import apihelper
ip = '167.86.103.90'
port = '8080'
token = '1027028612:AAG89TGIV1mLsgi1nS8VNQ6v3xDQy81ldTo'
bot = telebot.TeleBot(token)
apihelper.proxy={"https":"socks5://51.105.235.21:1080"}

dict = []


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "напиши команду")



@bot.message_handler(commands=['add'])
def send_welcome(message):
	bot.reply_to(message, "пришли геолокацию")


@bot.message_handler(content_types=['location'])
def handle_location(message):
	d = {}
	id = 2
	location = message.location
	d['longitude']=location.longitude
	d['latitude'] = location.latitude
	dict.append(d)

	with open('data.json', 'w') as f:
		json.dump(dict, f)

	print(location)


bot.polling()