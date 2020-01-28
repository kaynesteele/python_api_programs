import requests
import json

def getSummonerInfo(s):
    url = "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" +str(s) + "?api_key="
    test= requests.get(url)
    jsonText=json.loads(test.text)
    print(jsonText[0]['summonerName'])
    print("Rank: " + jsonText[0]['tier'] +" "+ jsonText[0]['rank'] + " " + str(jsonText[0]['leaguePoints']) + "lp")
    print("Win/Loss: " + str(jsonText[0]['wins']) + "/" + str(jsonText[0]['losses']) + "\n")

def getMatchId(s):
    url = "https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" +str(s) + "?api_key="
    test= requests.get(url)
    jsonText=json.loads(test.text)
    for i in jsonText['participants']:
        getSummonerInfo(i['summonerId'])

def main():
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/trick2g?api_key="
    test= requests.get(url)
    jsonText=json.loads(test.text)
    getMatchId(jsonText['id'])
main()
