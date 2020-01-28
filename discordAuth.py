import requests
import json

def main():
    url = "https://discordapp.com/api/v6/oauth2/token"
    data={"grant_type" : "client_credentials",
           "scope" : "bot messages.read"}
            
    test = requests.post(url,data=data,auth=("199950474177150976","EfaHRT6fqY6Ni12Fur3XgFNEHvZ0k23m"))
    print(test.text)

main()
