!pip install adafruit-io
x = " "  #ENTER ADAFRUIT_IO_USERNAME
y = " "  #ENTER ADAFRUIT_IO_KEY
from Adafruit_IO import Client,Feed
aio = Client(x,y)
feed = Feed(name = 'lightbot')  # Create a feed
result = aio.create_feed(feed)
from Adafruit_IO import Data
!pip install python-telegram-bot
from Adafruit_IO import Client,Data
from telegram.ext import Updater,CommandHandler
def on(bot,update):
  chat_id = update.message.chat_id
  aio.create_data('lightbot',Data(value = 1))
  bot.send_message(chat_id = chat_id,text = "Lights On")

def off(bot,update):
  chat_id = update.message.chat_id
  aio.create_data('lightbot',Data(value = 0))
  bot.send_message(chat_id = chat_id,text = "Lights Off")

u = Updater('1158092600:AAELI6p4rNsvMt4Mt6m5ksbi8Ecf1KbEHek')
dp = u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()

