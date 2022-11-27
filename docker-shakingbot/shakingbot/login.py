from getpass import getpass
from modules.shakepay import *
import json
import jwt

import os

if os.path.isfile("creds/.uuid") != True:
    f = open("creds/.uuid", "w")
    f.write("")
    f.close()

if os.path.isfile("creds/.jwtToken") != True:
    f = open("creds/.jwtToken", "w")
    f.write("")
    f.close()
else:
    if getJWT() != "":
        print("Looks like you already have a session, delete creds/.jwtToken to force this")
        exit()

shakepayUsername = input("Shakepay Username: ")
shakepayPassword = getpass("Shakepay Password: ")

## Ask user if Telegram notifications are wanted
def apiToken(question, default_no=True):
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

reply = apiToken("Would you like to receive notifications via Telegram when a successful shake occurs?")

## Login with provided credentials
print("Sending initial login request")

response = shakepayAPIAuth(shakepayUsername, shakepayPassword)
accessResponse = json.loads(response.text)
formatted_accessResponse = json.dumps(accessResponse)

if "accessToken" in accessResponse:
    saveJWT(accessResponse["accessToken"])

    jwtAccessToken = jwt.decode(accessResponse["accessToken"], algorithms="HS256", options={"verify_signature": False})

    if jwtAccessToken["mfa"]==True:
        smsCode = input("Login is being MFA'd, please enter your SMS code [numbers only, no dash] : ")
        response = shakepayAPIPost("/authentication", {"strategy":"mfa","mfaToken":smsCode})

        accessResponse = json.loads(response.text)

        if "accessToken" in accessResponse:
            saveJWT(accessResponse["accessToken"])

            jwtAccessToken = jwt.decode(accessResponse["accessToken"], algorithms="HS256", options={"verify_signature": False})
            
        else:
            print(accessResponse)

            
else:
    shakeAPIMessage = json.loads(formatted_accessResponse)
    print(shakeAPIMessage['message'])
