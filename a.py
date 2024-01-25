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
          bot.reply_to(message, '🚀YOU DO NOT A PERMISSION!🚀')
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
┣➤ ADMIN: @Akunbg
┗━━━━━━━━━━━━━━━━━┛
'''
    bot.reply_to(message, start_text)
