# - *- coding: utf- 8 - *-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
  update.message.reply_text("I'm ThePhoenixBot, the (not so) official bot of the Phoenix Programing Club at RCHS. What's your name?")
  
def convert_uppercase(bot, update):
  update.message.reply_text(update.message.text.upper())

def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater("547118601:AAHcbiwDzTOOtITcr7p5ITdZWTfAzOS0Z8Y")
  dispatcher = updater.dispatcher
  print("Bot started")

  # Add command handler to dispatcher
  start_handler = CommandHandler('start',start)
  upper_case = MessageHandler(Filters.text, convert_uppercase)
  dispatcher.add_handler(start_handler)
  dispatcher.add_handler(upper_case)

  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()

if __name__ == '__main__':
  main()
