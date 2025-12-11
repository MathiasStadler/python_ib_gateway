# FROM HERE
# IBKR Client Portal API - Launching and Authenticating the Gateway
# https://www.youtube.com/watch?v=t6IsvhxwLzw

# vis after 5:35 iserver/secdef/info

import requests
import json

#Disable SSl warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def confirmStatus():
    base_url = "https://localhost:5000/v1/api/"
    endpoint = "iserver/auth/status"
    
    auth_req = requests.get(url=base_url+endpoint,verify=False)
    print(auth_req)
    print(auth_req.text)

def contractInfo():
    base_url = "https://localhost:5000/v1/api/"
    # info instead search
    # endpoint = "iserver/secdef/search"
    endpoint = "iserver/secdef/info"
    conid = "conid=11004968"
    secType = "secType=FUT"
    # month = "month=SEP23"
    month = "month=DEC25"
    exchange = "exchange=CME"
    
    params = "&".join([conid,secType,month,exchange])
    request_url="".join([base_url,endpoint,"?",params])
    
    contract_req = requests.get(url=request_url,verify=False)
    contract_json = json.dumps(contract_req.json(),indent=2)
    
    
    
    
    # ES Futures 
    # json_body={"symbol" : "ES","secType" : "STK","name" : False}
        # contract_req = requests.post(url=base_url+endpoint,verify=False,json=json_body)
    contract_req = requests.get(url=request_url,verify=False)
    print(contract_req)
    
    contract_json = json.dumps(contract_req.json(),indent=2)
    print(contract_json)
    

if __name__ == "__main__":
    # confirmStatus()
    # contractSearch()
    contractInfo()

# INSIDE VENV
# pip3 install requests
# python src/01_auth:status.py

# <Response [200]>
#{"authenticated":true,"competing":false,"connected":true,"message":"",
# "MAC":"F4:03:43:DC:B4:60","serverInfo":{"serverName":"JifZ01116",
# "serverVersion":"Build 10.41.1c, Dec 3,
# 2025 3:36:17 PM"},
# "hardware_info":"096838b2|F4:03:43:DC:B4:60",
# "fail":""}
