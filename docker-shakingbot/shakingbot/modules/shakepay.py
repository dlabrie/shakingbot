import datetime
import jwt 
import logging
import requests
import time
import uuid
import json
import os

from getpass import getpass
from random import *
from modules.telegramnotif import *
from modules.discordnotif import *
from modules.uxios import *

def getUUID():
    filepath = "creds/.uuid"
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            fakeUUID = str(uuid.uuid4()).upper()
            f.write(fakeUUID)
    else:
        with open(filepath, "r") as f:
            fakeUUID = f.read().upper()
    return fakeUUID

def saveJWT(jwt):
    with open("creds/.jwtToken", "w") as f:
        f.write(jwt)

def getJWT():
    filepath = "creds/.jwtToken"
    if not os.path.exists(filepath):
        print(uxiosLoginFirst)
        exit()
    with open(filepath, "r") as f:
        jwt = f.read()
    return jwt

def getUserCreds():
    if not os.path.isfile("creds/.uuid"):
        with open("creds/.uuid", "w") as f:
            f.write("")

    if not os.path.isfile("creds/.jwtToken"):
        with open("creds/.jwtToken", "w") as f:
            f.write("")
    else:
        if getJWT() != "":
            print(uxiosExistingJWT)
            exit()

def shakepayAPIAuth(shakepayUsername, shakepayPassword):
    headers =  {
        "x-device-total-memory": "6014582784",
        "x-device-serial-number":"",
        "x-device-name": "",
        "x-device-has-notch": "false",
        "user-agent": "Shakepay App v1.9.52 (19052) on beep boop bot",
        "x-device-locale": "en-CA",
        "x-device-manufacturer": "Shakebot",
        "x-device-is-tablet": "false",
        "x-device-total-disk-capacity": "127881465856",
        "x-device-system-name": "Shakebot " + botVersion,
        "x-device-carrier": "",
        "x-device-model": "Created by domi & hydra",
        "x-device-id": "",
        "x-device-country": "CA",
        "x-device-mac-address": "02:00:00:00:00:00",
        "accept-language": "en-ca",
        "x-device-ip-address": "10.100.100.11",
        "x-device-unique-id": getUUID(),
        "content-type": "application/json",
        "accept": "application/json",
        "x-device-brand": "Shakebot",
        "accept-encoding": "gzip, deflate, br",
        "x-device-system-version": "",
    }
    credentials =  {"strategy":"local","totpType":"sms","username":shakepayUsername,"password":shakepayPassword}
    try:
        return requests.post("https://api.shakepay.com/authentication", json=credentials, headers=headers) 
    except Exception:
        print(uxiosShakepayAPIBackOff)
        time.sleep(5)
        return shakepayAPIAuth(shakepayUsername, shakepayPassword)

def shakepayAPIPost(endpoint, jsonData):
    headers =  {
        "authorization": getJWT(),
        "x-device-total-memory": "6014582784",
        "x-device-serial-number":"",
        "x-device-name": "",
        "x-device-has-notch": "false",
        "user-agent": "Shakepay App v1.9.52 (19052) on beep boop bot",
        "x-device-locale": "en-CA",
        "x-device-manufacturer": "Shakebot",
        "x-device-is-tablet": "false",
        "x-device-total-disk-capacity": "127881465856",
        "x-device-system-name": "Shakebot " + botVersion,
        "x-device-carrier": "",
        "x-device-model": "Created by domi & hydra",
        "x-device-id": "",
        "x-device-country": "CA",
        "x-device-mac-address": "02:00:00:00:00:00",
        "accept-language": "en-ca",
        "x-device-ip-address": "10.100.100.11",
        "x-device-unique-id": getUUID(),
        "content-type": "application/json",
        "accept": "application/json",
        "x-device-brand": "Shakebot",
        "accept-encoding": "gzip, deflate, br",
        "x-device-system-version": "",
    }
    try:
        return requests.post("https://api.shakepay.com"+endpoint, json=jsonData, headers=headers) 
    except Exception:
        print(uxiosShakepayAPIBackOff)
        time.sleep(5)
        return shakepayAPIPost(endpoint, jsonData)

def shakingSats():
    return shakepayAPIPost("/shaking-sats", {})

def checkUserNotif():
    if telegramOPT == False:
        telegramApiToken(uxiosTelegramOpt)
    else:
        print(uxiosExistingTelegramAPI)

    if discordOPT == False:
        discordWebhookReq(uxiosDiscordOpt)
    else:
        print(uxiosExistingDiscordWebhook)
