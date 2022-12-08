from modules.shakepay import *
from modules.telegramnotif import *
from modules.discordnotif import *

logging.basicConfig(filename='shakingbot.log', level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

testTelegramMessage(uxiosTelegramCheckConnection)
testDiscordMessage(uxiosDiscordCheckConnection)

while True:
    
    print("\n--- "+str(datetime.datetime.now()))
    logging.info(uxiosShakeAttempt)
    
    resp = shakingSats()
    apiPostResponse = json.loads(resp.text)
    formatted_apiPostResponse = json.dumps(apiPostResponse)
    APIMessage = json.loads(formatted_apiPostResponse)

    #APIMessage = {'success': True, 'currency': 'satoshis', 'streak': 69420, 'cumulativeTotal': 481900, 'amount': 1000, 'shakingTask': {}}
    #APIMessage = {'error': 'test'}

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
        if discordOPT == True:
            sendToDiscord(uxiosDiscordSuccessfulShake + streakAmount)
        time.sleep((3600*6)+randint(0, 7200))
    else:
        logging.info(uxiosFailedShake)
        if telegramOPT == True:
            sendToTelegram(uxiosTelegramFailedShake)
        if discordOPT == True:
            sendToDiscord(uxiosDiscordFailedShake)
        else:
            print(uxiosFailedShake)
            logging.info(uxiosFailedShake)
        time.sleep(1800)
