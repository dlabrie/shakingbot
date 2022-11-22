from modules.shakepay import *
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
    print(json.loads(resp.text));

    logging.info(json.loads(resp.text))
    time.sleep((3600*6)+randint(0, 7200))
