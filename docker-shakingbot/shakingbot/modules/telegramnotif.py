import os
import requests

from modules.shakepay import *
from modules.uxios import *

telegramOPT = os.path.exists("creds/.telegramAPIToken")


def checkTelegramOPT():
    if telegramOPT == True:
        rKey = open("creds/.telegramAPIToken", "r")
        rID = open("creds/.telegramChatID", "r")
        checkTelegramOPT.key = rKey.read()
        checkTelegramOPT.id = rID.read()
    else:
        return False


def testTelegramMessage(message):
    if telegramOPT == True:
        checkTelegramOPT()
        apiToken = checkTelegramOPT.key
        chatID = checkTelegramOPT.id
        apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
        try:
            response = requests.post(
                apiURL, json={'chat_id': chatID, 'text': message})
        except Exception as e:
            print(e)
    else:
        return False


def sendToTelegram(message):
    apiToken = checkTelegramOPT.key
    chatID = checkTelegramOPT.id
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    try:
        response = requests.post(
            apiURL, json={'chat_id': chatID, 'text': message})
    except Exception as e:
        print(e)


def telegramApiToken(question, default_no=True):
    choices = ' [y/N]: ' if default_no else ' [Y/n]: '
    prompt = f"{question}{choices}"
    default_answer = 'n' if default_no else 'y'
    reply = input(prompt).strip().lower() or default_answer
    if reply[0] in ('y', 'n'):
        if reply[0] == 'y':
            telegramAPIToken = input(uxiosReqTelegramAPI)
            with open('creds/.telegramAPIToken', 'w') as f:
                f.write(telegramAPIToken)
            telegramChatID = input(uxiousReqTelegramID)
            with open('creds/.telegramChatID', 'w') as f:
                f.write(telegramChatID)
        return False if reply[0] == 'n' else not default_no
    return False if default_no else True
