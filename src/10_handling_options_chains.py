# FROM HERE
# https://www.interactivebrokers.com/campus/ibkr-quant-news/handling-options-chains/

import requests
#Disable SSl warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import csv

def secdefSearch(symbol,listingExchange):
    url = f'https://localhost:5001/v1/api/iserver/secdef(search?symbol={symbol})'
    search_request = requests.get(url=url,verify=False)
    
    for contract in search_request.json():
        if contract["description"] == listingExchange:
            underConid = contract("conid")
             