#!/usr/bin/python3
# Imports from modules.
import requests
import json
import time


# File to save data in it.
currency_data = open("currency_data.txt", mode="w")


# URL details.
baseURL = "https://steamcommunity.com/market/priceoverview/"
params = {}
params["appid"] = "730"
params["market_hash_name"] = "StatTrak™ P250 | Steel Disruption (Factory New)"


# Titles
title1 = "Steam Price"
title2 = "Steam Number"


# Print and write the titles.
currency_data.writelines([title1.rjust(len(title1)+5), "\t", title2.rjust(len(title2)), "\n"])
print(title1.rjust(len(title1)+5), "\t", title2.rjust(len(title2)))


# Checks all numbers for currency data.
for i in range(45):
    try:
        params["currency"] = str(i)
        resp = requests.get(baseURL, params=params)
        price = str(resp.json()['lowest_price'])

        # Printing data to the terminal.
        print(price.rjust(len(title1)+5), "\t", str(i).rjust(len(title2)))

        # Writing to data to the file.
        currency_data.writelines([price.rjust(len(title1)+5), "\t", str(i).rjust(len(title2)), "\n"])
        time.sleep(7)
    except :
        pass

# Close the file.
currency_data.close()

# 24 is for rupees
