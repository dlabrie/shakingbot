import requests
import json
import os.path

teleOPT = os.path.isfile("creds/.telegramAPIToken")

def checkTelegramOPT():
    if teleOPT == True:
        rKey = open("creds/.telegramAPIToken", "r")
        rID = open("creds/.telegramChatID", "r")
        checkTelegramOPT.key = rKey.read()
        checkTelegramOPT.id = rID.read()
    else:
        return False

def send_to_telegram(message):
    apiToken = checkTelegramOPT.key
    chatID = checkTelegramOPT.id
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        #print(response)
    except Exception as e:
        print(e)
        