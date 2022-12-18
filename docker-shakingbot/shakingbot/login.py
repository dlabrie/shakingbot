from modules.shakepay import *

getUserCreds()

shakepayUsername = input(uxiosUsernameReq)
shakepayPassword = getpass(uxiosPasswordReq)

checkUserNotif()

print(uxiosSendingLogin)

with shakepayAPIAuth(shakepayUsername, shakepayPassword) as response:
    accessResponse = json.loads(response.text)
    formatted_accessResponse = json.dumps(accessResponse)

if "accessToken" in accessResponse:
    saveJWT(accessResponse["accessToken"])
    jwtAccessToken = jwt.decode(accessResponse["accessToken"], algorithms="HS256", options={
                                "verify_signature": False})
    if jwtAccessToken["mfa"] == True:
        smsCode = input(uxiosSMS)
        response = shakepayAPIPost(
            "/authentication", {"strategy": "mfa", "mfaToken": smsCode})
        accessResponse = json.loads(response.text)
        if "accessToken" in accessResponse:
            saveJWT(accessResponse["accessToken"])
            jwtAccessToken = jwt.decode(accessResponse["accessToken"], algorithms="HS256", options={
                                        "verify_signature": False})
        else:
            accessResponse = json.loads(response.text)
            formatted_accessResponse = json.dumps(accessResponse)
            shakeAPIMessage = json.loads(formatted_accessResponse)
            print(shakeAPIMessage['message'])
else:
    shakeAPIMessage = json.loads(formatted_accessResponse)
    print(shakeAPIMessage['message'])
