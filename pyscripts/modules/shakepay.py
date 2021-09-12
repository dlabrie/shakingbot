from getpass import getpass

import datetime
import calendar
import requests
import uuid
import json
import pytz
import csv
import time
import jwt

def getUUID():
    fakeUUID = ""
    ## Generate a unique device id if needed
    try:
        f = open(".uuid", "r")
        fakeUUID = f.read()
        f.close()
    except:
        f = open(".uuid", "w")
        fakeUUID = str(uuid.uuid4())
        f.write(fakeUUID.upper())
        f.close()

    if fakeUUID == "":
        f = open(".uuid", "w")
        fakeUUID = str(uuid.uuid4())
        f.write(fakeUUID.upper())
        f.close()
  
    return fakeUUID.upper()

def saveJWT(jwt):
    f = open(".jwtToken", "w")
    f.write(jwt)
    f.close()

def getJWT():
    jwt = ""
    try:
        f = open(".jwtToken", 'r')
        jwt = f.read()
        f.close()
    except IOError:
        print("Please login by using python3 login.py first.")
        f.close()
        exit()

    return jwt

def shakepayAPIAuth(shakepayUsername, shakepayPassword):
    #print("Calling Shakepay API Endpoint using POST /authentication")
    headers =  {
        "x-device-total-memory": "6014582784",
        "x-device-serial-number":"",
        "x-device-name": "",
        "x-device-has-notch": "false",
        "user-agent": "Shakepay App v1.7.24 (17024) on domi167 bot",
        "x-device-locale": "en-CA",
        "x-device-manufacturer": "Bot",
        "x-device-is-tablet": "false",
        "x-device-total-disk-capacity": "127881465856",
        "x-device-system-name": "Python",
        "x-device-carrier": "",
        "x-device-model": "Bot",
        "x-device-id": "",
        "x-device-country": "CA",
        "x-device-mac-address": "02:00:00:00:00:00",
        "accept-language": "en-ca",
        "x-device-ip-address": "10.100.100.11",
        "x-device-unique-id": getUUID(),
        "content-type": "application/json",
        "accept": "application/json",
        "x-device-brand": "Bot",
        "accept-encoding": "gzip, deflate, br",
        "x-device-system-version": "",
    }
    credentials =  {"strategy":"local","totpType":"sms","username":shakepayUsername,"password":shakepayPassword}
    try:
        return requests.post("https://api.shakepay.com/authentication", json=credentials, headers=headers) 
    except Exception:
        print("Request failed, backing off for 5 seconds.")
        time.sleep(5)
        return shakepayAPIAuth(shakepayUsername, shakepayPassword)

def shakepayAPIPost(endpoint, jsonData):
    #print("Calling Shakepay API Endpoint using POST "+endpoint)
    headers =  {
        "authorization": getJWT(),
        "x-device-total-memory": "6014582784",
        "x-device-serial-number":"",
        "x-device-name": "",
        "x-device-has-notch": "false",
        "user-agent": "Shakepay App v1.7.24 (17024) on domi167 bot",
        "x-device-locale": "en-CA",
        "x-device-manufacturer": "Bot",
        "x-device-is-tablet": "false",
        "x-device-total-disk-capacity": "127881465856",
        "x-device-system-name": "Python",
        "x-device-carrier": "",
        "x-device-model": "Bot",
        "x-device-id": "",
        "x-device-country": "CA",
        "x-device-mac-address": "02:00:00:00:00:00",
        "accept-language": "en-ca",
        "x-device-ip-address": "10.100.100.11",
        "x-device-unique-id": getUUID(),
        "content-type": "application/json",
        "accept": "application/json",
        "x-device-brand": "Bot",
        "accept-encoding": "gzip, deflate, br",
        "x-device-system-version": "",
    }
    try:
        return requests.post("https://api.shakepay.com"+endpoint, json=jsonData, headers=headers) 
    except Exception:
        print("Request failed, backing off for 5 seconds.")
        time.sleep(5)
        return shakepayAPIPost(endpoint, jsonData)

def shakingSats():
    return shakepayAPIPost("/shaking-sats", {})