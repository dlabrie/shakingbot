"""

uxios.py
User experience & input/output is the communication between an information processing system with the end user.

"""
### General ###
uxiosUsernameReq = "Shakepay Username: "
uxiosPasswordReq = "Shakepay Password: "
uxiosLoginFirst = "Please login by using python3 login.py first."
uxiosExistingJWT = "Looks like you already have a session, delete creds/.jwtToken to force this."
uxiosTelegramOpt = "Would you like to receive notifications via Telegram when a successful shake occurs?"
uxiosSendingLogin = "Sending initial login request..."
uxiosSMS = "Login is being MFA'd, please enter your SMS code [numbers only, no dash]: "
uxiosShakepayAPIBackOff = "Request failed, backing off for 5 seconds."
uxiosShakeAttempt = "Attempting to Shake" # No period to follow log format.
uxiosSuccessfulShake = "Succesfully Shaken | Current streak in days: "
uxiosFailedShake = "There was an error. Trying again in 30 minutes."

### Telegram ###
uxiosReqTelegramAPI = "Telegram Bot API Token: "
uxiousReqTelegramID = "Telegram Chat ID: "
uxiosTelegramCheckConnection = "🤖 Succesfully established connection with Telegram Bot."
uxiosTelegramSuccessfulShake = "✅ Shake Shake! Current streak in days: "
uxiosTelegramFailedShake = "❌ Some type of error occured! Trying again in 30 minutes."
uxiosExistingTelegramAPI = "It seems you already have previously entered Telegram bot details.\nIf you wish to change the API details, delete creds/.telegramAPIToken & creds/.telegramChatID to force this."
