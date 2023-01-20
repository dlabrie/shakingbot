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
            if fakeUUID == "":
                with open(filepath, "w") as f:
                    fakeUUID = str(uuid.uuid4()).upper()
                    f.write(fakeUUID)
    if fakeUUID == "":
        print("There was a problem generating a device id, cannot proceed.")
        exit()
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

headers = {
    "x-device-serial-number":"unknown",
    "x-device-total-memory":"5980209152",
    "x-device-name":"iPhone",
    "x-device-has-notch":"true",
    "user-agent":"Shakepay App v1.10.9 (11000900) on Apple iPhone 12 Pro (iOS 16.2)",
    "x-device-locale":"en",
    "x-device-manufacturer":"Apple",
    "x-device-is-tablet":"false",
    "x-device-total-disk-capacity":"127881465856",
    "x-device-system-name":"iOS",
    "x-device-carrier":"Eastlink",
    "x-device-id":"iPhone13,3",
    "x-device-model":"iPhone 12 Pro",
    "x-device-country":"CA",
    "x-device-mac-address":"02:00:00:00:00:00",
    "x-app-version":"1.10.9",
    "x-locale":"en",
    "x-device-tzoffset":"240",
    "accept-language":"en-CA,en-US;q=0.9,en;q=0.8",
    "x-device-ip-address":"192.168.2.18",
    "x-device-unique-id": getUUID(),
    "x-app-build":"11000900",
    "accept":"application/json",
    "accept-encoding":"gzip, deflate, br",
    "x-device-brand":"Apple",
    "x-device-system-version":"16.2",
    "x-notification-token": "undefined"
}

# initialize a session 
session = requests.Session()

def shakepayPullConfig():
    print("pulling app config")
    request = session.get("https://api.shakepay.com/config/11000900")
    # print the response dictionary 
    print(session.cookies.get_dict())   

def shakepayAPIAuth(shakepayUsername, shakepayPassword):
    headers2 = headers
    headers2["content-type"] = "application/json"
    credentials = {
        "password": shakepayPassword,
        "strategy": "local",
        "totpType": "sms",
        "username": shakepayUsername
    }
    try:
        return session.post("https://api.shakepay.com/authentication", json=credentials, headers=headers2)
    except Exception:
        print(uxiosShakepayAPIBackOff)
        time.sleep(5)
        return shakepayAPIAuth(shakepayUsername, shakepayPassword)

def shakepayAPIPost(endpoint, jsonData):
    try:
        return session.post("https://api.shakepay.com"+endpoint, json=jsonData, headers=headers)
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