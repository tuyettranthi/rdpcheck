import telebot
import datetime
import time
import os
import subprocess
import psutil
import sqlite3
import hashlib
import requests
import datetime

bot_token = '6720520102:AAEbC26o26MQExFBa5bnhe48eRFSAUACQ4Q' 
bot = telebot.TeleBot(bot_token)

allowed_group_id = -1001637267809

allowed_users = []
processes = []
ADMIN_ID = 6563859645

connection = sqlite3.connect('user_data.db')
cursor = connection.cursor()

  # Create the users table if it doesn't exist
cursor.execute('''
      CREATE TABLE IF NOT EXISTS users (
          user_id INTEGER PRIMARY KEY,
          expiration_time TEXT
      )
  ''')
connection.commit()
def TimeStamp():
      now = str(datetime.date.today())
      return now
def load_users_from_database():
      cursor.execute('SELECT user_id, expiration_time FROM users')
      rows = cursor.fetchall()
      for row in rows:
          user_id = row[0]
          expiration_time = datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
          if expiration_time > datetime.datetime.now():
              allowed_users.append(user_id)

def save_user_to_database(connection, user_id, expiration_time):
      cursor = connection.cursor()
      cursor.execute('''
          INSERT OR REPLACE INTO users (user_id, expiration_time)
          VALUES (?, ?)
      ''', (user_id, expiration_time.strftime('%Y-%m-%d %H:%M:%S')))
      connection.commit()
@bot.message_handler(commands=['adduser'])
def add_user(message):
      admin_id = message.from_user.id
      if admin_id != ADMIN_ID:
          bot.reply_to(message, '🔒YOU DO NOT A PERMISSION!🔒')
          return

      if len(message.text.split()) == 1:
          bot.reply_to(message, '🚀VUI LÒNG NHẬP ID NGƯỜI DÙNG 🚀')
          return

      user_id = int(message.text.split()[1])
      allowed_users.append(user_id)
      expiration_time = datetime.datetime.now() + datetime.timedelta(days=30)
      connection = sqlite3.connect('user_data.db')
      save_user_to_database(connection, user_id, expiration_time)
      connection.close()

      bot.reply_to(message, f'🚀USER ID {user_id} SUCCESS ADD TO PREMIUM BY ADMIN!🚀')

@bot.message_handler(commands=['start'])
def get_rdp(message):
    start_text = '''
━━➤ 🚀 Welcome to @dncrdp_bot!🚀
┏━━━━━━━━━━━━━━━━━┓
┣➤ JOIN TO GROUP
┣➤ t.me/suppertkl1
┣➤ t.me/altsforme1
┣➤ https://t.me/ALTSFORME1
┣➤ JOIN ALL? SEND [/help]
┣➤ ADMIN: @Nulltestfun1
┗━━━━━━━━━━━━━━━━━┛
'''
    bot.reply_to(message, start_text)

@bot.message_handler(commands=['ssh'])
def get_rdp(message):
    ssh_text = '''
👑GET FREE VPS SSH!👑
  ┏━━━━━━━━━━━━━━━━━┓
  ┣➤✳IP: 138.197.38.152
  ┣➤🔒PORT: 22
  ┣➤👤USER: master_kdvgzqcjjm
  ┣➤🔑PASS: ZVmeepJFf67p
  ┣➤🖥OS: [ERROR]
  ┣➤🔓PLAN: FREE-TRAIL
  ┣➤⏲️Expiry: 2 DAY
  ┣➤👤ADMIN: @Nulltestfun1
  ┗━━━━━━━━━━━━━━━━━┛
'''
    bot.reply_to(message, ssh_text)

@bot.message_handler(commands=['vnc'])
def get_rdp(message):
    vnc_text = '''
👑GET FREE VPS VNC!👑
  ┏━━━━━━━━━━━━━━━━━┓
  ┣➤✳IP: 0.tcp.ap.ngrok.io
  ┣➤🔒PORT: 19696
  ┣➤🖥OS: Windows 10
  ┣➤🔓PLAN: FREE-TRAIL
  ┣➤⏲️Expiry: UNKNOWN
  ┣➤👤ADMIN: @Nulltestfun1
  ┗━━━━━━━━━━━━━━━━━┛
'''
    bot.reply_to(message, vnc_text)

@bot.message_handler(commands=['rdp'])
def get_rdp(message):
    rdp_text = '''
👑GET FREE VPS RDP!👑
  ┏━━━━━━━━━━━━━━━━━┓
  ┣➤✳IP: 20.237.223.232
  ┣➤🔒PORT: 3389 / 22
  ┣➤👤USER: john
  ┣➤🔑PASS: 123456Hi@@//
  ┣➤🖥OS: win 11
  ┣➤🔓PLAN: FREE-TRAIL
  ┣➤⏲️Expiry: UNKNOWN!
  ┣➤👤ADMIN: @Nulltestfun1
  ┗━━━━━━━━━━━━━━━━━┛
'''
    bot.reply_to(message, rdp_text)

@bot.message_handler(commands=['help'])
def get_rdp(message):
    help_text = '''
🚀DNCRDP_BOT HELP COMMAND🚀
  ┏━━━━━━━━━━━━━━━━━┓
  ┣➤ Need help if you don't know [/help]
  ┣➤ GET FREE VPS SSH 2 - 8 HOURS [/ssh] [STOCK OUT!]
  ┣➤ GET FREE VPS VNC TIME: RANDOM [/vnc] [STOCK OUT!]
  ┣➤ GET FREE VPS RDP TIME: RANDOM [/rdp] [COMING SOON...]
  ┣➤ GET FREE PROXY [/proxy]
  ┣➤ ADMIN: @Nulltestfun1
  ┗━━━━━━━━━━━━━━━━━┛
'''
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['proxy'])
def get_proxy_file(message):
    proxy_file_path = "./proxy/proxy.txt"
    if os.path.exists(proxy_file_path):
        with open(proxy_file_path, "rb") as file:
            bot.send_document(message.chat.id, file)
    else:
        bot.reply_to(message, "🔒Proxy list file not found!🔒")

bot.polling()
