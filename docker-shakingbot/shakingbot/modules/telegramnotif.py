import requests
import json
import os.path

telegramOPT = os.path.isfile("creds/.telegramAPIToken")

def checkTelegramOPT():
    if telegramOPT == True:
        rKey = open("creds/.telegramAPIToken", "r")
        rID = open("creds/.telegramChatID", "r")
        checkTelegramOPT.key = rKey.read()
        checkTelegramOPT.id = rID.read()
    else:
        return False

def sendToTelegram(message):
    apiToken = checkTelegramOPT.key
    chatID = checkTelegramOPT.id
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        #print(response)
    except Exception as e:
        print(e)
    
## Ask user if Telegram notifications are wanted
def telegramApiToken(question, default_no=True):
    choices = ' [y/N]: ' if default_no else ' [Y/n]: '
    default_answer = 'n' if default_no else 'y'
    reply = str(input(question + choices)).lower().strip() or default_answer
    if reply[0] == 'y':
        telegramAPIToken = input("Telegram Bot API Token: ")
        with open('creds/.telegramAPIToken', 'w') as f:
            f.write(telegramAPIToken)
        telegramChatID = input("Telegram Chat ID: ")
        with open('creds/.telegramChatID', 'w') as f:
            f.write(telegramChatID)
    if reply[0] == 'n':
        return False
    else:
        return False if default_no else True