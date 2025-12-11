# FROM HERE
# IBKR Client Portal API - Launching and Authenticating the Gateway
# https://www.youtube.com/watch?v=t6IsvhxwLzw

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

def contractSearch():
    base_url = "https://localhost:5000/v1/api/"
    endpoint = "iserver/secdef/search"
    # ES Futures 
    json_body={"symbol" : "ORCL","secType" : "STK","name" : False}
    
    contract_req = requests.post(url=base_url+endpoint,verify=False,json=json_body)
    
    contract_json = json.dumps(contract_req.json(),indent=2)
    print(contract_json)
    

if __name__ == "__main__":
    # confirmStatus()
    contractSearch()

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
