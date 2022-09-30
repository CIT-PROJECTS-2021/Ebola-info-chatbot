import os
import telegram.ext
import twitter
from dotenv import load_dotenv

load_dotenv()

# telegram api token
TOKEN = os.getenv('TOKEN')

def menu(update, context):
    update.message.reply_text("1 : latest\n2 : facts\n3 : transmission\n4 : symptoms\n5 : prevention\n6 : treatment")

def invalid_response(update, context):
    message = "I'm sorry, I didn't understand your reply.\nI'm an automated system. Reply with a number corresponding to any topic to explore it."
    update.message.reply_text(message)
    menu(update, context)

def welcome(update, context):
    message = '''
    --- WELCOME TO EBOLA INFOBOT ---

   Get information and guidance about EBOLA.

   Reply with a number corresponding to any topic or the topic name to explore it :

   Type 'menu' for the menu.
    '''
    update.message.reply_text(message)
    menu(update, context)

def menu_handler(option, update, context):
    file_name = f"info\\{option}.txt"
    with open(file_name) as file:
        data = file.readlines()
        for line in data:
            try:
                update.message.reply_text(line)
            except:
                continue
        #print(data)

def message_handler(update, context):
    input = update.message.text
    input = input.lower()

    if input in ['1','2','3','4','5','6', 'latest', 'facts', 'transmission', 'treatment', 'symptoms', 'prevention']:
        if input in ['1','2','3','4','5','6']:
            matches = {'1' : 'latest', '2' : 'facts', '3' : 'transmission', '4' : 'symptoms', '5' : 'prevention', '6' : 'treatment'}
            input = matches[input]
        menu_handler(input, update, context)
    elif input == 'hi':
        welcome(update, context)
    elif input == 'menu':
        menu(update, context)
    else:
        invalid_response(update, context)

# updater provides a frontend of telegram bot to the programmer
updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

# handle various data and commands from the frontend
disp.add_handler(telegram.ext.CommandHandler("hi", welcome))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("menu", menu))
disp.add_handler(telegram.ext.CommandHandler("invalid_response", invalid_response))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, message_handler))

# start updater and fetch updates from telegram
updater.start_polling()
updater.idle()