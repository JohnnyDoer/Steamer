#!/usr/bin/python3
# Imports from modules.
import requests
import asyncio
import time
from datetime import datetime

# Imports from files.
from keys import client_secret, client_ID, public_key, bot_token

# Global variables.
CLIENT_ID = client_ID
CLIENT_SECRET = client_secret
PUBLIC_KEY = public_key
BOT_TOKEN = bot_token


# Reading wishlist.
def readWishlist():
    wishlist = open("wishlist.txt", mode="r")
    lines = wishlist.readlines()
    wishlist.close()

    wishlist = []
    for i in lines:
        data = i.split(", ")
        data = list(map(lambda s: s.strip(), data))
        wish = {}
        wish["Item"] = data[0]
        wish["Price"] = data[1]
        wish["Discord Name"] = data[2]
        wish["Discord ID"] = data[3]
        wishlist.append(wish)
    return wishlist


# Checking price on Steam.
def steamPrice(currency="24", appid="730"):
    wishlist = readWishlist()

    baseURL = "https://steamcommunity.com/market/priceoverview/"
    params = {}
    params["currency"] = "24" # Indian Rupees
    params["appid"] = "730" # CSGO
    msgs = []
    for wish in wishlist:
        params["market_hash_name"] = wish["Item"]
        try:
            resp = requests.get(baseURL, params=params)
            current_price = resp.json()["lowest_price"][2:]
            current_price = float(current_price.replace(",", ""))
            if current_price <= float(wish["Price"]):

                # string = "{0}, @{1}, found {2}, at Rs.{3} on {4}".format(wish['name'], wish['Discord Name'], wish['Item'], wish['Price'], datetime.now())
                string = f"{wish['Discord ID']}, we found { wish['Item']}, at Rs. {current_price} ( <= {wish['Price']}) on {datetime.now().strftime('%y-%m-%d %a %H:%M')}"
                msgs.append(string)
                print("Woohoo")
            else:
                print("Out of league.")
        except Exception as e:
            string = "Something failed."
            msgs.append(string)
            print(e)
        time.sleep(1)
    return msgs


# Saves a list of channels in channels.txt
def getChannel(message):
    string = message.channel.name + " " + str(message.channel.id) + "\n"
    channels = open("channels.txt", mode="r")
    rlines = channels.readlines()
    channels.close()
    if string in rlines:
        return
    channels = open("channels.txt", mode="a")
    lines = channels.writelines([message.channel.name, " ", str(message.channel.id), "\n"])
    channels.close()


# Saves a list of members in members.txt
def getMember(message):
    members = open("members.txt", mode="r")
    rlines = members.readlines()
    members.close()
    string = message.author.name + " " + "<@" + str(message.author.id) + ">" + "\n"
    if string in rlines:
        return
    members = open("members.txt", mode="a")
    lines = members.writelines([ message.author.name , " ", "<@", str(message.author.id), ">", "\n"])
    members.close()


# Adding items to wwishlist.
def addWish(message):
    msgs = []
    wishes = open("wishlist.txt", mode="r")
    rlines = wishes.readlines()
    wishes.close()
    data = message.content.replace("!wish ", "").split(", ")
    wish_item = data[0]
    price = data[1]
    baseURL = "https://steamcommunity.com/market/priceoverview/"
    params = {}
    params["currency"] = "24" # Indian Rupees
    params["appid"] = "730" # CSGO
    params["market_hash_name"] = wish_item
    resp = requests.get(baseURL, params=params)
    author_ID = f"<@{message.author.id}>"
    if not resp.json()['success']:
        string = f"{message.author.name}, {author_ID}, check the name of {wish_item}."
        msgs.append(string)
    else:
        string = wish_item + ", " + price + ", " + message.author.name + ", " + "<@" + str(message.author.id) + ">" + "\n"
        if string in rlines:
            return [wish_item + " already exists in the wishlist for Rs. " + price + "."]
        wishlist = open("wishlist.txt", mode="a")
        lines = wishlist.writelines([string])
        wishlist.close()
        string = f"{message.author.name}, {author_ID}, {wish_item} added to the wishlist for Rs. {price}."
        msgs.append(string)

    return msgs



def removeWish(message):
    pass
