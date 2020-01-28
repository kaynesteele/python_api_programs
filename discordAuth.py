import requests
import json

def main():
    url = "https://discordapp.com/api/v6/oauth2/token"
    data={"grant_type" : "client_credentials",
           "scope" : "bot messages.read"}
            
    test = requests.post(url,data=data,auth=("",""))
    print(test.text)

main()
