from modules.shakepay import *
from modules.telegramnotif import *
import os.path
import time
import datetime
import json
import logging

from random import *

logging.basicConfig(filename='shakingbot.log', level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

while True:
    
    print("\n--- "+str(datetime.datetime.now()))
    logging.info("Attempting to Shake")
    
    resp = shakingSats()
    apiPostResponse = json.loads(resp.text)
    formatted_apiPostResponse = json.dumps(apiPostResponse)
    APIMessage = json.loads(formatted_apiPostResponse)

    #Check if user optd for Telegram
    checkTelegramOPT()

    if "message" in APIMessage and APIMessage['message'] == "Prize already redeemed":
        print(APIMessage['message'])
        logging.info((APIMessage['message']))
        time.sleep((3600*6)+randint(0, 7200))
    elif "success" in APIMessage:
        streakAmount = str(APIMessage['streak'])
        print("Succesfully Shaken | Current Streak of " + streakAmount + " days")
        logging.info("Succesfully Shaken | Current Streak " + streakAmount + " days")
        if telegramOPT == True:
            sendToTelegram("✅ Succesfully Shaken 🎉 Streak of " + streakAmount + " days")
        time.sleep((3600*6)+randint(0, 7200))
    else:
        if telegramOPT == True:
            sendToTelegram("❌ Some type of error occured! Trying again in 30 minutes")
            logging.info("There was an error. Trying again in 30 minutes.")
            time.sleep(1800)
        else:
            print("There was an error. Trying again in 30 minutes.")
            logging.info("There was an error. Trying again in 30 minutes.")
            time.sleep(1800)
