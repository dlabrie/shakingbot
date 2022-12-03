import json
import jwt
import os

from getpass import getpass
from modules.shakepay import *
from modules.telegramnotif import *

if not os.path.isfile("creds/.uuid"):
    with open("creds/.uuid", "w") as f:
        f.write("")

if not os.path.isfile("creds/.jwtToken"):
    with open("creds/.jwtToken", "w") as f:
        f.write("")
else:
    if getJWT() != "":
        print("Looks like you already have a session, delete creds/.jwtToken to force this")
        exit()

shakepayUsername = input("Shakepay Username: ")
shakepayPassword = getpass("Shakepay Password: ")

if telegramApiToken("Would you like to receive notifications via Telegram when a successful shake occurs?"):
    ## Login with provided credentials
    print("Sending initial login request")

    response = shakepayAPIAuth(shakepayUsername, shakepayPassword)
    accessResponse = json.loads(response.text)

    if "accessToken" in accessResponse:
        saveJWT(accessResponse["accessToken"])

        jwtAccessToken = jwt.decode(accessResponse["accessToken"], algorithms="HS256", options={"verify_signature": False})

        if jwtAccessToken["mfa"] == True:
            smsCode = input("Login is being MFA'd, please enter your SMS code [numbers only, no dash] : ")
            response = shakepayAPIPost("/authentication", {"strategy":"mfa","mfaToken":smsCode})

            accessResponse = json.loads(response.text)

            if "accessToken" in accessResponse:
                saveJWT(accessResponse["accessToken"])

                jwtAccessToken = jwt.decode(accessResponse["accessToken"], algorithms="HS256", options={"verify_signature": False})

            else:
                print(accessResponse)

    else:
        shakeAPIMessage = json.loads(response.text)
        print(shakeAPIMessage['message'])
