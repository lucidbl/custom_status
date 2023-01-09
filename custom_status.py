
import requests
import time
from itertools import cycle

tokenz = {"authorization":"your token here"}


while True:
    #if you want more lyrics to roll in your status just copy and paste payloads and add numbers after
    payload = {
        "custom_status":{
            "text": "your lyrics"
        }
    }
    payload2 = {
        "custom_status":{
            "text": "your lyrics"
        }
    }
    payload3 = {
        "custom_status":{
            "text": "your lyrics"
        }
    }
    payload4 = {
        "custom_status":{
            "text": "your lyrics"
        }
    }
    payload5 = {
        "custom_status":{
            "text": "your lyrics"
        }
    }
    payload6 = {
        "custom_status":{
            "text": "your lyrics"
        }
    }
    payload7 = {
        "custom_status":{
            "text": "your lyrics"
        }
    }
    payload8 = {
        "custom_status":{
            "text": "your lyrics"
        }
    }
    #when u add more paylaods as in payload9 copy and paste the request but instead of it being e8 make it e9 ok  
    time.sleep(2)
    e = requests.patch("https://discord.com/api/v9/users/@me/settings", headers = tokenz, json = payload)
    time.sleep(2)
    e2 = requests.patch("https://discord.com/api/v9/users/@me/settings", headers = tokenz, json = payload2)
    time.sleep(2)
    e3 = requests.patch("https://discord.com/api/v9/users/@me/settings", headers = tokenz, json = payload3)
    time.sleep(2)
    e4 = requests.patch("https://discord.com/api/v9/users/@me/settings", headers = tokenz, json = payload4)
    time.sleep(2)
    e5 = requests.patch("https://discord.com/api/v9/users/@me/settings", headers = tokenz, json = payload5)
    time.sleep(2)
    e6 = requests.patch("https://discord.com/api/v9/users/@me/settings", headers = tokenz, json = payload6)
    time.sleep(2)
    e7 = requests.patch("https://discord.com/api/v9/users/@me/settings", headers = tokenz, json = payload7)
    time.sleep(2)
    e9 = requests.patch("https://discord.com/api/v9/users/@me/settings", headers = tokenz, json = payload8)
    print(e)
