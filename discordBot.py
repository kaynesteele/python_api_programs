import discord
import requests
import json
import time

client = discord.Client()
lolApiKey = "RGAPI-4350e045-389e-4141-92fb-c7b07800ef07"

def getSummonerInfo(s, message):
    url = "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" +str(s) + "?api_key=" + lolApiKey
    test= requests.get(url)
    jsonText=json.loads(test.text)
    for i in jsonText:
        if (i['queueType']=="RANKED_SOLO_5x5"): 
            return ("\n" + i['summonerName'] + " Rank: " + i['tier'] +" "+ i['rank'] + " " + str(i['leaguePoints']) + "LP" + "\n" + "Win/Loss: " + str(i['wins']) + "/" + str(i['losses']))
            print(i)
    print(jsonText[0]['summonerName'])
    print("Rank: " + jsonText[0]['tier'] +" "+ jsonText[0]['rank'] + " " + str(jsonText[0]['leaguePoints']) + "lp")
    print("Win/Loss: " + str(jsonText[0]['wins']) + "/" + str(jsonText[0]['losses']) + "\n")

def getMatchId(s, message):
    url = "https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" +str(s) + "?api_key=" + lolApiKey
    test= requests.get(url)
    testString=""
    jsonText=json.loads(test.text)
    for i in jsonText['participants']:
        testString += str(getSummonerInfo(i['summonerId'], message) + "\n")

    return testString

def main(message, name):
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + lolApiKey
    test= requests.get(url)
    jsonText=json.loads(test.text)
    return getMatchId(jsonText['id'], message)
def is_me(m):
    return m.author == client.user


def youtube(s):
    url="https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + s + "&key=AIzaSyC8XKm_lbuEq6r9Y_llr5AbMAT-bIddnTw"
    test1=requests.get(url)
    jsonText=json.loads(test1.text)
    return str(jsonText['items'][0]['id']['videoId'])

@client.event
async def on_ready():
    print("BOT IS CONNECTED AND READY")

@client.event
async def on_message(message):
    print(str(message.guild.name) +"@" + str(message.channel)+ "#"+ str(message.author.name)+ "-> " + str(message.content))
    if(message.content.lower().startswith('!youtube ')):
        await message.channel.send("https://youtube.com/watch?v=" + youtube(message.content[9:]))
    if(message.content.lower()=='!deletemessages'):
        print("test")
        await message.channel.purge(limit=100, check=is_me)
    if(message.content.lower().startswith('!lol ')):
        print("getting League Info")
        await message.channel.send(main(message, message.content[5:]))
        

client.run('MTk5OTUwNTAwNzk0MzM1MjMy.Xe8pgw.rYJ7G0d7_68fKYM8F80jEcfukyk')
