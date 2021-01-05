import requests
import json
import time


for i in range(100):
    try:
        URL = "https://steamcommunity.com/market/priceoverview/?currency=" + str(i) + "&appid=730&market_hash_name=StatTrak%E2%84%A2%20P250%20%7C%20Steel%20Disruption%20%28Factory%20New%29"
        resp = requests.get(URL)
        print(resp.json()['lowest_price'], i)
        time.sleep(10)
    except :
        pass

# 24 is for rupees
