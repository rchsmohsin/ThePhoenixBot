# - *- coding: utf- 8 - *-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
  update.message.reply_text("I'm ThePhoenixBot, the (not so) official bot of the Phoenix Programing Club at RCHS. What's your name?")
  
def dank(bot, update):
  update.message.reply_text("when you dank so hard but you don't succeed")
  
def hot(bot, update):
  update.message.reply_text("man's not hot")
  
def meme(bot, update):
  update.message.reply_text("CONK>BEPIS")
  
def meorg(bot, update):
  update.message.reply_text("beft!!!!!!!")
  
def defreply(bot, update):
  update.message.reply_text(update.message.text())
def photocomment(bot, update):
  update.message.reply_text("nice photo bro")
  
  
def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater("547118601:AAHcbiwDzTOOtITcr7p5ITdZWTfAzOS0Z8Y")
  dispatcher = updater.dispatcher
  print("Bot started")

  
  # Add command handler to dispatcher
  start_handler = CommandHandler('start',start)
  dank_handler = CommandHandler('dank',dank)
  hot_handler = CommandHandler ('hot',hot)
  meme_handler = CommandHandler('meme',meme)
  meorg_handler = CommandHandler('meorg',meorg)
  
  upper_case = MessageHandler(Filters.text, defreply)
  photo_filter = MessageHandler(Filters.photo, photocomment)
  
  dispatcher.add_handler(start_handler)
  dispatcher.add_handler(upper_case)
  dispatcher.add_handler(dank_handler)
  dispatcher.add_handler(hot_handler)
  dispatcher.add_handler(meme_handler)
  dispatcher.add_handler(meorg_handler)
  dispatcher.add_handler(photo_filter)
  
  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()

if __name__ == '__main__':
  main()

  #comment
