from modules.shakepay import *
import time
import datetime
import json

from random import *

counter = 0
while True:
    
    print("\n--- "+str(datetime.datetime.now()))
    
    resp = shakingSats()
    print(json.loads(resp.text)["message"]);        

    time.sleep((3600*6)+randint(0, 14400))