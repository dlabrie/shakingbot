import requests
import os

from modules.shakepay import logging
from modules.uxios import *

discordOPT = os.path.exists("creds/.discordWebhook")


def discordWebhookReq(question, default_no=True):
    choices = ' [y/N]: ' if default_no else ' [Y/n]: '
    prompt = f"{question}{choices}"
    default_answer = 'n' if default_no else 'y'
    reply = input(prompt).strip().lower() or default_answer
    if reply[0] in ('y', 'n'):
        if reply[0] == 'y':
            discordAPIToken = input(uxiosReqDiscordWebhook)
            with open('creds/.discordWebhook', 'w') as f:
                discordAPITokenParts = discordAPIToken.split('/')
                webhooks_index = discordAPITokenParts.index('webhooks')
                webhook_parts = discordAPITokenParts[webhooks_index + 1:]
                webhook_string = '/'.join(webhook_parts)
                f.write(str(webhook_string))
        return False if reply[0] == 'n' else not default_no
    return False if default_no else True


def checkDiscordOPT():
    if discordOPT == True:
        rURL = open("creds/.discordWebhook", "r")
        checkDiscordOPT.key = rURL.read()
    else:
        return False


def sendToDiscord(message):
    discordPayload = {
        "content": message,
        "username": "Shakebot " + botVersion,
        "avatar_url": "https://fujiwara.pw/i/vXXc8.png"
    }

    discordResponse = requests.post(
        "https://discord.com/api/webhooks/" + checkDiscordOPT.key, json=discordPayload)
    if discordResponse.status_code == 200 or 204:
        return True
    else:
        logging.info("Error sending Discord webhook message: HTTPS ERROR {}".format(
            discordResponse.status_code))


def testDiscordMessage(message):
    if discordOPT == True:
        checkDiscordOPT()
        discordPayload = {
            "content": message,
            "username": "Shakebot " + botVersion,
            "avatar_url": "https://fujiwara.pw/i/vXXc8.png"
        }

        discordResponse = requests.post(
            "https://discord.com/api/webhooks/" + checkDiscordOPT.key, json=discordPayload)
        if discordResponse.status_code == 200 or 204:
            return True
        else:
            logging.info("Error sending Discord webhook message: HTTPS ERROR {}".format(
                discordResponse.status_code))
