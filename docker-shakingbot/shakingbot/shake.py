from modules.shakepay import *
from modules.telegramnotif import *

logging.basicConfig(filename='shakingbot.log', level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

testTelegramMessage(uxiosTelegramCheckConnection)

while True:
    
    print("\n--- "+str(datetime.datetime.now()))
    logging.info(uxiosShakeAttempt)
    
    resp = shakingSats()
    apiPostResponse = json.loads(resp.text)
    formatted_apiPostResponse = json.dumps(apiPostResponse)
    APIMessage = json.loads(formatted_apiPostResponse)

    checkTelegramOPT()

    if "message" in APIMessage and APIMessage['message'] == "Prize already redeemed":
        print(APIMessage['message'])
        logging.info((APIMessage['message']))
        time.sleep((3600*6)+randint(0, 7200))
    elif "success" in APIMessage:
        streakAmount = str(APIMessage['streak'])
        print(uxiosSuccessfulShake + streakAmount)
        logging.info(uxiosSuccessfulShake + streakAmount)
        if telegramOPT == True:
            sendToTelegram(uxiosTelegramSuccessfulShake + streakAmount)
        time.sleep((3600*6)+randint(0, 7200))
    else:
        if telegramOPT == True:
            sendToTelegram(uxiosTelegramFailedShake)
            logging.info(uxiosFailedShake)
            time.sleep(1800)
        else:
            print(uxiosFailedShake)
            logging.info(uxiosFailedShake)
            time.sleep(1800)
