from getpass import getpass
from modules.shakepay import *
import json
import jwt

import os

if os.path.isfile("/opt/shakingbot/creds/.uuid") != True:
    f = open("/opt/shakingbot/creds/.uuid", "w")
    f.write("")
    f.close()

if os.path.isfile(".jwtToken") != True:
    f = open("/opt/shakingbot/creds/.jwtToken", "w")
    f.write("")
    f.close()
else:
    print("Looks like you already have a session, delete /opt/shakingbot/creds/.jwtToken to force this")
    exit()

shakepayUsername = input("Shakepay Usernamme : ")
shakepayPassword = getpass("Shakepay Password : ")

## Login with provided credentials
print("Sending initial login request")

response = shakepayAPIAuth(shakepayUsername, shakepayPassword)
accessResponse = json.loads(response.text)

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
    print(accessResponse)
